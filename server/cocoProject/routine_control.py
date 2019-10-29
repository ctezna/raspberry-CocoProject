from cocoProject import db
from cocoProject.models import Routine, Light
from crontab import CronTab
import os


class RoutineControl():
    cron = None

    def __init__(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        self.file = os.path.join(basedir, 'tasks.tab')
        self.cron = CronTab(tabfile=self.file)


    def new_cron(self, routineId, task, days, times):
        hours = []
        minutes = []
        dates = []
        days = days.split(',')
        for day in days:
            day = day.replace(',', '').strip()
            day = day.replace('Sunday', '0')
            day = day.replace('Monday', '1')
            day = day.replace('Tuesday', '2')
            day = day.replace('Wednesday', '3')
            day = day.replace('Thursday', '4')
            day = day.replace('Friday', '5')
            day = day.replace('Saturday', '6')
            if len(day) > 0:
                day = int(day)
                dates.append(day)
        times = times.split(',')
        for time in times:
            time = time.replace(',', '').strip().lower()
            hour = time.split(':')[0]
            minute = time.split(':')[1]
            hours.append(hour)
            minutes.append(minute)
        
        if task == 'Dispense Food':
            task = 'motor_control.py 4'
        if task == 'Light':
            light = Light.query.first()
            red = light.red
            green = light.green
            blue = light.blue
            brightness = light.brightness
            task = 'light_control.py {} {} {} {}'.format(red, green, blue, brightness)
            task2 = 'light_status.py {} {} {} {}'.format(red, green, blue, brightness)
            lightcmd = '$(which python3) /home/pi/raspberry-cocoproject/server/cocoProject/' + task2 +' >> ~/light-status.log 2>&1'
            job = self.cron.new(command=lightcmd, comment=str(routineId))
            job.dow.on(*dates)
            job.hour.on(*hours)
            job.minute.on(*minutes)
        cmd = '$(which python3) /home/pi/raspberry-cocoproject/server/cocoProject/'+ task + ' >> ~/cron.log 2>&1'
            
        job = self.cron.new(command=cmd, comment=str(routineId))
        job.dow.on(*dates)
        job.hour.on(*hours)
        job.minute.on(*minutes)
        self.cron.write()
        os.system("crontab " + self.file)

    def remove_cron(self, comment):
        self.cron.remove_all(comment=str(comment))
        self.cron.write()
        os.system("crontab " + self.file)

    def save_routine(self, routineId, task, days, times):
        self.new_cron(routineId, task, days, times)
        routine = Routine(id=routineId, task=task, days=days, times=times)
        db.session.add(routine)
        db.session.commit()
        task = {
            "id": routine.id,
            "task": routine.task,
            "days": routine.days,
            "times": routine.times
        }
        return task

    def delete_routine(self, routineId):
        self.remove_cron(routineId)
        routine = Routine.query.filter_by(id=routineId).first_or_404()
        db.session.delete(routine)
        db.session.commit()
        return 0

    def get_routines(self):
        routines = Routine.query.all()
        response = []
        for r in routines:
            routine = {
                "id" : r.id,
                "task": r.task,
                "days": r.days,
                "times": r.times
            }
            response.append(routine)
        return response
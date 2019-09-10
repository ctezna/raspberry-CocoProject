from cocoProject import db
from cocoProject.models import Routine
from crontab import CronTab


class RoutineControl():
    cron = None

    def __init__(self):
        self.cron = CronTab(tabfile='tasks.tab')


    def new_cron(self, routineId, task, days, times):
        if task == 'Dispense Food':
            task = 'motor_control.py 4'
        if task == 'Light':
            task = 'light_control.py 255 255 255 0.4'
        cmd = 'python3 '+ task
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
            
        job = self.cron.new(command=cmd, comment=routineId)
        job.day.on(*dates)
        job.hour.on(*hours)
        job.minute.on(*minutes)
        self.cron.write()

    def remove_cron(self, comment):
        self.cron.remove_all(comment=comment)
        self.cron.write()

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
from cocoProject import db
from cocoProject.models import Routine



def save_routine(routineId, task, days, times):
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

def delete_routine(routineId):
    routine = Routine.query.filter_by(id=routineId).first_or_404()
    db.session.delete(routine)
    db.session.commit()
    return 0

def get_routines():
    routines = Routine.query.all()
    response = []
    for r in routines:
        routine = {
            "id" : r.id,
            "task": r.task,
            "days": r.days,
            "times": r.times
        }
        response.append(r)
    return response
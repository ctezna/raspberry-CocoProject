import json, os
from cocoProject import db



def save_routine(task):
    basedir = os.path.abspath(os.path.dirname(__file__))
    routines = os.path.join(basedir, 'static', 'tasks','tasks.json')
    with open(routines, 'w') as f:
        json.dump(task, f)
    
    return task

def delete_routine(id):
    return 0
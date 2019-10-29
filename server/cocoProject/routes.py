from cocoProject import app, motor, camera, lightControl, routineControl, db
from flask import render_template, Response, url_for, jsonify, request
from time import sleep
import os, json


@app.route("/feed", methods=['GET','POST'])
def feed(delay=1):
	if motor != 404:
		#ring("foodShake.mp3")
		motor.feed(delay)
		rsp = {'response':1}
		return jsonify(rsp)
	rsp = {'response':0}
	return jsonify(rsp)

@app.route("/ring", methods=['GET','POST'])
def ring(sound="whistle.wav"):
	#soundControl.play(sound)
	return "ring"

def gen(camera):
	"""Video streaming generator function."""
	camera.start_camera_thread()
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
			   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/cam", methods=['GET','POST'])
def cam():
	"""Video streaming route. Put this in the src attribute of an img tag."""
	return Response(gen(camera),
					mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/camOff", methods=['GET','POST'])  
def camOff():
	camera.stop_camera_thread()
	rsp = {'response':1}
	return jsonify(rsp)

@app.route("/light", methods=['GET','POST'])
def light():
    red = int(request.args.get('red'))
    green = int(request.args.get('green'))
    blue = int(request.args.get('blue'))
    brightness = float(request.args.get('brightness'))
    lightControl.lightSwitch(red, green, blue, brightness)

    if brightness == 0:
        lightstat = '/home/pi/raspberry-cocoproject/server/cocoProject/lightstatus.json'
        with open(lightstat, "r+") as file:
            data = json.load(file)
            file.seek(0)
            json.dump({'status': False,
                        'red': data['red'],
                        'green': data['green'],
                        'blue': data['blue'],
                        'brightness': data['brightness']
                        }, file)
            file.truncate()
    else:
        lightstat = '/home/pi/raspberry-cocoproject/server/cocoProject/lightstatus.json'
        with open(lightstat, "r+") as file:
            file.seek(0)
            json.dump({'status':True,
                        'red': red,
                        'green': green,
                        'blue': blue,
                        'brightness': brightness
                        }, file)
            file.truncate()
    
    db.session.commit()
    
    rsp = {'response':1}
    return jsonify(rsp)

@app.route("/light/status")
def light_status():
    lightstat = '/home/pi/raspberry-cocoproject/server/cocoProject/lightstatus.json'
    data = ''
    with open(lightstat, "r") as json_file:
        data = json.load(json_file)
    return jsonify(data), 200

@app.route("/reboot", methods=['GET','POST'])
def reboot():
	cmd = "sudo reboot"
	os.system(cmd)
	rsp = {'response':1}
	return jsonify(rsp)

@app.route("/addRoutine", methods=['GET'])
def addRoutine():
    light_splice = ''
    if request.args.get('task') == 'Light':
        light_splice = request.args.get('light_splice')
        
    task = routineControl.save_routine(request.args.get('routine_id'),request.args.get('task'),\
			request.args.get('days'),request.args.get('times'), light_splice)
            
    return jsonify({'task': task}), 201

@app.route("/removeRoutine", methods=['GET'])
def removeRoutine():
	routineId = request.args.get('routine_id')
	routineControl.delete_routine(routineId)
	return jsonify({'routine': routineId}), 201

@app.route("/getRoutines", methods=['GET'])
def getRoutines():
	routines = routineControl.get_routines()
	return jsonify({'routines': routines}), 201
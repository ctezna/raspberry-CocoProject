from cocoProject import app, motor, lightStatus, camera, lightControl, soundControl, routineControl
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
	soundControl.play(sound)
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
	red = request.args.get('red')
	green = request.args.get('green')
	blue = request.args.get('blue')
	brightness = request.args.get('brightness')
	lightControl.lightSwitch(red, green,\
			blue, brightness)	
	rsp = {'response':1}
	return jsonify(rsp)

@app.route("/reboot", methods=['GET','POST'])
def reboot():
	cmd = "sudo reboot"
	os.system(cmd)
	rsp = {'response':1}
	return jsonify(rsp)

@app.route("/addRoutine", methods=['GET'])
def addRoutine():
	task = routineControl.save_routine(request.args.get('routine_id'),request.args.get('task'),\
			request.args.get('days'),request.args.get('times'))
	return jsonify({'task': task}), 201

@app.route("/removeRoutine", methods=['GET'])
def removeRoutine():
	routineId = request.args.get('id')
	routineControl.delete_routine(routineId)
	return jsonify({'routine': routineId}), 201

@app.route("/getRoutines", methods=['GET'])
def getRoutines():
	routines = routineControl.get_routines()
	return jsonify({'routines': routines}, 201)
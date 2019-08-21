from cocoProject import app, motor, lightStatus, camera
from flask import render_template, Response, url_for, jsonify, request
from cocoProject.routine_control import save_routine
from time import sleep
import os, json


@app.route("/feed", methods=['GET','POST'])
def feed(delay=1):
	if motor != 404:
		#ring("foodShake.mp3")
		motor.on()
		sleep(delay)
		motor.off()
		rsp = {'response':1}
		return jsonify(rsp)
	rsp = {'response':0}
	return jsonify(rsp)

@app.route("/ring", methods=['GET','POST'])
def ring(sound="whistle.wav"):
	ring = os.path.join("cocoProject", "static", "ringtones", sound)
	try:
		cmd = "omxplayer " + ring
		#os.system(cmd)
		pass
	except:
		print("ringtone error")
		pass
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
	return "cam off"

@app.route("/lightOn", methods=['GET','POST'])
def lightOn():
	lightOn = os.path.join("cocoProject", "lights", "lightOn.py")
	cmd = "sudo python3 " + lightOn
	os.system(cmd)
	lightStatus = 1
	rsp = {'response':1}
	return jsonify(rsp)

@app.route("/lightOff", methods=['GET','POST'])
def lightOff():
	lightOff = os.path.join("cocoProject", "lights", "lightOff.py")
	cmd = "sudo python3 " + lightOff
	os.system(cmd)
	lightStatus = 0
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
	task = {
		'id': request.args.get('id'),
		'task': request.args.get('task'),
		'days': request.args.get('days'),
		'times': request.args.get('times')
		}
	save_routine(task)
	return jsonify({'task': task}), 201
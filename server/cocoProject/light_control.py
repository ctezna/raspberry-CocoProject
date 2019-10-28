import threading, os, sys
from cocoProject.models import Light


class LightControl():
    
    def __init__(self):
        self.thread = None

    def lightSwitch(self, red, green, blue, brightness):
        if Light.query.count() != 1:
            light = Light(red=red, green=green, blue=blue, brightness=brightness)
            if brightness * red == 0:
                light.status = False
            else:
                light.status = True
            db.session.add(light)
            db.session.commit(light)
        else:
            light = Light.query.first()
            light.red = red
            light.green = green
            light.blue = blue
            light.brightness = brightness
            if brightness * red == 0:
                light.status = False
            else:
                light.status = True
            db.session.commit(light)
        LightControl.thread = threading.Thread(target=self._thread(red, green, blue, brightness))
        LightControl.thread.start()

    def _thread(self, red, green, blue, brightness):
        basedir = os.path.abspath(os.path.dirname(__file__))
        lightFile = os.path.join(basedir, "lights", "lightController.py")
        cmd = "sudo python3 " + lightFile + " " +  str(red) + " "\
             + str(green) + " " + str(blue) + " " + str(brightness)
        if int(red) == -1 and int(green) == -1 and int(blue) == -1:
            lightFile = os.path.join("cocoProject", "lights", "rainbow.py")
            cmd = "sudo python3 " + lightFile + " " + str(brightness)
        elif int(red) == -2 and int(green) == -2 and int(blue) == -2:
            lightFile = os.path.join("cocoProject", "lights", "effects.py")
            cmd = "sudo python3 " + lightFile + " " + str(brightness)
        os.system(cmd)


if __name__ == "__main__":
    light = LightControl()
    light.lightSwitch(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
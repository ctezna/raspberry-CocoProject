import threading, os


class LightControl():
    thread = None
    
    def __init__(self):
        self.thread = None

    def lightSwitch(self, red, green, blue, brightness):
        LightControl.thread = threading.Thread(target=self._thread(red, green, blue, brightness))
        LightControl.thread.start()

    def _thread(self, red, green, blue, brightness):
        lightFile = os.path.join("cocoProject", "lights", "lightController.py")
        cmd = "sudo python3 " + lightFile + " " +  str(red) + " "\
             + str(green) + " " + str(blue) + " " + str(brightness)
        if int(red) == -1 and int(green) < == -1 and int(blue) < == -1:
            lightFile = os.path.join("cocoProject", "lights", "rainbow.py")
            cmd = "sudo python3 " + lightFile + " " + str(brightness)
        elif int(red) == -2 and int(green) < == -2 and int(blue) < == -2:
            lightFile = os.path.join("cocoProject", "lights", "effects.py")
            cmd = "sudo python3 " + lightFile + " " + str(brightness)
        os.system(cmd)
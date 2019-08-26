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
        if int(red) < 0 and int(green) < 0 and int(blue) < 0:
            lightFile = os.path.join("cocoProject", "lights", "rainbow.py")
            cmd = "sudo python3 " + lightFile + " " + str(brightness)
        os.system(cmd)
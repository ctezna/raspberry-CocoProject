import threading


class LightControl():
    thread = None
    
    def __init__(self):
        self.thread = None

    def lightSwitch(self, filename):
        LightControl.thread = threading.Thread(target=self._thread(filename))
        LightControl.thread.start()

    def _thread(self, filename):
        lightFile = os.path.join("cocoProject", "lights", filename)
        cmd = "sudo python3 " + lightFile
        os.system(cmd)
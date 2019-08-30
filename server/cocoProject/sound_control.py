import threading, os


class SoundControl():
    thread = None
    
    def __init__(self):
        self.thread = None

    def play(self, sound):
        SoundControl.thread = threading.Thread(target=self._thread(sound))
        SoundControl.thread.start()

    def _thread(self, sound):
        ring = os.path.join("cocoProject", "static", "ringtones", sound)
        try:
            cmd = "omxplayer " + ring
            os.system(cmd)
            pass
        except:
            pass
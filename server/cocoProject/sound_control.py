import threading, os, pygame


class SoundControl():
    
    def __init__(self):
        self.thread = None

    def play(self, sound):
        SoundControl.thread = threading.Thread(target=self._thread(sound))
        SoundControl.thread.start()

    def _thread(self, sound):
        ring = os.path.join("cocoProject", "static", "ringtones", sound)
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(ring)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.stop()
            pass
        except:
            pass
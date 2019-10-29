import os, json

if __name__ == "__main__":
    lightstat = '/home/pi/raspberry-cocoproject/server/cocoProject/lightstatus.json'
    with open(lightstat, "a") as file:
        file.seek(0)
        json.dump({'status':True}, file)
        file.truncate()


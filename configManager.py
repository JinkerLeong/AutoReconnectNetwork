import json
from sys import stdout

class config(object):
    class UsbDevice(object):
        def __init__(self, usbD):
            self.name = usbD['name']
            self.ip = usbD['ip']
            self.netmask = usbD['netmask']

    def __init__(self, a,b,c,d):
        self.startAfter = a
        self.waitToCheck = b
        self.targetHost = c
        self.usbDevices = []
        for device in d:
            self.usbDevices.append(config.UsbDevice(device))

def jsonToConfig(d):
    return config(d['startAfter'],d['waitToCheck'],d['targetHost'], d['usbDevices'])

def loadConfig(configFile):
    with open(configFile) as f:
        config = json.load(f, object_hook=jsonToConfig)
        return config

def printConfig(config):
    print("=========================")
    print("[Config]")
    print(f"Start after seconds: {config.startAfter}")
    print(f"Wait to check seconds: {config.waitToCheck}")
    print(f"Target host: {config.targetHost}")
    print("=========================")
    stdout.flush()
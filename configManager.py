import json
from sys import stdout

globalConfig = None

class config(object):
    class UsbDevice(object):
        def __init__(self, usbD):
            self.name = usbD['name']
            self.ip = usbD['ip']
            self.netmask = usbD['netmask']

    def __init__(self, a,b,c,d,e):
        self.startAfter = int(a)
        self.waitToCheck = int(b)
        self.targetHost = c
        self.pingCount = d
        self.usbDevices = []
        for device in e:
            self.usbDevices.append(config.UsbDevice(device))

def jsonToConfig(d):
    return config(d['startAfter'],d['waitToCheck'],d['targetHost'], d['pingCount'], d['usbDevices'])

def loadConfig(configFile)->config:
    with open(configFile) as f:
        global globalConfig
        globalConfig = jsonToConfig(json.load(f))
        return globalConfig

def getConfig()->config:
    return globalConfig

def printConfig(config : config):
    print("=========================")
    print("[Config]")
    print(f"Start after seconds: {config.startAfter}")
    print(f"Wait to check seconds: {config.waitToCheck}")
    print(f"Target host: {config.targetHost}")
    print(f"Ping count: {config.pingCount}")
    print("=========================")
    stdout.flush()
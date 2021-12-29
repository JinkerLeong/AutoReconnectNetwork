import json
from configModule.myconfig import *
from sys import stdout

globalConfig:config = None

def jsonToConfig(d):
    return config(d['startAfter'],d['waitToCheck'],d['targetHost'], d['pingCount'], d['usbDevices'])

def loadConfig(configFile)->config:
    with open(configFile) as f:
        global globalConfig
        globalConfig = jsonToConfig(json.load(f))
        return globalConfig

def getConfig()->config:
    return globalConfig

def printConfig():
    print("=========================")
    print("[Config]")
    print(f"Start after seconds: {globalConfig.startAfter}")
    print(f"Wait to check seconds: {globalConfig.waitToCheck}")
    print(f"Target host: {globalConfig.targetHost}")
    print(f"Ping count: {globalConfig.pingCount}")
    print("=========================")
    stdout.flush()
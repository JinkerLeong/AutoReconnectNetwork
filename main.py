#!/usr/bin/python3

import sys, subprocess, time, functools, configManager

print = functools.partial(print,flush=True)
print("load config from /etc/AutoReconnectNetwork/config.json")
config = configManager.loadConfig("/etc/AutoReconnectNetwork/config.json")


def checkNetworkPass():
    result = subprocess.run(f"ping -c 2 {config.targetHost}", shell=True, capture_output=True)
    return result.stdout and result.stdout.decode("utf-8").find("2 received") != -1

def restartNetworking():
    subprocess.run("systemctl restart networking", shell=True, capture_output=True)

def existDevice(deviceName):
    result = subprocess.run(f"ip link show {deviceName}", shell=True, capture_output=True)
    return result.stdout and result.stdout.decode("utf-8").find("does not exist") == -1

def restartUsbDevices():
    for device in config.usbDevices:
        if existDevice(device.name):
            print(f"Exists {device.name}, restarting it..")
            subprocess.run(f"ifconfig {device.name} up", shell=True, capture_output=True)
            subprocess.run(f"ifconfig {device.name} {device.ip} netmask {device.netmask}", shell=True, capture_output=True)
        else:
            print(f"No exists {device.name}.")

def checkArgv():
    for a in sys.argv:
        if a == "-t":
            config.startAfter = 0

if __name__ == "__main__":
    checkArgv()
    print(f"Starting script after {config.startAfter} seconds:")
    time.sleep(config.startAfter)
    print("====================")
    print("[Config]")
    print(f"Target host:  {config.targetHost}")
    print(f"Wait to check:  {config.waitToCheck}")
    print("====================")
    print("Now runing script...")
    while True:
        print("Check networking...")
        if checkNetworkPass():
            print("Networking normal..")
        else:
            print("Networking not access, trying restart networking..")
            restartNetworking()
            print("Networking restart done...")
        restartUsbDevices()
        print(f"Wait {config.waitToCheck} seconds to check again...")
        time.sleep(config.waitToCheck)
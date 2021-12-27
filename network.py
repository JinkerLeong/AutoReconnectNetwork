import subprocess, configManager

config = configManager.getConfig()

def checkNetworkPass():
    result = subprocess.run(f"ping -c 1 {config.targetHost}", shell=True, capture_output=True)
    return result.stdout and result.stdout.decode("utf-8").find("1 received") != -1

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
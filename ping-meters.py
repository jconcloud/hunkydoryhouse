import os, threading, time

def pinghost(hostname):
  return os.system("ping -c 1 " + hostname)


WAIT_TIME_SECONDS = 10
meter2F = "192.168.86.102"
meter3F = "192.168.86.103"

ticker = threading.Event()
while not ticker.wait(WAIT_TIME_SECONDS):
  response2F = pinghost(meter2F)
  print(response2F)
  response3F = pinghost(meter3F)
  print(response3F)

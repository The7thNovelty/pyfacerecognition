import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if wlan.isconnected() == True:
  print("Already connected")
else:
  wlan.connect(ssid,password)


import webcam
webcam.run()

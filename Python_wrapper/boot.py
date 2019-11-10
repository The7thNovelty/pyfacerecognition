import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if wlan.isconnected() == True:
  print("Already connected")
else:
  wlan.connect('NetGearCisco-WPA2','$eem@V@ibh@v')


import webcam
webcam.run()
from firebase import firebase
import random

#it has been made for our video

firebase = firebase.FirebaseApplication('https://smart-connected-cars-92ce7.firebaseio.com/', None)

speed=0
RPM=0
fuel=92

speedRandomIncrement = [10,13,14,15,8]
speedRandomDecrement = [13,14,12,15]

#The RPM to Linear Velocity formular is :
#  v = r × RPM × 0.10472
startingRPM=0
RPM=speed/(0.066664)
overallCount=0
fuelCount=0
toggle=True

while 1:
  if speed>400:
      toggle=False
  elif speed<380:
      toggle=True
  if toggle==True and overallCount<45:
    speed=speed+random.choice(speedRandomIncrement)
  else:
    speed=speed-random.choice(speedRandomDecrement)
  RPM=speed/(0.066664)
  fuelCount=fuelCount+1
  if fuelCount==20:
      fuel=fuel-1
      fuelCount=0
  if overallCount < 4:
      speed = 0
      startingRPM += random.choice([1920, 1832, 1840, 1967, 1011])
      if startingRPM>6000:
          startingRPM=6000
      RPM=startingRPM
  if speed<0:
      speed=0
      RPM=0
  data =  { 'fuel': int(fuel),
              'rpm': int(RPM),
              'speed': int(speed)
            }
  result = firebase.put('/livedata/','len4245' ,data)
  overallCount=overallCount+1
print(result)
from firebase import firebase

#It will keep on updating real time database

firebase = firebase.FirebaseApplication('https://smart-connected-cars-92ce7.firebaseio.com/', None)

i=10
j=55
k=16
for line in open('input', 'r'):
  data =  { 'fuel': int(k),
              'rpm': int(j),
              'speed': int(i)
            }
  i=i+1
  j=j+7
  result = firebase.put('/livedata/','len4245' ,data)
print(result)
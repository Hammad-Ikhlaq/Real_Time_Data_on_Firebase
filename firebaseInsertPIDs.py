from firebase import firebase

firebase = firebase.FirebaseApplication('https://smart-connected-cars-92ce7.firebaseio.com/', None)
for line in open('input', 'r'):
  values = [str(s) for s in line.split("', '")]
  data =  { 'Causes': values[8],
              'description': values[4],
              'dtc_id': values[1],
              'id': int(values[0]),
              'solutions': values[9],
              'symptoms': values[5],
              'technical_description': values[3],
              'title': values[2]
            }
  result = firebase.put('/tbl_dtc_data_practice/'+values[1]+'/',data)
print(result)
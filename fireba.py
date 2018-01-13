from firebase import firebase
firebase = firebase.FirebaseApplication('https://auth-7ba82.firebaseio.com',None)
result = firebase.get('/userProfile',None)
print result

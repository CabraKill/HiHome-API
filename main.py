from src.handler.firebase.firebaseHandler import FirebaseHandler
from src.handler.firebase.auth2 import FireThread

# firebase = FirebaseHandler()
# result = firebase.getToken()
# print(result)

fireThread = FireThread()
fireThread.start()
# fireThread.close()
fireThread.join()
print("done")
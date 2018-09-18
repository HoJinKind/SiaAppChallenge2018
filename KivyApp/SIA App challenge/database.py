import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class database:
    def __init__(self, firebase_url='https://bamboo-shift-184017.firebaseio.com', key = 'mykey.json', uid = 'dev'):
        self.cred = credentials.Certificate(key)
        self.url = firebase_url
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': firebase_url,
            'databaseAuthVariableOverride': {
                'uid': uid
            }
        })
        
    def get_plates(self):
        return db.reference().get()['plates']
    
    def set_plates(self, li):
        db.reference().child('plates').set(li)


        

if __name__ == '__main__':

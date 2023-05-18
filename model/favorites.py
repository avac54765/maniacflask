""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


# Define FAV class
class FAV(db.Model):
    __tablename__ = 'FAVS'

    #  Notes schema
    id = db.Column(db.Integer, primary_key=True)
    _uid = db.Column(db.String(255), unique=True, nullable=False)
    _songname = db.Column(db.String, unique=True, nullable=False)
    _artist = db.Column(db.String, unique=False, nullable=False)
    _album = db.Column(db.String, unique=False, nullable=False)


    
    # Notes object
    def __init__(self, id, uid, songname, artist, album):
        self.userID = id
        self._uid = uid
        self._songname = songname
        self._artist = artist
        self._album = album
        
    
    
    # getter method
    @property
    def uid(self):
        return self._uid
    
    # setter function
    @uid.setter
    def uid(self, uid):
        self._uid = uid
        
   
    def is_uid(self, uid):
        return self._uid == uid


     # getter method
    @property
    def songname(self):
        return self._songname
    
    # setter function
    @songname.setter
    def songname(self, songname):
        self._songname = songname

     # getter method
    @property
    def artist(self):
        return self._artist
    
    # setter function
    @artist.setter
    def artist(self, artist):
        self._artist = artist
    
     # getter method
    @property
    def album(self):
        return self._album
    
    # setter function
    @album.setter
    def album(self, album):
        self._album = album

    
    
    
    

    # json dumps output
    def __str__(self):
        return json.dumps(self.read())


    # CRUD create to add new record
    def create(self):
        try:
            db.session.add(self)  
            db.session.commit()  
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read returns dictionary
    def read(self):        
        return {
            "id": self.id,
            "uid": self.uid,
            "songname": self.songname,
            "artist": self.artist,
            "album": self.album
        }

   #  def update(self, uid='', duration2=''):
    #    """only updates values with length"""
    #    if len(uid) > 0:
     #       self.uid = uid
      #  if len(duration2) > 0:
      #      self.duration2 = duration2
      #  db.session.commit()
      #  return self

    # CRUD delete: remove item
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing """


# making tester data to test database creation
def initFAVs():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        i1 = FAV(id='33', uid='alexa', songname='Home Movies', artist='Beach Weather', album='Chit Chat')
        i2 = FAV(id='24', uid='ava', songname='Night Changes', artist='One Direction', album='Four')
        i3 = FAV(id='56', uid='TomHolland', songname='A Thousand Years', artist='James Arthur', album='single')
        i4 = FAV(id='23', uid='dylan', songname='past life', artist='Elijah Woods', album='single')
        i5 = FAV(id='59', uid='jm1021', songname='on life', artist='Sammy Rash', album='single')

        favs = [i1, i2, i3, i4, i5]

        """Builds sample user/note(s) data"""
        for fav in favs:
            try:
                '''add a few 1 to 4 notes per user'''
                for num in range(randrange(1, 4)):
                    '''add FAV data to table'''
                    fav.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {FAV.id}")
    

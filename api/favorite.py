from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource 
from datetime import datetime

from model.favorites import FAV

# CODE INSPO CREDIT: John Mortensen

FAV_api = Blueprint('FAV_api', __name__,
                   url_prefix='/api/FAV')


api = Api(FAV_api)

# create the API for FAV
class FAVAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            # setting parameters for garbage data
            ''' Avoid garbage in, error checking '''
            
            songname= body.get('songname')
            if songname is None or len(songname) < 2:
                return {'message': f'Song Name is missing, or is less than 2 characters'}, 211
            
            id = body.get('id')
            artist = body.get('artist')
            if artist is None or len(artist) < 2:
                return {'message': f'Artist is missing, or is less than 2 characters'}, 211
            album = body.get('album')
            if album is None or len(songname) < 2:
                return {'message': f'Album is missing, or is less than 2 characters'}, 211
            uid = str(datetime.now()) # temporary UID that is unique to fill garbage data
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 214

            from model.favorites import FAV
            fo = FAV(id=id,
                      uid=uid,
                      songname=songname,
                      artist=artist,
                      album=album,
                    )
            

            
            ''' #2: Key Code block to add user to database '''
           
            ISPE = io.create()

            
            if ISPE:
                return jsonify(ISPE.read())
            # failure returns error
            return {'message': f'Processed {name2}, either a format error or User ID {uid} is duplicate'}, 215

    class _Read(Resource):
        def get(self):
            ISPEs = ISPE.query.all()    # read database
            json_ready = [ISPE.read() for ISPE in ISPEs]  # json output
            return jsonify(json_ready)  

    # RESTapi endpoints
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
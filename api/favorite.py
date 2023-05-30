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
                return {'message': f'Artist is missing, or is less than 2 characters'}, 212
            album = body.get('album')
            if album is None or len(songname) < 2:
                return {'message': f'Album is missing, or is less than 2 characters'}, 213
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
           
            FAV = fo.create()

            
            if FAV:
                return jsonify(FAV.read())
            # failure returns error
            return {'message': f'Processed {songname}, either a format error or User ID {uid} is duplicate'}, 215

    class _Read(Resource):
        def get(self):
            FAVs = FAV.query.all()    # read database
            json_ready = [FAV.read() for FAV in FAVs]  # json output
            return jsonify(json_ready)  
        
    class _Delete(Resource):
        def delete(self):
            ''' Read data for JSON body '''
            body = request.get_json()

        # Extract the song details from the request body
            songname = body.get('songname')
            artist = body.get('artist')
            album = body.get('album')



            return {'message': 'Song deleted successfully'}, 200  # Return a success response

    # RESTapi endpoints
    api.add_resource(_Create, '/create')
    api.add_resource(_Delete,'/delete')
    api.add_resource(_Read, '/')
from flask_restplus import Namespace, Resource, fields
from flask import current_app

api = Namespace('players', description='Players related operations')

player = api.model('Player', {
    'id': fields.String(required=True, description='The player identifier'),
    'name': fields.String(required=True, description='The player name'),
})

@api.route('/')
class PlayerList(Resource):
    def get(self):
        '''List all players'''
        return current_app.players.to_json(orient='records')

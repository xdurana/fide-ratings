from flask import Blueprint
from flask_restplus import Api

from apis.players import api as players

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint,
    title='Chess FIDE ratings',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(players)

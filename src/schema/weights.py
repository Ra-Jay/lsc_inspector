from flask_restx import fields
from ..extensions import api 

weights_model = api.model("Weights", {
    "id": fields.Integer,
    "url": fields.String,
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime
})
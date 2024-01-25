from marshmallow import Schema,fields, validates
from utils.config import Config

class AuthSchema(Schema):
    username = fields.Str(required=True,validate=validates.Regexp(Config.GEN_REGEX))
    password = fields.Str(required=True,validate=validates.Regexp(Config.PWD_REGEX)) 


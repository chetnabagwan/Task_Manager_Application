from marshmallow import Schema,fields,validate
from utils.config import Config

class RegisterSchema(Schema):
    username = fields.Str(required=True,validate=validate.Regexp(Config.GEN_REGEX))
    password = fields.Str(required=True,validate=validate.Regexp(Config.PWD_REGEX)) 

class LoginSchema(Schema):
    username = fields.Str(required=True,validate=validate.Regexp(Config.GEN_REGEX))
    password = fields.Str(required=True)
    access_token = fields.Str(dump_only=True)


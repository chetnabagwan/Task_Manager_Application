from marshmallow import Schema,fields,validate
from utils.config import Config

class RegisterSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True,validate=validate.Regexp(Config.PWD_REGEX)) 
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone_number = fields.Int(required=True)
    gender = fields.Str(required=True)

class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    access_token = fields.Str(dump_only=True)


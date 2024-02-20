from marshmallow import Schema,fields,validate
from utils.config import Config

class AssignTasksSchema(Schema):
    user_id = fields.Int(required=True)
    task_name = fields.Str(required=True,validate=validate.Regexp(Config.GEN_REGEX))
    task_desc = fields.Str(required=True,validate=validate.Regexp(Config.GEN_REGEX))
    due_date = fields.Date(required=True)
    category =  fields.Str(required=True,validate=validate.Regexp(Config.GEN_REGEX))
    
class CreateTasksSchema(Schema):
    task_name = fields.Str(required=True,validate=validate.Regexp(Config.GEN_REGEX))
    task_desc = fields.Str(required=True,validate=validate.Regexp(Config.GEN_REGEX))
    due_date = fields.Date(required=True)
    category =  fields.Str(required=True,validate=validate.Regexp(Config.GEN_REGEX))
class UserSchema(Schema):
    user_id = fields.Int(required=True)
    username = fields.Str(required=True,validate=validate.Regexp(Config.GEN_REGEX))

class UsersResponseSchema(Schema):
    data = fields.Nested(UserSchema)

class UpdateTaskSchema(Schema):
    task_id = fields.Int(required=True)
    task_name = fields.Str()
    task_desc = fields.Str()
    due_date = fields.Date()
    is_completed = fields.Int()

class UpdateProfileSchema(Schema):
    name = fields.Str()
    email = fields.Str()
    phone_number = fields.Int()
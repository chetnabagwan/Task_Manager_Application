from marshmallow import Schema,fields,validate
from utils.config import Config

class AssignTasksSchema(Schema):
    user = fields.Int(required=True)
    task_name = fields.Str(required=True,validate=validate.Regexp(Config.GEN_REGEX))
    task_desc = fields.Str(required=True,validate=validate.Regexp(Config.GEN_REGEX))
    category =  fields.Str(required=True,validate=validate.Regexp(Config.GEN_REGEX))
    
    


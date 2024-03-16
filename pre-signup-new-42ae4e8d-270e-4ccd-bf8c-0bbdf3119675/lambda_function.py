import json
from utils import validate

def lambda_handler(event, context):
    print(event['userName'])
    if(validate(event['userName'])):
        event['response']['autoConfirmUser'] = True
        event['response']['autoVerifyEmail'] = True
        return event
    else:
        return event
        
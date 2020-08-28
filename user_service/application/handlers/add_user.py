from user_service.application.service.user_service import UserService

user_service = UserService()

def add_user(event, context):
    firstname = event['body']['firstname']
    lastname = event['body']['lastname']
    email = event['body']['email']
    phonenumber = event['body']['phonenumber']
    if user_service.insert_user(firstname, lastname, email, phonenumber):
        return {
                "statusCode": 200,
                "body": firstname+" user inserted successfully"
            }
    else:
        return {
                "statusCode": 500,
                "body": "Failed to add the user "+firstname
            }
    

if __name__ == '__main__':
    event = {
        'body': {
            'firstname': '',
            'lastname': '',
            'phonenumber': '',
            'email': ''
        }
    }
    add_user(event, 'abc')
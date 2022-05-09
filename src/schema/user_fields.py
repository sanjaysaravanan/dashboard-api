""" Model for User """

from flask_restx import fields


def create_user():
    """ Fields definition for User """

    return {
        "firstName": fields.String(
            required=True,
            description="First Name",
            example="Enter first name"
        ),
        "lastName": fields.String(
            required=True,
            description="Last Name",
            example="Enter last name"
        ),
        'email': fields.String(
            required=True,
            description='EmailId of the user',
            pattern=r"^([a-zA-Z0-9_\-\.]+){1,64}@([a-zA-Z0-9_\-\.]+)"
                    r"{1,255}\.([a-zA-Z]{2,5})$",
            example="Enter email"
        ),
        'password': fields.String(
            required=True,
            description='User password',
            pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)'
                    r'(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$',
            example="Enter password"
        )
    }


def login_user():
    """ Fields definition for login user """

    return {
        'email': fields.String(
            required=True,
            description='EmailId of the user',
            pattern=r"^([a-zA-Z0-9_\-\.]+){1,64}@([a-zA-Z0-9_\-\.]+)"
                    r"{1,255}\.([a-zA-Z]{2,5})$",
            example="Enter email"
        ),
        'password': fields.String(
            required=True,
            description='User password',
            pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)'
                    r'(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$',
            example="Enter password"
        )
    }

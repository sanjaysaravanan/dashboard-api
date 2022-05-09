""" Todo Model """

from flask_restx import fields


def todo():
    """ fields description """

    return {
        'description': fields.String(
            required=True,
            description="Describes the todo",
            example="enter a description"
        ),
        'targetDate': fields.DateTime(
            dt_format='ISO_8601',
            required=True,
            description="target or due date for todo"
        ),
        'completed': fields.Boolean(
            required=True,
            default=False,
            description="is todo completed or not"
        ),
        'todoId': fields.String(
            required=True,
            description="Id for the Todo",
            pattern=r'^([a-z0-9])([a-z0-9\-]+)([a-z0-9]'
            + ')$'
        )
    }

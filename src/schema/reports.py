""" Todo Model """

from flask_restx import fields


def report():
    """ fields description """

    return {
        'description': fields.String(
            required=True,
            description="Describes the todo",
            example="enter a description"
        ),
        'name': fields.String(
            required=True,
            description="Name of the Report",
            example="Enter a name for the report",
        ),
        'type': fields.String(
            required=True,
            description="Name of the Report",
            example="Enter a name for the report",
        )
    }

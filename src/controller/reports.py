""" Graph generation Endpoint """

from fastapi import Body
from flask import request
from flask_restx import Namespace, Resource, reqparse
from numpy import true_divide

from service.reports import Reports
from werkzeug.datastructures import FileStorage

from schema.reports import report

upload_parser = reqparse.RequestParser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)
upload_parser.add_argument('name', type=str, location='form')
upload_parser.add_argument('description', type=str, location='form')
upload_parser.add_argument('type', type=str, location='form')

NS = Namespace(
    'reports',
    description='Operations related to tiles'
)

REPORT = NS.model("Report", report())


@NS.route("")
class ReportsController(Resource):
    """ Graph Generation """
    @NS.expect(upload_parser)
    def post(self):
        """ Return file location to Service """
        args = upload_parser.parse_args()
        data = {
            "name": args.get('name', ''),
            "description": args.get('description', ''),
            "type": args.get('type', '')
        }
        return Reports().file_to_dataframe(
            args.get("file", ""), data)

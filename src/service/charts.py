""" Charts Service """
import pandas as pd
import uuid

from service.base import Base


class Charts(Base):
    """ Charts Service """

    def get_all(self):
        """ Get all the Charts """
        reports = list(self.collection.find({}, {"_id": 0}))
        return reports

    def delete_one(self, chart_id):
        """ Delete one Chart """
        try:
            self.collection.delete_one({"id": chart_id})
            return {
              "message": "Chart Deleted Successfully"
            }
        except Exception as ex:
            return {
                "errorMsg": "Something went wrong, please try after some time"
            }

    def save_chart(self, data):
        """ Store a Chart """
        try:

            print(data)

            write_obj = {
              **data,
              "id": str(uuid.uuid4())
            }

            self.collection.insert_one(write_obj)
            return {
              "message": "Chart Created Successfully"
            }
        except Exception as ex:
            print(ex)
            return {
                "errorMsg": "Something went wrong, please try after some time"
            }

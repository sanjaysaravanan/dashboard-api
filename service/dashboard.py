""" Dashboard Service """
from service.base import Base

class Dashboard(Base):
    """ Dashboard Service """

    def get_dashboard(self):
        """ get the layout """
        try:
            dashboard = self.collection.find_one({'id': 'dashboard'}, {"_id": 0})
            if dashboard:
                return dashboard
            else:
                return {}
        except Exception as ex:
            return self.something_went_wrong(ex)

    def save_dashboard(self, data):
        """ Store a Line Chart """
        try:
            write_obj = {
              **data,
              'id': 'dashboard'
            }
            self.collection.update_one({'id': 'dashboard'}, { "$set": write_obj }, upsert=True)
            return {
                "message": "Dash Saved Successfully",
                "updated_data": data
            }
        except Exception as ex:
            return self.something_went_wrong(ex)

""" Todos Service """
from service.base import Base


class Todos(Base):
    """ Todos Service """

    def get_todos(self):
        """ Get all todos """
        items = list(self.collection.find({}, {'_id': 0}))

        if items:
            return {
                'result': items
            }, 200

        return {
            'result': items
        }, 404

    def get_todos_email(self, email):
        """ Returns all the todos for a email """

        items = list(self.collection.find(
            {'userEmail': email}, {'_id': 0, 'userEmail': 0}
        ))

        if items:
            return {
                'result': items
            }, 200

        return {
            'result': items
        }, 404

    def create_one(self, email, data):
        """ Create a todos for a email """

        data['userEmail'] = email
        self.collection.insert_one(data)
        data.pop('_id')

        return {
            'message': 'Todos created for email {}'.format(
                email
            ),
            'item': data
        }, 201

    def get_one(self, email, todo_id):
        """ Get a todo """

        item = self.collection.find_one(
            {'todoId':  todo_id, 'userEmail': email},
            {'_id': 0}
        )

        if item:
            return item, 200

        return {
            'message': 'Todo with id {} not found'.format(
                todo_id
            )
        }, 404

    def update_one(self, email, data, todo_id):
        """ Update a todo """

        item = self.collection.find_one(
            {'todoId':  todo_id, 'userEmail': email}
        )

        if item:
            self.collection.find_and_modify(
                query={"todoId": todo_id},
                update={"$set": data}
            )
            return {
                'message': 'Todo with id {} updated'.format(
                    todo_id
                )
            }, 200

        return {
            'message': 'Todo with id {} not found'.format(
                todo_id
            )
        }, 404

    def delete_one(self, email, todo_id):
        """ Delete a todo """

        result = self.collection.delete_one(
            {'userEmail': email, 'todoId': todo_id}
        )

        if result.deleted_count:
            return {
                'message': 'Todo with id {} deleted'.format(
                    todo_id
                )
            }, 200

        return {
            'message': 'Todo with id {} not found'.format(
                todo_id
            )
        }, 404

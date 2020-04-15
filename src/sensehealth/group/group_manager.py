"""Manager class to create and edit groups."""
from ..user.user import User


class GroupManager(object):
    """Group class to handle data for a group of users."""

    def __init__(self, db_handler):
        """Construct user with key data."""
        self._db_handler = db_handler
        return

    def create_group(self, data):
        """Create group in database."""
        response = self._db_handler.put(
            ['group_data'],
            data,
            auto_id=True
        )
        group_id = response['name']
        for admin in data['admin']:
            User(admin, self._db_handler).add_group(
                group_id,
                data['group_name']
            )
        response = {
            'group_id': response['name'],
            'group_name': data['group_name']
        }
        return response

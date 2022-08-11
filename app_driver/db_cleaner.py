
class DbCleaner:

    def __init__(self, connection):
        self.connection = connection

    def delete_all_users(self):
        with self.connection.cursor(self) as cursor:
            cursor.execute("DELETE * from users")


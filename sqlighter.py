# Import

import sqlite3

# Main Class


class SQLighter:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_report(self, user_id):
        with self.connection:
            self.cursor.execute(
                f"INSERT INTO `persons` (`user_id`, `report`) VALUES ({user_id}, 1)"
            )

    def show_info(self, user_id):
        with self.connection:
            return self.cursor.execute(
                f"SELECT * FROM `persons` WHERE `user_id` = ?", (user_id,)
            ).fetchone()

    def update_report(self, user_id, report):
        with self.connection:
            self.cursor.execute(
                f"UPDATE `persons` SET `report` = {report} WHERE `user_id` = {user_id}"
            )

    def close(self):
        self.connection.close()

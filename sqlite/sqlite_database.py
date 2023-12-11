import sqlite3
from typing import Any

class SQLiteDB:
    def __init__(self, database_name: str):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        
    def get_num_row(self, table_name: str) -> int:
        """
        Find how many rows are there in a table.
        
        :param table_name: Name of the table.
        :return: Number of rows for that table.
        """
        self.cursor.execute(f"SELECT * FROM {table_name};")
        result = self.cursor.fetchall()
        return len(result)
    
    def create_table(self, table_name: str, column_name: list[str], column_datatype: list[str]) -> None:
        """
        Create a table in the database.
        
        :param table_name: The table's name.
        :param column_name: All the column names.
        :param column_datatype: What type of variable each column store. This is not enforced.
        If the input is convertable to column type it will be converted, otherwise it will stay the same.
        """
        self.cursor.execute('BEGIN TRANSACTION;')
        table_string = "("
        for name, datatype in zip(column_name, column_datatype):
            table_string += f"{name} {datatype}, "
        table_string = table_string[:-2]
        table_string += ")"
        self.cursor.execute(f"CREATE TABLE {table_name} {table_string}")
        self.connection.commit()
        
    def insert_row(self, table_name: str, row_content: list[str]) -> None:
        """
        Insert one row into a table.
        
        :param table_name: Table name.
        :param row_content: The content to be put into that row.
        """
        self.cursor.execute('BEGIN TRANSACTION;')
        row_content = tuple(row_content)
        self.cursor.execute(f"INSERT INTO {table_name} VALUES {row_content}")
        self.connection.commit()
        
    def insert_many_rows(self, table_name: str, rows_content: list[tuple[Any]]) -> None:
        """
        Insert many rows into a table.
        
        :param table_name: Table name.
        :param rows_content: A list of tuples with each element in the list representing a row.
        """
        self.cursor.execute("BEGIN TRANSACTION;")
        place_holder = "(" + len(rows_content[0])*"?,"
        place_holder = place_holder[:-1] + ")"
        
        self.cursor.executemany(f"INSERT INTO {table_name} VALUES {place_holder}", rows_content)
        self.connection.commit()
        
    def display_table(self, table_name: str) -> list[tuple[Any]]:
        """
        Display the given table.
        
        :param table_name: The table name you want to display.
        :return: A list with each row represented by a tuple.
        """
        self.cursor.execute(f"SELECT * FROM {table_name};")
        result = self.cursor.fetchall()
        return result
    
    def display_table_with_row_id(self, table_name: str) -> list[tuple[Any]]:
        """
        Display the given table.
        
        :param table_name: The table name you want to display.
        :return: A list with each row represented by a tuple.
        """
        self.cursor.execute(f"SELECT rowid, * FROM {table_name};")
        result = self.cursor.fetchall()
        return result
    
    def display_rowid(self, table_name: str, rowid: int) -> tuple[Any]:
        """
        Display the row with this specific row id.
        It is basically a row id condition.
        
        :param table_name: The table name you want to display.
        :param rowid: The row we are looking for. Rowid begins with 1.
        :return: A tuple representing the row with the corresponding rowid.
        """
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE rowid = {rowid}")
        result = self.cursor.fetchone()
        return result
    
    def display_row_conditional(self, table_name: str, condition: str) -> list[tuple[Any]]:
        """
        Display all rows that satisfies a certain condition.
        
        :param table_name: The table name you want to display.
        :param condition: The condition used for WHERE in SQL
        :return: A list of tuple with each element in the list representing a row that satisfies requirements.
        """
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {condition}")
        result = self.cursor.fetchall()
        return result
    
    def update_row_conditional(self, table_name: str, change: str, condition: str) -> None:
        """
        Update table based on a condition.
        
        :param table_name: The name of the table you want to make changes to.
        :param change: What changes you want to make.
        :param condition: The condition for selecting which row to apply changes to.
        """
        self.cursor.execute("BEGIN TRANSACTION;")
        self.cursor.execute(f"UPDATE {table_name} SET {change} WHERE {condition}")
        self.connection.commit()
        
    def update_rowid(self, table_name: str, change: str, rowid: int) -> None:
        """
        Make changes to the row with given rowid.
        
        :param table_name: The table you want to change.
        :param change: What change you want to make
        :param rowid: The rowid of the row you want to change.
        """
        self.cursor.execute("BEGIN TRANSACTION;")
        self.cursor.execute(f"UPDATE {table_name} SET {change} WHERE rowid = {rowid}")
        self.connection.commit()
        
    def delete_row_conditional(self, table_name: str, condition: str) -> None:
        """
        Delete a row in the table based on which row satisfies the condition.
        
        :param table_name: The table you want to change.
        :param condition: The condition for selecting which row to apply changes to.
        """
        self.cursor.execute("BEGIN TRANSACTION;")
        self.cursor.execute(f"DELETE from {table_name} WHERE {condition}")
        self.connection.commit()
        
    def delete_rowid(self, table_name: str, rowid: str) -> None:
        """
        Delete a row in the table based on rowid
        
        :param table_name: The table to be changed.
        :param rowid: The rowid of the row to be deleted.
        """
        self.cursor.execute("BEGIN TRANSACTION;")
        self.cursor.execute(f"DELETE from {table_name} WHERE rowid={rowid}")
        self.connection.commit()
        
    def display_table_with_order(self, table_name: str, order_by: str = "rowid", order: str = "ASC") -> list[tuple[Any]]:
        """
        Display a table with order.
        
        :param table_name: The table you want to display.
        :param order_by: Display the table that's been ordered by this.
        :param order: The order to display by, can either be ASC for ascending or DESC for descending.
        """
        assert order == "ASC" or order == "DESC", "Order can only be either 'ASC' or 'DESC'"
        self.cursor.execute(f"SELECT rowid, * FROM {table_name} ORDER BY {order_by} {order}")
        result = self.cursor.fetchall()
        return result
        
    def drop_table(self, table_name: str) -> None:
        """
        Delete a table.
        
        :param table_name: The name of the table.
        """
        self.cursor.execute("BEGIN TRANSACTION;")
        self.cursor.execute(f"DROP TABLE {table_name}")
        self.connection.commit()
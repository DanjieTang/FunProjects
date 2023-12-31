from sqlmodel import create_engine, SQLModel, Session, select, desc, and_, or_
from sqlalchemy.sql.expression import BinaryExpression
from sqlalchemy.orm.attributes import InstrumentedAttribute
from dataclass import *
from typing import Any, Iterable


class SQLModelWrapper:
    """
    Wrapper for SQLModel
    
    :param engine: The engine connecting the database.
    """
    def __init__(self, database_name: str):
        sqlite_url = f"sqlite:///{database_name}" # For now, we are only going to use sqlite.
        self.engine = create_engine(sqlite_url)
        SQLModel.metadata.create_all(self.engine) # Create all the tables in dataclass file.
        
    def insert(self, data: SQLModel | list[SQLModel]) -> SQLModel | list[SQLModel]:
        """
        Store data into database.
        
        :param data: The dataclass to be stored into database.
        :return: Same objects as input, but refreshed by database.
        """
        with Session(self.engine) as session:
            if isinstance(data, list):
                # Enter here if data is a list of models
                for object in data:
                    session.add(object)
            else:
                session.add(data)
                
            # Commit data into database
            session.commit()
            
            # Refresh objects
            if isinstance(data, list):
                # Enter here if data is a list of models
                for object in data:
                    session.refresh(object)
            else:
                session.refresh(data)
                
        return data      
                
    
    @staticmethod
    def create_condition(conditions: tuple[Any] | list[Any]) -> BinaryExpression:
        """
        Recursively combine all the conditions into one condition.
        
        :param conditions: Tuples represent or relationship, list represent and relationship. 
               Example: [(Superhero.age > 65, Superhero.age < 18), Superhero.team == 'Avengers'] represents 
               if the age is bigger than 65 or smaller than 18 and they belong to avengers team then True
        :return: One binary Expression that represent all the conditions.
        """
        if isinstance(conditions, list):
            # Compute logical AND for a list, recursively processing each element
            return and_(SQLModelWrapper.create_condition(condition) if isinstance(condition, (list, tuple)) else condition for condition in conditions)
        elif isinstance(conditions, tuple):
            # Compute logical OR for a tuple, recursively processing each element
            return or_(SQLModelWrapper.create_condition(condition) if isinstance(condition, (list, tuple)) else condition for condition in conditions)
        else:
            raise ValueError("Input must be a list or a tuple")
    
    @staticmethod
    def create_statement(tables: Iterable[SQLModel] | SQLModel, conditions: BinaryExpression | list[Any] | tuple[Any] | None, order_by: InstrumentedAttribute = None, increment: bool = True) -> BinaryExpression:
        """
        Create statement for performing SQL query.
        
        :param tables: The tables you want to retrieve.
        :param conditions: Tuples represent or relationship, list represent and relationship. 
               Example: [(Superhero.age > 65, Superhero.age < 18), Superhero.team == 'Avengers'] represents 
               if the age is bigger than 65 or smaller than 18 and they belong to avengers team then True
        """
        # Table selection.
        if isinstance(tables, Iterable):
            # Select all given tables
            statement = select(*tables)
            
            # Join all tables after the first one
            for table in tables[1:]:
                statement = statement.join(table)
        else:
            # If user simply provided one table. Select directly.
            statement = select(tables)
        
        # Add in conditions.
        if isinstance(conditions, BinaryExpression):
            statement = statement.where(conditions)
        elif isinstance(conditions, (list, tuple)):
            conditions = SQLModelWrapper.create_condition(conditions) # This combines all the conditions into one long condition
            statement = statement.where(conditions)
            
        # If user has explicitly want result to be in some order.
        if order_by:
            if increment:
                statement = statement.order_by(order_by)
            else:
                statement = statement.order_by(desc(order_by))
            
        return statement
    
    def select_id(self, table: SQLModel, id: int) -> SQLModel | None:
        """
        Retrieve one record from a table using id.
        
        :param table: The table you want to retrieve.
        :param id: The specific id of the record you want to retrieve.
        :return: The sqlmodel object representing the record. Return None when none can be found.
        """
        with Session(self.engine) as session:
            data = session.get(table, id)
        
        return data
    
    def select_one(self, tables: Iterable[SQLModel] | SQLModel, conditions: BinaryExpression | list[Any] | tuple[Any] | None = None) -> SQLModel | None:
        """
        Retrieve one record from a tables. It will only return the record if there is exactly 
        one record that matches the condition. If more than one or less than one meets the condition, it will
        raise an error.
        
        :param tables: The tables you want to retrieve.
        :param conditions: Tuples represent or relationship, list represent and relationship. 
               Example: [(Superhero.age > 65, Superhero.age < 18), Superhero.team == 'Avengers'] represents 
               if the age is bigger than 65 or smaller than 18 and they belong to avengers team then True
        :return: The sqlmodel object representing the record if found. Otherwise return None.
        """
        statement = SQLModelWrapper.create_statement(tables, conditions)
        
        with Session(self.engine) as session:
            data = session.exec(statement).one()
        return data
        
    def select_first(self, tables: Iterable[SQLModel] | SQLModel, conditions: BinaryExpression | list[Any] | tuple[Any] | None = None, order_by: InstrumentedAttribute = None, increment: bool = True) -> SQLModel | None:
        """
        Retrieve one record from a tables. If more than one record satisfies the condition, return the first one.
        If none statisfies the condition, return None.
        
        :param tables: The tables you want to retrieve.
        :param conditions: Tuples represent or relationship, list represent and relationship. 
               Example: [(Superhero.age > 65, Superhero.age < 18), Superhero.team == 'Avengers'] represents 
               if the age is bigger than 65 or smaller than 18 and they belong to avengers team then True
        :param order_by: The order to organize result.
        :param increment: Are we ordering by increment or decrement.
        :return: The sqlmodel object representing the record if found. Otherwise return None.
        """
        statement = SQLModelWrapper.create_statement(tables, conditions, order_by, increment)
        
        with Session(self.engine) as session:
            data = session.exec(statement).first()
            
        return data
        
    def select_many(self, tables: Iterable[SQLModel] | SQLModel, conditions: BinaryExpression | list[Any] | tuple[Any] | None = None, order_by: InstrumentedAttribute = None, increment: bool = True, limit: int = 1, offset: int = 0) -> list[SQLModel]:
        """
        Retrieve many records from a tables.
        
        :param tables: The tables you want to retrieve.
        :param conditions: Tuples represent or relationship, list represent and relationship. 
               Example: [(Superhero.age > 65, Superhero.age < 18), Superhero.team == 'Avengers'] represents 
               if the age is bigger than 65 or smaller than 18 and they belong to avengers team then True
        :param order_by: The order to organize result.
        :param increment: Are we ordering by increment or decrement.
        :param limit: Return a maximum of {limit} number of SQLModels in a list. The actual returned result might 
                      be fewer if there's not enough satisfies the statement.
        :param offset: Start returning from 
        :return: A list of SQLModels. Only returning the sqlmodels that satifies the statement. If none statisfies, return an 
                 empty list.
        """
        statement = SQLModelWrapper.create_statement(tables, conditions, order_by, increment)
        
        with Session(self.engine) as session:
            data = session.exec(statement.offset(offset).limit(limit)).all()
            
        return data
        
    def select(self, tables: Iterable[SQLModel] | SQLModel, conditions: BinaryExpression | list[Any] | tuple[Any] | None = None, order_by: InstrumentedAttribute = None, increment: bool = True) -> list[SQLModel]:
        """
        Retrieve all records that statifies the statement.
        
        :param tables: The tables you want to retrieve.
        :param conditions: Tuples represent or relationship, list represent and relationship. 
               Example: [(Superhero.age > 65, Superhero.age < 18), Superhero.team == 'Avengers'] represents 
               if the age is bigger than 65 or smaller than 18 and they belong to avengers team then True
        :param order_by: The order to organize result.
        :param increment: Are we ordering by increment or decrement.
        """
        statement = SQLModelWrapper.create_statement(tables, conditions, order_by, increment)
        
        with Session(self.engine) as session:
            data = session.exec(statement).all()
                
        return data
        
    def delete(self, data: SQLModel | list[SQLModel]) -> bool:
        """
        Remove given data from database.
        
        :param data: Either one or many sqlmodel objects representing records that are to be deleted from database.
        :return: If successful deleted, return True. Otherwise return False.
        """
        try:
            with Session(self.engine) as session:
                if isinstance(data, list):
                    # Enter here if data is a list of SQLModel objects
                    for element in data:
                        session.delete(element)
                else:
                    session.delete(data)
                session.commit()
            return True
        except:
            return False
                    
        
    def delete_statement(self, tables: Iterable[SQLModel] | SQLModel, conditions: BinaryExpression | list[Any] | tuple[Any] | None = None) -> bool:
        """
        Remove some records from database based on tables and statement.
        
        :param tables: The tables you want to retrieve.
        :param conditions: Tuples represent or relationship, list represent and relationship. 
               Example: [(Superhero.age > 65, Superhero.age < 18), Superhero.team == 'Avengers'] represents 
               if the age is bigger than 65 or smaller than 18 and they belong to avengers team then True
        :return: Return True if successfully removed record, False otherwise.
        """
        objects = self.select(tables, conditions)
        return self.delete(objects)
from sqlalchemy import create_engine, and_, or_, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import BinaryExpression
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql import select
from dataclass import *
from typing import Any, Iterable
from sqlalchemy.orm import sessionmaker

class SQLAlchemyWrapper():
    def __init__(self, storage_name: str = ""):
        database_url = f"sqlite:///{storage_name}" # For now, we are only going to use sqlite.
        self.engine = create_engine(database_url)
        Base.metadata.create_all(bind=self.engine)
        self.Session = sessionmaker(bind=self.engine)
        
    def insert(self, data = Base | list[Base]) -> None:
        """
        Store data into database.
        
        :param data: The dataclass to be stored into database.
        """
        with self.Session() as session:
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
            return and_(SQLAlchemyWrapper.create_condition(condition) if isinstance(condition, (list, tuple)) else condition for condition in conditions)
        elif isinstance(conditions, tuple):
            # Compute logical OR for a tuple, recursively processing each element
            return or_(SQLAlchemyWrapper.create_condition(condition) if isinstance(condition, (list, tuple)) else condition for condition in conditions)
        else:
            raise ValueError("Input must be a list or a tuple")
            
    @staticmethod
    def create_statement(session: sessionmaker, tables: Iterable[Base] | Base, conditions: BinaryExpression | list[Any] | tuple[Any] | None, order_by: InstrumentedAttribute = None, increment: bool = True, limit: int | None = None, offset: int | None = None) -> BinaryExpression:
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
            statement = session.query(tables[0])
            
            # Join all tables after the first one
            for table in tables[1:]:
                statement = statement.join(table)
        else:
            # If user simply provided one table. Select directly.
            statement = session.query(tables)
        
        # Add in conditions.
        if isinstance(conditions, BinaryExpression):
            statement = statement.filter(conditions)
        elif isinstance(conditions, (list, tuple)):
            conditions = SQLAlchemyWrapper.create_condition(conditions) # This combines all the conditions into one long condition
            statement = statement.filter(conditions)
            
        # If user has explicitly want result to be in some order.
        if order_by:
            if increment:
                statement = statement.order_by(order_by)
            else:
                statement = statement.order_by(desc(order_by))
                
        if offset:
            statement = statement.offset(offset)
            
        if limit:
            statement = statement.limit(limit)
            
        return statement
    
    def select_id(self, table: Base, id: int) -> Base | None:
        """
        Retrieve one record from a table using id.
        
        :param table: The table you want to retrieve.
        :param id: The specific id of the record you want to retrieve.
        :return: The sqlmodel object representing the record. Return None when none can be found.
        """
        with self.Session() as session:
            data = session.get(table, id)
        
            return data
        
    def select_one(self, tables: Iterable[Base] | Base, conditions: BinaryExpression | list[Any] | tuple[Any] | None = None) -> Base | None:
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
        with self.Session() as session:
            data = SQLAlchemyWrapper.create_statement(session, tables, conditions).one()
            return data
        
    def select_first(self, tables: Iterable[Base] | Base, conditions: BinaryExpression | list[Any] | tuple[Any] | None = None) -> Base | None:
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
        with self.Session() as session:
            data = SQLAlchemyWrapper.create_statement(session, tables, conditions).first()
            return data
        
    def select_many(self, tables: Iterable[Base] | Base, conditions: BinaryExpression | list[Any] | tuple[Any] | None = None, order_by: InstrumentedAttribute = None, increment: bool = True, limit: int | None = None, offset: int | None = None) -> list[Base]:
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
        with self.Session() as session:
            data = SQLAlchemyWrapper.create_statement(session, tables, conditions, order_by=order_by, increment=increment, limit=limit, offset=offset).all()
            return data
        
    def select(self, tables: Iterable[Base] | Base, conditions: BinaryExpression | list[Any] | tuple[Any] | None = None, order_by: InstrumentedAttribute = None, increment: bool = True) -> list[Base]:
        """
        Retrieve all records that statifies the statement.
        
        :param tables: The tables you want to retrieve.
        :param conditions: Tuples represent or relationship, list represent and relationship. 
               Example: [(Superhero.age > 65, Superhero.age < 18), Superhero.team == 'Avengers'] represents 
               if the age is bigger than 65 or smaller than 18 and they belong to avengers team then True
        :param order_by: The order to organize result.
        :param increment: Are we ordering by increment or decrement.
        """
        with self.Session() as session:
            data = SQLAlchemyWrapper.create_statement(session, tables, conditions, order_by=order_by, increment=increment).all()
            return data
        
    def delete(self, data: Base | list[Base]) -> bool:
        """
        Remove given data from database.
        
        :param data: Either one or many sqlmodel objects representing records that are to be deleted from database.
        :return: If successful deleted, return True. Otherwise return False.
        """
        try:
            with self.Session() as session:
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
                    
        
    def delete_statement(self, tables: Iterable[Base] | Base, conditions: BinaryExpression | list[Any] | tuple[Any] | None = None) -> bool:
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
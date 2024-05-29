from dataclass import *
from sqlalchemy import create_engine
from sqlalchemy_wrapper import SQLAlchemyWrapper

database = SQLAlchemyWrapper("test", database="postgres")

team1 = Team(name = "Iron Man's team")
database.insert(team1)

hero1 = Superhero(name="Iron Man", real_name="Tony Stark", team_id=team1.id, age=40)
hero2 = Superhero(name="Spider Man", real_name="Peter Parker", team_id=team1.id, age=16)
hero3 = Superhero(name="Black Panther", real_name="Tony Stark", team_id=team1.id, age=32)
database.insert([hero1, hero2, hero3])

team2 = Team(name = "Captain America's team")
database.insert(team2)

hero4 = Superhero(name="Captain America", real_name="Steve Rogers", team_id=team2.id, age=100)
database.insert(hero4)

# spider_man = database.select_one(Superhero, Superhero.name == "Spider Man")
# database.delete(spider_man)

database.delete_statement(Superhero, Superhero.age > 16)

for superhero in database.select(Superhero, Superhero.team_id == team1.id):
    print(superhero.name)
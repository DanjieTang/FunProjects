from dataclass import *
from sqlalchemy import create_engine
from sqlalchemy_wrapper import SQLAlchemyWrapper

database = SQLAlchemyWrapper("test")

############ Insert into database #################
team1 = Team(name = "Iron Man's team")
database.insert(team1)

hero1 = Superhero(name="Iron Man", real_name="Tony Stark", team_id=team1.id, age=40)
hero2 = Superhero(name="Spider Man", real_name="Peter Parker", team_id=team1.id, age=16)
hero3 = Superhero(name="Black Panther", real_name="T'challa", team_id=team1.id, age=32)
database.insert([hero1, hero2, hero3])

team2 = Team(name = "Captain America's team")
database.insert(team2)

hero4 = Superhero(name="Captain America", real_name="Steve Rogers", team_id=team2.id, age=100)
hero5 = Superhero(name="Ant Man", real_name="Scott Lang", team_id=team2.id, age=31)
database.insert([hero4, hero5])

############ Select from database #################
heros = database.select(Superhero) # Select all heros

# Here's all the heros
for hero in heros:
    print(hero.name)
print()
    
# Here's all the teenager heros
teenager_heros = database.select(Superhero, [Superhero.age < 18])
for hero in teenager_heros:
    print(hero.name)
print()

# Here's all the teenager heros OR heros with name == "Captain America"
heros = database.select(Superhero, (Superhero.name == "Captain America", Superhero.age < 18))
for hero in heros:
    print(hero.name)
print()

# Here's all heros on Iron Man's team AND above the age of 20
heros = database.select(Superhero, [Superhero.team_id == team1.id, Superhero.age > 20])
for hero in heros:
    print(hero.name)
print()

# If I know that 100% there's only one record that satisfies this condition.
# If there's more than 1 or less than 1 then will run into error.
hero = database.select_one(Superhero, Superhero.name == "Iron Man")
print(hero.real_name)

############ Update database #################

# It's spiderman's birthday
spider_man = database.select_one(Superhero, Superhero.name == "Spider Man")
spider_man.age += 1
database.insert(spider_man)


############ Delete from database #################

# If I want to delete one specific record
spider_man = database.select_one(Superhero, Superhero.name == "Spider Man")
database.delete(spider_man)
heros = database.select(Superhero) # Select all heros

# Here's all the heros
for hero in heros:
    print(hero.name)
print()

# Deleting everything in these 2 tables.
database.delete_statement(Superhero)
database.delete_statement(Team)
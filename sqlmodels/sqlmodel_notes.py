from sqlmodel import create_engine, SQLModel, Session, select, or_
from dataclass import *

# Database file name
file_name = "database.db"

# Keeping the engine as a global parameter.
sqlite_url = f"sqlite:///{file_name}" # For now we are going to be running on sqlite
engine = create_engine(sqlite_url)
SQLModel.metadata.create_all(engine) # Create all the tables.

# Create hero
# Add heros into database
with Session(engine) as session:
    hero1 = Superhero(name="Tony Stark", hero_name="Iron Man")
    hero2 = Superhero(name="Steve Rogers", hero_name="Captain America")
    hero3 = Superhero(name="Peter Parker", hero_name="Spider Man")
    session.add(hero1)
    session.add(hero2)
    session.add(hero3)
    session.commit()
    
    # If want to access the entire object after commiting use refresh
    session.refresh(hero1)
    hero1 # Now you can access hero1
    # Or simply access any attribute of an object and it will refresh automatically
    hero2.name

# View the table
with Session(engine) as session:
    table = session.exec(select(Superhero)).all()
    
# Create 2 teams
with Session(engine) as session:
    team1 = Team(name="Iron man team", headquarter="Stark Tower")
    team2 = Team(name="Cap's team", headquarter="Shield")
    session.add(team1)
    session.add(team2)
    session.commit()
    
# Update those heros team information
with Session(engine) as session:
    team1 = session.exec(select(Team).where(Team.name == "Iron man team")).one()
    team2 = session.exec(select(Team).where(Team.name == "Cap's team")).one()
    
    iron_man = session.exec(select(Superhero).where(Superhero.hero_name == "Iron Man")).one()
    iron_man.team_id = team1.id
    
    captain = session.exec(select(Superhero).where(Superhero.hero_name == "Captain America")).one()
    captain.team_id = team2.id
    
    spider_man = session.exec(select(Superhero).where(Superhero.hero_name == "Spider Man")).one()
    spider_man.team_id = team1.id
    
    session.add(iron_man)
    session.add(captain)
    session.add(spider_man)
    session.commit()
    
# View the table
with Session(engine) as session:
    table = session.exec(select(Superhero)).all()
    
# Remove a record
with Session(engine) as session:
    # Some magic wizard cast a spell and everyone forgets about spider man
    spider_man = session.exec(select(Superhero).where(Superhero.name == "Peter Parker")).one()
    session.delete(spider_man)
    session.commit()
    
# View the table
with Session(engine) as session:
    table = session.exec(select(Superhero)).all()
    
# Add spider man back
with Session(engine) as session:
    # Some magic wizard cast a spell and everyone forgets about spider man
    spider_man = Superhero(name="Peter Parker", hero_name="Spider Man")
    team1 = session.exec(select(Team).where(Team.name == "Iron man team")).one()
    spider_man.team_id = team1.id
    session.add(spider_man)
    session.commit()
    
# Update all heros to have age tag
with Session(engine) as session:
    iron_man = session.exec(select(Superhero).where(Superhero.name == "Tony Stark")).one()
    spider_man = session.exec(select(Superhero).where(Superhero.name == "Peter Parker")).one()
    captain = session.exec(select(Superhero).where(Superhero.name == "Steve Rogers")).one()
    
    iron_man.age = 50
    spider_man.age = 16
    captain.age = 100
    
    session.add(iron_man)
    session.add(spider_man)
    session.add(captain)
    session.commit()
    
# View the table
with Session(engine) as session:
    table = session.exec(select(Superhero)).all()
    # print(table)
   
# Condition select 
with Session(engine) as session:
    allowed_to_drink = session.exec(select(Superhero).where(Superhero.age >= 19)).all() # I live in Ontario
    # print(allowed_to_drink)
    
    # But only iron man's team is having a party
    team = session.exec(select(Team).where(Team.name == "Iron man team")).one()
    drinking = session.exec(select(Superhero).where(Superhero.age >=19, Superhero.team_id == team.id)).all()
    # print(drinking)
    
    # These are the heros that are jealous
    # Or condition
    jealous = session.exec(select(Superhero).where(or_(Superhero.age < 19, Superhero.team_id != team.id))).all()
    # print(jealous)
    
# Display hero with team information
# Displaying information across multiple tables.
with Session(engine) as session:
    all_heros = session.exec(select(Superhero, Team).join(Team)).all()
    # for hero, team in all_heros:
    #     print(hero, team)
        
# Relationship
with Session(engine) as session:
    spider_man = session.exec(select(Superhero).where(Superhero.name == "Peter Parker")).one()
    
    # For some reason spider man decided to quit iron team
    spider_man.team = None
    session.add(spider_man)
    session.commit()
    
# View the table
with Session(engine) as session:
    table = session.exec(select(Superhero)).all()
    # print(table)
    
# Relationship
with Session(engine) as session:
    captain_team = session.exec(select(Team).where(Team.name == "Cap's team")).one()
    spider_man = session.exec(select(Superhero).where(Superhero.name == "Peter Parker")).one()
    
    # For some reason spider man decided to quit iron team
    spider_man.team = captain_team
    session.add(spider_man)
    session.commit()
    
# View the table
with Session(engine) as session:
    table = session.exec(select(Team, Superhero).join(Superhero)).all()
    # for team, hero in table:
    #     print(team, hero)
            
# Access spider man's team
with Session(engine) as session:
    spider_man = session.exec(select(Superhero).where(Superhero.name == "Peter Parker")).one()
    print(spider_man.team)
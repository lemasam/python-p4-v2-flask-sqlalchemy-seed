!/usr/bin/env python3
server/seed.py

from app import app
from models import db, Pet

with app.app_context():

    # Detele all rows in the "pets" table
    Pet.query.delete()
    
    #   create an empty list 
    pets =[]
    
    # Add some Pet instances to the list
    pets.append(Pet(name="Fido", species="Dog"))
    pets.append(Pet(name="whiskers", species="Cat"))
    pets.append(Pet(name="Hermie", species="Hamster"))
    pets.append(Pet(name="Slither", species="Snake"))
    
    # insert each Pet in the list into database table
    db.session.add_all(pets)
    
    # commit the transaction
    db.session.commit()
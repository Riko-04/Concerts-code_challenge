from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert  # Import your models

# Connect to the database
engine = create_engine('sqlite:///db/concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

# Drop all tables and create them again
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Seed data
def seed_data():
    # Create instances of Band
    band1 = Band(name="The Rolling Stones", hometown="London")
    band2 = Band(name="The Beatles", hometown="Liverpool")

    # Create instances of Venue
    venue1 = Venue(title="Madison Square Garden", city="New York")
    venue2 = Venue(title="The O2 Arena", city="London")

    # Add bands and venues to the session
    session.add_all([band1, band2, venue1, venue2])
    session.commit()

    # Create instances of Concert
    concert1 = Concert(date="2023-06-01", band_id=band1.id, venue_id=venue1.id)
    concert2 = Concert(date="2023-07-01", band_id=band1.id, venue_id=venue2.id)
    concert3 = Concert(date="2023-08-01", band_id=band2.id, venue_id=venue1.id)

    # Add concerts to the session
    session.add_all([concert1, concert2, concert3])
    session.commit()

# Run the seed function
if __name__ == "__main__":
    seed_data()
    print("Database seeded successfully!")

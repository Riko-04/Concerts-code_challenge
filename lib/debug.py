# debug.py

import logging
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Band, Venue, Concert, Base

# Configure logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Connect to the database
engine = create_engine('sqlite:///db/test_db.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()

# Create tables if they don't exist
Base.metadata.create_all(engine)

# Query all bands
bands = session.query(Band).all()
print("Bands:")
for band in bands:
    print(f"Band: {band.name}, Hometown: {band.hometown}")

# Query all venues
venues = session.query(Venue).all()
print("\nVenues:")
for venue in venues:
    print(f"Venue: {venue.title}, City: {venue.city}")

# Query all concerts
concerts = session.query(Concert).all()
print("\nConcerts:")
for concert in concerts:
    band = session.query(Band).filter_by(id=concert.band_id).first()
    venue = session.query(Venue).filter_by(id=concert.venue_id).first()
    print(f"Concert: {band.name} at {venue.title} on {concert.date}")

# 1. Adding a New Band
new_band = Band(name="Pink Floyd", hometown="Cambridge")
session.add(new_band)
session.commit()
print(f"\nAdded new band: {new_band.name}, Hometown: {new_band.hometown}")

# 2. Adding a New Venue
new_venue = Venue(title="Wembley Stadium", city="London")
session.add(new_venue)
session.commit()
print(f"Added new venue: {new_venue.title}, City: {new_venue.city}")

# 3. Adding a New Concert
new_concert = Concert(date="2023-09-01", band_id=new_band.id, venue_id=new_venue.id)
session.add(new_concert)
session.commit()
print(f"Added new concert: {new_band.name} at {new_venue.title} on {new_concert.date}")

# 4. Querying All Bands from a Specific Hometown
bands_from_london = session.query(Band).filter_by(hometown="London").all()
print("\nBands from London:")
for band in bands_from_london:
    print(f"Band: {band.name}, Hometown: {band.hometown}")

# 5. Querying All Concerts for a Specific Band
rolling_stones_concerts = session.query(Concert).join(Band).filter(Band.name == "The Rolling Stones").all()
print("\nConcerts by The Rolling Stones:")
for concert in rolling_stones_concerts:
    venue = session.query(Venue).filter_by(id=concert.venue_id).first()
    print(f"Concert at {venue.title} on {concert.date}")

# 6. Updating a Band's Hometown
band_to_update = session.query(Band).filter_by(name="The Beatles").first()
if band_to_update:
    band_to_update.hometown = "Manchester"
    session.commit()
    print(f"Updated {band_to_update.name}'s hometown to {band_to_update.hometown}")

# 7. Deleting a Concert
concert_to_delete = session.query(Concert).filter_by(date="2023-09-01").first()
if concert_to_delete:
    session.delete(concert_to_delete)
    session.commit()
    print(f"Deleted concert on {concert_to_delete.date}")

session.close()

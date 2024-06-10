from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Band, Venue, Concert

# Connect to the database
engine = create_engine('sqlite:///db/test_db.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()

def list_bands():
    bands = session.query(Band).all()
    print("Bands:")
    for band in bands:
        print(f"Band ID: {band.id}, Name: {band.name}, Hometown: {band.hometown}")

def list_venues():
    venues = session.query(Venue).all()
    print("Venues:")
    for venue in venues:
        print(f"Venue ID: {venue.id}, Title: {venue.title}, City: {venue.city}")

def list_concerts():
    concerts = session.query(Concert).all()
    print("Concerts:")
    for concert in concerts:
        band = session.query(Band).filter_by(id=concert.band_id).first()
        venue = session.query(Venue).filter_by(id=concert.venue_id).first()
        print(f"Concert ID: {concert.id}, Band: {band.name}, Venue: {venue.title}, Date: {concert.date}")

def add_band(name, hometown):
    new_band = Band(name=name, hometown=hometown)
    session.add(new_band)
    session.commit()
    print(f"Added new band: ID: {new_band.id}, Name: {new_band.name}, Hometown: {new_band.hometown}")

def add_venue(title, city):
    new_venue = Venue(title=title, city=city)
    session.add(new_venue)
    session.commit()
    print(f"Added new venue: ID: {new_venue.id}, Title: {new_venue.title}, City: {new_venue.city}")

def add_concert(date, band_id, venue_id):
    new_concert = Concert(date=date, band_id=band_id, venue_id=venue_id)
    session.add(new_concert)
    session.commit()
    print(f"Added new concert: ID: {new_concert.id}, Date: {new_concert.date}, Band ID: {new_concert.band_id}, Venue ID: {new_concert.venue_id}")

def main():
    while True:
        print("\nChoose an option:")
        print("1. List Bands")
        print("2. List Venues")
        print("3. List Concerts")
        print("4. Add Band")
        print("5. Add Venue")
        print("6. Add Concert")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_bands()
        elif choice == "2":
            list_venues()
        elif choice == "3":
            list_concerts()
        elif choice == "4":
            name = input("Enter band name: ")
            hometown = input("Enter band hometown: ")
            add_band(name, hometown)
        elif choice == "5":
            title = input("Enter venue title: ")
            city = input("Enter venue city: ")
            add_venue(title, city)
        elif choice == "6":
            date = input("Enter concert date (YYYY-MM-DD): ")
            band_id = int(input("Enter band ID: "))
            venue_id = int(input("Enter venue ID: "))
            add_concert(date, band_id, venue_id)
        elif choice == "0":
            print("Goodbye!!!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

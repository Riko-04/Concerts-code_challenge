import os
import sys
from sqlalchemy import func as sa

sys.path.append(os.getcwd())

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///db/concerts.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)

    concerts = relationship('Concert', back_populates='band')

    def __repr__(self):
        return f'Band: {self.name}'

    def venues(self):
        return {concert.venue for concert in self.concerts}

    def play_in_venue(self, venue, date):
        new_concert = Concert(band_id=self.id, venue_id=venue.id, date=date)
        session.add(new_concert)
        session.commit()

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]

    @classmethod
    def most_performances(cls):
        return session.query(cls).join(Concert).group_by(cls.id).order_by(sa.func.count(Concert.id).desc()).first()

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)

    concerts = relationship('Concert', back_populates='venue')

    def __repr__(self):
        return f'Venue: {self.title}'

    def bands(self):
        return {concert.band for concert in self.concerts}

    def concert_on(self, date):
        return session.query(Concert).filter_by(venue_id=self.id, date=date).first()

    def most_frequent_band(self):
        return session.query(Band).join(Concert).filter_by(venue_id=self.id).group_by(Band.id).order_by(sa.func.count(Concert.id).desc()).first()

class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    band_id = Column(Integer, ForeignKey('bands.id'), nullable=False)
    venue_id = Column(Integer, ForeignKey('venues.id'), nullable=False)

    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def __repr__(self):
        return f'Concert: {self.band.name} at {self.venue.title} on {self.date}'

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

# Create tables
Base.metadata.create_all(engine)

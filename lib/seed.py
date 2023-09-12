#!/usr/bin/env python3

# Script goes here!

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebies

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Seed some sample data
company1 = Company(name="Company A", founding_year=1990)
company2 = Company(name="Company B", founding_year=2000)

dev1 = Dev(name="Developer 1")
dev2 = Dev(name="Developer 2")

session.add_all([company1, company2, dev1, dev2])
session.commit()

import click
from models import Base, Country, Landmark
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///world_landmarks.db'  # Change this if you want to use a different database

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('country_name')
def add_country(country_name):
    new_country = Country(name=country_name)
    session.add(new_country)
    session.commit()
    click.echo(f"Added {country_name} to the database.")

@cli.command()
def list_countries():
    countries = session.query(Country).all()
    for country in countries:
        click.echo(country.name)

@cli.command()
@click.argument('country_name')
@click.argument('landmark_name')
@click.argument('city_name')
def add_landmark(country_name, landmark_name, city_name):
    country = session.query(Country).filter_by(name=country_name).first()
    if not country:
        click.echo(f"Country {country_name} not found.")
        return

    new_landmark = Landmark(name=landmark_name, city=city_name, country=country)
    session.add(new_landmark)
    session.commit()
    click.echo(f"Added {landmark_name} in {country_name}.")

@cli.command()
@click.argument('country_name')
def list_landmarks(country_name):
    country = session.query(Country).filter_by(name=country_name).first()
    if not country:
        click.echo(f"Country {country_name} not found.")
        return

    click.echo(f"Landmarks in {country_name}:")
    for landmark in country.landmarks:
        click.echo(f"- {landmark.name} in {landmark.city}")

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    cli()

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
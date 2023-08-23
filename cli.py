
DATABASE_URL = 'sqlite:///world_landmarks.db'  # Change this if you want to use a different database

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass
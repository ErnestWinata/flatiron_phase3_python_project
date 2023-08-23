

class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
  

class Landmark(Base):
   __tablename__ = 'landmarks'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String)
    visited = Column(Boolean, default=False)
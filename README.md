World Landmark CLI Application
Phase 3 Project for Flatiron School

This CLI application allows users to manage world landmarks, including adding countries, landmarks, and marking landmarks as visited.

Features of this application:
- add a new country to the database
- list all countries in the database
- add a landmark to a specific country
- list landmarks for a specific country
- mark landmarks as visited

Installation

1. Clone this repo to your local machine
   https://github.com/ErnestWinata/flatiron_phase3_python_project
2. Install the required dependencies using Pipenv
   pipenv install
3. Create the database tables
   pipenv run python cli.py
4. Run the CLI Application
   - to add a country
     pipenv run python cli.py add-country "Country"

   - to list countries
     pipenv run python cli.py list-countries

   - to add a landmark
     pipenv run python cli.py add-landmark "Country" "Landmark" "City"

   - to list a landmark in a particular country
     pipenv run python cli.py list-landmarks "Country"

   - to mark as having visited a landmark
     pipenv run python cli.py mark-visited "Country" "Landmark"

5. To exit the virtual environment
      exit

Contributing
Contributions and collaborations are welcome! Please submit a pull request if you find any issues or want to enhance the application.

License
This project is licensed under the MIT License - see the LICENSE file for details.

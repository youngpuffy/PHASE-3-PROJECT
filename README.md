# PHASE-3-PROJECT
 this is a simple WIFI management system that simulates user account creation, payment handling, and active WIFI session tracking using python and SQLite.

 ## Project Structure
 PHASE-3-PROJECT/
│
├── lib/
│   ├── db/
│   │   ├── connection.py       # Database connection and initialization
│   │   └── init.sql            # SQL script to set up DB tables
│   ├── models/
│   │   ├── user.py             # User model
│   │   ├── payment.py          # Payment model
│   │   └── wifi_session.py     # WiFi session model
│   └── scripts/
│       └── run_example.py      # Script to simulate user creation, payments, and sessions
│
├── main.py                     # Entry point to run the simulation
├── Pipfile                     # Project dependencies
├── Pipfile.lock                # Locked versions of dependencies
└── README.md                   # This file

## Features
- creates user account with unique usernames
- user-related payment tracking
- able to start and track active WIFI sessions
- fetching active session for any user.


## Requirements 
- python 3.8+
- pipenv for dependency management

## installation and Setup
1. Clone the repository
git clone https://github.com/youngpuffy/PHASE-3-PROJECT.git

cd PHASE-3-PROJECT

2. Install dependencies
using pipenv
-pipenv install
-pipenv shell

3. Database initialization
first ensure the init.sql contains the table creation scripts.
it will be initialized automatically when you run the program for the first time.

## Running the Application
having installed the pipenv in the terminal pipenv shell to activate a virtual environment with your dependencies, then  use the below method to show the output.
 python3 main.py

 you can also run the application in the root directory of the project
 using:  python3 main.py
 
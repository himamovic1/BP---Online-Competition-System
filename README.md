# Online Competition System
## Tim 10

Repository for a semestral project

## Requirements
- Python 3.6
- JetBrains Pycharm 2017 (Community will do just fine)
- PostgreSQL (9.6 preferably, or newer)
- psqlODBC (09.06 preferably, or newer)

#### Optional 
- PgAdmin 4

## How To
### Configure mail:
Before running PyCharm add two environment variables:
```
SETX ETF_FLASK_MAIL_USERNAME "place your email here"
SETX ETF_FLASK_MAIL_MAGIC_WORD "place your email pw here"
```
  
 On linux OS change SETX with export.
 Depending on e-mail client, you may need to configure settings in your e-mail client
 
### Server side:
  - Create a dedicated virtual environment (To be explained later)
  - Navigate to project root directory and run: ```pip install -r requirements\dev.txt" command.```
  - Run dbinit.py script to initialize the database (this is needed only once, when running the app for the first time) ```~\ETF-COMPETITION> python dbinit.py```
  - Run application ```~\ETF-COMPETITION> python run_app.py```

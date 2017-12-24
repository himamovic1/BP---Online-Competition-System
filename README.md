# Online Competition System
## Tim 10

Repository for a semestral project

## Requirements
- Python 3.6
- JetBrains Pycharm 2017 (Community will do just fine)
- PostgreSQL (9.6 preferably, or newer)
- psqlODBC (09.06 preferably, or newer)
- Oracle Instant Client (Basic version will do just fine), don't forget to set up PATH variable.
- cx_Oracle-5.3, install from project root directory:```pip install cx_Oracle-5.3+oci12c-cp36-cp36m-win_amd64.whl```
  if you need different version of cx_Oracle you can [download from here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_oracle)

#### Optional 
- PgAdmin 4

## How To
### Configure mail:
Prije pokretanja PyCharm-a dodati dvije environment varijable sa naredbama:
- SETX ETF_FLASK_MAIL_USERNAME "place your email here"
- SETX ETF_FLASK_MAIL_MAGIC_WORD "place your email pw here"
  
 U zavisnosti od mail-a koji koristite možda će biti potrebno promijeniti neke postavke u samom mail clientu
 
### Server side:
  - Create a dedicated virtual environment (To be explained later)
  - Navigate to project root directory and run: ```pip install -r requirements\dev.txt" command.```

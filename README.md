## INSTRUCTION TO GENERATE THE DATABASE FROM THE DUMP FILE

The dump file is stored as dump.sql inside the given folder
Assume the folder name is A and it is stored in your home folder ,use the following commands to generate the database from the dump file

```
CREATE DATABASE FOOTBALL;
USE FOOTBALL;
source ~/A/dump.sql;

```

It is preferable to create a virtual environment to run the CLI

## INSTRUCTION TO CREATE THE VIRTUAL ENVIRONMENT AND RUN IT

Inside the submission folder run the following commands to create and activate the virtual environment  and install the requirements

```
python3.8 -m venv venv
source/bin/activate
pip install -r requirements.txt

```

To Start the Command Line Interface use the following command

```
python MiniWorld.py

```
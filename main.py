#!/usr/bin/env python2
# coding: utf-8

from sys import argv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('main.cfg')
db = SQLAlchemy(app)

if __name__ == '__main__':
    from routes import *

    if len(argv) == 2:
        if argv[1] == "init_db":
            db.drop_all()
            db.create_all()
            print "Init done"
        else:
            print "Unknown command"
            exit(1)
    app.run(debug=True)  # Change before prod

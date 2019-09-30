#!/usr/bin/env python2
# coding: utf-8

from sys import argv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

app = Flask(__name__)

app.config.from_pyfile('main.cfg')

db = SQLAlchemy(app)
ma = Marshmallow(app)


if __name__ == '__main__':
    from routes import *

    if len(argv) == 2:
        if argv[1] == "init_db":
            db.drop_all()
            db.create_all()
            db.session.add(Utilisateurs("Derle", "Nora", datetime(1987, 8, 11, 0, 0, 0, 0)))
            db.session.add(Utilisateurs("Pres", "Jack", datetime(1976, 3, 5, 0, 0, 0, 0)))
            db.session.add(Biens("Maison familiale", "Dans un quartier pavillonnaire recherche, avec acces arret de bus et ecoles a moins de 5 minutes a pieds, proche centre ville et ses commodites, 200m^2", "maison", "Poissy", 6, "4 chambres", 1))
            db.session.add(Biens("Appartement T3", "Tres bien situe dans la ville, ce T3 a tout pour vous satisfaire", "appartement", "Conflans", 3, "2 chambres, 1 cave", 2))
            db.session.add(Biens("Villa", "Grande villa", "villa", "Poissy", 7, "5 chambres", 2))
            db.session.commit()
            print "Init done"
        else:
            print "Unknown command"
            exit(1)
    app.run(debug=True)  # Change before prod

# Tuodaan Flask k�ytt��n
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy k�ytt��n
from flask_sqlalchemy import SQLAlchemy
# K�ytet��n tasks.db-nimist� SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee t�m�n sovelluksen tiedostojen kanssa
# samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
# Pyydet��n SQLAlchemy� tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota k�ytet��n tietokannan k�sittelyyn
db = SQLAlchemy(app)

# Luetaan kansiosta application tiedoston views sis�lt�
from application import views

from application.tasks import models
from application.tasks import views

# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()
# Tuodaan Flask kaytt00n
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy kayttoon
from flask_sqlalchemy import SQLAlchemy
# Kaytetaan tasks.db-nimista SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee taman sovelluksen tiedostojen kanssa
# samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
# Pyydetaan SQLAlchemya tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota kaytetaan tietokannan kasittelyyn
db = SQLAlchemy(app)

# Luetaan kansiosta application tiedoston views sisalto
from application import views

from application.tasks import models

from application.tasks import views

from application.auth import models
from application.auth import views 

# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()

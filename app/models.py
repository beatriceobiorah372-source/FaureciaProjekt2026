import sqlalchemy as sa
import sqlalchemy.orm as so
from . import db


class User(db.Model):
    __tablename__ = "benutzer"
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(100))
    email: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True)

class Project(db.Model):
    __tablename__ = "projekt"
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    titel: so.Mapped[str] = so.mapped_column(sa.String(120))
    user_id: so.Mapped[int] = so.mapped_column(
        sa.Integer,
        sa.ForeignKey("benutzer.id")
    )

class Forecast(db.Model):
    __tablename__ = "prognose"
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    wert: so.Mapped[float] = so.mapped_column(sa.Float)
    projekt_id: so.Mapped[int] = so.mapped_column(
        sa.Integer,
        sa.ForeignKey("projekt.id")
    )

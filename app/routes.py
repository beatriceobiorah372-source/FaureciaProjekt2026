from flask import render_template, redirect, url_for, Blueprint
from . import db
from .models import User, Project, Forecast
from .forms import UserForm, ProjectForm, ForecastForm

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template(
        "index.html",
        user=User.query.all(),
        projekte=Project.query.all(),
        prognosen=Forecast.query.all()
    )


@bp.route("/user/add", methods=["GET", "POST"])
def user_add():
    form = UserForm()
    if form.validate_on_submit():
        db.session.add(User(form.data))
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("index.html", form=form, seite="user")


@bp.route("/projekt/add", methods=["GET", "POST"])
def projekt_add():
    form = ProjectForm()
    form.user_id.choices = [(u.id, u.name) for u in User.query.all()]
    if form.validate_on_submit():
        db.session.add(Project(form.data))
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("index.html", form=form, seite="projekt")


@bp.route("/prognose/add", methods=["GET", "POST"])
def prognose_add():
    form = ForecastForm()
    form.projekt_id.choices = [(p.id, p.titel) for p in Project.query.all()]
    if form.validate_on_submit():
        db.session.add(Forecast(form.data))
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("index.html", form=form, seite="prognose")


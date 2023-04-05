from flask import Flask, render_template
from flask_migrate import Migrate
from models.User import db
from routes.user import user_bp

app = Flask(__name__)

app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix="/users")

@app.route('/', methods=["GET"])
def index():
  return render_template("index.html")

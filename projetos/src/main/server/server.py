from flask import Flask

from ..routers.calculators import calc_route_bp

app = Flask(__name__)

app.register_blueprint(calc_route_bp)
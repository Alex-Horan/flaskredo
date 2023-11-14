from flask import (
    Blueprint, g, redirect, render_template, url_for, session
)

from ecom.auth import login_required
from ecom.db import get_db

bp = Blueprint('store', __name__)

@bp.route('/')
def index():
    return 'testing'
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash
import click
from ecom.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')




##########################################################################################################################



def create_adm(uname, pwrd):
    try:
        db = get_db()
        db.execute(
            'INSERT INTO dev_ad (uname, password) VALUES (?,?)', (uname, generate_password_hash(pwrd))
        )
        db.commit()
    except db.IntegrityError:
        return "failed to create admin account"
    

##############################################################################################################################



@click.command('make-admin')
@click.argument('uname')
@click.argument('pwrd')
def create_adm_command(uname, pwrd):
    create_adm(uname, pwrd)
    click.echo(f"created admin user '{uname}'")


##################################################################################################################################




def init_admin(app):
    app.cli.add_command(create_adm_command)



####################################################################################################################################
####################################################################################################################################

@bp.route('/login', methods=('POST'))
def ad_login():
    pass
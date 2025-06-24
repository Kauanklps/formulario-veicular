from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
import sqlite3
import os

logout_bp = Blueprint('logout', __name__)

def get_db_connection():
    db_path = os.path.join(current_app.root_path, 'instance', 'database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@logout_bp.route('/logout')
def logout():
    session.clear()  # ou session.pop('usuario', None)
    return redirect(url_for('home.home'))  # redireciona para a página inicial

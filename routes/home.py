from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
import sqlite3
import os

home_bp = Blueprint('home', __name__)

def get_db_connection():
    db_path = os.path.join(current_app.root_path, 'instance', 'database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@home_bp.route('/')
def home():
    return render_template('home.html')
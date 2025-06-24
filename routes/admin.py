from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
import sqlite3
import os

admin_bp = Blueprint('admin', __name__)

def get_db_connection():
    db_path = os.path.join(current_app.root_path, 'instance', 'database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@admin_bp.route('/admin')
def dashboard():
    if not session.get('admin'):
        return redirect(url_for('admin.login'))

    conn = get_db_connection()
    registros = conn.execute("SELECT * FROM checklist ORDER BY data DESC").fetchall()
    conn.close()
    return render_template('admin.html', registros=registros)

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
import sqlite3
import os

login_bp = Blueprint('login', __name__)

logout_bp = Blueprint('login', __name__)


def get_db_connection():
    db_path = os.path.join(current_app.root_path, 'instance', 'database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario == 'Planejamento' and senha == 'teclado.01':
            session['admin'] = True
            return redirect(url_for('admin.dashboard'))
        else:
            flash("Credenciais inválidas.")
    return render_template('login.html')

@logout_bp.route('/logout')
def logout():
    session.clear()  # ou session.pop('usuario', None)
    return redirect(url_for('home'))  # redireciona para a página inicial

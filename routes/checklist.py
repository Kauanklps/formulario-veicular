from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
import sqlite3
from datetime import datetime
import os

checklist_bp = Blueprint('checklist', __name__)

def get_db_connection():
    db_path = os.path.join(current_app.root_path, 'instance', 'database.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@checklist_bp.route('/checklist', methods=['GET', 'POST'])
def checklist():
    if request.method == 'POST':
        data = {
            'colaborador': request.form.get('colaborador'),
            'veiculo': request.form.get('veiculo'),
            'quilometragem': request.form.get('quilometragem'),
            'ultima_validacao': request.form.get('ultima_validacao'),
            'oleo': request.form.get('oleo'),
            'freio': request.form.get('freio'),
            'aditivo': request.form.get('aditivo'),
            'pneus': request.form.get('pneus'),
            'observacoes': request.form.get('observacoes'),
            'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        # Validação simples
        if not all([data['colaborador'], data['veiculo'], data['quilometragem']]):
            flash('Preencha todos os campos obrigatórios.')
            return redirect(url_for('checklist.checklist'))

        conn = None  # Inicializa a variável para evitar erro no finally
        try:
            conn = get_db_connection()
            conn.execute("""
                INSERT INTO checklist (
                    colaborador, veiculo, quilometragem, ultima_validacao,
                    oleo, freio, aditivo, pneus, observacoes, data
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data['colaborador'], data['veiculo'], data['quilometragem'], data['ultima_validacao'],
                data['oleo'], data['freio'], data['aditivo'], data['pneus'],
                data['observacoes'], data['data']
            ))
            conn.commit()
            flash("Checklist enviado com sucesso!", "success")
        except Exception as e:
            print("Erro ao salvar o checklist.", "danger", e)
            flash("Preencha todos os campos obrigatórios.", "warning")
        finally:
            if conn:  # Só fecha se foi definido
                conn.close()

        return redirect(url_for('checklist.checklist'))

    return render_template('checklist.html')

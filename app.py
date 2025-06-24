from flask import Flask, render_template
from routes.checklist import checklist_bp
from routes.admin import admin_bp
from routes.login import login_bp
from routes.home import home_bp
from routes.logout import logout_bp

app = Flask(__name__)
app.secret_key = 'chave_super_secreta'

app.register_blueprint(checklist_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(home_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
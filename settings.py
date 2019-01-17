from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///C:/Users/Shaun/Desktop/PythonAPIFlask/database.db'
app.config['SQLALCHEMY_DATABASE_MODIFICATIONS'] = False


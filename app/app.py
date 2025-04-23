from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100))

class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200))

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'))

@app.route('/')
def index():
    doctores = Doctor.query.all()
    hospitales = Hospital.query.all()
    return render_template('cuestionario.html', doctores=doctores, hospitales=hospitales)

@app.route('/agendar', methods=['POST'])
def agendar():
    nombre = request.form['nombre']
    edad = request.form['edad']
    doctor_id = request.form['doctor']
    hospital_id = request.form['hospital']
    paciente = Paciente(nombre=nombre, edad=edad, doctor_id=doctor_id, hospital_id=hospital_id)
    db.session.add(paciente)
    db.session.commit()
    return redirect(url_for('index'))

@app.cli.command('initdb')
def initdb_command():
    db.create_all()
    db.session.add(Doctor(nombre='Dra. María Pérez', especialidad='Pediatría'))
    db.session.add(Doctor(nombre='Dr. Juan López', especialidad='General'))
    db.session.add(Hospital(nombre='Hospital Central', direccion='Av. Principal'))
    db.session.add(Hospital(nombre='Clínica Rural', direccion='Calle 10 de Agosto'))
    db.session.commit()
    print('Base de datos inicializada.')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

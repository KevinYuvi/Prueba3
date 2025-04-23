from app import db

class Turno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_hospital = db.Column(db.String(100))
    nombre_doctor = db.Column(db.String(100))
    especialidad = db.Column(db.String(100))
    nombre_paciente = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(10))
    sintomas = db.Column(db.Text)
    notas = db.Column(db.Text)

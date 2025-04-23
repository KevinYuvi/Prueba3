from flask import render_template, request, redirect, url_for
from app import app, db
from app.modelos import Turno

@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        turno = Turno(
            nombre_hospital=request.form['nombre_hospital'],
            nombre_doctor=request.form['nombre_doctor'],
            especialidad=request.form['especialidad'],
            nombre_paciente=request.form['nombre_paciente'],
            edad=request.form['edad'],
            genero=request.form['genero'],
            sintomas=request.form['sintomas'],
            notas=request.form['notas']
        )
        db.session.add(turno)
        db.session.commit()
        return redirect(url_for('confirmacion', id=turno.id))
    return render_template('formulario_turno.html')

@app.route('/confirmacion/<int:id>')
def confirmacion(id):
    turno = Turno.query.get_or_404(id)
    return render_template('confirmacion.html', turno=turno)


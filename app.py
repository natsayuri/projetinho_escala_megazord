# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///work_schedule.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payroll_id = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    valkyrie = db.Column(db.String(100))
    discipline = db.Column(db.String(100))
    holiday_group = db.Column(db.String(1))
    schedule = db.Column(db.String(50))
    hired_date = db.Column(db.Date)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    hours = db.Column(db.Float)
    type = db.Column(db.String(50))  # 'holiday', 'overtime', etc.

@app.route('/employees', methods=['GET', 'POST'])
def handle_employees():
    if request.method == 'POST':
        data = request.json
        new_employee = Employee(
            payroll_id=data['payroll_id'],
            name=data['name'],
            valkyrie=data['valkyrie'],
            discipline=data['discipline'],
            holiday_group=data['holiday_group'],
            schedule=data['schedule'],
            hired_date=datetime.strptime(data['hired_date'], '%Y-%m-%d').date()
        )
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({"message": "Employee added successfully"}), 201
    else:
        employees = Employee.query.all()
        return jsonify([{
            "id": e.id,
            "name": e.name,
            "payroll_id": e.payroll_id,
            "discipline": e.discipline,
            "holiday_group": e.holiday_group
        } for e in employees])

@app.route('/generate_schedule', methods=['POST'])
def generate_schedule():
    # Lógica para gerar a escala
    # Esta é uma implementação simplificada
    employees = Employee.query.all()
    for employee in employees:
        # Aqui você implementaria a lógica real de geração de escala
        new_schedule = Schedule(
            employee_id=employee.id,
            date=datetime.now().date(),
            hours=8,
            type='regular'
        )
        db.session.add(new_schedule)
    db.session.commit()
    return jsonify({"message": "Schedule generated successfully"}), 200

@app.route('/export_csv', methods=['GET'])
def export_csv():
    # Lógica para exportar dados para CSV
    # Implementação simplificada
    data = "Payroll ID,Name,Total Overtime Hours\n"
    employees = Employee.query.all()
    for employee in employees:
        overtime = sum(s.hours for s in Schedule.query.filter_by(employee_id=employee.id, type='overtime'))
        data += f"{employee.payroll_id},{employee.name},{overtime}\n"
    return data, 200, {'Content-Type': 'text/csv'}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
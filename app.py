from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db2.sqlite3'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
socketio = SocketIO(app)

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_cost = db.Column(db.Integer, default=10000)
    in_use = db.Column(db.Boolean, default=False)

class Table2(db.Model):
    unique_num = db.Column(db.Integer, primary_key=True,autoincrement=True)
    id = db.Column(db.Integer)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    cost = db.Column(db.Float, default=0.0)


with app.app_context():
    db.create_all()
    if Table.query.count() == 0:
        for i in range(1, 11):
            new_table = Table(id=i)
            db.session.add(new_table)
        db.session.commit()
    if Table2.query.count() == 0:
        db.session.commit()

@app.route('/')
def index():
    tables = Table.query.all()
    return render_template('index.html', tables=tables)

@app.route('/start/<int:table_id>', methods=['POST'])
def start_game(table_id):
    table = Table.query.get(table_id)
    if table and not table.in_use:
        new_table = Table2(id=table_id,start_time=datetime.now())
        db.session.add(new_table)
        table.in_use = True
        db.session.commit()
        socketio.emit('update', {'table': table_id, 'status': 'started','unique_id':new_table.unique_num})
    return jsonify(success=True)

@app.route('/stop/<int:table_id>', methods=['POST'])
def stop_game(table_id):
    table = Table.query.get(table_id)
    table2 = Table2.query.filter(Table2.id == table_id , Table2.end_time == None).first()
    print(table2)
    print(table2)
    if table and table.in_use:
        table2.end_time = datetime.now()
        duration = (table2.end_time - table2.start_time).total_seconds() / 3600
        table2.cost = int(duration * table.table_cost)
        table.in_use = False
        db.session.commit()
        socketio.emit('update', {'table': table_id, 'status': 'stopped', 'cost': table2.cost})
    return jsonify(success=True)

@app.route('/today_report')
def report():
    tables = Table2.query.all()
    daily_income = sum(table.cost for table in tables if table.end_time and table.end_time.date() == datetime.today().date())
    daily_income = int(daily_income)
    return render_template('report.html', daily_income=daily_income, monthly_income=daily_income)

@app.route('/yesterday_report')
def yesterday_report():
    tables = Table2.query.all()
    yesterday = datetime.today().date() - timedelta(days=1)
    yesterday_income = sum(table.cost for table in tables if table.end_time and table.end_time.date() == yesterday)
    yesterday_income = int(yesterday_income)
    return render_template('report2.html', daily_income=yesterday_income, monthly_income=yesterday_income)

if __name__ == '__main__':
    socketio.run(app, host="192.168.43.33", port=5001, debug=True)


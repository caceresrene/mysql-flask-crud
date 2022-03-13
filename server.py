from flask import Flask, render_template, request, redirect, session

from users import User

app = Flask(__name__)

@app.route('/')
def home():
	return redirect('/users')

@app.route('/users')
def dashboard():
	return render_template('dashboard.html', users=User.get_all())

@app.route('/users/new')
def register():
	return render_template('register.html')

@app.route('/users/create', methods=['POST'])
def procesado():
	User.save(request.form)
	return redirect('/users')

@app.route('/users/<id>/destroy')
def delete(id):
	data = {'id': id} # la informacion necesita ser pasada como diccionario
	User.delete(data)
	return redirect('/users')

@app.route('/users/<id>/edit')
def edit(id):
	data = {'id': id}
	tabla = User.get_table(data)[0]
	return render_template('edit.html', id = tabla['id'] ,nombre = tabla['first_name'], apellido = tabla['last_name'], email = tabla['email'])

@app.route('/users/update/<id>', methods=['POST'])
def update(id):
	User.update(request.form)
	return redirect('/users')

@app.route('/users/<id>')
def show(id):
	data = {'id': id}
	tabla = User.get_table(data)[0]
	print(User.get_table(data))
	return render_template('show.html', id = tabla['id'] ,nombre = tabla['first_name'], apellido = tabla['last_name'], email = tabla['email'], created_at = tabla['created_at'], updated_at = tabla['updated_at'])

if __name__ == '__main__':
	app.run(debug=True)
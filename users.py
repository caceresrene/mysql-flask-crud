from mysqlconnection import connectToMySQL

class User:
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all(cls):
    results = connectToMySQL('users_schema').query_db('SELECT * FROM users;')
    users = []
    for row_user in results:
      users.append(cls(row_user))
    return users

  @classmethod
  def save(cls, data):
    query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'
    # devuelve el id de la nueva fila
    result = connectToMySQL('users_schema').query_db(query, data)
    return result
  
  @classmethod
  def delete(cls, data):
    query = "DELETE FROM users WHERE id = %(id)s;"
    result = connectToMySQL('users_schema').query_db(query, data)
    return result

  @classmethod
  def update(cls, data):
    query = 'UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s'
    result = connectToMySQL('users_schema').query_db(query, data)
    return result

  @classmethod
  def get_table(cls, data):
    query = 'SELECT * FROM users WHERE id = %(id)s'
    result = connectToMySQL('users_schema').query_db(query, data)
    return result
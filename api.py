import pymysql
import flask
from flask import request,jsonify
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='', 
                            database='software_workshop', 
                            cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor(pymysql.cursors.DictCursor)

app = flask.Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return '''<h1>Distant Reading Archive<h1>
    <p>This site is a prototype API for distant reading of science fiction novels.</p>'''


@app.route('/greet', methods=['GET'])
def greet():
    return "HELLO WORLD"


@app.route('/api/v1/book/all', methods=['GET'])
def all_book():
    if request.method == 'GET':
        cursor.execute("SELECT * FROM workshop")
        data = cursor.fetchall()
        return jsonify(data)


@app.route('/api/v1/book', methods=['POST'])
def find_book():
    if request.is_json:
        if request.method == 'POST':
            jsonData = request.get_json() 
            title = jsonData['title']  
            cursor.execute("SELECT * FROM workshop WHERE title= %s", (title))  
            data = cursor.fetchall()  
            return jsonify(data)   


if __name__ == '__main__':
    app.run()    
 
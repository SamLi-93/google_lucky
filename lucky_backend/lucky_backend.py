from flask import Flask
from flask import Response
import json
from flask import jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_HOST'] = '35.194.183.62'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'lucky'
mysql.init_app(app)



@app.route("/", methods=['GET', 'POST'])
def home():
    data = []
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM images")
    results = cur.fetchall()
    for row in results:
        print(row)
        data.append(row)

    test = json.dumps(data)

    resp = Response(test)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



if __name__ == '__main__':
    app.run()

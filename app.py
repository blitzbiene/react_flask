from flask import Flask,render_template,request,g,jsonify
import sqlite3


app = Flask(__name__)
def connect_db():
    sql = sqlite3.connect('data.db')
    sql.row_factory = sqlite3.Row
    return sql
def get_db():
    if not hasattr(g,'sqlite'):
        g.sqlite = connect_db()
    return g.sqlite

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite'):
        g.sqlite.close()


@app.route('/<id>',methods=["GET"])
def index(id):
    try:
        db = get_db()
        cur = db.execute("select * from shops where id =?",[id])
        res = cur.fetchone()
        dict = {'id':res['id'],'name':res['name'],'latitude':res['latitude'],'longitude':res['longitude']}
        return jsonify(dict)
    except:
        return jsonify({'status':'failed'})



if __name__ == "__main__":
    app.run()

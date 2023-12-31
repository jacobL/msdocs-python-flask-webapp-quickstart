import os
import pymssql
import pymysql
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
    """
    conn = pymssql.connect(
    server='iddlinedb.database.windows.net', 
    user='idd',
    password='9l5YHtOCTyRJ',
    database='iddlinedb',
    as_dict=False
    )
    n = 'd'
    #app.config.from_object('iddline3.development')
    cur = conn.cursor()
    cur.execute('select * from aism_accounts')
    for r in cur :
        n = r[0] #os.environ['gg']   #os.getenv("gg")
    """ 
    n='ccc'
    conn  =  pymysql . connect ( 
    host = 'linemysql.mysql.database.azure.com' ,port=3306 ,  
    user = 'idd' ,  passwd = "9l5YHtOCTyRJ",db="linemysql" ) 
    cur = conn.cursor()
    cur.execute('select * from aism_accounts')
    for r in cur :
        n = r[1]+'==1 '
    
    print('Request for index page received : ',n)
    return render_template('index.html',name=n)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()

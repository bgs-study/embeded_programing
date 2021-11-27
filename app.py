from flask import Flask, render_template,request,jsonify
from pymongo import MongoClient
app = Flask(__name__)

client= MongoClient('localhost',27017)
db = client.dbCoCo

@app.route('/')
def home():
    # Render the page
    return render_template('main.html')


@app.route('/login_page')
def goMain():
    return render_template('login first.html')


@app.route('/pin')
def goPinchange():
    return render_template('pin_change.html')


@app.route('/pin_change' , methods=['POST'])
def pin_changing():
    
    pre = request.form['prepin']
    new = request.form['newpin']
    
    db.pin.update_one({'pin':pre},{'$set':{'pin': new}})

    return jsonify({'msg':'비밀번호변경 완료'})


@app.route('/login', methods=['POST'])
def init():    
    pinnum = request.form['pinnum']
    pin = db.pin.find_one({'pin':pinnum})
    print(pin)
    if(pin == "" or pin == None):
        return jsonify({'msg':'로그인실패.잘못된비밀번호'})
    else:
       return jsonify({'msg':'로그인성공'})
    



#@app.route('/pin', methods=['GET'])
#def present_pin():
    #pin = list(db.pin.find({},{'_id':False}))
    #return jsonify({'msg': pin})#    return 'get'

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)



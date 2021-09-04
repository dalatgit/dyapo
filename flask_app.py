"""prototipo DYAPO"""
from flask import jsonify
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Column, Text, Integer, Numeric
from sqlalchemy import func

import pusher
import mistune

REGRESAR_A_LISTADO = "<a href='/dp_list_data'>Regresar a Listado</a>"

app = Flask(__name__)
app.config["DEBUG"] = True

# local
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="****",
    password="****",
    hostname="****",
    databasename="****",
)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# models
class General(db.Model):
    """General"""
    __tablename__ = 'general'
    id = Column(Integer, primary_key=True, autoincrement=True)
    control_id = Column(Integer)
    quantity_page = Column(Integer)
    current_page = Column(Integer)

class Pages(db.Model):
    """pages"""
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    p_seq = Column(Numeric(10,2))
    p_title = Column(Text)
    p_data_mk = Column(Text)
    p_data_html = Column(Text)

@app.route('/dp_put_data', methods=['GET', 'POST'])
def dp_put_data():
    if request.method == 'GET':
        return render_template('dp_put_data.html', mkid="0", mkdata="")
    
    hid_id=request.form.get('hid_id')
    mkdata=request.form.get('mkdata')

    page_id = int(hid_id)

    if page_id == 0:
        # new page
        # get next sequence
        q_result = db.session.query(func.max(Pages.p_seq)).scalar()
        if q_result is None:
            next_seq = 10
        else:
            next_seq = q_result + 10

        # insert new data
        cmm = Pages(
            p_seq = next_seq,
            p_data_mk = mkdata,
            p_title = mkdata.split('\n', 1)[0],
            p_data_html = mistune.markdown(mkdata)
            )

        db.session.add(cmm)
        db.session.commit()
        return "Nueva diapositiva grabada. " + REGRESAR_A_LISTADO

    # update page
    one_mk = db.session.query(Pages).get(page_id)
    one_mk.p_title = mkdata.split('\n', 1)[0]
    one_mk.p_data_mk = mkdata
    one_mk.p_data_html = mistune.markdown(mkdata)
    db.session.commit()
    return "Diapositiva editada. " + REGRESAR_A_LISTADO

@app.route("/dp_list_data", methods=['GET'])
def dp_list_data():
    query_result = db.session.query(Pages).order_by(Pages.p_seq)
    return render_template("dp_list_data.html", query_result=query_result)

@app.route("/participante", methods=['GET'])
def participante():
    query_result = db.session.query(Pages).order_by(Pages.p_seq)
    return render_template("participante.html", query_result=query_result)

@app.route("/dp_expo", methods=['GET'])
def dp_expo():
    query_result = db.session.query(Pages).order_by(Pages.p_seq)
    return render_template("dp_expo.html", query_result=query_result)

@app.route('/dp_edit_data', methods=['GET'])
def dp_edit_data():
    # read current data
    mkid = request.args.get('mkid')
    # print(f"mkid={mkid}")
    one_mk = db.session.query(Pages).get(int(mkid))
    mkdata = one_mk.p_data_mk
    # print(f"mkdata={mkdata}")
    return render_template('dp_put_data.html', mkid=mkid, mkdata=mkdata)

@app.route('/dp_get_data_html', methods=['GET'])
def dp_get_data_html():
    valor = request.args.get('valor', default = "0_0", type = str)
    dp_id = valor.split("_")[0]
    dp_index = valor.split("_")[1]
    one_mk = db.session.query(Pages).get(int(dp_id))
    if one_mk is None:
        data_html = ""
    else:
        data_html = one_mk.p_data_html
    return data_html

@app.route('/dp_notify', methods=['GET'])
def dp_notify():
    valor = request.args.get('valor', default = "0_0", type = str)
    pusher_client = pusher.Pusher(app_id=u'*', key=u'*', secret=u'*', cluster=u'*')
    pusher_client.trigger('my-channel', 'my-event', {
        'valor': valor
    })
    return ""

# ruta informativa
@app.route('/info', methods=['GET'])
def info():
    """info"""
    return "versión 1.7"

if __name__ == '__main__':
    app.run()
"""programa principal"""
from flask import jsonify
from flask import Flask, request, render_template

from flask_cors import CORS

import pusher

from pages_data import get_page_html

# aplicación principal
app = Flask(__name__)
CORS(app)

contador_presenter = 1
diccionario_presenter = {}

# ruta informativa
@app.route('/info', methods=['GET'])
def info():
    """"""
    return "info 1.2"

@app.route('/get_presenter', methods=['GET'])
def get_presenter():
    """get_presenter"""
    global contador_presenter
    global diccionario_presenter
    contador_presenter = contador_presenter + 1
    diccionario_presenter[contador_presenter] = 1
    return str(contador_presenter)

@app.route('/get_page', methods=['GET'])
def get_page():
    """get_page"""
    global diccionario_presenter
    page_id = request.args.get('page', default = 0, type = int)
    presenter_id = request.args.get('presenter', default = 0, type = int)
    print(f"page_id={page_id}")
    print(f"presenter_id={presenter_id}")
    if presenter_id > 0:
        # avisar
        pusher_client = pusher.Pusher(app_id=u'*', key=u'*', secret=u'*', cluster=u'*')
        pusher_client.trigger('my-channel', 'my-event', {
            'presenter': presenter_id,
            'page': page_id
        })
    diccionario_presenter[presenter_id] = page_id
    return get_page_html(page_id)

# ************************ start server
if __name__ == '__main__':
    #app.run(debug=True,host='0.0.0.0')
    app.run()

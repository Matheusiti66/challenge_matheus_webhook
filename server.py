from flask import Flask
from pyngrok import ngrok, conf
from flask import Flask, request, jsonify
from core.services.starkbank import StarkBank

app = Flask(__name__)
conf.get_default().auth_token = "2kHybAS47QSfWFfjWcM1wEwJf1n_QF8EvitBm6B2BzhKv3AR"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        service = StarkBank()
        data = request.get_json()
        response = service.send_transfer(data=data)
        return jsonify({"status": response['status'] , "message":response['message']}), response['statusCode']
    
    except Exception as Err:
        return jsonify({"status": response['status'] , "message":Err}), response['statusCode']

if __name__ == '__main__':
    url = ngrok.connect(5000)
    print(f" * ngrok tunnel \"{url}\" -> \"http://127.0.0.1:5000\"")
    app.run(port=5000)
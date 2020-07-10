from flask import Flask

app = Flask(__name__)
@app.route("/test/",methods=["GET","POST"])



def application(environ, start_response):
    headers = [('Content-type', 'text/plain')]
    status = '200 OK'
    start_response(status, headers)
    with app.test_request_context():
        note = request.args.get('fields')
        return ["Response is: {0}".format(note).encode('utf-8')]

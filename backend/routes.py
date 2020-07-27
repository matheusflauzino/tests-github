import json
import datetime
from flask import Flask, request, Response
from flask_cors import CORS


from main import getContribuitions

app = Flask(__name__)
CORS(app)


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


@app.route('/teste', methods=['GET'])
def home():
    return {"status": 200, "message": "Welcome"}


@app.route('/contribuitions', methods=['POST'])
def contribuitions():
    body = request.get_json()

    if("repository" not in body):
        return {"status": 400, "message": "Repository not found"}

    if body["repository"] == "":
        return {"status": 400, "message": "Repository not found"}

    data = getContribuitions(body["repository"])
    return Response(json.dumps(data,  indent=1,
                               default=default),  mimetype='application/json')


app.debug = True
app.run()

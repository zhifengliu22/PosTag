# coding=utf-8
import thulac
from flask import Flask, request, jsonify, make_response
from flask_cors import *
import json

def tagging(content):
    thu1 = thulac.thulac()
    text = thu1.cut(content, text=True)
    return text

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/POSTagging/", methods=["POST"])
def POStagg():
    if request.method == "POST":
        json_dict = request.get_json()
        content = json_dict["content"]
        tag_result = tagging(content)
        tag_result1 = {"success": "true", "msg": tag_result}
        result1 = json.dumps(tag_result1, ensure_ascii=False)
        return result1
    else:
        return """<html><dody>
        Something went horribly wrong
        </body></html>"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)
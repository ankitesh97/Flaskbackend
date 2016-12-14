from flask import Flask,request
import json
import base64
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

dummy = open("dummy.txt","r").read()
data = [{"Book_id":1,"Title":"Lorem", "Cover":"http://localhost:4000/static/abcd.jpg","Ratings":"4/5", "Author":"Lorem Ipsum"},
{"Book_id":2,"Title":"alpha", "Cover":"http://localhost:4000/static/xyz.jpg","Ratings":"3/5", "Author":"ferri ipsum "},
{"Book_id":3,"Title":"beta", "Cover":"http://localhost:4000/static/alpha.jpeg","Ratings":"2/5", "Author":"abcd Ipsum"},
{"Book_id":4,"Title":"gamma", "Cover":"http://localhost:4000/static/beta.jpeg","Ratings":"1/5", "Author":"xyz Ipsum"},
{"Book_id":5,"Title":"abcd", "Cover":"http://localhost:4000/static/gamma.jpeg","Ratings":"5/5", "Author":"alpha Ipsum"},
{"Book_id":6,"Title":"xyz", "Cover":"http://localhost:4000/static/delta.jpg","Ratings":"4/5", "Author":"beta Ipsum"},
{"Book_id":7,"Title":"delta", "Cover":"http://localhost:4000/static/ferro.jpg","Ratings":"3/5", "Author":"gamma Ipsum"},
{"Book_id":8,"Title":"ferro", "Cover":"http://localhost:4000/static/fala.jpeg","Ratings":"4/5", "Author":"delta Ipsum"}]

summary = [{"id":1, "summary":dummy},{"id":1, "summary":dummy},{"id":2, "summary":dummy},
{"id":8, "summary":dummy},{"id":5, "summary":dummy},{"id":3, "summary":dummy},
{"id":7, "summary":dummy},{"id":6, "summary":dummy},{"id":4, "summary":dummy}]

@app.route('/api/v1.0/get_books_data')
def get_books_data():
	
	response = {"payload":data}
	json_data = json.dumps(response)
	return json_data


@app.route('/api/v1.0/get_book_summary', methods=['POST'])
def get_book_summary():
	#{"payload":{"id":1}}
	jdata = request.data
	data = json.loads(jdata)["payload"]
	temp = {}
	for x in summary:
		if x["id"] == data['id']:
			temp = x
	return json.dumps({"payload":temp})

if(__name__ == "__main__"):
	app.run(debug=True,host='0.0.0.0',port=4000)

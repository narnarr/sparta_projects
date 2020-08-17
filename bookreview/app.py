from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta_review

# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    title = request.form.get('title')
    author = request.form.get('author')
    review = request.form.get('review')
    doc = {'title': title,
           'author': author,
           'review': review
           }
    db.bookreviews.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다!'})

@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.bookreviews.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'reviews': reviews})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
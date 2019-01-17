from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {
        'name': 'Green Eggs and Ham',
        'price': 7.99,
        'isbn': 978039400165
    },
    {
        'name': 'The Cat in The Hat',
        'price': 6.99,
        'isbn': 9782371000193
    },
]

# GET /books/978039400165

#GET /books - if anyone goes to a route, default is GET
@app.route('/books')
def get_books():
    return jsonify({'books': books})

@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }
    return jsonify(return_value)
 
app.run(port=5000)

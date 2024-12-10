from flask import Flask 

app = Flask(__name__)

items = [
    {
        'name': "momos",
        'price': 39
    },
    {
        'name': "mango mojito",
        'price': 33
    }
]

@app.route('/')
def fun():
    food_name_list = [i['name']for i in items]
    return {'food':food_name_list}

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask , request, jsonify

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
    return {'food': items}

@app.post('/add_items')
def add_items():

    request_data = request.get_json()# get jason data but returen the python dictionary 
    items.append(request_data)
    return {'message': "items added succefully"},201
     

@app.get('/<string:name>')
def items_name(name):
    
    for item in items:
        
        if item['name'] == name:
            return item
    
    return {"error": "Item not found"}, 404
# another way to get the data from the like 

@app.get("/data/")
def items_list():
    name = request.args.get('name')  # Get 'name' from query parameters

    for item in items:
        if item["name"] == name:  # Corrected to match the key in dictionary
            return jsonify(item)  # Return the item as a JSON response

    return jsonify({"error": "Item not found"}), 404 
if __name__ == '__main__':
    app.run(debug=True)
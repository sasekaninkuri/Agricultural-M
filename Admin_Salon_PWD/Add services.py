
from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data to store services (you might want to use a database in a real application)
services = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Add', methods=['POST'])
def add_service():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        service = { 'name': name, 'price': price}
        services.append(service)
        
        return "Service added successfully!"
    else:
        return "Invalid request method"

if __name__ == '__main__':
    app.run(debug=True)

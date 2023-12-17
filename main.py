from flask import Flask, render_template, url_for, request, redirect, jsonify
# from mapping2 import 

app = Flask(__name__, static_url_path="")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/menu') #,methods=['POST]
def menu():
    #startCity = str(request.form['startCity'])
    #finishCity = str(request.form['finishCity'])
    
    return render_template('menu.html')

@app.route('/about')
def about():
    return render_template('about.html')


from mapping2 import process
@app.route('/api/process',methods=['POST'])
def routes():
    # Assuming the JSON body contains 'start' and 'finish'
    
    # Extract 'start' and 'finish' from the JSON data
    start = request.json.get('start')
    finish = request.json.get('finish')

    # Call the 'process' function with 'start' and 'finish'
    shortest_path_length, shortest_path_length_car, shortest_path_length_train, route_path = process(start, finish)
    # print('xxx', x, y, z)

    # Convert the values to JSON format
    result_json = jsonify(
        {'shortest_path_length': shortest_path_length, 
         'shortest_path_length_car': shortest_path_length_car, 
         'shortest_path_length_train': shortest_path_length_train,
         'route_path': route_path})

    return result_json

    
    
if __name__ == '__main__': app.run(debug=True)
#flask run
#python -m flask run (2)
#export FLASK_APP=namafile.py/file yang dituju (1)

#export FLASK_ENV=development (1)
#python -m flask run (2)
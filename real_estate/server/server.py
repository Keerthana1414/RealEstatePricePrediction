from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_price', methods=['POST'])
def predict_price():
    sqft = float(request.form['sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    bedroom = int(request.form['bedroom'])

    response = jsonify({
        'estimated_price' : util.get_estimated_price(location, sqft, bath, bedroom)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print('Starting Python Flask Server')
    util.load_artifacts()
    app.run(debug=True)
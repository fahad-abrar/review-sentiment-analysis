from flask import Flask, request, jsonify
from model import Review_Prediction_model
from producer import produce_content
from consumer import consume_content


app = Flask(__name__)

# instantiate the model once at the start
review_model = Review_Prediction_model()

@app.route('/api', methods=['GET'])
def getapi():
    return 'This is a GET request.'

@app.route('/api', methods=['POST'])
def postapi():
    data = request.get_json()
    content = data.get('content')
    
    prediction = review_model.print_result(content)
    print('----->>>>',prediction)
    produce_content(prediction)
    
    # send the result as a JSON response
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(debug=True)

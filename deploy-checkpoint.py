from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
#load the model
model = pickle.load(open('saved_model.sav', 'rb'))

@app.route('/')
def homr():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    sepal_length = float(request.force['SepalLengthCm'])
    sepal_width = float(request.force['SepalWidthCm'])
    petal_length = float(request.force['PetalLengthCm'])
    petal_width = float(request.force['PetalWidthCm'])
    results = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debugs=True)

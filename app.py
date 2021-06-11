from flask import Flask, render_template, request
import pickle
from sklearn.linear_model import LinearRegression
 
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return render_template('index.html')
 
 
 
@app.route('/predict',methods=['POST'])
def predict():
 
    if request.method == 'POST':
 
        Height = request.form['Height']
 
        data =[[float(Height)]]
 
        lr = pickle.load(open('weight.pkl', 'rb'))
        prediction = lr.predict(data)
 
    return render_template('index.html', prediction=prediction)
 
 
 
if __name__ == '__main__':
    app.run(debug=False)
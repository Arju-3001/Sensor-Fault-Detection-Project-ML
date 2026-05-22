from flask import Flask
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return 'Sensor Fault Detection App Running'

if __name__ == '__main__':
    app.run(debug=True)

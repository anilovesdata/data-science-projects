# app.py – FIXED IN 3 SECONDS
from flask import Flask, render_template, request
import sqlite3, os
from PIL import Image
import numpy as np

app = Flask(__name__)
emo = ["Angry","Disgust","Fear","Happy","Sad","Surprise","Neutral"]

def predict(img):
    x = np.array(img.resize((48,48)).convert('L'))
    x = x.reshape(1,48,48,1)/255.0
    return emo[np.argmax(model.predict(x, verbose=0))]

@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='POST':
        name = request.form['name']
        age  = request.form['age']
        file = request.files['photo']
        path = 'static/'+file.filename
        file.save(path)

        emotion = predict(Image.open(path))
        msg = "You are frowning. Why are you sad?" if emotion=="Sad" else \
              "You are smiling! Keep it up!" if emotion=="Happy" else \
              f"You are {emotion.lower()}."

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, age INT, photo TEXT, emotion TEXT)')
        c.execute('INSERT INTO students VALUES (?,?,?,?)', (name,age,path,emotion))
        conn.commit(); conn.close()

        return f"<h1>{msg}</h1><img src='{path}' width=300><br><a href='/'>Again</a>"
    return render_template('index.html')

if __name__=='__main__':
    os.makedirs('static', exist_ok=True)
    # MODEL LOADS ONLY WHEN YOU RUN THE APP
    from tensorflow.keras.models import load_model
    global model
    model = load_model('face_emotionModel.h5')
    print("🚀 MODEL LOADED – APP STARTING")
    app.run(debug=True)
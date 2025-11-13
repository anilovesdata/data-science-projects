## Overview

This web application detects a person's **emotion** either from an uploaded image or a live webcam capture.

---

The project was built using **Python** for the web app and model training, and **Streamlit** for hosting. It logs each user's activity (name, image, and prediction result) into a local **SQLite** database

## Features

Detects emotions from:

- Uploaded image files
- Webcam input.

Displays:

- Detected dominant emotion
- Confidence scores for all emotions.

Includes both:

- A custom CNN model.
- A deepFace fallback model (Just in case the CNN model has issues.)

## NOTE

- This web app saves your uploaded image to a local database. Now while I have no particular use for your image. This is a public repo, meaning anyone can access that sort of data. I'll implement a work around that keeps your details private to you.

## How to run it

To test it out on your own machine:

- Clone the repo:
  git clone https://github.com/Oluwatomi-Omotoso/Emotion-Detector/tree/main/OMOTOSO_23CG034133_Emotion_detector_web_app.git

- I suggest you work on it in a virtual environment, just in case you break something.
- Install the dependencies:

  pip install -r requirements.txt

- And then you run the program

  streamlit run app.py

**OR**

You could just try out the live web app I made, you can find it here: [Live demo](https://oluwatomi-omotoso-emotion-detector.streamlit.app/)

## Optional

You could train your own model for improved resuls.

Here's the dataset I used it for mine: https://www.kaggle.com/datasets/msambare/fer2013

## Author

Name: Mene Anirejuoritse Nicole

Matric No.: 23CG034095

Institution: Covenant University

Course: CSC 331 — Machine Learning & AI Project

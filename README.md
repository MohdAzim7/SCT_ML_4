
#  Hand Gesture Recognition System using Machine Learning + HOG

An **interactive Machine Learning web application** that recognizes and classifies hand gestures from uploaded images.

This project uses **Histogram of Oriented Gradients (HOG)** for feature extraction and **Random Forest / SVM classifiers** for gesture prediction.

The model is deployed using a **Streamlit web app**, allowing users to upload gesture images and receive real-time predictions with confidence scores.

---

#  Project Highlights

* ✔ Recognizes 10 different hand gestures
* ✔ HOG feature extraction for gesture analysis
* ✔ Random Forest / SVM classification model
* ✔ Confidence score output for predictions
* ✔ Interactive Streamlit web interface
* ✔ Fast and lightweight ML-based system

---

#  Machine Learning Approach

This project follows a classical ML pipeline for image-based gesture recognition.

## Workflow:

1. Load LeapGestRecog dataset
2. Preprocess gesture images (resize + grayscale)
3. Extract HOG features
4. Train classifier model
5. Evaluate prediction accuracy
6. Deploy with Streamlit interface

---

## Algorithm Used:

* Random Forest Classifier
* Feature Extraction: HOG (Histogram of Oriented Gradients)

---

#  Recognized Gestures

The system can identify:

1. Palm
2. L
3. Fist
4. Fist Moved
5. Thumb
6. Index
7. OK
8. Palm Moved
9. C
10. Down

---

#  Features

##  Gesture Classification

Users can upload an image and the model predicts one of the 10 hand gestures.

---

##  Confidence Score

The model provides prediction confidence percentage for detected gesture.

---

##  Real-Time Prediction

Instant gesture recognition after image upload.

---

#  Tech Stack

* Python
* OpenCV
* Scikit-learn
* Scikit-image (HOG)
* NumPy
* Pandas
* Streamlit
* Joblib

---

#  Dataset Used

**Dataset:** LeapGestRecog
**Source:** [https://www.kaggle.com/datasets/gti-upm/leapgestrecog](https://www.kaggle.com/datasets/gti-upm/leapgestrecog)

---

#  How to Run the Project

## 1 Clone the Repository

```bash id="yq6p4x"
git clone https://github.com/keerthanarajr/SCT_ML_4.git
cd SCT_ML_4
```

---

## 2 Install Dependencies

```bash id="0u67hj"
pip install -r requirements.txt
```

---

## 3 Train the Model

```bash id="sx13j4"
python -m src.train_model
```

After training, the model will be saved as:

```bash id="ql7xy5"
saved_model/gesture_model.pkl
```

---

## 4 Run the Application

```bash id="6ocd53"
streamlit run app.py
```

The app will open in your browser automatically.

---

#  Application Features

*  Upload gesture image
*  Preview uploaded image
*  Predict hand gesture
*  Show confidence score

---

#  Project Objective

The goal of this project is to demonstrate how classical machine learning can be applied to hand gesture recognition tasks.

It helps understand:

* Image preprocessing techniques
* HOG feature extraction
* Gesture classification using ML models
* Real-time ML deployment using Streamlit

---

#  Limitations

* Optimized mainly for LeapGestRecog dataset images
* External real-world images may reduce accuracy
* Sensitive to lighting and background noise

---

#  Future Improvements

* Add webcam live gesture detection
* Upgrade to CNN / Deep Learning model
* Improve real-world gesture accuracy
* Enable real-time gesture tracking

---

If you like this project, give it a star on GitHub 


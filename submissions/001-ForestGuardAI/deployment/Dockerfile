# ============================================================
# AI BASED DEFORESTATION MONITORING SYSTEM (DUMMY VERSION)
# Technologies Used:
# OpenCV + TensorFlow + Matplotlib (PyChart)
# ============================================================

import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from datetime import datetime
import random

# ============================================================
# GLOBAL CONFIGURATION
# ============================================================

IMAGE_SIZE = 128
THRESHOLD = 0.5
STATE_NAME = "Tamil Nadu"

# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def print_header():
    print("="*60)
    print("AI Environmental Monitoring Dashboard")
    print("State:", STATE_NAME)
    print("Time:", datetime.now())
    print("="*60)


def load_image(path):
    image = cv2.imread(path)
    if image is None:
        raise ValueError("Image not found! Place sample.jpg in folder.")
    image = cv2.resize(image, (IMAGE_SIZE, IMAGE_SIZE))
    return image


def preprocess_image(image):
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image


def show_image(image):
    cv2.imshow("Input Satellite Image", image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# ============================================================
# NDVI CALCULATION (Dummy Vegetation Index)
# ============================================================

def calculate_ndvi(image):
    # Simulating Red and NIR bands using channels
    red = image[:, :, 2].astype(float)
    nir = image[:, :, 1].astype(float)

    numerator = nir - red
    denominator = nir + red + 1e-5

    ndvi = numerator / denominator
    return ndvi


def display_ndvi(ndvi):
    plt.imshow(ndvi, cmap='RdYlGn')
    plt.colorbar()
    plt.title("NDVI Vegetation Index")
    plt.show()

# ============================================================
# TENSORFLOW DUMMY MODEL
# ============================================================

def build_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model


def predict_deforestation(model, image):
    prediction = model.predict(image)
    return prediction[0][0]

# ============================================================
# ALERT SYSTEM
# ============================================================

def generate_alert(score):
    if score > THRESHOLD:
        return "🚨 ALERT: Possible Deforestation Detected!"
    else:
        return "✅ Forest Area Stable"


# ============================================================
# DUMMY POACHING DETECTION (SIMULATION)
# ============================================================

def simulate_poaching_detection():
    humans_detected = random.randint(0, 5)
    vehicles_detected = random.randint(0, 3)

    risk_score = humans_detected * 0.6 + vehicles_detected * 0.4

    return humans_detected, vehicles_detected, risk_score

# ============================================================
# DATA VISUALIZATION (PYCHART / MATPLOTLIB)
# ============================================================

def show_forest_bar_chart():
    categories = ["Forest Area", "Deforested Area"]
    values = [random.randint(60, 90), random.randint(10, 40)]

    plt.figure()
    plt.bar(categories, values)
    plt.title("Forest Monitoring Report")
    plt.xlabel("Category")
    plt.ylabel("Percentage")
    plt.show()


def show_trend_graph():
    years = list(range(2000, 2026))
    forest_cover = [random.randint(60, 90) for _ in years]

    plt.figure()
    plt.plot(years, forest_cover)
    plt.title("Forest Cover Trend (2000-2025)")
    plt.xlabel("Year")
    plt.ylabel("Forest Cover %")
    plt.show()

# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    print_header()

    # Load Image
    image = load_image("sample.jpg")
    show_image(image)

    # NDVI
    ndvi = calculate_ndvi(image)
    display_ndvi(ndvi)

    # Preprocess
    processed_image = preprocess_image(image)

    # Build Model
    model = build_model()

    # Prediction
    score = predict_deforestation(model, processed_image)
    print("Deforestation Probability:", score)

    # Alert
    alert_message = generate_alert(score)
    print(alert_message)

    # Simulate Poaching Detection
    humans, vehicles, risk = simulate_poaching_detection()
    print("\nPoaching Detection Report")
    print("Humans Detected:", humans)
    print("Vehicles Detected:", vehicles)
    print("Risk Score:", risk)

    # Charts
    show_forest_bar_chart()
    show_trend_graph()

    print("\nSystem Execution Completed Successfully!")

# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()

# Diabetes Prediction App

This is a **Streamlit** web application that predicts whether a person is likely to have diabetes based on user input. The app uses a **machine learning model** trained on medical data.

---

## Features
- Interactive UI with sliders for user input
- Model-based diabetes prediction
- User-friendly interface
- Real-time results

---

## Requirements
Ensure you have the following installed:

```bash
pip install streamlit numpy pandas pickle
```

---

## How to Run the App
1. Clone this repository or download the project files.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
streamlit run app.py
```

4. The app will open in your default browser.

---

## Usage
1. Adjust the slider values in the sidebar for different health parameters.
2. Click the **Predict** button to get the result.
3. The app will display whether the person is likely to have diabetes or not.

---

## Model Information
- The model is loaded from `prod.pkl`.
- It is a machine learning classifier trained on medical dataset features such as:
  - Pregnancies
  - Glucose Level
  - Blood Pressure
  - Skin Thickness
  - Insulin Level
  - BMI
  - Diabetes Pedigree Function
  - Age

---

## File Structure
```
.
├── app.py             # Main Streamlit app script
├── prod.pkl           # Pre-trained machine learning model
├── README.md          # Documentation
```

---

## Troubleshooting
- If you encounter errors while running the app, ensure all dependencies are installed.
- If `prod.pkl` is missing or outdated, retrain the model and replace the file.

---

## Author
**sudershan**

---

## License
This project is for educational purposes. Feel free to modify and use it.

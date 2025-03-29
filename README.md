# ML Microservice Project

## Description
This project exposes a trained Random Forest model (bank marketing dataset) as a RESTful microservice using Flask.

## Files
- `app.py`: Flask application
- `model.pkl`: Trained ML model
- `label_encoders.pkl`: Encoders for categorical features
- `requirements.txt`: Python dependencies

## Run Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask app:
```bash
python app.py
```

3. Test the API using curl or Postman:
```bash
curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{
           "age": 35,
           "job": "technician",
           "marital": "single",
           "education": "tertiary",
           "default": "no",
           "balance": 1000,
           "housing": "yes",
           "loan": "no",
           "contact": "cellular",
           "day": 5,
           "month": "may",
           "duration": 200,
           "campaign": 1,
           "pdays": 999,
           "previous": 0,
           "poutcome": "unknown"
         }'
```

## Deploy to Render

1. Push project to GitHub.
2. Go to [Render](https://render.com).
3. Create new Web Service.
4. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`

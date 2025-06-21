from src.pipelines.predict_pipeline import FormData, Predict
from src.logger import logger
from src.exception import AppException
import sys, os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form = request.get_json()
        stuRecord = {
            "gender": [form["gender"]],
            "race_ethnicity": [form["race_ethnicity"]],  
            "parental_level_of_education": [form["parental_level_of_education"]],
            "lunch": [form["lunch"]],
            "test_preparation_course": [form["test_preparation_course"]],
            "reading_score": [int(form['reading_score'])],   
            "writing_score": [int(form['writing_score'])]    
        }

        formdata = FormData(stuRecord)
        df = formdata.get_df()
        predictor = Predict()
        result = predictor.predictValue(df)

        logger.info(f"Prediction result: {result}")
        return jsonify({"result": result})

    except Exception as e:
        logger.error(f"Exception in /predict: {e}")
        raise AppException(e, sys)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
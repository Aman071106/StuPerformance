# ✨ Student Performance Prediction Model: End-to-End ML Implementation 🤖

This project demonstrates a full machine learning pipeline, including modular structure, EDA, model building, and AWS deployment using Elastic Beanstalk and CI/CD with CodePipeline.

---

## ✅ Installation and Environment Setup

### 1. Git Repository Setup

* Clone the repository.
* Set up a new Conda environment (recommended inside VSCode for ease of visibility).

### 2. Required Files

* `requirements.txt`
* `setup.py`
* `.gitignore` (based on GitHub Python template)

> Note: If `-e .` fails with `setup.py`, use `pyproject.toml` for newer pip versions.

---

## 📁 Initial Project Structure

```
StuperformancePrediction/
├── pyproject.toml
├── setup.py
├── requirements.txt
├── .gitignore
├── LICENCE
├── README.md
├── src/
│   └── __init__.py
```

---

## 📂 Project Modules and Utilities

### Structure:

```
StuPrediction/
├── src/
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── predict_pipeline.py
│   │   ├── train_pipeline.py
│   └── test.py
```

### Testing

* `test.py` is used to verify each module individually during development.

---

## 📊 EDA & Model Training

* Best done inside a Jupyter Notebook.
* Use visualizations to show EDA and model insights to stakeholders.

---

## ✍️ Data Ingestion

* Implemented using `@dataclass` when appropriate.
* Add `.artifacts` and `.envs` folders to `.gitignore`.

---

## 🔄 Data Transformation

* Implement transformations inside `data_transformation.py`.
* Save pipelines using `joblib` or `pickle` via utility functions.

---

## 🔧 Model Training

* Use `RandomizedSearchCV` or `GridSearchCV` for tuning.
* Always save the **trained model**, not a fresh untrained instance.

---

## 🛍️ Prediction Pipeline + UI

### Backend (Flask): `endpoints.py`

### Frontend (Streamlit): `app.py`

Directory:

```
StuPrediction/
├── appBackend/
│   └── endpoints.py
├── appFrontend/
│   └── app.py
```

---

## 🏙️ Deployment

> **Repository contains multiple deployment setups to learn different strategies.**

### a) AWS Elastic Beanstalk Deployment
**Note:You’ve correctly granted broad permissions (though ideally not recommended for production), so the pipeline should now have enough access to AWS services.This means we have given all permissions in code pipeline in this deployment which is generally not recommmended. We should create custom inline policies and give permissions as error occured**

#### IAM Overview

| User Type | Permissions                            |
| --------- | -------------------------------------- |
| **Root**  | Full account access. Use sparingly.    |
| **IAM**   | Restricted. Use for daily development. |

### Security Best Practices

* Enable MFA
* Set budget alerts
* Monitor Free Tier usage

### AWS Setup Steps

1. Create an AWS account
2. Link billing method
3. Install EB CLI or use AWS Console

### Project Structure (for Beanstalk Flask)

```
StuPrediction/
├── application.py        # Flask Entry Point
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── src/
│   └── pipelines/
│       └── predict_pipeline.py
```

Inside `application.py`:

```python
application = Flask(__name__)
app = application
```

### .ebextensions/python.config

```yaml
option_settings:
  "aws:elasticbeanstalk:container:python":
    WSGIPath: application:application
```

---

## 🚀 Elastic Beanstalk Roles (via IAM)

### 1. `aws-elasticbeanstalk-service-role`

* **Trusted Entity:** Elastic Beanstalk
* **Policies:**

  * `AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy`
  * `AWSElasticBeanstalkService`

### 2. `aws-elasticbeanstalk-ec2-role`

* **Trusted Entity:** EC2
* **Policies:**

  * `AWSElasticBeanstalkWebTier`
  * `AWSElasticBeanstalkWorkerTier`
  * `AWSElasticBeanstalkMulticontainerDocker`

Assign these roles in EB under `Configuration → Security`.

---

## 📦 CodePipeline for CD (Continuous delivery)

### Source: GitHub (OAuth)

> Skipping build/test stages is fine for now.

### Execution Modes:

| Mode       | Behavior                | Use Case                      |
| ---------- | ----------------------- | ----------------------------- |
| Superseded | Cancels previous builds | ✅ Recommended for web apps    |
| Queued     | Runs sequentially       | For builds that must complete |
| Parallel   | All in parallel         | For stateless microservices   |

### Why Superseded?

You’re deploying a **single app**, so only latest commit matters.

---

## 🔐 Common Permissions Fixes

* For `cloudformation:GetTemplate` error: add inline policy with CloudFormation read access.
* For `S3 bucket access`: ensure EB has permission to read/write to the deployment bucket.
* Custom permission json for codepipeline:
```bash
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Action": [
				"cloudformation:*",
				"s3:*",
				"ec2:*",
				"autoscaling:*",
				"elasticbeanstalk:*"
			],
			"Resource": "*"
		}
	]
}
```
---

## 💡 Tips

* Use logs from EB → Logs → Full logs to debug deployment errors.
* If using Streamlit or other non-WSGI, prefer Docker + ECR + EB.
* Commit and push → Release change on CodePipeline → Auto deploy

---

Happy Learning and Deploying ✨

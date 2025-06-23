# **Student performance prediction model for learning End to end ML implementation 🤖**

This project will be based on a generic ml project structure that can be used in ml/dl etc.


Steps)
# Installation types setup
1)Git{Repository} setup
    # Setting  up a new env(conda)
Note:
    If you create a conda env inside vscode inside a specific repo we will get that folder there and can see it from here but if we created the env somewhere else(generally in anaconda3/envs) then that same folder will be present there.
2)requirements.txt
3)setup.py
4)gitignore with template in github

For above process and many other such processes/steps there are also automated ways but we will learn them later first by learnign basics

Current state
CarPricePrediction/
├── pyproject.toml   (for newer pips as -e . will break down)   
├── setup.py            
├── requirements.txt
├── .gitignore
├── LICENCE           
├── README.md
├── src/
│   └──__init__.py



Part 2)Project structure setup with exception,logging,utils,components
CarPricePrediction/
├── pyproject.toml   (for newer pips as -e . will break down)   
├── setup.py            
├── requirements.txt
├── .gitignore
├── LICENCE           
├── README.md
├── src/
│   └──__init__.py
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│   └── components/      
│       ├── __init__.py
│       └── data_ingestion.py
│       └── data_transformation.py
│       └── model_trainer.py
│   └── components/       
│       ├── __init__.py
│       └── predict_pipeline.py
│       └── train_pipeline.py
│   └── test.py

Testing done after and in between each part in test.py

Part3)
EDA model training and fe etc

These things are bst to do in jupyter notebook first in an organized manner then w replicate same code in modular way.
For everything in project there should be a reason
We show the eda n model_training to the stake holder



First we creat a basic model then improve the model

Part4)Implement data ingestion
When to use dataclass decorator --when there is only class attributes
add to git ignore
# Environments
.artifacts


Part 5)Data transformation.py
folder structure same
utils use also seen like pkl file saving

Part6) model_trainer.py
also seen hyperparameter tuning and custom error in appexception

Important point error :
-when we save a model/transfoemer etc and we get a log saving RnadomForestRegressor() empty brackets it means new instance is being saved or no training has occured , so keep in mind to pass the trained model or processor in pkl path instead of a new instance

Part7) predict_pipeline.py and Flask backend and streamlit frontend
StuPrediction/
-appBackend/
endpoints.py
-appFrontend/
app.py
rest structure remains same


Part 8) Deployment
Note: my repo contains multiple apps for same purpose to show different deployment techniques
Techniques learnt(Creation of pipelines in deployment)
a) AWS deployment (beanstalk)
ref: https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/lecture/44058702#overview
//
In AWS, IAM user and root user are very different in terms of their purpose, scope, and security implications.

🔐 Root User
What it is: The root user is the AWS account owner — the identity that was used to create the AWS account.

Permissions: Has unrestricted access to all resources and services in the account.

Use cases:

Setting up billing and payment info

Creating the first IAM user

Changing account settings (e.g., close account, modify support plan)

Managing root MFA settings

Security best practice:
✅ Use only when absolutely necessary
❌ Do not use it for daily tasks
✅ Enable MFA (multi-factor authentication)

👤 IAM User (Identity and Access Management User)
What it is: A user created under the AWS account using IAM to manage access and permissions.

Permissions: Only has the permissions explicitly granted via IAM policies.

Use cases:

Regular development, administration, and operational tasks

Assigning roles, groups, and granular permissions

Used for multi-user access control

Best practice:
✅ Create an IAM user for each individual
✅ Assign least privilege principle — only what they need
✅ Use groups and roles to manage permissions efficiently
🛡️ Best Practices to Stay Safe
Tip	Why It Helps
Set a billing budget	Email alerts when spending crosses limits
Monitor Free Tier usage monthly	Spot services that may start charging
Enable billing alerts	Activates CloudWatch usage tracking
Delete unused resources	Prevent background charges
Use AWS Cost Explorer	Understand where money is going


-first create a aws account on [site](https://aws.amazon.com/) and link your credit or debit card
-requires two configuration files   (python.config and .ebextensions)

- diagram:
box(github repo)->connected to below box
box(elasticbeanstalk- An instance of cloud env type thing(linux machine here) present in aws)

now the connection is a pipeline to push code,artifacts etc to the elasticbeanstalk instance
We will use codepipeline in aws , as we press deploy button in our cloud macchine it the latest code will be deployed to it through the pipeline
This pipeline is called continuous delivery pipeline

Note: direct github(without docker) to elasticBeanStalk deplooyment will work ony  for single application.py file that shoudl be WSGI Based like flask or fast not streamlit otherwise we need to use docker.
So the first method will work for single application.py file.
like this
StuPrediction/
├── application.py            # Flask entry point (renamed from app.py)
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── src/
│   ├── pipelines/
│   │   └── predict_pipeline.py
│   ├── logger.py
│   ├── exception.py
also do
application = Flask(__name__)
app=application
like this
Steps:
1)config files and git push
2)aws instance of elasticbeanstalk
3)code pipeline

- config files:
#### .ebsextensions folder
contains the python.config file

```bash
option_settings:
    "aws:elasticbeanstalk:container:python":
        WSGIPath: application:application
```
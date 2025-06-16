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
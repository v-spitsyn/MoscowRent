MoscowRent
==============================

Analysis of Moscow rental property's pricing

The project presents building a model that predicts rental price per square meter for 1 to 5-room flats in Moscow. The data for training were scraped from advertisements on a popular classified avito.ru. Scraping was conducted daily from August 1 to August 14, leading to 14 thousand observations. Random forest is used for prediction and achieves mean absolute percentage error of 16%.

Description of the files (in the order of execution):
1) scraping.py - scraping data from Avito and saving them to pickles
2) stations.py - downloading information about Moscow underground stations and computing their distances to the city center
3) make_dataset.py - constructing a dataframe for exploratory data analysis from pickle files
4) eda.ipynb  - exploratory analysis of the prices, publications flow and commissions 
5) modelling.ipynb - hyperparameter optimization with cross-validation
6) build_features.py - constructing a dataframe for training from pickle files
7) train_model.py - training random forest with hyperparameters found in modelling.py
8) predict_model.py - making predictions with the trained model

Only eda.ipynb and modelling.ipynb contain comments.

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models
    │
    ├── notebooks          <- Jupyter notebooks.
    │   |
    |   ├── eda.ipynb      <- Exploratory data analysis
    |   └── modelling.ipynb<- Hyperparameter optimization
    |
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment
    ├── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   ├── make_dataset.py
        |   ├── scraping.py
        |   └── stations.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   ├── build_features.py
        │   
        |   
        ├── models         <- Scripts to train models and then use trained models to make
            │                 predictions
            ├── predict_model.py
            └── train_model.py


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

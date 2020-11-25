MoscowRent
==============================

Analysis of Moscow rental property's pricing

The project presents building a model that predicts rental price per square meter for 1 to 5-room flats in Moscow. The data for training were scraped from advertisements on a popular classified avito.ru. Scraping was conducted daily from August 1 to August 14, leading to a 13 thousand observations. Random forest is used for prediction and achieves mean absolute percentage error of 16%.

The logical order of files is 
scraping.py -> make_dataset.py -> eda.ipynb -> modelling.ipynb -> build_features.py -> train_model.py -> predict_model.py

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
        |   └── scraping.py
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

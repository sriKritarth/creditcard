array(['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9',
       'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18',
       'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27',
       'V28', 'Amount'], dtype=object)

# Credit Card Fraud Detection

A machine learning project for detecting credit card fraud using Random Forest classifier.

## Quick Start

### Prerequisites
- Python 3.11+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd creditcard
```

2. Install dependencies:
```bash
pip install -r dev-requirements.txt
```

3. Train the model:
```bash
make train
```

4. Run the applications:
```bash
# FastAPI app
make run-api

# Streamlit app
make run-streamlit
```

### Available Commands

- `make data` - Process the raw data
- `make train` - Train the machine learning model
- `make test` - Run tests
- `make lint` - Run linting checks
- `make format` - Format code with black
- `make sort-imports` - Sort imports with isort
- `make run-api` - Run FastAPI application
- `make run-streamlit` - Run Streamlit application

## API Usage

The FastAPI application provides a REST API for fraud detection:

- **GET** `/` - Health check endpoint
- **POST** `/predict` - Predict fraud probability

Example prediction request:
```json
{
  "Time": 0.0,
  "V1": -1.359807134,
  "V2": -0.072781173,
  "V3": 2.536346738,
  "V4": 1.378155224,
  "V5": -0.338261077,
  "V6": 0.462387778,
  "V7": 0.239598554,
  "V8": 0.098697901,
  "V9": 0.36378697,
  "V10": 0.090794172,
  "V11": -0.551599533,
  "V12": -0.617800856,
  "V13": -0.991389847,
  "V14": -0.311169354,
  "V15": 1.468176972,
  "V16": -0.470400525,
  "V17": 0.207971242,
  "V18": 0.02579058,
  "V19": 0.40399296,
  "V20": 0.251412098,
  "V21": -0.018306778,
  "V22": 0.277837576,
  "V23": -0.11047391,
  "V24": 0.066928075,
  "V25": 0.128539358,
  "V26": -0.189114844,
  "V27": 0.133558377,
  "V28": -0.021053053,
  "Amount": 149.62
}
```

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

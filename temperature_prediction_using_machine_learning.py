# -*- coding: utf-8 -*-
"""TEMPERATURE PREDICTION USING MACHINE LEARNING

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hNlWfhYswoOZ9Dgv8OEVw7eeuYc_i0Ac
"""



""""Weather in Szeged 2006-2016" (**TEMPERATURE PREDICTION USING MACHINE LEARNING**)
Hourly/daily summary with temperature, pressure, wind speed and more.
""Temperature Prediction using Machine learning and comparison between different regression Models""

This Data has been from(https://www.kaggle.com/budincsevity/szeged-weather).
"""

import warnings

weather.isnull().any()   ## Checks weather there is any null value present in the dataset



warnings.filterwarnings('ignore')
import os
import pandas as pd
import numpy as np

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LinearRegression

import tensorflow as tf
from tensorflow import keras

from sklearn import preprocessing

weather = pd.read_csv('weatherHistory.csv')

weather.head()

weather.columns

weather.shape

weather.describe()

weather.isnull().any() ## to check for null values in the datasets

weather.isnull().all()

""""CHECKING THE NUMBER OF NULLS IN %""""

round(100*(weather.isnull().sum()/len(weather.index)),2)

"""Now,We will try to impute Null with the maximum Occured values"""



weather['Precip Type'].value_counts()

weather.loc[weather['Precip Type'].isnull(),'Precip Type']-'rain'

weather.loc[weather['Precip Type'].isnull(),'Precip Type']-'snow'

weather.loc[weather['Precip Type']=='rain','Precip Type']=1  ## Inputing binary values in Type Columns
weather.loc[weather['Precip Type']=='snow','Precip Type']=0

weather_num = weather[list(weather.dtypes[weather.dtypes!='object'].index)]

weather_y = weather_num.pop('Temperature (C)')
weather_X = weather_num



"""**Spilliting the Data for training and Testing purpose
**
"""

train_X,test_X,train_y,test_y = train_test_split(weather_X,weather_y,test_size=.3,random_state=5)

train_X

"""*BUILDING THE MODEL
*
"""

model = LinearRegression()
model.fit(train_X,train_y)

prediction = model.predict(train_X)

np.mean((prediction-train_y)**2)

"""## **Getting started**

The document you are reading is not a static web page, but an interactive environment called a **Colab notebook** that lets you write and execute code.

For example, here is a **code cell** with a short Python script that computes a value, stores it in a variable, and prints the result:
"""

Error- .903800

pd.DataFrame({'actual':train_y,'prediction':prediction,'diff':(train_y-prediction)})

prediction = model.predict(test_X)

np.mean((prediction-test_y)**2)



"""**POLYNOMIAL REGRESSION
**
"""

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=4)
X_poly = poly.fit_transform(train_X)
poly.fit(X_poly,train_y)

Lin2 = LinearRegression()
Lin2.fit(X_poly, train_y)

prediction2 = Lin2.predict(poly.fit_transform(test_X))  ## Calculating the erroe
np.mean((prediction2-test_y)**2)

pd.DataFrame({'Actual':test_y,'prediction':prediction2,'diff':(test_y-prediction2)})

"""DECISION TREE REGRESSION - 
CART
"""

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(train_X,train_y)

prediction3 = regressor.predict(test_X)
np.mean((prediction3-test_y)**2)

pd.DataFrame({'Actual':test_y,'prediction':prediction3,'diff':(test_y-prediction3)})



"""ERROR = .008

Random Forest with maximum Dept — 10
"""

from sklearn.ensemble import RandomForestRegressor
regr = RandomForestRegressor(max_depth=10,random_state =0,n_estimators=100)
regr.fit(train_X,train_y)

prediction4 = regr.predict(test_X)
np.mean((prediction4-test_y)**2)

pd.DataFrame({'Actual':test_y,'prediction':prediction4,'diff':(test_y-prediction4)})

"""ERROR -  .008

Random Forest with maximum depth — 50
"""

regr2 = RandomForestRegressor(max_depth=50,random_state=0,n_estimators=100)
regr2.fit(train_X,train_y)

prediction5 = regr2.predict(test_X)
np.mean((prediction5-test_y)**2)

pd.DataFrame({'Actual':test_y,'prediction':prediction5,'diff':(test_y-prediction5)})

"""Error — 0.0019
This gives the least error.
But we should always take care that our model is not overfitting the data. So sometimes even a model with least error can predict very bad outputs for more generalized inputs.

Comparison:

ERROR

Linear Regression => .902
Polynomial regression => 0.999
CART => .008
RANDOM FOREST DEPTH -10  => .008
RANDOM FOREST DEPTH - 50 => .002

Colab notebooks allow you to combine **executable code** and **rich text** in a single document, along with **images**, **HTML**, **LaTeX** and more. When you create your own Colab notebooks, they are stored in your Google Drive account. You can easily share your Colab notebooks with co-workers or friends, allowing them to comment on your notebooks or even edit them. To learn more, see [Overview of Colab](/notebooks/basic_features_overview.ipynb). To create a new Colab notebook you can use the File menu above, or use the following link: [create a new Colab notebook](http://colab.research.google.com#create=true).

Colab notebooks are Jupyter notebooks that are hosted by Colab. To learn more about the Jupyter project, see [jupyter.org](https://www.jupyter.org).

## Data science

With Colab you can harness the full power of popular Python libraries to analyze and visualize data. The code cell below uses **numpy** to generate some random data, and uses **matplotlib** to visualize it. To edit the code, just click the cell and start editing.
"""

import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()

"""You can import your own data into Colab notebooks from your Google Drive account, including from spreadsheets, as well as from Github and many other sources. To learn more about importing data, and how Colab can be used for data science, see the links below under [Working with Data](#working-with-data).

## Machine learning

With Colab you can import an image dataset, train an image classifier on it, and evaluate the model, all in just [a few lines of code](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb). Colab notebooks execute code on Google's cloud servers, meaning you can leverage the power of Google hardware, including [GPUs and TPUs](#using-accelerated-hardware), regardless of the power of your machine. All you need is a browser.

Colab is used extensively in the machine learning community with applications including:
- Getting started with TensorFlow
- Developing and training neural networks
- Experimenting with TPUs
- Disseminating AI research
- Creating tutorials

To see sample Colab notebooks that demonstrate machine learning applications, see the [machine learning examples](#machine-learning-examples) below.

## More Resources

### Working with Notebooks in Colab
- [Overview of Colaboratory](/notebooks/basic_features_overview.ipynb)
- [Guide to Markdown](/notebooks/markdown_guide.ipynb)
- [Importing libraries and installing dependencies](/notebooks/snippets/importing_libraries.ipynb)
- [Saving and loading notebooks in GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
- [Interactive forms](/notebooks/forms.ipynb)
- [Interactive widgets](/notebooks/widgets.ipynb)
- <img src="/img/new.png" height="20px" align="left" hspace="4px" alt="New"></img>
 [TensorFlow 2 in Colab](/notebooks/tensorflow_version.ipynb)

<a name="working-with-data"></a>
### Working with Data
- [Loading data: Drive, Sheets, and Google Cloud Storage](/notebooks/io.ipynb) 
- [Charts: visualizing data](/notebooks/charts.ipynb)
- [Getting started with BigQuery](/notebooks/bigquery.ipynb)

### Machine Learning Crash Course
These are a few of the notebooks from Google's online Machine Learning course. See the [full course website](https://developers.google.com/machine-learning/crash-course/) for more.
- [Intro to Pandas](/notebooks/mlcc/intro_to_pandas.ipynb)
- [Tensorflow concepts](/notebooks/mlcc/tensorflow_programming_concepts.ipynb)
- [First steps with TensorFlow](/notebooks/mlcc/first_steps_with_tensor_flow.ipynb)
- [Intro to neural nets](/notebooks/mlcc/intro_to_neural_nets.ipynb)
- [Intro to sparse data and embeddings](/notebooks/mlcc/intro_to_sparse_data_and_embeddings.ipynb)

<a name="using-accelerated-hardware"></a>
### Using Accelerated Hardware
- [TensorFlow with GPUs](/notebooks/gpu.ipynb)
- [TensorFlow with TPUs](/notebooks/tpu.ipynb)

<a name="machine-learning-examples"></a>

## Machine Learning Examples

To see end-to-end examples of the interactive machine learning analyses that Colaboratory makes possible, check out the [AI Hub](https://aihub.cloud.google.com/) project.

A few featured examples:

- [Neural Style Transfer](https://aihub.cloud.google.com/p/products%2F7f7495dd-6f66-4f8a-8c30-15f211ad6957): Use deep learning to transfer style between images.
- [EZ NSynth](https://aihub.cloud.google.com/p/products%2Fcddd17cf-5f86-4ce7-b6b6-03c5e52ee0fb): Synthesize audio with WaveNet auto-encoders.
- [Fashion MNIST with Keras and TPUs](https://aihub.cloud.google.com/p/products%2F7a0acf15-0be0-41a6-9bdb-5a5abd4e8fbf): Classify fashion-related images with deep learning.
- [DeepDream](https://aihub.cloud.google.com/p/products%2Ff9e8fc11-ad0f-410a-bebe-2482066ce570): Produce DeepDream images from your own photos.
- [Convolutional VAE](https://aihub.cloud.google.com/p/products%2Ff5e8dd20-6b34-44a0-bc45-6e345e36a4e7): Create a generative model of handwritten digits.
"""
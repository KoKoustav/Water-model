import numpy as np
import pickle
import warnings
from sklearn.exceptions import DataConversionWarning
import os

# Define a filter function to suppress the specific warning
def warn(*args, **kwargs):
    pass

# Suppress sklearn warnings
warnings.warn = warn

# Define an environment variable for the model path
MODEL_PATH = os.environ.get('MODEL_PATH', 'trained_model.sav')
load_model = pickle.load(open(MODEL_PATH, 'rb'))


# Correctly formatted input data
# input_data = '5.324941855611651,280.08965491445105,35344.658047005905,13.043806107761025,180.20674636482346,392.42149580418476,10.50481954758385,55.084667854857926,4.427137925692965'
input_data = '1.0,7,0,0,0,0,0,0,0'

# Convert the input string into a NumPy array
input_values = [float(val) for val in input_data.split(',')]

input_data_as_numpy_array = np.asarray(input_values)

# Reshape the array
input_data_reshape = input_data_as_numpy_array.reshape(1, -1)


# Now you can make predictions
prediction = load_model.predict(input_data_reshape)
print(prediction)

if prediction[0] == 1:
    print("The water is drinkable")
else:
    print("The water is not drinkable")
    
import numpy as np
from PIL import Image # Python Imaging Library - For operations like: Image open, resize image, etc..
from IPython.display import Image as show_image  # For displaying our test images to you
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_resnet_v2 import preprocess_input, decode_predictions



img = Image.open("sportscar.jpg").resize((299,299))


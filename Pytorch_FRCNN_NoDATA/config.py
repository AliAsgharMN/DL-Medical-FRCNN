import torch

BATCH_SIZE = 16 # increase / decrease according to GPU memeory
RESIZE_TO = 416 # resize the image for training and transforms
NUM_EPOCHS = 50 # number of epochs to train for
NUM_WORKERS = 4

DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# training images and XML files directory
TRAIN_DIR = 'data/Uno Cards.v2-raw.voc/train'
# validation images and XML files directory
VALID_DIR = 'data/Uno Cards.v2-raw.voc/valid'

# classes: 0 index is reserved for background
# CLASSES = [
#     '__background__', '11', '9', '13', '10', '6', '7', '0', '5', '4', '2', '14', 
#     '8', '12', '1', '3'
# ]

# Debug --> class names changed
CLASSES = [
    '__background__', 'post_S1_top', 'ant_S1_top', 'post_L5_bot', 'ant_L5_bot', 'post_L1_top', 'ant_L1_top', 'post_C7_top', 'ant_C7_top', 'post_FH', 'ant_FH'
]

NUM_CLASSES = len(CLASSES)

# whether to visualize images after crearing the data loaders
VISUALIZE_TRANSFORMED_IMAGES = True

# location to save model and plots
OUT_DIR = 'outputs'
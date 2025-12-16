import os

ENV_NAME = "highway-fast-v0"
TOTAL_TIMESTEPS = 50000  
LEARNING_RATE = 5e-4

LOG_DIR = "./logs/"
MODEL_DIR = "./models/"
VIDEO_DIR = "./videos/"

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)
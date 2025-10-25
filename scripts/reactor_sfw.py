from transformers import pipeline
from PIL import Image
import io
import logging
import os
import comfy.model_management as model_management
from reactor_utils import download
from scripts.reactor_logger import logger

MODEL_EXISTS = False

def nsfw_image(img_data, model_path: str):
    return False

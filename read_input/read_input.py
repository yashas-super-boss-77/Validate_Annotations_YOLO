import json
import os

def read_config(config_path):
    with open(config_path, 'r') as file:
        data_dict = json.load(file)
    return data_dict

def read_data():
    config_path = "/home/kingkong/projects/annotations_to_pdf/configs/config_read_input.json"
    config = read_config(config_path)

    images_path = config["input_images_path"]
    labels_path = config["label_images_path"]

    return images_path, os.listdir(images_path), labels_path, os.listdir(labels_path)
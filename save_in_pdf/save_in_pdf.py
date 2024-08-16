from fpdf import FPDF
import os
import json

def read_config(config_path):
    with open(config_path, 'r') as file:
        data_dict = json.load(file)
    return data_dict

def save_pdf(processed_image_list):

    # Create a PDF object
    pdf = FPDF(orientation='P', unit='mm', format='A4')

    config_file_path = "/home/kingkong/projects/annotations_to_pdf/configs/save_in_pdf.json"
    config_file = read_config(config_file_path)

    output_pdf = config_file["path"]

    index = 0
    for processed_image in processed_image_list:
        
        index += 1
        # Save the processed image temporarily
        temp_image_path = f"temp_image_{index}.jpg"
        processed_image.save(temp_image_path)

        # Add the image to the PDF
        pdf.add_page()
        pdf.image(temp_image_path, x=10, y=10, w=190)  # Adjust the position and size if necessary

        # Optionally, delete the temporary image file
        os.remove(temp_image_path)
    
    print (pdf)

    # Save the PDF
    pdf.output(output_pdf)
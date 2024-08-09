import os
from PIL import Image, ImageDraw, ImageFont


def draw_bounding_box(image_path, label_path):
    # Open the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Optional: Load a font for the labels
    try:
        font = ImageFont.truetype("arial.ttf", size=32)  # Use a truetype font
    except IOError:
        font = ImageFont.load_default() 

    # Get image dimensions
    image_width, image_height = image.size

    # Read the label file
    with open(label_path, 'r') as f:
        for line in f:
            # Assume labels are in the format: x_min, y_min, x_max, y_max
            parts = line.strip().split(' ')
            
            cl, x, y, w, h = map(float, parts[:5])

            # Convert normalized coordinates to pixel coordinates
            x *= image_width
            y *= image_height
            w *= image_width
            h *= image_height

            # print (x, y)
            # print (w, h)
            # x_min = x
            # y_min = y
            # x_max = x + w
            # y_max = y + h
            # Calculate the top-left corner of the bounding box
            x_min = (x - w) / 2
            y_min = (y - h) / 2
            
            # Calculate the bottom-right corner of the bounding box
            x_max = (x + w) / 2
            y_max = (y + h) / 2
            
            # Calculate text size and position
            bbox = draw.textbbox((x_min, y_min - 30), "bullet_holes", font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            text_x = x_min
            text_y = y_min - text_height - 2  # Position the text slightly above the box
            text_y = max(0, text_y) 

            # Draw the bounding box
            draw.rectangle([x_min, y_min, x_max, y_max], outline="red", width=5)

            # # Put the label text above the bounding box
            draw.text((text_x, text_y), "bullet_hole", fill="white", font=font)

    return image
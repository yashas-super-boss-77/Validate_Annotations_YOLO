# read the images and labels
import read_input.read_input as read_input
import annotate_data.annotate_data as annotate_data
import save_in_pdf.save_in_pdf as save_in_pdf
import os
from tqdm import tqdm

images_path, images_list, labels_path, labels_list = read_input.read_data()
print ("Read input paths")

processed_image_list = []

for i in tqdm(range(len(images_list))):

    # annotate the data
    processed_image = annotate_data.draw_bounding_box(os.path.join(images_path, images_list[i]), os.path.join(labels_path, images_list[i][:-3]+"txt"))

    processed_image_list.append(processed_image)
                                                      

# save it in the pdfs format
save_in_pdf.save_pdf(processed_image_list)



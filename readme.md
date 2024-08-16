# Annotations Validator (YOLO)

This converts the annotations (YOLO) into pdf so that it can be helpful for anyone who wish to validate the annotations. It will take the images and labels as input directory and produce a pdf with annotations market. This will help the validator to just go through the pdf and validate the annotations. Otherwise who will go install the annotator in their systems and run the code, solve the dependencies and then load the image dir and then labels dir, all hectic. This code written by me (and chatgpt) will avoid all that hasle.

## Installation


```bash
pip install pillow
pip install opencv-python
pip install fpdf
pip install tqdm
```

## Usage

```
Add the paths to input and output directory in these config files,
1. configs/config_read_input.json
2. configs/save_in_pdf.json

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
No license

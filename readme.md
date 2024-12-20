# Writer.Hand Tool

Writer.Hand is a Python tool designed to add text to images with customizable positions and padding. It uses the Python Imaging Library (PIL) to manipulate images and draw text on them.

It can also used to convert text files to customised handwritten notes.

![Demo Image](images/sample.jpg)

## Features

- Add text to images at specified positions.
- Customize padding around the text.
- Support for various font styles and sizes.
- Split text into lines that fit within the drawable area.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/tineshnehete/writer.hand.git
   ```
2. Navigate to the project directory:
   ```sh
   cd writer.hand
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

```python
from writer_hand import add_text_to_image

file_path = 'path/to/your/image.png'
text = 'Your text here'
position = (50, 50, 50, 50)  # (left, top, right, bottom)
padding = (10, 10, 10, 10)  # (left, top, right, bottom)
output = 'path/to/output/image.png'

add_text_to_image(file_path, text, position, padding, output=output)
```

### Parameters

- `file_path` (str): Path to the image file.
- `text` (str): Text to be added to the image.
- `position` (tuple): (left, top, right, bottom) position to start writing the text.
- `padding` (tuple): (left, top, right, bottom) padding around the text.
- `output` (str, optional): Path to save the output image. If not provided, the original image will be overwritten.
- `args` (list, optional): List of arguments to pass to `draw.text()` method.
- `kwargs` (dict, optional): Dictionary of keyword arguments to pass to `draw.text()` method.

## Example

```python
from PIL import ImageFont

file_path = 'path/to/your/image.png'
text = 'Hello, World!'
position = (50, 50, 50, 50)
padding = (10, 10, 10, 10)
output = 'path/to/output/image.png'
font = ImageFont.truetype('arial.ttf', 24)

add_text_to_image(file_path, text, position, padding, output=output, font=font)
```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

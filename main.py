# write text to image
# import imagefont

from PIL import Image, ImageDraw, ImageFont


def create_a4_size_white_page(file_path):
    """
    Create a white page with A4 size.
    :param file_path: str, path to save the white page.
    :return: str, path to the white

    """
    image = Image.new("RGB", (2480, 3508), "white")
    image.save(file_path)

    print("A white page with A4 size is created successfully.")
    return file_path


def write_text_on_page(text, file_path, position, padding=(2, 2, 2, 2), output=None, *args, **kwargs):
    """
    Write text on the white page.
    :param text: str, text to write on the page.
    :param file_path: str, path to save the page with text.
    :param position: tuple, (left, top, right, bottom) position to start writing the text.
    :param padding: tuple, (left, top, right, bottom) padding around the text.
    :param args: list, list of arguments to pass to draw.text() method.
    :param kwargs: dict, dictionary of keyword arguments to pass to draw.text() method.
    :return: str, path to the page with text.
    """
    if output is None:
        output = file_path
    image= Image.open(file_path)

    draw = ImageDraw.Draw(image)
    font = kwargs.get('font', None)

    # Calculate the drawable area
    top, right, bottom, left = position
    pad_top, pad_right, pad_bottom, pad_left = padding
    drawable_width = image.size[0] - left - right - pad_left - pad_right
    drawable_height = image.size[1] - top - bottom - pad_top - pad_bottom

    # Split text into lines that fit within the drawable width
    lines = []
    words = text.split()
    current_line = words[0]

    for word in words[1:]:
        test_line = current_line + ' ' + word
        width, _ = draw.textbbox((0, 0), test_line, font=font)[2:]
        if width <= drawable_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)

    # Draw each line of text with padding
    y = top + pad_top
    for line in lines:
        draw.text((left + pad_left, y), line, *args, **kwargs)
        # Adjust line height based on font size
        y += font.getbbox(line)[3] if font else 20
        y += pad_bottom  # Add padding in y direction

    image.save(output)
    print(f"Text '{text}' is written on the page successfully.")
    return file_path


# font = ImageFont.truetype(
#     "./fonts/2.ttf"
#     , 100)
# print(
#     write_text_on_page(
#         '''
#         Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

# Why do we use it?
# It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


# Where does it come from?
# Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

# The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
#         ''',
#         "note_book.jpeg",
#         (430, 100,0,250),
#         (0,0,0,0),
#         fill="blue",
#         font=font
#     )
# )


# write cli wrapper
if __name__ == "__main__":
    import argparse
    import os
    parser = argparse.ArgumentParser(description="Write text on image.")
    parser.add_argument("--text", type=str, help="Text to write on the image.")
    parser.add_argument("--txtfile", type=str, help="Path to the text file.")
    parser.add_argument("image", type=str, help="Path to the image.")
    parser.add_argument("output", type=str,
                        help="Path to save the image with text.")
    parser.add_argument("position", type=int, nargs=4,
                        help="Position to start writing the text (left, top, right, bottom).")
    parser.add_argument("padding", type=int, nargs=4,
                        help="Padding around the text (left, top, right, bottom).")
    parser.add_argument(
        "--font", type=str, default="./fonts/2.ttf",  help="Path to the font file.")
    parser.add_argument("--font-size", type=int, default=20, help="Font size.")
    parser.add_argument("--fill", type=str, default="black",
                        help="Color to fill the text.")
    args = parser.parse_args()

    # Validate image path
    if not os.path.isfile(args.image):
        print(f"Error: The image file '{args.image}' does not exist.")
        exit(1)

    # Validate output directory
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        print(f"Error: The output directory '{output_dir}' does not exist.")
        exit(1)

    # Read text from the file if provided
    if args.txtfile:
        if not os.path.isfile(args.txtfile):
            print(f"Error: The text file '{args.txtfile}' does not exist.")
            exit(1)
        with open(args.txtfile, "r") as file:
            text = file.read()
    elif args.text:
        text = args.text
    else:
        print("Error: Either --text or --txtfile must be provided.")
        exit(1)
    print(text)
    # Validate position and padding
    if any(p < 0 for p in args.position):
        print("Error: Position values must be non-negative.")
        exit(1)
    if any(p < 0 for p in args.padding):
        print("Error: Padding values must be non-negative.")
        exit(1)

    font = ImageFont.truetype(args.font, args.font_size)
    write_text_on_page(text, args.image, tuple(
        args.position), tuple(args.padding), args.output, fill=args.fill, font=font)    
    print(f"Text '{text}' is written on the image successfully.")
    print(f"Image with text is saved at '{args.output}'.")
    print("Done.")

# write command
# python main.py "Hello World" "note_book.jpeg" "output.jpeg" 430 100 0 250 2 2 2 2 --font "./fonts/2.ttf" --font-size 100 --fill "blue"
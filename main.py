from PIL import Image
from PIL.Image import Image as PILImage

# How many characters to print in each line
CHARACTERS_PER_LINE = 50

image = Image.open("image_path.png")

width, height = image.size

def squash_height(image, scaler: int):
    new_height = round(image.height / scaler)
    return image.resize((image.width, new_height))

def fit_width(img: PILImage, cols: int):
    # Scale to a target text width; adjust height to preserve aspect ratio
    w, h = img.size
    if w <= cols:
        return img
    new_w = cols
    new_h = max(1, round(h * (new_w / w)))
    return img.resize((new_w, new_h), Image.Resampling.LANCZOS)

def create(img: PILImage, color = "white"):
    """For each pixel in the image, print out a corresponding symbol for corresponding amounts
        of light/dark. Also has the option to change the color of the output text.

    Args:
        img (PILImage): Image which we want to convert to ascii.
        color (str, optional): Choose the color of the symbols. Defaults to "white".
    """
    # Convert to have alpha if it doesn't already so we can later check for transparency
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    match color.lower():
        case "red": esc_color = "\x1b[31m"
        case "green": esc_color = "\x1b[32m"
        case "blue": esc_color = "\x1b[34m"
        case "yellow": esc_color = "\x1b[93m"
        case "black": esc_color = "\x1b[30m"
        case _: esc_color= "\x1b[37m"
            
    for i in range(img.height):
        row = ""
        
        for j in range(img.width):
            # (j,i) so it is oriented correctly.
            r, g, b, a = img.getpixel((j,i))
            grey = round((r + g + b) / 3)
            
            # Set transparent pixels as black, so they do not show up
            if (a == 0):
                img.putpixel((j, i), (0,0,0))
                grey = 0

            if grey < 22: row += " "
            elif grey < 43: row += "."
            elif grey < 64: row += "-"
            elif grey < 85: row += "="
            elif grey < 107: row += "+"
            elif grey < 128: row += "*"
            elif grey < 149: row += "x"
            elif grey < 170: row += "#"
            elif grey < 192: row += "$"
            elif grey < 213: row += "&"
            elif grey < 234: row += "X"
            else: row += "@"

        # Create new line after each row
        print(f"{esc_color}{row}")


# Reduce rows to compensate for character ratio of ~1:2
scaled = squash_height(image, 2)

# Set how many characters to generate in each row
scaled = fit_width(scaled, CHARACTERS_PER_LINE)

# Create the ascii
create(scaled)

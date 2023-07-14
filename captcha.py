import random
from PIL import Image, ImageDraw, ImageFont

def generate_captcha(width, height, length):
    # Create a blank image with a yellow background
    image = Image.new('RGB', (width, height), 'yellow')
    draw = ImageDraw.Draw(image)
    
    # Define the characters to be used in the CAPTCHA
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    
    # Generate a random string of the specified length
    captcha_text = ''.join(random.sample(characters, length))
    
    # Define the font and its size
    font = ImageFont.truetype('arial.ttf', 72)
    
    # Calculate the text size and position it in the center
    text_width, text_height = draw.textsize(captcha_text, font)
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2
    
    # Draw the text on the image
    draw.text((text_x, text_y), captcha_text, font=font, fill='black')
    
    # Add some noise to the image
    for x in range(width):
        for y in range(height):
            if random.random() < 0.1:
                draw.point((x, y), fill='black')
    
    # Return the generated CAPTCHA image and the corresponding text
    return image, captcha_text

width = 700  # Width of the CAPTCHA image
height = 350  # Height of the CAPTCHA image
length = 6   # Length of the CAPTCHA text

captcha_image, captcha_text = generate_captcha(width, height, length)
captcha_image.save('captcha.png')
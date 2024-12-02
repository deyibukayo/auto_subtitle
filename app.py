from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Load a font (use a suitable font file on your system)
font_path = "C:\\Windows\\Fonts\\GOTHICBI.ttf"  # Update this with the actual font path
font_size = 60
font = ImageFont.truetype(font_path, font_size)

# Read subtitle text from file and render it
with open('sub.txt', 'r') as file:
    lines = file.readlines()

# Positioning the text at the lower center
text_color = (255, 255, 255)  # White color for text
glow_color = (0, 0, 0)  # Red glow color
glow_radius = 5  # Radius of the glow effect

# Create the output folder for the processed images
Path('sub').mkdir(exist_ok=True)

# Loop through each line in the file and draw it
for i, line in enumerate(lines):
    # Create a new image with transparent background (1920x1080)
    width, height = 1920, 1080
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # Get a drawing context
    draw = ImageDraw.Draw(image)
    
    line = line.strip()  # Remove any surrounding whitespace/newlines
    # Calculate width and height of the text using textbbox
    bbox = draw.textbbox((0, 0), line, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Position the text (horizontal center and bottom)
    x_position = (width - text_width) // 2  # Center horizontally
    y_position = 950  # Stack vertically from bottom

    # Draw glowing text (outer glow)
    for dx in range(-glow_radius, glow_radius + 1):
        for dy in range(-glow_radius, glow_radius + 1):
            if dx**2 + dy**2 <= glow_radius**2:
                # Draw the glow around the text
                draw.text((x_position + dx, y_position + dy), line, font=font, fill=glow_color)

    # Draw the main text over the glow
    draw.text((x_position, y_position), line, font=font, fill=text_color)

    # Save the image with transparent background
    image.save(f"sub/{i + 1}.png", format="PNG")
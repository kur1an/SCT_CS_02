from PIL import Image
import random

def load_image(input_path):
    image = Image.open(input_path)
    return image

def save_image(image, output_path):
    image.save(output_path)

def swap_pixels(image, key):
    random.seed(key)
    pixels = list(image.getdata())
    width, height = image.size

    for _ in range(1000):  
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)

        index1, index2 = y1 * width + x1, y2 * width + x2
        pixels[index1], pixels[index2] = pixels[index2], pixels[index1]

    image.putdata(pixels)
    return image

def apply_math_operation(image, key, operation='add'):
    random.seed(key)
    pixels = list(image.getdata())
    
    if operation == 'add':
        pixels = [( (r + key) % 256, (g + key) % 256, (b + key) % 256 ) for r, g, b in pixels]
    elif operation == 'subtract':
        pixels = [( (r - key) % 256, (g - key) % 256, (b - key) % 256 ) for r, g, b in pixels]
    
    image.putdata(pixels)
    return image

def encrypt_image(input_path, output_path, key):
    image = load_image(input_path)
    image = apply_math_operation(image, key, 'add')
    image = swap_pixels(image, key)
    save_image(image, output_path)
    print(f'Image encrypted and saved to {output_path}')

def decrypt_image(input_path, output_path, key):
    image = load_image(input_path)
    image = swap_pixels(image, key)
    image = apply_math_operation(image, key, 'subtract')
    save_image(image, output_path)
    print(f'Image decrypted and saved to {output_path}')

if __name__ == '__main__':
    mode = input('Choose mode (encrypt/decrypt)e/d: ').strip().lower()
    input_path = input('Enter the input image path: ').strip()
    output_path = input('Enter the output image path: ').strip()
    key = int(input('Enter the key: ').strip())
    
    if mode == 'e':
        encrypt_image(input_path, output_path, key)
    elif mode == 'd':
        decrypt_image(input_path, output_path, key)
    else:
        print('Invalid mode selected.')
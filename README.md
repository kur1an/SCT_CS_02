Here's a `README.md` file for your image encryption tool:

```markdown
# Image Encryption Tool

This tool provides a simple yet effective way to encrypt and decrypt images using pixel manipulation techniques. It allows users to securely alter image data using a key-based encryption method.

## Features

- **Encryption**: Encrypt images by scrambling pixel positions and applying mathematical operations.
- **Decryption**: Decrypt previously encrypted images to restore them to their original state.
- **Command-Line Interface**: Easy-to-use CLI for interacting with the tool.

## How It Works

### Encryption Process

1. **Load Image**: Load the input image.
2. **Pixel Manipulation**: Randomly swap pixel positions and apply mathematical operations.
3. **Save Encrypted Image**: Save the modified image to a new file.

### Decryption Process

1. **Load Encrypted Image**: Load the previously encrypted image.
2. **Reverse Pixel Manipulation**: Undo the pixel swaps and mathematical operations.
3. **Save Decrypted Image**: Save the restored image to a new file.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/SCT_CS_2.git
   cd SCT_CS_2
   ```

2. **Install Dependencies**:
   Make sure you have Python installed on your system. Additionally, install the required libraries using pip:
   ```bash
   pip install pillow
   ```

## Usage

1. **Encrypt an Image**:
   - Run the script: `python image_encryption_tool.py`
   - Choose the encryption mode.
   - Provide the input image path.
   - Specify the output path for the encrypted image.
   - Enter the encryption key.

2. **Decrypt an Image**:
   - Run the script: `python image_encryption_tool.py`
   - Choose the decryption mode.
   - Provide the input image path (encrypted image).
   - Specify the output path for the decrypted image.
   - Enter the decryption key.

## Example

Encrypt an image:

```bash
python image_encryption_tool.py
Choose mode (encrypt/decrypt): encrypt
Enter the input image path: input_image.jpg
Enter the output image path: encrypted_image.jpg
Enter the encryption key: 12345
```

Decrypt an image:

```bash
python image_encryption_tool.py
Choose mode (encrypt/decrypt): decrypt
Enter the input image path: encrypted_image.jpg
Enter the output image path: decrypted_image.jpg
Enter the decryption key: 12345
```

## License

This project is licensed under the [MIT License](LICENSE).
```

You can customize this README file further to include additional information or instructions specific to your project.
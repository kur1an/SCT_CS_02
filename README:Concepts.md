# Image Encryption Tool

## Theory, Concept, and Logic

### Pixel Manipulation

In digital images, each pixel represents a color, typically defined by its red, green, and blue (RGB) components. Pixel manipulation involves altering these values to modify the appearance of the image.

#### Swapping Pixels

- **Concept**: Swapping pixels involves randomly exchanging the positions of pixels in the image.
- **Logic**: This process scrambles the image, making it appear different without altering the pixel values themselves.
- **Implementation**: Randomly swap pixel positions based on a cryptographic key.

### Mathematical Operations on Pixels

Mathematical operations can be applied to the RGB values of pixels to further alter the image.

#### Addition and Subtraction

- **Concept**: Addition and subtraction operations add or subtract a constant value from each RGB component of every pixel.
- **Logic**: This shifts the color values, changing the overall appearance of the image.
- **Implementation**: Add a key to each pixel’s RGB values during encryption and subtract it during decryption.

### Encryption Process

1. **Load Image**: Load the input image.
2. **Pixel Manipulation**: Swap pixel positions and apply mathematical operations based on a cryptographic key.
3. **Save Encrypted Image**: Save the modified image to a new file.

### Decryption Process

1. **Load Encrypted Image**: Load the previously encrypted image.
2. **Reverse Pixel Manipulation**: Undo the pixel swaps and mathematical operations using the same cryptographic key.
3. **Save Decrypted Image**: Save the restored image to a new file.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/SCT_CS_2.git
   cd SCT_CS_2
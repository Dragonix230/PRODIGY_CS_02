from PIL import Image
import random

# Image Encryption function
def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Encrypt the image by modifying pixel values
    random.seed(key)  # Use the key as the seed for reproducibility
    encrypted_pixels = []
    
    for pixel in pixels:
        # Generate a pseudo-random number
        offset = random.randint(0, 255)
        
        # Encrypt pixel by adding the offset
        encrypted_pixel = tuple((value + offset) % 256 for value in pixel)
        encrypted_pixels.append(encrypted_pixel)

    # Create a new image with encrypted pixels
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("encrypted_image.png")
    print("Image successfully encrypted and saved as 'encrypted_image.png'")

# Image Decryption function
def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Decrypt the image by reversing the encryption process
    random.seed(key)  # Use the same key to ensure reproducibility
    decrypted_pixels = []

    for pixel in pixels:
        # Generate a pseudo-random number
        offset = random.randint(0, 255)

        # Decrypt pixel by subtracting the offset
        decrypted_pixel = tuple((value - offset) % 256 for value in pixel)
        decrypted_pixels.append(decrypted_pixel)

    # Create a new image with decrypted pixels
    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save("decrypted_image.png")
    print("Image successfully decrypted and saved as 'decrypted_image.png'")

# Main function to prompt user for input
def main():
    action = input("Would you like to (e)ncrypt or (d)ecrypt an image? ").lower()
    image_path = input("Please enter the path to the image file: ")
    key = int(input("Please enter a numeric key for encryption/decryption: "))

    if action == 'e':
        encrypt_image(image_path, key)
    elif action == 'd':
        decrypt_image(image_path, key)
    else:
        print("Invalid option. Please choose 'e' for encrypt or 'd' for decrypt.")

# Run the program
if __name__ == "__main__":
    main()

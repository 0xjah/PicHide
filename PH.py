import argparse
import stepic

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="🔒 Encrypt an image using a given APK.")
    
    parser.add_argument(
        '--image', 
        type=str, 
        required=True, 
        help='🖼️ Path to the input image file to be encrypted.'
    )
    
    parser.add_argument(
        '--name', 
        type=str, 
        required=True, 
        help='💾 Name for the output encrypted image file.'
    )
    
    parser.add_argument(
        '--apk', 
        type=str, 
        required=True, 
        help='🔑 Encryption key (APK) to use for the encryption.'
    )
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Extracting arguments
    image = args.image
    name = args.name
    apk = args.apk
    
    # Encrypt the image
    try:
        img = stepic.Image(filename=image)
        img.encrypt(apk)
        img.save(name)
        print(f"✅ Image '{image}' has been successfully encrypted and saved as '{name}'.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()


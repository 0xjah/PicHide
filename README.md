# Image Encryption Tool 🔒

This script allows you to encrypt an image using a given encryption key (APK). 

## Features
- Encrypt images with a user-defined key.
- Save the encrypted image with a specified name.

## Requirements
- Python 3.x
- `stepic` library

## Installation

1. Clone the repository or download the script.
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line:

```bash
python PH.py --image path/to/image.png --name output_image.png --apk your_apk
```

### Arguments
- `--image`: 🖼️ Path to the input image file.
- `--name`: 💾 Name for the output encrypted image file.
- `--apk`: 🔑 Encryption key.

## Example

```bash
python PH.py --image input.png --name encrypted_image.png --apk my_secret_key
```


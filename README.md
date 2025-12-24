# AI Image Renamer 🤖📁

An intelligent image renaming tool powered by Google's Gemini AI that automatically identifies and renames your images based on their content. Perfect for organizing photos of characters, celebrities, landmarks, brands, and general images.

![Python](https://img.shields.io/badge/python-3.8+-blue)
![Gemini](https://img.shields.io/badge/Gemini-2.0%20Flash-orange)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

- **🎯 Smart Recognition**: Identifies characters, celebrities, landmarks, and brands
- **🎨 Multi-Format Support**: Works with JPG, JPEG, PNG, and WebP images
- **🔄 Duplicate Handling**: Automatically handles filename collisions with counters
- **🛡️ Safe Renaming**: Cleans special characters for cross-platform compatibility
- **⚡ Batch Processing**: Processes entire folders automatically
- **📊 Real-time Feedback**: Shows progress and results in console

## 🎬 How It Works

The tool uses Google's Gemini AI to analyze each image and generate descriptive names:

```
DSC_1234.jpg  →  Tony Stark Iron Man.jpg
IMG_5678.png  →  Eiffel Tower Paris.png
photo.jpg     →  Golden Retriever Puppy.jpg
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key (free tier available)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/ai-image-renamer.git
cd ai-image-renamer
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Get Your Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### Step 4: Configure the Script

Open the script and replace the API key:

```python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

## 📦 Requirements

Create a `requirements.txt` file with:

```
google-generativeai>=0.3.0
Pillow>=10.0.0
```

## 🎮 Usage

### Basic Usage

Place your images in a folder and run:

```bash
python "Gemini File Renamer.py"
```

By default, it processes images in the current directory (`./`).

### Custom Folder

To process a specific folder, modify the last line:

```python
# Process images in a specific folder
rename_with_intelligence("C:/Users/YourName/Pictures/Vacation")

# Or use relative paths
rename_with_intelligence("../my_images")
```

### Example Output

```
🔍 Identifying: DSC_0001.jpg...
✅ Renamed: Spider Man Homecoming.jpg

🔍 Identifying: IMG_2345.png...
✅ Renamed: Golden Gate Bridge.png

🔍 Identifying: photo_123.jpg...
✅ Renamed: Sunset Beach Ocean.jpg

🔍 Identifying: duplicate.jpg...
✅ Renamed: Pikachu Pokemon (1).jpg
```

## ⚙️ Configuration

### Change AI Model

You can switch between Gemini models:

```python
# Faster, lower cost (default)
model = genai.GenerativeModel('gemini-2.0-flash-lite')

# More accurate, higher cost
model = genai.GenerativeModel('gemini-2.0-flash')

# Most powerful
model = genai.GenerativeModel('gemini-2.0-pro')
```

### Customize Prompt

Modify the prompt to change naming behavior:

```python
prompt = (
    "Describe this image in exactly 3 words. "
    "Focus on the main subject. "
    "Use Title Case with spaces."
)
```

### Adjust Processing Speed

Change the delay between API calls:

```python
# Faster (may hit rate limits)
time.sleep(0.5)

# Safer for large batches
time.sleep(2)
```

### Add More File Formats

Expand supported formats:

```python
if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp', '.tiff']:
```

## 🔧 Advanced Features

### Process Multiple Folders

```python
folders = ["./vacation", "./screenshots", "./downloads"]

for folder in folders:
    print(f"\n📂 Processing: {folder}")
    rename_with_intelligence(folder)
```

### Add Prefix/Suffix

```python
# Add date prefix
from datetime import datetime
prefix = datetime.now().strftime("%Y%m%d")
new_file_name = f"{prefix}_{clean_name}{file_path.suffix}"

# Add category suffix
new_file_name = f"{clean_name}_character{file_path.suffix}"
```

### Filter by Name Pattern

```python
for file_path in path.iterdir():
    # Only process files starting with "IMG_"
    if file_path.name.startswith("IMG_") and file_path.suffix.lower() in ['.jpg', '.png']:
        # ... process
```

## 🛡️ Safety Features

- **Non-destructive**: Only renames, never deletes files
- **Collision Detection**: Adds (1), (2), etc. to prevent overwrites
- **Cross-platform**: Removes illegal filename characters
- **Error Handling**: Continues processing even if one file fails
- **Original Extension**: Preserves file format

## 🔍 Troubleshooting

### "Invalid API Key" Error
- Verify your API key is correct
- Check if API key has proper permissions
- Ensure you're using a valid Gemini API key (not other Google APIs)

### Rate Limit Errors
- Increase `time.sleep()` value
- Reduce batch size
- Check your [API quota](https://aistudio.google.com/app/apikey)

### Poor Recognition Quality
- Try a more powerful model (`gemini-2.0-flash` or `gemini-2.0-pro`)
- Ensure images are clear and well-lit
- Modify prompt to be more specific for your use case

### Permission Errors
- Run script with appropriate permissions
- Check folder write access
- Ensure files aren't open in other programs

## 💰 Cost Considerations

Gemini API pricing (as of 2024):

| Model | Free Tier | Paid Tier |
|-------|-----------|-----------|
| gemini-2.0-flash-lite | 15 RPM | $0.075 / 1M tokens |
| gemini-2.0-flash | 15 RPM | $0.30 / 1M tokens |

**Example**: Renaming 100 images with flash-lite ≈ $0.01-0.02

*Check [Google's pricing page](https://ai.google.dev/pricing) for current rates*


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google Gemini AI](https://ai.google.dev/) - Vision and language model
- [Pillow](https://python-pillow.org/) - Image processing library

## ⚠️ Important Notes

- **API Key Security**: Never commit your API key to version control
- **Backup First**: Always backup important files before batch renaming
- **Rate Limits**: Free tier has request limits (15 requests/minute)
- **Privacy**: Images are sent to Google's servers for processing

**⭐ If this tool helps organize your image library, consider giving it a star!**

import os
import time
import google.generativeai as genai
from pathlib import Path
from PIL import Image
import re

# 1. Setup API
genai.configure(api_key="Api Key")
model = genai.GenerativeModel('gemini-2.0-flash-lite') # Or 'gemini-2.5-flash'

def rename_with_intelligence(folder_path):
    path = Path(folder_path)
    
    for file_path in path.iterdir():
        if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp']:
            print(f"🔍 Identifying: {file_path.name}...")
            
            try:
                with Image.open(file_path) as img:
                    # THE MASTER PROMPT: Optimized for characters, franchises, and landmarks
                    prompt = (
                        "Identify the specific subject of this image. "
                        "1. If it's a character or celebrity, name them. "
                        "2. If it's a franchise (Marvel, Star Wars, etc.), include it. "
                        "3. If it's a landmark or specific brand, name it. "
                        "4. Otherwise, give a 3-word description. "
                        "Output ONLY 2-5 words in Title Case with spaces. No symbols."
                    )
                    
                    response = model.generate_content([prompt, img])
                
                # Clean up the AI output
                suggestion = response.text.strip()
                # Remove any characters that Windows/Mac don't allow in filenames
                clean_name = re.sub(r'[\\/:*?"<>|]', '', suggestion)
                
                new_file_name = f"{clean_name}{file_path.suffix}"
                new_file_path = path / new_file_name

                # Handle name collisions (duplicates)
                counter = 1
                while new_file_path.exists() and file_path != new_file_path:
                    new_file_name = f"{clean_name} ({counter}){file_path.suffix}"
                    new_file_path = path / new_file_name
                    counter += 1

                if file_path != new_file_path:
                    os.rename(file_path, new_file_path)
                    print(f"✅ Renamed: {new_file_path.name}")
                
                # Small delay for API stability
                time.sleep(1)
                
            except Exception as e:
                print(f"❌ Error: {e}")

# Path to your image folder
rename_with_intelligence("./")
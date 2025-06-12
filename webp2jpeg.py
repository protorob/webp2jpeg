from pathlib import Path
from PIL import Image

# 1. Set your source directory here:
src_folder = Path("/path/to/your/folder")

# 2. (Optional) Set your output directory; if you omit this, converted 
#    files will be saved alongside the originals. out_folder = src_folder / "converted_jpeg"
out_folder = src_folder
out_folder.mkdir(exist_ok=True)

# 3. Loop through all .webp files in the source folder
for webp_path in src_folder.glob("*.webp"):
    # Open the .webp image
    with Image.open(webp_path) as im:
        # Ensure it's in RGB mode (JPEG doesn’t support transparency)
        rgb_im = im.convert("RGB")
        # Build the output file path, with .jpg suffix
        jpeg_path = out_folder / (webp_path.stem + ".jpg")
        # Save it as JPEG (you can tweak quality=… from 1–95)
        rgb_im.save(jpeg_path, "JPEG", quality=95)

        print(f"Converted {webp_path.name} → {jpeg_path.name}")

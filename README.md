# 🖼️ Image Resizer Tool

A powerful Python script for batch resizing and converting images. Automate your image processing tasks with ease!

## ✨ Features

- **Batch Processing**: Resize multiple images at once
- **Multiple Resize Options**: Width, height, percentage, or exact dimensions
- **Format Conversion**: Convert between JPEG, PNG, WEBP, GIF, BMP, TIFF
- **Aspect Ratio Control**: Maintain or ignore aspect ratios
- **Smart Error Handling**: Clear messages and automatic folder creation
- **Progress Tracking**: See which images are being processed
- **10 Ready-to-Use Examples**: Common use cases pre-configured

## 🚀 Quick Start

### Prerequisites

```bash
# Install Python (3.7 or higher)
# Download from: https://www.python.org/downloads/

# Install Pillow library
pip install Pillow
```

### Installation

1. **Download the script** (`image.py`)
2. **Place it in your project folder** (e.g., `D:\python intern\`)
3. **Run the script**:
   ```bash
   python image.py
   ```
4. **Follow the prompts** to create the input folder
5. **Add your images** to the `input_images` folder
6. **Run again** to process images!

## 📁 Folder Structure

```
your-project/
│
├── image.py                 # Main script
├── input_images/            # Put your original images here
│   ├── photo1.jpg
│   ├── photo2.png
│   └── ...
│
└── output/                  # Resized images will be saved here
    ├── thumbnails/
    ├── instagram/
    ├── email/
    └── ...
```

## 💡 Usage Examples

### Example 1: Website Thumbnails (300px wide)
```python
example_1_website_thumbnails()
```
Perfect for blog posts, galleries, and previews.

### Example 2: Instagram Posts (1080x1080)
```python
example_2_instagram_posts()
```
Square format for Instagram feed posts.

### Example 3: Email Attachments (50% smaller)
```python
example_3_email_attachments()
```
Reduce file size for faster email sending.

### Example 4: Web Optimization (WebP format)
```python
example_4_web_optimization()
```
Convert to WebP for 30% smaller file sizes.

### Example 5: Product Photos (800x800)
```python
example_5_product_photos()
```
Exact dimensions for e-commerce platforms.

### Example 6: YouTube Thumbnails (1280x720)
```python
example_6_youtube_thumbnails()
```
Standard HD format for YouTube.

### Example 7: Profile Pictures (150x150)
```python
example_7_profile_pictures()
```
Small avatars for social media profiles.

### Example 8: Format Conversion (PNG to JPEG)
```python
example_8_batch_format_conversion()
```
Batch convert image formats without resizing.

### Example 9: HD Wallpapers (1920x1080)
```python
example_9_hd_wallpapers()
```
Full HD desktop backgrounds.

### Example 10: Tiny Icons (10% scale)
```python
example_10_tiny_icons()
```
Create small icons from larger images.

## 🔧 Custom Usage

### Basic Function Call
```python
resize_images(
    input_folder="input_images",
    output_folder="output/custom",
    width=800,
    height=600,
    scale_percent=None,
    output_format='JPEG',
    maintain_aspect=True
)
```

### Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `input_folder` | str | Folder with original images | `"input_images"` |
| `output_folder` | str | Folder for resized images | `"output/custom"` |
| `width` | int | Target width in pixels | `800` |
| `height` | int | Target height in pixels | `600` |
| `scale_percent` | int | Scale by percentage | `50` (half size) |
| `output_format` | str | Convert to format | `'JPEG'`, `'PNG'`, `'WEBP'` |
| `maintain_aspect` | bool | Keep aspect ratio | `True` or `False` |

## 📋 Supported Formats

**Input & Output:**
- JPEG / JPG
- PNG
- GIF
- BMP
- TIFF
- WEBP

## 🎯 Common Use Cases

### Resize for Social Media
```python
# Instagram Feed (1080x1080)
resize_images("input_images", "output/instagram", width=1080, height=1080)

# Facebook Cover (820x312)
resize_images("input_images", "output/facebook", width=820, height=312)

# Twitter Header (1500x500)
resize_images("input_images", "output/twitter", width=1500, height=500)
```

### Optimize for Web
```python
# Reduce file size by 60%
resize_images("input_images", "output/web", scale_percent=40)

# Convert to WebP for better compression
resize_images("input_images", "output/webp", width=1200, output_format='WEBP')
```

### Create Multiple Sizes
```python
# Small thumbnails
resize_images("input_images", "output/small", width=200)

# Medium size
resize_images("input_images", "output/medium", width=600)

# Large size
resize_images("input_images", "output/large", width=1200)
```

## 🛠️ Troubleshooting

### Error: "FileNotFoundError: input_images not found"
**Solution:** Run the script and type `yes` when prompted to create the folder, then add your images.

### Error: "No module named PIL"
**Solution:** Install Pillow:
```bash
pip install Pillow
```

### Images look distorted
**Solution:** Set `maintain_aspect=True` to keep original proportions:
```python
resize_images("input_images", "output", width=800, maintain_aspect=True)
```

### Folder is empty warning
**Solution:** Add image files (JPG, PNG, etc.) to the `input_images` folder.

### JPEG conversion fails
**Solution:** The script automatically converts RGBA to RGB for JPEG compatibility.

## 📊 Performance

- **Speed**: Processes ~10-20 images per second (varies by size)
- **Memory**: Efficient - processes one image at a time
- **Quality**: Uses high-quality LANCZOS resampling

## 🔐 Safety Features

- **Non-destructive**: Original images are never modified
- **Error handling**: Continues processing even if one image fails
- **Automatic folder creation**: Creates output folders as needed
- **Format validation**: Only processes supported image formats

## 📝 Tips & Best Practices

1. **Always keep backups** of original images
2. **Test with a few images first** before batch processing
3. **Use WebP format** for smallest file sizes on web
4. **Maintain aspect ratio** to avoid distortion
5. **Use descriptive output folder names** for organization

## 🤝 Contributing

Feel free to fork, modify, and improve this script for your needs!

## 📄 License

Free to use for personal and commercial projects.

## 🆘 Support

If you encounter issues:
1. Check the error message carefully
2. Verify folder paths exist
3. Ensure images are in supported formats
4. Check that Pillow is installed correctly

## 🎓 Learn More

- [Pillow Documentation](https://pillow.readthedocs.io/)
- [Image Optimization Guide](https://developers.google.com/speed/docs/insights/OptimizeImages)
- [WebP Format Benefits](https://developers.google.com/speed/webp)

---

**Made with ❤️ for automating image tasks**

**Version:** 1.0  
**Last Updated:** October 2025

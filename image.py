import os
from PIL import Image
from pathlib import Path

def resize_images(input_folder, output_folder, width=None, height=None, 
                  scale_percent=None, output_format=None, maintain_aspect=True):
    """
    Resize and convert images in batch.
    
    Args:
        input_folder: Path to folder containing images
        output_folder: Path to save resized images
        width: Target width in pixels (optional)
        height: Target height in pixels (optional)
        scale_percent: Scale by percentage (e.g., 50 for 50%) (optional)
        output_format: Convert to format (e.g., 'JPEG', 'PNG', 'WEBP') (optional)
        maintain_aspect: Keep aspect ratio (default: True)
    """
    
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"❌ ERROR: Input folder '{input_folder}' not found!")
        print(f"\nPlease create the folder and add images:")
        print(f"  1. Create folder: {os.path.abspath(input_folder)}")
        print(f"  2. Add your images to this folder")
        print(f"  3. Run the script again\n")
        return
    
    # Check if folder has any images
    all_files = os.listdir(input_folder)
    if not all_files:
        print(f"⚠️ WARNING: Folder '{input_folder}' is empty!")
        print(f"Please add images to: {os.path.abspath(input_folder)}\n")
        return
    
    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Supported image formats
    supported_formats = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    
    # Track processed images
    processed = 0
    failed = 0
    
    print(f"Starting batch image processing...")
    print(f"Input folder: {input_folder}")
    print(f"Output folder: {output_folder}\n")
    
    # Read all files in input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        # Check if it's a file and has supported extension
        if not os.path.isfile(file_path):
            continue
            
        file_ext = Path(filename).suffix.lower()
        if file_ext not in supported_formats:
            continue
        
        try:
            # Open image
            with Image.open(file_path) as img:
                print(f"Processing: {filename} ({img.size[0]}x{img.size[1]})")
                
                # Convert RGBA to RGB if saving as JPEG
                if output_format and output_format.upper() == 'JPEG' and img.mode == 'RGBA':
                    img = img.convert('RGB')
                
                # Calculate new dimensions
                original_width, original_height = img.size
                
                if scale_percent:
                    # Resize by percentage
                    new_width = int(original_width * scale_percent / 100)
                    new_height = int(original_height * scale_percent / 100)
                    
                elif width and height:
                    # Both dimensions specified
                    if maintain_aspect:
                        # Calculate which dimension to prioritize
                        ratio = min(width / original_width, height / original_height)
                        new_width = int(original_width * ratio)
                        new_height = int(original_height * ratio)
                    else:
                        new_width = width
                        new_height = height
                        
                elif width:
                    # Only width specified
                    ratio = width / original_width
                    new_width = width
                    new_height = int(original_height * ratio)
                    
                elif height:
                    # Only height specified
                    ratio = height / original_height
                    new_width = int(original_width * ratio)
                    new_height = height
                    
                else:
                    # No resize specified, just convert format if needed
                    new_width = original_width
                    new_height = original_height
                
                # Resize image
                resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Prepare output filename
                name_without_ext = Path(filename).stem
                if output_format:
                    output_ext = f".{output_format.lower()}"
                else:
                    output_ext = file_ext
                
                output_filename = f"{name_without_ext}{output_ext}"
                output_path = os.path.join(output_folder, output_filename)
                
                # Save image
                if output_format:
                    resized_img.save(output_path, format=output_format.upper())
                else:
                    resized_img.save(output_path)
                
                print(f"✓ Saved: {output_filename} ({new_width}x{new_height})\n")
                processed += 1
                
        except Exception as e:
            print(f"✗ Failed to process {filename}: {str(e)}\n")
            failed += 1
    
    # Summary
    print("="*50)
    print(f"Processing complete!")
    print(f"Successfully processed: {processed} images")
    print(f"Failed: {failed} images")
    print("="*50)


# =============================================================================
# EXAMPLE USAGE SCENARIOS
# =============================================================================

def example_1_website_thumbnails():
    """Create website thumbnails - 300px wide"""
    print("\n📸 EXAMPLE 1: Creating website thumbnails...")
    resize_images(
        input_folder="input_images",
        output_folder="output/thumbnails",
        width=300
    )

def example_2_instagram_posts():
    """Resize for Instagram posts - 1080x1080 square"""
    print("\n📱 EXAMPLE 2: Instagram square posts...")
    resize_images(
        input_folder="input_images",
        output_folder="output/instagram",
        width=1080,
        height=1080,
        maintain_aspect=True  # Will fit within 1080x1080
    )

def example_3_email_attachments():
    """Reduce file size for email - 50% scale"""
    print("\n📧 EXAMPLE 3: Compressing for email...")
    resize_images(
        input_folder="input_images",
        output_folder="output/email",
        scale_percent=50
    )

def example_4_web_optimization():
    """Convert to WebP for faster web loading"""
    print("\n🚀 EXAMPLE 4: Web optimization (WebP format)...")
    resize_images(
        input_folder="input_images",
        output_folder="output/webp",
        width=1920,
        output_format='WEBP'
    )

def example_5_product_photos():
    """E-commerce product photos - exact 800x800"""
    print("\n🛍️ EXAMPLE 5: E-commerce product photos...")
    resize_images(
        input_folder="input_images",
        output_folder="output/products",
        width=800,
        height=800,
        maintain_aspect=False  # Exact size, may distort
    )

def example_6_youtube_thumbnails():
    """YouTube thumbnail size - 1280x720"""
    print("\n🎥 EXAMPLE 6: YouTube thumbnails...")
    resize_images(
        input_folder="input_images",
        output_folder="output/youtube",
        width=1280,
        height=720,
        output_format='JPEG'
    )

def example_7_profile_pictures():
    """Small profile pictures - 150x150"""
    print("\n👤 EXAMPLE 7: Profile pictures...")
    resize_images(
        input_folder="input_images",
        output_folder="output/profiles",
        width=150,
        height=150
    )

def example_8_batch_format_conversion():
    """Convert all PNG to JPEG (no resize)"""
    print("\n🔄 EXAMPLE 8: Converting PNG to JPEG...")
    resize_images(
        input_folder="input_images",
        output_folder="output/converted",
        output_format='JPEG'
    )

def example_9_hd_wallpapers():
    """Create HD wallpapers - 1920x1080"""
    print("\n🖼️ EXAMPLE 9: HD wallpapers...")
    resize_images(
        input_folder="input_images",
        output_folder="output/wallpapers",
        width=1920,
        height=1080,
        maintain_aspect=True
    )

def example_10_tiny_icons():
    """Create tiny icons - 10% original size"""
    print("\n🔸 EXAMPLE 10: Tiny icons...")
    resize_images(
        input_folder="input_images",
        output_folder="output/icons",
        scale_percent=10
    )


if __name__ == "__main__":
    print("="*60)
    print("IMAGE RESIZER TOOL - SAMPLE EXAMPLES")
    print("="*60)
    
    # SETUP CHECK
    input_folder = "input_images"
    
    if not os.path.exists(input_folder):
        print(f"\n⚠️ SETUP REQUIRED ⚠️\n")
        print(f"The '{input_folder}' folder doesn't exist yet.")
        print(f"\nQuick Setup Steps:")
        print(f"  1. Create a folder named: {input_folder}")
        print(f"  2. Put your images in that folder")
        print(f"  3. Run this script again")
        print(f"\nFull path: {os.path.abspath(input_folder)}\n")
        
        # Ask if user wants to create folder automatically
        create = input("Would you like me to create the folder now? (yes/no): ").strip().lower()
        if create in ['yes', 'y']:
            os.makedirs(input_folder, exist_ok=True)
            print(f"\n✓ Created folder: {input_folder}")
            print(f"Now add your images to this folder and run the script again!\n")
        else:
            print(f"\nPlease create the folder manually and try again.\n")
    else:
        print("\nUncomment the example you want to run:\n")
        
        # Uncomment ONE example to run:
        
        example_1_website_thumbnails()      # 300px wide thumbnails
        # example_2_instagram_posts()       # 1080x1080 Instagram
        # example_3_email_attachments()     # 50% smaller for email
        # example_4_web_optimization()      # WebP format for web
        # example_5_product_photos()        # 800x800 product images
        # example_6_youtube_thumbnails()    # 1280x720 YouTube
        # example_7_profile_pictures()      # 150x150 avatars
        # example_8_batch_format_conversion() # PNG to JPEG
        # example_9_hd_wallpapers()         # 1920x1080 wallpapers
        # example_10_tiny_icons()           # 10% scale icons
        
        # Custom example:
        # resize_images("input_images", "output/custom", width=500, output_format='PNG')
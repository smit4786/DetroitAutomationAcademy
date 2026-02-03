#!/usr/bin/env python3
"""
Simple QR Code Generator using only built-in Python libraries
Generates SVG and PNG formats without external qrcode package
"""

import os
import sys
import urllib.parse
import base64
from pathlib import Path

# GitHub URLs for issue templates
GITHUB_REPO = "https://github.com/smit4786/DetroitAutomationAcademy"
ISSUE_TEMPLATE_URL = f"{GITHUB_REPO}/issues/new?template=enrollment-inquiry.md"

def create_qr_code_svg(data: str, size: int = 200, border: int = 20) -> str:
    """
    Generate QR code as SVG using a simple grid-based approach.
    Uses a free QR code API for simplicity.
    """
    # URL encode the data
    encoded_data = urllib.parse.quote(data)
    
    # Use API to generate QR code
    qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size={size}x{size}&data={encoded_data}"
    
    return qr_api_url


def download_qr_code(url: str, filename: str, format: str = "png") -> bool:
    """Download QR code image from API and save locally."""
    try:
        import urllib.request
        urllib.request.urlretrieve(url, filename)
        return True
    except Exception as e:
        print(f"✗ Error downloading QR code: {e}")
        return False


def generate_svg_qr_code(data: str, size: int = 10, filename: str = "qr_code.svg") -> None:
    """Generate QR code as SVG using simple dot matrix."""
    # For a simple solution, use an online API
    print(f"Using QR API to generate: {filename}")
    
    encoded_data = urllib.parse.quote(data)
    svg_api = f"https://api.qrserver.com/v1/create-qr-code/?format=svg&size=300x300&data={encoded_data}"
    
    try:
        import urllib.request
        urllib.request.urlretrieve(svg_api, filename)
        print(f"✓ Generated SVG: {filename}")
    except Exception as e:
        print(f"✗ Error generating SVG: {e}")


def generate_png_qr_codes(data: str, output_dir: str = "qr_codes") -> None:
    """Generate QR codes in multiple sizes as PNG."""
    import urllib.request
    
    os.makedirs(output_dir, exist_ok=True)
    
    sizes = {
        "poster": 500,      # Large
        "sign": 400,        # Medium  
        "card": 200,        # Small
        "social": 300,      # Web
    }
    
    print(f"\n📍 Generating QR codes in: {output_dir}/\n")
    
    for config_name, size in sizes.items():
        filename = os.path.join(output_dir, f"enrollment_qr_{config_name}_{size}px.png")
        
        # Use QR API
        encoded_data = urllib.parse.quote(data)
        api_url = f"https://api.qrserver.com/v1/create-qr-code/?size={size}x{size}&data={encoded_data}&margin=20"
        
        try:
            urllib.request.urlretrieve(api_url, filename)
            print(f"✓ Generated PNG: {filename}")
        except Exception as e:
            print(f"✗ Error generating {config_name}: {e}")


def main():
    """Main function."""
    print("🔳 Detroit Automation Academy - QR Code Generator")
    print("=" * 60)
    print(f"\n📱 Encoding URL: {ISSUE_TEMPLATE_URL}\n")
    
    # Create output directory
    output_dir = "qr_codes"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate PNG QR codes
    try:
        generate_png_qr_codes(ISSUE_TEMPLATE_URL, output_dir)
    except Exception as e:
        print(f"\n✗ Error generating QR codes: {e}")
        print("\nNote: This tool requires internet connection to use QR code API.")
        print("Alternative: Use online QR code generator at https://www.qr-code-generator.com/")
        return 1
    
    print(f"\n{'='*60}")
    print(f"✓ QR codes generated in: {os.path.abspath(output_dir)}")
    print(f"{'='*60}\n")
    
    print("📋 Generated files:")
    for file in sorted(os.listdir(output_dir)):
        filepath = os.path.join(output_dir, file)
        size = os.path.getsize(filepath) / 1024  # KB
        print(f"   - {file} ({size:.1f} KB)")
    
    print("\n🔗 TEST THE QR CODES:")
    print(f"   1. Open your smartphone camera")
    print(f"   2. Point at printed QR code")
    print(f"   3. Tap the notification to open: {ISSUE_TEMPLATE_URL}")
    print(f"\n✅ QR codes ready for printing and distribution!")
    print("\n📖 See QR_CODE_DEPLOYMENT.md for printing guidelines.")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
QR Code Generator for Detroit Automation Academy Issue Templates

This script generates QR codes for GitHub issue templates and application portals.
Supports multiple formats (PNG, SVG, PDF) for different use cases (posters, signs, business cards).

Usage:
    python3 generate_qr_codes.py
    python3 generate_qr_codes.py --size 10 --format png
    python3 generate_qr_codes.py --all-formats

Output:
    Generates files in ./qr_codes/ directory:
    - enrollment_qr_*.png (raster, scalable)
    - enrollment_qr_*.svg (vector, highest quality)
    - enrollment_qr_*.pdf (print-ready)
"""

import os
import sys
import argparse
import qrcode
from pathlib import Path
from typing import List, Tuple

# GitHub URLs for issue templates
GITHUB_REPO = "https://github.com/smit4786/DetroitAutomationAcademy"
ISSUE_TEMPLATE_URL = f"{GITHUB_REPO}/issues/new?template=enrollment-inquiry.md"

# Application portal URL (when deployed)
APPLICATION_PORTAL_URL = "https://detroitautomationacademy.org/apply"

# QR code configurations for different use cases
QR_CONFIGS = {
    "poster": {
        "size": 15,
        "border": 4,
        "fill_color": "#0066CC",
        "back_color": "#FFFFFF",
        "description": "Large format for posters (36\" x 24\")",
    },
    "sign": {
        "size": 12,
        "border": 3,
        "fill_color": "#0066CC",
        "back_color": "#FFFFFF",
        "description": "Medium format for event signs (24\" x 18\")",
    },
    "card": {
        "size": 8,
        "border": 2,
        "fill_color": "#000000",
        "back_color": "#FFFFFF",
        "description": "Small format for business cards (3.5\" x 2\")",
    },
    "social": {
        "size": 10,
        "border": 2,
        "fill_color": "#0066CC",
        "back_color": "#FFFFFF",
        "description": "Social media format (Instagram, Facebook)",
    },
}


def create_qr_code(
    data: str,
    size: int = 10,
    border: int = 4,
    fill_color: str = "#0066CC",
    back_color: str = "#FFFFFF",
) -> qrcode.QRCode:
    """
    Create a QR code object with specified parameters.
    
    Args:
        data: URL or text to encode
        size: Box size in pixels (higher = more pixels per module)
        border: Border width in boxes
        fill_color: Color of QR code modules (hex format)
        back_color: Background color (hex format)
    
    Returns:
        qrcode.QRCode object
    """
    qr = qrcode.QRCode(
        version=1,  # Auto-determine size
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Highest error correction
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create image with specified colors
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img


def generate_png(
    img,
    filename: str,
    size: int = 10,
) -> None:
    """Save QR code as PNG image."""
    img.save(filename)
    print(f"✓ Generated PNG: {filename}")


def generate_svg(
    data: str,
    filename: str,
) -> None:
    """Generate QR code as SVG vector format (highest quality for print)."""
    import qrcode.image.svg
    
    factory = qrcode.image.svg.SvgPathImage
    qr = qrcode.QRCode(
        image_factory=factory,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="#0066CC", back_color="#FFFFFF")
    img.save(filename)
    print(f"✓ Generated SVG: {filename}")


def generate_pdf(
    img,
    filename: str,
) -> None:
    """Save QR code as PDF (print-ready)."""
    try:
        from PIL import Image
        import io
        
        # Convert PIL Image to PDF
        pdf_path = filename.replace(".png", ".pdf")
        img.save(pdf_path, "PDF")
        print(f"✓ Generated PDF: {pdf_path}")
    except ImportError:
        print(f"⚠ Pillow PDF support not available. Skipping PDF generation.")
    except Exception as e:
        print(f"✗ Error generating PDF: {e}")


def main():
    """Main function to generate QR codes."""
    parser = argparse.ArgumentParser(
        description="Generate QR codes for Detroit Automation Academy issue templates"
    )
    parser.add_argument(
        "--url",
        type=str,
        default=ISSUE_TEMPLATE_URL,
        help=f"URL to encode (default: {ISSUE_TEMPLATE_URL})",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=10,
        help="QR code size in pixels (default: 10)",
    )
    parser.add_argument(
        "--format",
        choices=["png", "svg", "pdf", "all"],
        default="all",
        help="Output format (default: all)",
    )
    parser.add_argument(
        "--config",
        choices=list(QR_CONFIGS.keys()),
        help="Use predefined configuration (poster, sign, card, social)",
    )
    parser.add_argument(
        "--all-configs",
        action="store_true",
        help="Generate QR codes for all predefined configurations",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="qr_codes",
        help="Output directory (default: qr_codes)",
    )
    
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Determine which configurations to generate
    configs_to_generate = {}
    if args.all_configs:
        configs_to_generate = QR_CONFIGS
    elif args.config:
        configs_to_generate = {args.config: QR_CONFIGS[args.config]}
    else:
        # Use default or custom size
        configs_to_generate = {
            "default": {
                "size": args.size,
                "border": 4,
                "fill_color": "#0066CC",
                "back_color": "#FFFFFF",
                "description": "Custom configuration",
            }
        }
    
    print(f"Generating QR codes for: {args.url}\n")
    
    # Generate QR codes for each configuration
    for config_name, config in configs_to_generate.items():
        print(f"\n{'='*60}")
        print(f"Configuration: {config_name.upper()}")
        print(f"Description:  {config['description']}")
        print(f"Size:         {config['size']}px")
        print(f"{'='*60}")
        
        # Create QR code
        img = create_qr_code(
            args.url,
            size=config["size"],
            border=config["border"],
            fill_color=config["fill_color"],
            back_color=config["back_color"],
        )
        
        # Generate requested formats
        if args.format in ["png", "all"]:
            png_file = os.path.join(
                args.output_dir,
                f"enrollment_qr_{config_name}_{config['size']}px.png"
            )
            generate_png(img, png_file, config["size"])
        
        if args.format in ["svg", "all"]:
            svg_file = os.path.join(
                args.output_dir,
                f"enrollment_qr_{config_name}.svg"
            )
            generate_svg(args.url, svg_file)
        
        if args.format in ["pdf", "all"]:
            pdf_file = os.path.join(
                args.output_dir,
                f"enrollment_qr_{config_name}.pdf"
            )
            generate_pdf(img, pdf_file)
    
    print(f"\n{'='*60}")
    print(f"✓ QR codes generated in: {os.path.abspath(args.output_dir)}")
    print(f"{'='*60}\n")
    
    # Print usage instructions
    print("📋 USAGE INSTRUCTIONS:")
    print(f"\n1. **Posters (36\" x 24\")**")
    print(f"   File: enrollment_qr_poster_*.png")
    print(f"   Use: Large event signage, high visibility")
    print(f"\n2. **Signs (24\" x 18\")**")
    print(f"   File: enrollment_qr_sign_*.png")
    print(f"   Use: Table signs, zone markers")
    print(f"\n3. **Business Cards (3.5\" x 2\")**")
    print(f"   File: enrollment_qr_card_*.png")
    print(f"   Use: Handout to guests")
    print(f"\n4. **Social Media**")
    print(f"   File: enrollment_qr_social_*.png")
    print(f"   Use: Instagram, Facebook, email campaigns")
    print(f"\n5. **Vector (SVG - Highest Quality)**")
    print(f"   File: enrollment_qr_*.svg")
    print(f"   Use: Print shops, professional reproduction")
    print(f"\n6. **Print-Ready (PDF)**")
    print(f"   File: enrollment_qr_*.pdf")
    print(f"   Use: Send directly to printer")
    
    # Print QR code URL for testing
    print(f"\n🔗 TEST THE QR CODE:")
    print(f"   URL: {args.url}")
    print(f"   Use a QR code scanner app to verify the link works")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

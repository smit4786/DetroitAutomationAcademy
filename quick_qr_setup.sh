#!/bin/bash
# Quick-start script for generating QR codes for Detroit Automation Academy
# Usage: ./quick_qr_setup.sh

set -e  # Exit on error

echo "🔳 Detroit Automation Academy - QR Code Generation"
echo "=================================================="
echo ""

# Check if required packages are installed
echo "📦 Checking dependencies..."

if ! python3 -c "import qrcode" 2>/dev/null; then
    echo "⚠️  qrcode package not found. Installing..."
    pip3 install qrcode[pil] pillow --quiet
    echo "✓ qrcode package installed"
fi

echo ""
echo "📋 Available generation options:"
echo ""
echo "1. Generate all formats (recommended for first-time setup)"
echo "   ./quick_qr_setup.sh --all"
echo ""
echo "2. Generate specific format"
echo "   ./quick_qr_setup.sh --format png"
echo "   ./quick_qr_setup.sh --format svg"
echo ""
echo "3. Generate for specific use case"
echo "   ./quick_qr_setup.sh --config poster"
echo "   ./quick_qr_setup.sh --config card"
echo ""
echo "4. Generate all configurations"
echo "   ./quick_qr_setup.sh --all-configs"
echo ""
echo "Default (no arguments): Generate all formats and all configs"
echo ""

# Determine command
if [ "$1" == "--all" ]; then
    echo "🔳 Generating all formats for all configurations..."
    python3 generate_qr_codes.py --all-configs --format all
elif [ "$1" == "--format" ]; then
    echo "🔳 Generating $2 format..."
    python3 generate_qr_codes.py --format "$2"
elif [ "$1" == "--config" ]; then
    echo "🔳 Generating $2 configuration..."
    python3 generate_qr_codes.py --config "$2" --format all
elif [ "$1" == "--all-configs" ]; then
    echo "🔳 Generating all configurations in all formats..."
    python3 generate_qr_codes.py --all-configs --format all
else
    echo "🔳 Generating all formats for all configurations (default)..."
    python3 generate_qr_codes.py --all-configs --format all
fi

echo ""
echo "✅ QR code generation complete!"
echo ""
echo "📍 Output location: ./qr_codes/"
echo ""
echo "📋 Next steps:"
echo "   1. Test QR codes by scanning with your smartphone"
echo "   2. Upload PNG/PDF files to print shop"
echo "   3. See QR_CODE_DEPLOYMENT.md for printing guidelines"
echo ""

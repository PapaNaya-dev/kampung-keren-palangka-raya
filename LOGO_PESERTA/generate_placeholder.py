#!/usr/bin/env python3
"""
Script untuk membuat placeholder logo sederhana menggunakan PIL/Pillow
Jika PIL tidak tersedia, akan dibuat file SVG sebagai fallback
"""

import os

# Coba buat dengan PIL
try:
    from PIL import Image, ImageDraw, ImageFont
    
    def create_placeholder_pil(filename, size=(200, 200)):
        img = Image.new('RGBA', size, (240, 240, 240, 255))
        draw = ImageDraw.Draw(img)
        
        # Gambar border
        draw.rectangle([10, 10, size[0]-10, size[1]-10], outline=(150, 150, 150, 255), width=2)
        
        # Tambahkan teks
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        except:
            font = ImageFont.load_default()
        
        text = "LOGO"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (size[0] - text_width) // 2
        y = (size[1] - text_height) // 2
        draw.text((x, y), text, fill=(100, 100, 100, 255), font=font)
        
        img.save(filename)
        print(f"✓ Placeholder PNG dibuat: {filename}")
        return True
except ImportError:
    print("PIL/Pillow tidak tersedia, menggunakan SVG fallback...")

def create_placeholder_svg(filename):
    svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#f0f0f0" stroke="#969696" stroke-width="2"/>
  <text x="100" y="110" font-family="Arial, sans-serif" font-size="24" font-weight="bold" 
        text-anchor="middle" fill="#646464">LOGO</text>
  <text x="100" y="140" font-family="Arial, sans-serif" font-size="12" 
        text-anchor="middle" fill="#969696">Placeholder</text>
</svg>'''
    
    with open(filename.replace('.png', '.svg'), 'w') as f:
        f.write(svg_content)
    print(f"✓ Placeholder SVG dibuat: {filename.replace('.png', '.svg')}")

if __name__ == '__main__':
    placeholder_file = 'placeholder_logo.png'
    try:
        if not create_placeholder_pil(placeholder_file):
            create_placeholder_svg(placeholder_file)
    except Exception as e:
        print(f"Error: {e}")
        create_placeholder_svg(placeholder_file)

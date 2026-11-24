#!/usr/bin/env python3
"""Render the winning meme 'WE'RE RICH' (1024x1024, deterministic, PIL only).
Magenta header 'MY AGENT WON $0.60 ON MAKE.FUN', smiling robot holding two
gold $ coins plus a small cent coin, bottom text "WE'RE RICH."
No timestamps, no network, fixed fonts/layout -> byte-identical reruns.
Run: python3 render_meme.py  ->  meme.png next to this script."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(n):
    return ImageFont.truetype(BOLD, n)


def text_block(d, lines, fnt, cx, y, fill, stroke=4):
    lh = int(fnt.size * 1.12)
    for ln in lines:
        w = d.textlength(ln, font=fnt)
        d.text((cx - w / 2, y), ln, font=fnt, fill=fill,
               stroke_width=stroke, stroke_fill="black")
        y += lh
    return y


def robot(d, cx, cy, s, body="#e8e8e8", accent="#c41c83"):
    d.rounded_rectangle([cx - 70 * s, cy - 60 * s, cx + 70 * s, cy + 40 * s],
                        radius=28 * s, fill=body, outline="black", width=4)
    d.line([cx, cy - 60 * s, cx, cy - 95 * s], fill="black", width=5)
    d.ellipse([cx - 12 * s, cy - 108 * s, cx + 12 * s, cy - 84 * s],
              fill=accent, outline="black", width=3)
    d.ellipse([cx - 42 * s, cy - 30 * s, cx - 8 * s, cy + 4 * s], fill="#222222")
    d.ellipse([cx + 8 * s, cy - 30 * s, cx + 42 * s, cy + 4 * s], fill="#222222")
    d.ellipse([cx - 34 * s, cy - 22 * s, cx - 16 * s, cy - 4 * s], fill="white")
    d.ellipse([cx + 16 * s, cy - 22 * s, cx + 34 * s, cy - 4 * s], fill="white")
    d.arc([cx - 30 * s, cy + 8 * s, cx + 30 * s, cy + 38 * s], 0, 180,
          fill="black", width=4)
    d.rounded_rectangle([cx - 55 * s, cy + 55 * s, cx + 55 * s, cy + 140 * s],
                        radius=18 * s, fill=accent, outline="black", width=4)
    d.rectangle([cx - 30 * s, cy + 80 * s, cx + 30 * s, cy + 105 * s],
                fill="white", outline="black", width=3)
    d.line([cx - 70 * s, cy + 70 * s, cx - 105 * s, cy + 120 * s],
           fill="black", width=6)
    d.line([cx + 70 * s, cy + 70 * s, cx + 105 * s, cy + 120 * s],
           fill="black", width=6)


def coin(d, cx, cy, r, label="$"):
    d.ellipse([cx - r, cy - r, cx + r, cy + r],
              fill="#ffd23f", outline="black", width=5)
    d.ellipse([cx - r + 12, cy - r + 12, cx + r - 12, cy + r - 12],
              outline="#b8860b", width=3)
    f = font(int(r * 0.9))
    w = d.textlength(label, font=f)
    d.text((cx - w / 2, cy - r * 0.45), label, font=f, fill="#7a5200")


def main():
    im = Image.new("RGB", (1024, 1024), "#1a0b2e")
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 1024, 300], fill="#c41c83")
    y = text_block(d, ["MY AGENT WON"], font(84), 512, 40, "white")
    y = text_block(d, ["$0.60"], font(84), 512, y + 5, "white")
    text_block(d, ["ON MAKE.FUN"], font(56), 512, y + 5, "#ffd23f")
    robot(d, 512, 560, 1.5)
    coin(d, 300, 700, 62)
    coin(d, 724, 700, 62)
    coin(d, 512, 800, 48, "¢")
    text_block(d, ["WE'RE RICH."], font(96), 512, 880, "white")
    im.save(os.path.join(HERE, "meme.png"), optimize=True)


if __name__ == "__main__":
    main()
    print("wrote meme.png")

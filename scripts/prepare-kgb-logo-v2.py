from collections import deque
from pathlib import Path
import sys

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
source_path = Path(sys.argv[1])
output_path = ROOT / "public" / "assets" / "kgb-logo-v2.png"

image = Image.open(source_path).convert("RGBA")
width, height = image.size
pixels = image.load()


def is_background(p):
    return min(p[0], p[1], p[2]) >= 245


# Flood-fill the white background from the borders so inner whites (whiskers) stay.
background = bytearray(width * height)
queue = deque()
for x in range(width):
    for y in (0, height - 1):
        queue.append((x, y))
for y in range(height):
    for x in (0, width - 1):
        queue.append((x, y))
while queue:
    x, y = queue.popleft()
    if 0 <= x < width and 0 <= y < height and not background[y * width + x] and is_background(pixels[x, y]):
        background[y * width + x] = 1
        queue.extend(((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))

for y in range(height):
    for x in range(width):
        r, g, b, _ = pixels[x, y]
        pixels[x, y] = (255, 255, 255, 0) if background[y * width + x] else (r, g, b, 255)

bounds = image.getchannel("A").getbbox()
pad = 6
image = image.crop((bounds[0] - pad, bounds[1] - pad, bounds[2] + pad, bounds[3] + pad)) if bounds else image
image.save(output_path, "PNG", optimize=True)
print(f"Saved {output_path} ({image.width}x{image.height})")

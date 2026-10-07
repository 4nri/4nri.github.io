from pathlib import Path
import base64

root = Path(__file__).resolve().parents[1]
src = root / "assets" / "background_masks_rgb_135x240.png.base64"
dst = root / "assets" / "background_masks_rgb_135x240.png"

dst.write_bytes(base64.b64decode(src.read_text(encoding="utf-8").strip()))
print(dst)

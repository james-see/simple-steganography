"""Simple Python steganography tool for hiding messages in PNG images."""

from __future__ import annotations

from pathlib import Path

import stepic
from PIL import Image

__version__ = "1.0.6"


def hide_message(
    image_path: str | Path, message: str, output_path: str | Path = "stegtest.png"
) -> Path:
    """Hide a text message in a PNG image and save the result."""
    output = Path(output_path)
    with Image.open(image_path) as image:
        encoded = stepic.encode(image.convert("RGB"), message.encode("utf-8"))
        encoded.save(output, "PNG")
    return output


def reveal_message(image_path: str | Path) -> str:
    """Reveal a hidden text message from a PNG image."""
    with Image.open(image_path) as image:
        decoded = stepic.decode(image)
    return decoded.decode("utf-8") if isinstance(decoded, (bytes, bytearray)) else str(decoded)


def main() -> None:
    image_path = input("full path of image location: ").strip()
    if not image_path:
        image_path = "pngs/original.png"

    message = input("message to hide: ")
    output_path = hide_message(image_path, message)
    print(f"The message you hid in the image: {reveal_message(output_path)}")


if __name__ == "__main__":
    main()

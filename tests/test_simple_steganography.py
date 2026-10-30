"""Smoke tests for simple-steganography."""

from pathlib import Path

from PIL import Image

import simple_steganography as ss


def test_hide_and_reveal_roundtrip(tmp_path: Path) -> None:
    image_path = tmp_path / "original.png"
    output_path = tmp_path / "hidden.png"
    Image.new("RGB", (64, 64), "white").save(image_path)

    ss.hide_message(image_path, "hello world", output_path)

    assert output_path.exists()
    assert ss.reveal_message(output_path) == "hello world"


def test_version() -> None:
    assert ss.__version__ == "1.0.6"

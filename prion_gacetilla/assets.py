from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple

from PIL import Image as PILImage

from .config import BAND_PHOTO_PATH, COVER_PATH, LOGO_PATH, ASSETS_DIR


@dataclass(frozen=True)
class PreparedAssets:
    cover: Path
    logo: Path
    band_photo: Path
    logo_ratio: float
    band_photo_ratio: float


def _read_existing_image(
    output_path: Path,
) -> Optional[Tuple[Path, Tuple[int, int]]]:
    if not output_path.exists():
        return None

    with PILImage.open(output_path) as image:
        return output_path, image.size


def optimize_image(
    input_path: Path,
    output_name: str,
    max_width: int = 1800,
    max_height: int = 1800,
    quality: int = 85,
) -> Tuple[Path, Tuple[int, int]]:
    output_path = ASSETS_DIR / output_name
    existing_image = _read_existing_image(output_path)
    if existing_image is not None:
        return existing_image

    with PILImage.open(input_path) as image:
        if image.mode != "RGB":
            image = image.convert("RGB")

        image.thumbnail(
            (max_width, max_height),
            PILImage.Resampling.LANCZOS,
        )
        dimensions = image.size
        image.save(
            output_path,
            "JPEG",
            quality=quality,
            optimize=True,
            progressive=True,
        )

    return output_path, dimensions

def optimize_image_png(
    input_path: Path,
    output_name: str,
    max_width: int = 1800,
    max_height: int = 1800,
) -> Tuple[Path, Tuple[int, int]]:
    output_path = ASSETS_DIR / output_name
    existing_image = _read_existing_image(output_path)
    if existing_image is not None:
        return existing_image

    with PILImage.open(input_path) as image:
        # Mantener transparencia
        if image.mode != "RGBA":
            image = image.convert("RGBA")

        image.thumbnail(
            (max_width, max_height),
            PILImage.Resampling.LANCZOS,
        )

        dimensions = image.size

        image.save(
            output_path,
            "PNG",
            optimize=True,
        )

    return output_path, dimensions


def prepare_assets() -> PreparedAssets:
    cover, _ = optimize_image(
        COVER_PATH,
        "aberrant_calamity_optimized.jpg",
        max_width=1800,
        max_height=1800,
        quality=82,
    )
    band_photo, band_size = optimize_image(
        BAND_PHOTO_PATH,
        "prion_banda_optimized.jpg",
        max_width=1800,
        max_height=1800,
        quality=82,
    )

    logo, logo_size = optimize_image_png(
        LOGO_PATH,
        "Prion-logo_optimized.png",
        max_width=1800,
        max_height=1800,
    )

    return PreparedAssets(
        cover=cover,
        logo=logo,
        band_photo=band_photo,
        logo_ratio=logo_size[1] / logo_size[0],
        band_photo_ratio=band_size[1] / band_size[0],
    )

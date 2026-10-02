from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = PROJECT_DIR / "src" / "images"
OUTPUT_PATH = PROJECT_DIR / "PRION_Gacetilla_de_Prensa_2026_FINAL.pdf"

COVER_PATH = ASSETS_DIR / "aberrant_calamity.webp"
LOGO_PATH = ASSETS_DIR / "Prion-logo.webp"
BAND_PHOTO_PATH = ASSETS_DIR / "PRION_photo_2019.webp"

SOCIAL_LINKS = {
    "Facebook": "https://www.facebook.com/Priondeathmetal",
    "Instagram": "https://www.instagram.com/prion_death_metal/",
    "YouTube": "https://www.youtube.com/priondeath",
    "Bandcamp": "https://prion.bandcamp.com/",
    "Spotify": "https://open.spotify.com/intl-es/artist/5FXU7Dmtuv0xN8Ic3FTeW4",
}

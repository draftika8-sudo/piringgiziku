"""
Configuration settings untuk PiringGiziku
"""
import os

# Paths
MODEL_PATH = "model/best.pt"
ASSETS_PATH = "assets"
MAKANAN_SEHAT_IMAGE = os.path.join(ASSETS_PATH, "makanan sehat.png")
ISI_PIRINGKU_IMAGE = os.path.join(ASSETS_PATH, "isi_piringku.png")

# Model Config
CONFIDENCE_THRESHOLD = 0.5

# Page Configuration
PAGE_TITLE = "PiringGiziku"
PAGE_ICON = "🥗"
PAGE_LAYOUT = "wide"
SIDEBAR_STATE = "expanded"

# Color Palette
COLOR_PRIMARY = "#2E7D32"
COLOR_PRIMARY_DARK = "#1B5E20"
COLOR_LIGHT = "#E8F5E9"
COLOR_SUCCESS = "#C8E6C9"
COLOR_WARNING = "#FFF9C4"
COLOR_ERROR = "#FFCDD2"

# Font Awesome CDN
FONT_AWESOME_CDN = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"

# Detection Colors for Bounding Boxes
DETECTION_COLORS = {
    "makanan_pokok": (169, 209, 142),
    "lauk_pauk": (255, 179, 102),
    "sayur": (144, 202, 249),
    "buah": (239, 154, 154)
}

# Font Configuration
LABEL_FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
LABEL_FONT_SIZE = 24

# Food Groups Mapping
FOOD_GROUPS_MAPPING = {
    "makanan_pokok": "Makanan Pokok",
    "lauk_pauk": "Lauk Pauk",
    "sayur": "Sayuran",
    "buah": "Buah"
}

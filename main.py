from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Palette Studio")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

FEATURED_PALETTES = [
    {
        "name": "Arctic Dusk",
        "tags": ["cool", "minimal"],
        "colors": ["#E8F4F8", "#A8D8EA", "#4A90D9", "#2C3E6B", "#1A1F3A"],
    },
    {
        "name": "Terra Bloom",
        "tags": ["warm", "earthy"],
        "colors": ["#FFF8F0", "#F4C88A", "#D97B4F", "#8B3A2A", "#3D1A14"],
    },
    {
        "name": "Forest Mist",
        "tags": ["nature", "muted"],
        "colors": ["#F2F5F0", "#B8CDB5", "#6A9A72", "#3D6B4F", "#1E3328"],
    },
    {
        "name": "Neon Pulse",
        "tags": ["vibrant", "dark"],
        "colors": ["#0D0D0D", "#1A1A2E", "#16213E", "#00D4FF", "#FF006E"],
    },
    {
        "name": "Peach Dream",
        "tags": ["soft", "pastel"],
        "colors": ["#FFF0EB", "#FFD6C8", "#FFB3A0", "#FF8C7A", "#E85D5D"],
    },
    {
        "name": "Midnight Ink",
        "tags": ["dark", "moody"],
        "colors": ["#F5F5F7", "#C8C8D0", "#6B6B85", "#2E2E4A", "#0A0A18"],
    },
]

STATS = [
    {"value": "50K+", "label": "Palettes Generated"},
    {"value": "12K+", "label": "Happy Designers"},
    {"value": "200+", "label": "Curated Collections"},
    {"value": "4.9★", "label": "Average Rating"},
]


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "palettes": FEATURED_PALETTES,
            "stats": STATS,
        },
    )


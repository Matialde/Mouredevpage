import reflex as rx
from enum import Enum

app = rx.App(
    stylesheets=[
        "https://fonts.google.com/share?selection.family=Comfortaa:wght@300..700|Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900"
    ],
)

class Font(Enum):
    DEFAULT = "Poppins"
    TITLE = "Poppins"
    LOGO = "Comfortaa"  

class FontWeight(Enum):
    LIGHT = "300"
    MEDIUM = "500"
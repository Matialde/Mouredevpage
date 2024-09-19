import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Text_color as Text_color
from link_bio.styles.colors import Color as Color

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.text.strong(
            title, 
            aling_items="start",
            font_weigth="bold", 
            color= Color.PRIMARY.value, 
            as_="span"
        ),
        f" {body}", 
        font_size= Size.MEDIUM.value, #se le hace eso al body para que tenga un espacio en blanco.
        color= Text_color.BODY.value
    )
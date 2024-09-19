import reflex as rx
from link_bio.components.title import title
from link_bio.components.link_sponsor import link_sponsor
from link_bio.views import constants as constants
from link_bio.styles.styles import Size

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.flex(  #para que sea responsive (no funcionó).
            link_sponsor(
                "/1.png",
                constants.ELGATO_URL,
                "logotivo de el gato"
            ),
            link_sponsor(
                "/2.png",
                constants.MVP_URL,
                "logotipo de Microsoft MVP"
            ),
            spacing=Size.VERYBIG.value,
            colums= [1, 1, 2, 2, 2] #con esta lista cambiaría de dos a una columna cuando se vuelve mobile, pero no funciona, (brais usó "rx.responsive_grid" a mi ni me aparece).
        ),
        width="100%",   
        align_items="start"
    )       

import reflex as rx
import datetime
from link_bio.views import constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Text_color as Text_color

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
            height=Size.VERYBIG.value
            ),
        rx.link(
            f"© 2014-{datetime.date.today().year} MoureDev by Brais Moure v4.",
            href= const.MOUREDEV_URL,  # sin estas href no llevaría a ningún lado.
            is_external=True,
            font_size= Size.MEDIUM.value
        ),  # con esto se abre en otra pestaña y no en la misma.
        rx.text("BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD."),
        margin_top="0px",
        align_items="center",
        text_align="center",
        color=Text_color.FOOTER.value
    )


# ACA CON EL COMPONENTE RX.IMAGE LE CARGAMOS LA IMAGEN QUE TENEMOS GUARDADA EN ESTE CASO FAVICON.ICO Y HAY QUE PONERLE EL RECURSO SRC=FAVICON.ICO.
# PARA QUE SE ACTUALICE EL AÑO PODEMOS IMPORTAR DATETIME, INTERPOLAMOS TEXTO Y PONEMOS EL AÑO DE LA FECHA DE SISTEMA (datetime.date.today().year).
#En Python, la notación f{} se utiliza para crear f-strings (o formatted string literals), que son una forma concisa y conveniente de formatear cadenas de texto. Las f-strings te permiten incluir expresiones de Python dentro de una cadena y que estas se evalúen de forma directa.
import reflex as rx
from link_bio.styles import styles
from link_bio.styles.styles import Size as Size


def link_button(title: str, body: str,image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=styles.Size.MEDIUM.value,
                    alt=title #De esta forma el texto alternativo va a ser el título del botón, para que sea accesible.
                        ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(
                        body,
                        spacing= Size.SMALL.value,
                        style=styles.button_body_style,
                        margin= Size.ZERO.value,
                        padding_y= Size.SMALL.value,
                        padding_right= Size.SMALL.value
                    ),  # ASI SE AGREGAN MATI JE.
                ),
            width= "100%" #acá agarro el icono y el texto para que ocupen todo el boton y no se corran para el centro.
            )
        ),  # para que el botón ocupe todo el width tengo que ponerlo ahí.
        href=url,
        is_external=True,  # CON ESTO HACEMOS QUE NO ABRA EN LA MISMA VENTANA SINO UNA NUEVA.
        align_items="center",
        text_align="center",
        width="100%"
    )

# CREAMOS ESTA FUNCION LINK_BUTTON PARA QUE ESTA RECIBA UN TEXTO DE TIPO STRING (NOMBRE DEL BOTON) Y UNA URL QUE VA A SER EL LINK EN DONDE SE VA A REDIRIGIR LA PÁGINA.
# ESTE BOTON VA A SER UN COMPONENTE EN SI.
# EL COMPONENTE LINK TIENE UNA PROPIEDAD QUE SE LLAMA HREF Y EL LINK A PARTIR DE LO QUE LE PONGAMOS LLAMA A UNA URL. LE CARGAMOS LA URL EN LINKS.PY y LOS RECIBE ACA EN LINK_BUTTON.PY.

# VAMOS A ESTILAR EL BOTON DE FORMA GENERICA. EN EL ARCHIVO STYLES.PY VAMOS A CREAR ESTILOS PARA TODA LA APLICACION (BASE_STYLE).

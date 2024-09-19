import reflex as rx
from link_bio.styles.styles import Size
from link_bio.components.title import title

def link_sponsor(image:str, url:str, alt:str) -> rx.Component:
    return rx.hstack(
        rx.image(
            src= image,
            heigth= Size.VERYBIG.value,
            width= "auto", #NO SE POR QUE PERO SI NO LE PONGO ESTO NO APARECE LA IMAGEN.
            spacing= Size.VERYBIG.value,
            alt=alt #esto es para que sea accesible.
        ),
        href=url,           #ESTOS DOS SON LOS PARAMETROS DE NAVEGACION
        is_external=True
    )
        
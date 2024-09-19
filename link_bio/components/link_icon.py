import reflex as rx
from link_bio.styles.styles import Size

def link_icon(image:str, url:str, alt:str) -> rx.Component:
    return rx.link( #como nos va a retornar un incono cliqueable tenemos que retornar un link.   
        rx.image(
            src= image,
            width= Size.LARGE.value, #NO SE POR QUE PERO SI NO LE PONGO ESTO NO APARECE LA IMAGEN.
            spacing= Size.VERYBIG.value,
            alt=alt #esto es para que sea accesible.
        ),
        href=url,           #ESTOS DOS SON LOS PARAMETROS DE NAVEGACION
        is_external=True
    )   
    
from enum import (
    Enum
)  # enum es una clase de python para crear clases enumeradas. (enumeración)
import reflex as rx
from .colors import Color as Color
from .colors import Text_color as Text_color
from .fonts import Font, FontWeight

# constants
MAX_WEIDTH = "560px"

#HACEMOS UN ARRAY PARA LAS HOJAS DE ESTILO.
STYLESHEETS = [ 
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap", #ahí seleccionamos el tamaño de la fuente y el tipo de la fuente por eso se pone el nombre de la familia (poppins) y después el parámetro wght que es para elegir el tamaño (300, 500).
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
] #ahora hay que cargar estas fuentes a la applicación al igual que se cargaría un css. al igual que se carga el base_style se carga stylesheets.


# sizes
class Size(Enum):  # creamos una clase que va a diferenciar los tamaños de espacios por defecto.
    ZERO = "0em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERYBIG = "4em"

# ES UNA BUENA PRACTICA DADO QUE SE UNA RESPONSIVE Y PAGINAS ACCESIBLES SE USAN TAMAÑOS RELATIVOS EN LUGAR DE PX, LA FORMA DE REPRESENTAR LOS TAMAÑOS RELATIVOS ES A TRAVES DE "em" EL TAMAÑA 1 DE "em" TOMA EL TAMAÑO DE FUENTE DE LA APLICACIÓN. SI EL TAMAÑO DE FUENTE DEL COMPONENTE SON 16PX ENTONCES 1 EM SERÁN 16PX.

# VAMOS A CREAR ESTILOS QUE SEAN PARA TODA LA APLICACIÓN, TODOS LOS BOTONES DE LA APLICACION SE VAN A COMPORTAR DE UNA MANERA CONCRETA. CREAMOS BASE_STYLE. CREAMOS UN MAPA EN EL QUE LE VOY DICIENDO LO QUE QUIERO HACER.

# Styles

BASE_STYLE = {
    "font_family" : Font.DEFAULT.value,
    "font_weight" : FontWeight.LIGHT,
    "background_color": Color.BACKGROUND.value,
    rx.heading: {
        "Size": "lg",
        "color" : Text_color.HEADER.value,
        "font_family" : Font.DEFAULT.value,
        "font_weight" : FontWeight.MEDIUM
    },
    rx.button: {  # con esto estoy diciendo que todos los botones de mi app tengan esas propiedades.
        "width": "100%",
        "height": "100%",  # con esto definimos que todos los botones de la app van a ocupar su máximo.
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "Color": Text_color.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {  #esto es para que cuando pasemos el mouse sobre el botón cambie de color.
            "background_color": Color.SECUNDARY.value
        } 
    },
    rx.link: {
        "text_decoration": "none",  # para sacar el subrayado cada vez que pasamos por arriba del link.
        "_hover": {},  # la propiedad _hover es la que nos indica un estado alternativo, para cuando pasamos el mouse por encima, si se lo pasamos vacío no va a hacer nada.
    },
}

# PARA QUE EL BASE_STYLE HAGA EFECTO TENEMOS QUE ESTABLECER ESTE ESTILO COMO UN ESTILO GENERAL Y ESTO SE HACE CUANDO LANZAMOS LA APP DESDE LA CREACION HASTA LA COMPILACION POR ESO HAY QUE AGREGAR EN "app = rx.App()" EL ESTILO, Y QUEDARIA ASI "app = rx.App(style= styles.BASE_STYLE)". AHI ESTAMOS DICIENDO QUE DENTRO DE ESA APLICACION HAY UNA PROPIEDAD QUE ES STYLE Y AHI LE CARGAMOS EL BASE_STYLE.

navbar_title_style= dict(
    font_family= Font.LOGO.value,
    font_weight= FontWeight.LIGHT,
    font_size= Size.LARGE.value
)
title_style= dict(
    width= "100%",
    padding_top = Size.DEFAULT.value,
)

button_title_style = dict(
    font_family= Font.TITLE.value,
    font_weight= FontWeight.MEDIUM,
    font_size=Size.DEFAULT.value, 
    color= Text_color.HEADER.value
    )
button_body_style = dict(
    font_weight= FontWeight.LIGHT,
    font_size=Size.MEDIUM.value, 
    color= Text_color.BODY.value
    )

# YA CREAMOS DOS DICCIONARIOS CON EL STYLE DEL TITULO DEL BOTÓN Y DEL CUERPO DE TEXTO DEL BOTON, AHORA HAY QUE AGREGARLOS EN EL ARCHIVO LINK_BUTTON.PY


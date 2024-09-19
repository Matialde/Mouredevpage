import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
import link_bio.styles.styles as styles #Así importamos todos los estilos. para el navbar.

def navbar() -> rx.Component:
    return rx.hstack(  # primero creamos la barra de navegación, esa barra que va siempre arriba. el hstack es el componente que permite poner cosas de forma horizontal.Si no lo retornamos no podemos ver el componente. En cambio vstack acamoda las cosas de forma vertical.
        rx.text(
            rx.box(
                rx.text.strong("moure", color= Color.PRIMARY.value, as_="span"),
                rx.text.strong("dev", color= Color.SECUNDARY.value, as_="span"),
                style=styles.navbar_title_style
            )
            #"mouredev"  # Este es el componente hijo (children)
        ),
        position="sticky",  # al igual que tenemos el elemento text también podemos representar más propiedades dentro del hstack, una propiedad tipica de css es position, Sticky es una posición que queda fija.
        bg=Color.CONTENT.value,  # la propiedad bg sirve para determinar el color de atrás.
        padding_x=Size.BIG.value,  # el padding es una propiedad que sirve para marcar espacios hacia afuera del elemetno. Se puede hacer un padding de acuerdo a los ejes x e y, esto puede hacerse con padding_x y padding_y.
        padding_y=Size.DEFAULT.value,
        z_index="999",  # con este z_index  indico el índice máximo 999 para asegurar que siempre esté en la parte superior. controla el orden enq ue los elementos se superponen.Un elemento con un z-index más alto se mostrará delante de elementos con un z-index más bajo.
        top="0"#con esto la barra queda fija cuando bajemos en la página.
    )

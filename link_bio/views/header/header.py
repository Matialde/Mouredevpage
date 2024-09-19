import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Text_color as Text_color
from link_bio.styles.colors import Color as Color
from link_bio.components.title import title
from datetime import datetime
from link_bio.views import constants

def experience():
    exp = datetime.today().year - 2010
    return exp

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="BM",
                src="avatar.jpg",
                size="7",
                radius="full",
                bg= Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color= Color.BACKGROUND.value,
                color= Text_color.BODY.value
                ),
            rx.vstack(
                rx.heading("Brais Moure"),
                rx.text(
                    "@mouredev",
                    margin_bottom="0px",  # PARA QUE QUEDE BIEN PEGADO A LA PARTE DE ARRIBA.
                    color=Text_color.HEADER.value
                ),
                rx.hstack(
                    link_icon("/icons/github.svg", constants.GITHUB_URL, "github"),
                    link_icon("/icons/x.svg", constants.TWITTER_X_URL, "x"), 
                    link_icon("/icons/insta.svg", constants.INSTAGRAM_URL, "instagram"),
                    link_icon("/icons/tiktok.svg", constants.TIKTOK_URL, "tiktok"),
                    link_icon("/icons/spotify.svg", constants.SPOTIFY_URL, "spotify"),
                    link_icon("/icons/linke.svg", constants.LINKEDIN_URL, "linkedin"),
                    spacing=Size.BIG.value
                )
            ),
                align_items="start",
                margin=Size.ZERO.value,
                padding=Size.ZERO.value
        ),
        rx.flex(
            info_text(f"{experience()} +", "años de experiencia"),
            rx.spacer(), #el spacer crea un espacio ficticio que empuja el contenido hacia un lado.
            info_text("100+", "aplicaciones creadas"),
            rx.spacer(),
            info_text("1M+", "seguidores"),
            width="100%" #para que con los spacer ocupe todo el ancho.
        ),
        rx.text(
            f"Soy ingeniero de software desde hace más de {experience()} años." 
            " Actualmente trabajo como freelance full-stack developer iOS y Android." 
            " Además, creo contenido formativo sofrbre programación en redes. Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!",
            color= Text_color.BODY.value,
            font_size= Size.DEFAULT.value,
            align_text="left"
        ),
        spacing=Size.BIG.value, #esto es para dividir espacio entre los componentes, con el Size tenemos un espacio ya estandar y no corremos el riesgo de dejar más pixeles y que quede desprolijo.
        align_items="left"
    )

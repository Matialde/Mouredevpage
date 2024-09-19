import reflex as rx
from link_bio.components.link_button import link_button  #ACA TRAIGO EL LINK_BUTTON Y LO COMPLETO.
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size
from link_bio.views import constants as constants

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Twitch", 
            "Transmisiones sobre programación de lunes a viernes",
            "icons/twitch.svg", 
            constants.TWITCH_URL
        ),
        link_button(
            "Youtube", 
            "Tutoriales sobre desarrollo de software semanales",
            "icons/youtube.svg", 
            constants.YOUTUBE_URL
            ),
        link_button(
            "Youtube (canal secundario)",
            "Emisiones en directo destacadas",
            "icons/youtube.svg", 
            constants.YOUTUBE_SECONDARY_URL,
        ),
        link_button(
            "Discord", 
            "El chat y los grupos de estudio de la comunidad",
            "icons/discord.svg", 
            constants.DISCORD_URL
        ),
        link_button(
            "Retos de programación", 
            "Ejercicios semanales para practicar lógica de programación",
            "icons/gear-solid.svg", 
            constants.CODE_CHALLENGES_URL
        ),
        title("Recursos y más"),
        link_button(
            "Git y GitHub desde cero", 
            "aquí puede comprar mi libro en formato físico y eBook", 
            "icons/git.svg",
            constants.BOOK_URL
        ),
        link_button(
            "Libros recomendados", 
            "Mi listado de libros sobre programación, ciencia y tecnología", 
            "icons/book-solid.svg", 
            constants.BOOKS_URL),
        link_button(
            "Mi setup",
            "Listado con todos los elementos que uso en mi trabajo",
            "icons/computer.svg",
            constants.SETUP_URL,
        ),
        link_button(
            "Mouredev", 
            "Mi sitio web", 
            "icons/logo.png", 
            constants.MOUREDEV_URL
        ),
        link_button(
            "Invitame un café", 
            "¿Quieres ayudarme a que siga creando contenido?", 
            "icons/mug.svg",
            constants.COFFEE_URL
        ),
        title("Contacto"),
        link_button(
            "MyPublicInbox", 
            "Respuesta rápida y con preferencia", 
            "icons/envelope2.svg", 
            constants.MYPUBLICINBOX_URL                    
        ),
        link_button(
            "Email", 
            constants.EMAIL,
            "icons/envelope.svg", 
            f"mail to: {constants.EMAIL}"
        ),
        align_items="center",
        text_align="center",
        width="100%",
        spacing=Size.MEDIUM.value
    )

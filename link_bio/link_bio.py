import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.components.footer import footer
from link_bio.views.links.links import links
from link_bio.views.sponsors.sponsors import sponsors
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

#class State(
#    rx.State
#):  # ESTE ES EL STATE SIEMPRE LA HACEMOS COMO UNA CLASE Y MANEJA LOS ESTADOS.
#   pass

def index() -> rx.Component:  # ESTE ES EL COMPONENTE GRAFICO
    return rx.box(  # SIEMRPE QUE TENGAMOS UN COMPONENTE HAY QUE RETORNARLO.
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WEIDTH,
                width="100%",
                align_items="start",
                text_align="Start",
                margin_y=Size.BIG.value,  # margen alrededor del componente (hacia afuera). se pueden hacer vertical (margin_y) u horizontal (margin_x). ACA IMPORTAMOS EL STYLES DEFINIDO EN styles
                padding=Size.BIG.value  # margen hacia adentro del componente.
            )
        ),
        rx.center(footer()),
    )
    # Este navbar va a llamar al componente.

# LA IDEA DE REFLEX ES QUE CADA UNO DE LOS COMPONENTES SEA UN MODULO Y QUE ESOS COMPONENTES QUE SE VAN CREANDO (EJEMPLO EL .HSTACK) SEAN COMPONENTES REALES DENTRO DE LA ESTRUCTURA DE NUESTRO PROYECTO POR ESO SE CREA UNA CARPETA LLAMADO COMPONENTES Y AHI PONEMOS POR EJEMPLO EL ARCHIVO NAVBAR (BARRA DE NAVEGACIÓN Y AHÍ PONEMOS TODO LO QUE CREAMOS )

app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets= styles.STYLESHEETS #CON ESTO VA A CARGAR LA FUENTE DE LA HOJA DE ESTILO. (LO QUE SERIA UN CSS)
)  # CON LA VARIABLE APP ES COMO SE GENERA LA APLICACIÖN CON REFLEX Y AHÍ SE AÑADEN LAS PÁGINAS QUE QUERRAMOS.
app.add_page(
    index,
    title="MoureDev | Te enseño programación y desarrollo de software",
    description= "Hola, mi nombre es Brais Moure. Soy ingeniero de software, desarrollador freelance full-stack y divulgador.", #esto es lo que va  aparecer en google. 
    image="avatar.jpg"#imagen que va a aparecer en la previsualización.
)  # seleccionamos index que es la página que queremos cargar y luego la compilamos.
app._compile()  

# BRAIS VA A DIVIDIR SU PAGINA EN TRES PARTES EL HEADER (cabezera), LUEGO UNA SECCION DE LINKS Y ABAJO TENDRIA UNA SECCION DE FOOTER (PIE DE PAGINA).

# LOS COMPONENTES DE REFLEX ESTAN ENVOLVIENDO LOS DIFERENTES COMPONENTES DE REACT, POR LO TANTO REFLEX USA REACT. LOS COMPONENTES ESTAN FORMADOS POR DOS PARTES BASICAS, LOS CHILDRENS Y LOS PROPS. LOS CHILDREN SON LOS COMPONENTES A LOS QUE SE PUEDE PASAR EL VALOR DEL COMPONENTE O SE LE PUEDE PASAR MAS COMPONENTES. DESPUES ESTAN LAS PROPIEDADES QUE SON ATRIBUTOS QUE AFECTAN EL COMPORTAMIENTO. rx.text("Hello World!", color="blue", font_size="1.5em") EN ESTE CASO "Hello World!" ES EL HIJO MIENTRAS QUE color="blue", font_size="1.5em" SON LAS PROPIEDADES.

# LOS COMPONENTES QUE USA REFLEX NO SON CREADOS POR LA GENTE DE REFLEX SINO QUE ESTAN UTILIZANDO POR DEBAJO COMPONENTES DE REACT, MAS EN CONCRETO COMPONENTES DE CHAKRA UI, CHAKRA UI ES UNA LIBRERIA DE COMPONENTES DE REACT.

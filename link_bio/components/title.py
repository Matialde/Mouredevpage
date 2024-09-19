import reflex as rx
from link_bio.styles import styles


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="lg", 
        style= styles.title_style,
        align="left"
        )
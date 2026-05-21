import customtkinter as ctk


class MessageLabel(ctk.CTkLabel):

    def __init__( self, parent, text, text_color, wraplength
    ):

        super().__init__(
            parent,
            text=text,
            text_color=text_color,
            font=("Segoe UI", 12),
            justify="left",
            anchor="w",
            wraplength=wraplength
        )
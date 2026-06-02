import customtkinter as ctk


class MessageWidget(ctk.CTkLabel):

    def __init__(self, parent, text):

        super().__init__(
            parent,
            text=text,
            anchor="w",
            justify="left",
            font=("Segoe UI", 13),
            text_color="white"
        )
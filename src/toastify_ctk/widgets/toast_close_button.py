import customtkinter as ctk


class CloseButton(ctk.CTkButton):

    def __init__(self, parent, command):

        super().__init__(
            parent,
            text="✕",
            width=28,
            height=28,
            corner_radius=5,
            fg_color="transparent",
            hover_color="#333333",
            command=command
        )
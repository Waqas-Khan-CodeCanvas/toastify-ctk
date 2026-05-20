import customtkinter as ctk


class CloseButton(ctk.CTkButton):

    def __init__(
        self,
        parent,
        command,
        text_color="#FFFFFF"
    ):

        super().__init__(
            parent,
            text="✕",
            command=command,
            width=24,
            height=24,
            corner_radius=12,
            fg_color="transparent",
            hover_color="#2B2B2B",
            text_color=text_color,
            font=("Segoe UI", 12, "bold")
        )
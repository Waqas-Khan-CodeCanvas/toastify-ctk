import customtkinter as ctk


class IconWidget(ctk.CTkLabel):

    def __init__(self, parent, icon, color):

        super().__init__(
            parent,
            text=icon,
            text_color=color,
            font=("Segoe UI", 18, "bold")
        )
import customtkinter as ctk

class AccentBar(ctk.CTkLabel):
    def __init__(self, parent, color):
        super().__init__(
            parent,
            text="",
            width=5,
            fg_color=color,
            corner_radius=0
        )
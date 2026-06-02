import customtkinter as ctk

class ToastContent(ctk.CTkFrame):
    def __init__(self, parent, HEIGHT):
        super().__init__(
            parent,
            fg_color="transparent",
            height=HEIGHT - 6
        )
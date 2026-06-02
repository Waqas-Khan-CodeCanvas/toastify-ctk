import customtkinter as ctk


class ProgressBar(ctk.CTkProgressBar):

    def __init__(self, parent, color):

        super().__init__(
            parent,
            height=4,
            corner_radius=0,
            progress_color=color
        )

        self.set(1)
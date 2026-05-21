import customtkinter as ctk


class ProgressBar(ctk.CTkProgressBar):

    def __init__( self, parent, progress_color, fg_color
    ):

        super().__init__(
            parent,
            height=4,
            corner_radius=0,
            progress_color=progress_color,
            fg_color=fg_color
        )

        self.set(1)

    def set_progress(self, value: float):

        value = max(0.0, min(1.0, value))
        self.set(value)
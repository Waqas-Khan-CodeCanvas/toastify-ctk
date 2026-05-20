import customtkinter as ctk


ICONS = {
    "info": "ℹ",
    "success": "✔",
    "warning": "⚠",
    "error": "✖",
}


class ToastIcon(ctk.CTkLabel):

    def __init__(
        self,
        parent,
        toast_type,
        color
    ):

        super().__init__(
            parent,
            text=ICONS.get(toast_type, "●"),
            text_color=color,
            font=("Segoe UI", 20, "bold"),
            width=24,
            anchor="center"
        )
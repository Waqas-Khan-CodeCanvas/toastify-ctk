import tkinter as tk
import customtkinter as ctk

from src.toastify_ctk.widgets.rounded_rect import RoundedRect
from src.toastify_ctk.widgets.toast_icon import ToastIcon
from src.toastify_ctk.widgets.message_label import MessageLabel
from src.toastify_ctk.widgets.close_button import CloseButton
from src.toastify_ctk.widgets.progress_bar import ProgressBar

from themes.default_theme import THEME


class ToastCard(ctk.CTkFrame):

    PADDING = 16

    def __init__(
        self,
        parent,
        config,
        on_close
    ):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.config_data = config
        self.on_close = on_close

        self.width = config.width
        self.height = config.height

        self.toast_color = THEME[
            config.toast_type
        ]

        self._build()

    def _build(self):

        # Background Canvas
        self.canvas = tk.Canvas(
            self,
            width=self.width,
            height=self.height,
            highlightthickness=0,
            bd=0,
            # bg=self.master.cget("fg_color")  TODO:checkout this error
            bg="#000000"
        )

        self.canvas.place(
            relx=0,
            rely=0,
            relwidth=1,
            relheight=1
        )

        RoundedRect(
            self.canvas,
            0,
            0,
            self.width,
            self.height,
            radius=16,
            fill=THEME["surface"],
            outline=THEME["border"],
            width=1
        )

        # Accent Bar

        self.canvas.create_rectangle(
            0,
            0,
            6,
            self.height,
            fill=self.toast_color,
            outline=""
        )

        
        # Content Layer
        self.content = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.content.place(
            relx=0,
            rely=0,
            relwidth=1,
            relheight=1
        )

        
        # Icon
        self.icon = ToastIcon(
            self.content,
            self.config_data.toast_type,
            self.toast_color
        )

        self.icon.place(
            x=22,
            rely=0.5,
            anchor="w"
        )

        
        # Message
        self.message = MessageLabel(
            self.content,
            self.config_data.message,
            THEME["text"],
            self.width - 120
        )

        self.message.place(
            x=60,
            rely=0.5,
            anchor="w"
        )

        
        # Close Button
        if self.config_data.closable:

            self.close_button = CloseButton(
                self.content,
                self.on_close,
                THEME["text"]
            )

            self.close_button.place(
                x=self.width - 36,
                y=18
            )

        
        # Progress Bar
        if self.config_data.show_progress:

            self.progress = ProgressBar(
                self.content,
                self.toast_color,
                THEME["progress_bg"]
            )

            self.progress.place(
                x=0,
                y=self.height - 4,
                relwidth=1
            )

    def set_progress(self, value):

        if hasattr(self, "progress"):
            self.progress.set_progress(value)
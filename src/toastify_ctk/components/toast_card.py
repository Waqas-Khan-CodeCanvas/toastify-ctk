import customtkinter as ctk

from components.widgets.accent_bar import AccentBar
from components.widgets.icon_widget import IconWidget
from components.widgets.message_widget import MessageWidget
from components.widgets.close_button import CloseButton
from components.widgets.progress_bar import ProgressBar

from animations.progress_controller import ProgressController
from components.widgets.toast_content import ToastContent


class ToastCard(ctk.CTkFrame):

    WIDTH = 280
    HEIGHT = 60

    def __init__(
        self,
        parent,
        message="Toast Message",
        icon="✓",
        color="#22C55E",
        duration=5000,
        on_close=None
    ):

        super().__init__(
            parent,
            width=self.WIDTH,
            height=self.HEIGHT,
            corner_radius=5,
            fg_color="#1f1f1f"
        )

        self.on_close = on_close

        # IMPORTANT
        self.pack_propagate(False)
        self.grid_propagate(False)

        # ACCENT BAR 
        self.accent = AccentBar(self , color)
        self.accent.pack(side="left", fill="y")

        # MAIN CONTENT AREA
        content = ToastContent(self , self.HEIGHT)
        content.pack( side="top", fill="x", expand=False, padx=10, pady=(10, 5) )

        content.grid_columnconfigure(1, weight=1)

        # ICON
        self.icon = IconWidget(content, icon, color)
        self.icon.grid( row=0, column=0, padx=(0, 10), pady=0, sticky="w" )

        # MESSAGE
        self.message = MessageWidget(content, message)
        self.message.grid( row=0,column=1,sticky="w",pady=0)

        # CLOSE BUTTON
        self.close_btn = CloseButton(content, self.close)
        self.close_btn.grid( row=0, column=2, padx=(10, 0), pady=0, sticky="e" )

        # PROGRESS BAR
        self.progress = ProgressBar(self, color)

        self.progress.pack( side="bottom", fill="x" )

        # CONTROLLER
        self.controller = ProgressController( self, self.progress, duration, self.close )

    def start(self):
        self.controller.start()

    def close(self):

        self.controller.stop()

        if self.on_close:
            self.on_close()

    def destroy_toast(self):

        self.controller.stop()
        self.destroy()
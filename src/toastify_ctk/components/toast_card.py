import customtkinter as ctk

from src.toastify_ctk.widgets.toast_accent_bar import AccentBar
from src.toastify_ctk.widgets.toast_icon import IconWidget
from src.toastify_ctk.widgets.toast_message_label import MessageWidget
from src.toastify_ctk.widgets.toast_close_button import CloseButton
from src.toastify_ctk.widgets.toast_progress_bar import ProgressBar
from src.toastify_ctk.widgets.toast_content import ToastContent

from animations.progress_controller import ProgressController


class ToastCard(ctk.CTkFrame):
    theme ={
        "colors":{
            "success":"#22C55E",
            "info":"#3B82F6",
            "warning":"#F59E0B",
            "error":"#EF4444"
        },
        "icons":{
            "success":"✓",
            "info":"ℹ",
            "warning":"⚠",
            "error":"✕"
        }
    }
    
    WIDTH = 280
    HEIGHT = 60

    def __init__(
        self,
        parent,
        message="Toast Message",
        toast_type = "success",
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
        self.accent = AccentBar(self , self.theme["colors"][toast_type])
        self.accent.pack(side="left", fill="y")

        # MAIN CONTENT AREA
        content = ToastContent(self , self.HEIGHT)
        content.pack( side="top", fill="x", expand=False, padx=10, pady=(10, 5) )

        content.grid_columnconfigure(1, weight=1)

        # ICON
        self.icon = IconWidget(content, self.theme["icons"][toast_type], self.theme["colors"][toast_type])
        self.icon.grid( row=0, column=0, padx=(0, 10), pady=0, sticky="w" )

        # MESSAGE
        self.message = MessageWidget(content, message)
        self.message.grid( row=0,column=1,sticky="w",pady=0)

        # CLOSE BUTTON
        self.close_btn = CloseButton(content, self.close)
        self.close_btn.grid( row=0, column=2, padx=(10, 0), pady=0, sticky="e" )

        # PROGRESS BAR
        self.progress = ProgressBar(self, self.theme["colors"][toast_type])

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














# import customtkinter as ctk

# from src.toastify_ctk.widgets.toast_accent_bar import AccentBar
# from src.toastify_ctk.widgets.toast_icon import IconWidget
# from src.toastify_ctk.widgets.toast_message_label import MessageWidget
# from src.toastify_ctk.widgets.toast_close_button import CloseButton
# from src.toastify_ctk.widgets.toast_progress_bar import ProgressBar
# from src.toastify_ctk.widgets.toast_content import ToastContent

# from animations.progress_controller import ProgressController


# class ToastCard(ctk.CTkFrame):
#     """
#     Visual toast component.
#     """

#     WIDTH = 280
#     HEIGHT = 60

#     def __init__(
#         self,
#         parent,
#         *,
#         message: str,
#         icon: str,
#         color: str,
#         duration: int,
#         on_close=None,
#     ):
#         super().__init__(
#             parent,
#             width=self.WIDTH,
#             height=self.HEIGHT,
#             corner_radius=6,
#             fg_color="#1f1f1f",
#         )

#         self.on_close = on_close

#         self.pack_propagate(False)
#         self.grid_propagate(False)

#         self.accent = AccentBar(self, color)
#         self.accent.pack(side="left", fill="y")

#         content = ToastContent(self, self.HEIGHT)
#         content.pack(fill="x", padx=10, pady=(8, 5))

#         content.grid_columnconfigure(1, weight=1)

#         IconWidget(content, icon, color).grid(row=0, column=0, padx=(0, 10))
#         MessageWidget(content, message).grid(row=0, column=1, sticky="w")
#         CloseButton(content, self.close).grid(row=0, column=2, padx=(10, 0))

#         self.progress = ProgressBar(self, color)
#         self.progress.pack(side="bottom", fill="x")

#         self.controller = ProgressController(
#             self,
#             self.progress,
#             duration,
#             self.close,
#         )

#     def start(self):
#         self.controller.start()

#     def close(self):
#         self.controller.stop()

#         if self.on_close:
#             self.on_close()



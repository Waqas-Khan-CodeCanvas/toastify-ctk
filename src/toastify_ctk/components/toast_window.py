import customtkinter as ctk

from src.toastify_ctk.components.toast_card import ToastCard
from core.animator import Animator

class ToastWindow(ctk.CTkToplevel):

    def __init__(self, root, model):
        super().__init__(root)

        self.config_data = model

        self.overrideredirect(True)
        self.attributes("-topmost", True)

        self.geometry(
            f"{model.width}x{model.height}+100+-150"
        )

        # IMPORTANT:
        # transparent is NOT allowed for CTkToplevel

        self.configure(
            # fg_color=root.cget("fg_color")
            fg_color="#333333"
        )

        self.card = ToastCard(
            self,
            model,
            self.destroy_toast
        )

        self.card.pack(
            fill="both",
            expand=True
        )

        Animator.slide_down(
            self,
            start_y=-150,
            end_y=50,
            on_complete=self.start_timer
        )

    def start_timer(self):

        self.elapsed = 0
        self.update_progress()

    def update_progress(self):

        self.elapsed += 50

        ratio = 1 - (
            self.elapsed / self.config_data.duration
        )

        self.card.set_progress(ratio)

        if self.elapsed >= self.config_data.duration:
            self.destroy_toast()
        else:
            self.after(50, self.update_progress)

    def destroy_toast(self):

        self.destroy()












# class ToastWindow(ctk.CTkToplevel):

#     def __init__(self, root, config):
#         super().__init__(root)

#         self.config_data = config

#         self.overrideredirect(True)
#         self.attributes("-topmost", True)

#         self.geometry(
#             f"{config.width}x{config.height}+100+-150"
#         )

#         self.configure(
#             fg_color="transparent"
#         )

#         self.card = ToastCard(
#             self,
#             config,
#             self.destroy_toast
#         )

#         self.card.pack(
#             fill="both",
#             expand=True
#         )

#         Animator.slide_down(
#             self,
#             start_y=-150,
#             end_y=50,
#             on_complete=self.start_timer
#         )

#     def start_timer(self):

#         self.elapsed = 0
#         self.update_progress()

#     def update_progress(self):

#         self.elapsed += 50

#         ratio = 1 - (
#             self.elapsed / self.config_data.duration
#         )

#         self.card.set_progress(ratio)

#         if self.elapsed >= self.config_data.duration:
#             self.destroy_toast()
#         else:
#             self.after(50, self.update_progress)

#     def destroy_toast(self):

#         self.destroy()
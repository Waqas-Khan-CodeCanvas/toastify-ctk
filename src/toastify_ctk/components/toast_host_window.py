# import customtkinter as ctk

# from src.toastify_ctk.components.toast_card import ToastCard


# class ToastHostWindow(ctk.CTkToplevel):

#     def __init__(
#         self,
#         master,
#         *,
#         message: str,
#         icon: str,
#         color: str,
#         duration: int,
#         width: int,
#         height: int,
#         x: int,
#         y: int,
#         on_close=None
#     ):

#         super().__init__(master)

#         self.width = width
#         self.height = height

#         self._external_close = on_close

#         self.overrideredirect(True)
#         self.attributes("-topmost", True)

#         self.geometry(
#             f"{width}x{height}+{x}+{y}"
#         )

#         self.configure(
#             fg_color="#000001"
#         )

#         self.card = ToastCard(
#             self,
#             message=message,
#             icon=icon,
#             color=color,
#             duration=duration,
#             on_close=self._handle_close
#         )

#         self.card.pack(
#             fill="both",
#             expand=True
#         )

#         self.after(
#             10,
#             self.card.start
#         )

#     def _handle_close(self):

#         if callable(self._external_close):
#             self._external_close(self)

#         if self.winfo_exists():
#             self.destroy()

#     def destroy_toast(self):

#         try:
#             self.card.destroy_toast()
#         except Exception:
#             pass

#         if self.winfo_exists():
#             self.destroy()



















import customtkinter as ctk

from src.toastify_ctk.components.toast_card import ToastCard


class ToastHostWindow(ctk.CTkToplevel):
    """
    Single toast window container.
    """

    def __init__(
        self,
        master,
        *,
        message: str,
        icon: str,
        color: str,
        duration: int,
        width: int,
        height: int,
        x: int,
        y: int,
        on_close=None,
    ):
        super().__init__(master)

        self._on_close = on_close

        self.overrideredirect(True)
        self.attributes("-topmost", True)

        self.geometry(f"{width}x{height}+{x}+{y}")

        self.configure(fg_color="#000000")

        self.card = ToastCard(
            self,
            message=message,
            icon=icon,
            color=color,
            duration=duration,
            on_close=self._handle_close,
        )

        self.card.pack(fill="both", expand=True)

        self.after(10, self.card.start)

    def _handle_close(self):
        if callable(self._on_close):
            self._on_close(self)

        self.destroy()
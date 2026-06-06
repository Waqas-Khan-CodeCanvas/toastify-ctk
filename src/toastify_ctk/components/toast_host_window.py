
import customtkinter as ctk


class ToastHostWindow(ctk.CTkFrame):
    
    def __init__(self , master):
        super().__init__(master , fg_color="transparent")
        self.place(relx=0 , rely=0 , relwidth=1  , relheight=1)
        
    def toast_container(self,x_offset=10 , y_offset=10):
        self.toast_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.toast_frame.place(relx=0 , rely=0 ,x=x_offset , y=y_offset, anchor="nw") #anchor : must be n, ne, e, se, s, sw, w, nw, or center
        return self.toast_frame





# import customtkinter as ctk

# from src.toastify_ctk.components.toast_card import ToastCard


# class ToastHostWindow(ctk.CTkToplevel):
#     """
#     Single toast window container.
#     """

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
#         on_close=None,
#     ):
#         super().__init__(master)

#         self._on_close = on_close

#         self.overrideredirect(True)
#         self.attributes("-topmost", True)

#         self.geometry(f"{width}x{height}+{x}+{y}")

#         self.configure(fg_color="#000000")

#         self.card = ToastCard(
#             self,
#             message=message,
#             icon=icon,
#             color=color,
#             duration=duration,
#             on_close=self._handle_close,
#         )

#         self.card.pack(fill="both", expand=True)

#         self.after(10, self.card.start)

#     def _handle_close(self):
#         if callable(self._on_close):
#             self._on_close(self)

#         self.destroy()
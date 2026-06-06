
from src.toastify_ctk.components.toast_host_window import ToastHostWindow
from src.toastify_ctk.components.toast_card import ToastCard
class ToastManager():
    
    def __init__(self ,parent_window):
        self.toast_host_window = ToastHostWindow(parent_window)
        self.toast_container = self.toast_host_window.toast_container()
        self.toasts = []
        
    def show_toast(self , message="Toast Message!!!" ,ttype="info"):
        toast = ToastCard(self.toast_container , message , ttype  )
        toast.pack(pady=5 , padx=5)
        self.toasts.append(toast)
        
        toast.after(5000 , lambda:self._remove_toast(toast))
        
    def _remove_toast(self,toast):
        if toast in self.toasts:
            self.toasts.remove(toast)
            toast.destroy()

        














# from __future__ import annotations

# from enum import Enum
# import customtkinter as ctk

# from src.toastify_ctk.components.toast_host_window import ToastHostWindow


# class ToastType(str, Enum):
#     INFO = "info"
#     SUCCESS = "success"
#     WARNING = "warning"
#     ERROR = "error"


# class ToastManager:
#     WIDTH = 280
#     HEIGHT = 60

#     OFFSET_X = 10
#     OFFSET_Y = 10
#     SPACING = 10

#     THEME = {
#         "info": ("ℹ", "#3498DB"),
#         "success": ("✓", "#2ECC71"),
#         "warning": ("⚠", "#F1C40F"),
#         "error": ("✕", "#E74C3C"),
#     }

#     def __init__(self, root: ctk.CTk):
#         self.root = root
#         self.toasts: list[ToastHostWindow] = []

#         # ✅ IMPORTANT: keep toasts aligned with window movement/resize
#         self.root.bind("<Configure>", self._on_root_change)

#     # ---------------- PUBLIC ----------------
#     def show(self, message: str, toast_type: ToastType, duration: int = 5000):
#         if duration <= 0:
#             duration = 5000

#         icon, color = self.THEME.get(
#             toast_type.value,
#             self.THEME["info"],
#         )

#         x, y = self._position(len(self.toasts))

#         toast = ToastHostWindow(
#             master=self.root,
#             message=message,
#             icon=icon,
#             color=color,
#             duration=duration,
#             width=self.WIDTH,
#             height=self.HEIGHT,
#             x=x,
#             y=y,
#             on_close=self.remove,
#         )

#         self.toasts.append(toast)

#     def remove(self, toast: ToastHostWindow):
#         if toast in self.toasts:
#             self.toasts.remove(toast)

#         self._restack()

#     # ---------------- INTERNAL ----------------
#     def _on_root_change(self, event=None):
#         self._restack()

#     def _restack(self):
#         self.toasts = [t for t in self.toasts if t.winfo_exists()]

#         self.root.update_idletasks()

#         for i, toast in enumerate(self.toasts):
#             x, y = self._position(i)
#             toast.geometry(f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}")

#     def _position(self, index: int) -> tuple[int, int]:
#         self.root.update_idletasks()

#         root_x = self.root.winfo_rootx()
#         root_y = self.root.winfo_rooty()
#         root_w = self.root.winfo_width()

#         x = root_x + root_w - self.WIDTH - self.OFFSET_X

#         y = root_y + self.OFFSET_Y + index * (self.HEIGHT + self.SPACING)

#         return x, y
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
#     """
#     Manages creation, positioning, and removal of toast notifications.
#     """

#     DEFAULT_WIDTH = 280
#     DEFAULT_HEIGHT = 60

#     STACK_SPACING = 20

#     OFFSET_X = 10
#     OFFSET_Y = 10

#     THEME = {
#         "colors": {
#             "info": "#3498DB",
#             "success": "#2ECC71",
#             "warning": "#F1C40F",
#             "error": "#E74C3C",
#         },
#         "icons": {
#             "info": "ℹ",
#             "success": "✓",
#             "warning": "⚠",
#             "error": "✕",
#         },
#     }

#     def __init__(self, root: ctk.CTk) -> None:
#         self.root = root
#         self.__toasts: list[ToastHostWindow] = []

#     def show(
#         self,
#         message: str,
#         toast_type: ToastType | str = ToastType.SUCCESS,
#         duration: int = 5000,
#     ) -> None:
#         """
#         Display a new toast notification.
#         """

#         if duration <= 0:
#             raise ValueError("duration must be greater than 0")

#         toast_type = str(toast_type)

#         if toast_type not in self.THEME["colors"]:
#             toast_type = ToastType.INFO.value

#         x, y = self._get_position(len(self.__toasts))

#         toast = ToastHostWindow(
#             self.root,
#             message=message,
#             icon=self.THEME["icons"][toast_type],
#             color=self.THEME["colors"][toast_type],
#             duration=duration,
#             width=self.DEFAULT_WIDTH,
#             height=self.DEFAULT_HEIGHT,
#             x=x,
#             y=y,
#             on_close=self.remove,
#         )

#         self.__toasts.append(toast)

#     def remove(self, toast: ToastHostWindow) -> None:
#         """
#         Remove a toast and reposition remaining toasts.
#         """

#         if toast not in self.__toasts:
#             return

#         self.__toasts.remove(toast)
#         self.restack()

#     def restack(self) -> None:
#         """
#         Recalculate positions of all active toasts.
#         """

#         self.__toasts = [
#             toast
#             for toast in self.__toasts
#             if toast.winfo_exists()
#         ]

#         for index, toast in enumerate(self.__toasts):
#             x, y = self._get_position(index)

#             toast.geometry(
#                 f"{self.DEFAULT_WIDTH}x"
#                 f"{self.DEFAULT_HEIGHT}+"
#                 f"{x}+{y}"
#             )

#     def _get_position(self, index: int) -> tuple[int, int]:
#         """
#         Calculate the position of a toast based on its stack index.
#         """

#         screen_width = self.root.winfo_screenwidth()

#         stack_height = (
#             self.DEFAULT_HEIGHT
#             + self.STACK_SPACING
#         )

#         x = (
#             screen_width
#             - self.DEFAULT_WIDTH
#             - self.OFFSET_X
#         )

#         y = (
#             self.OFFSET_Y
#             + index * stack_height
#         )

#         return x, y

















from __future__ import annotations

from enum import Enum
import customtkinter as ctk

from src.toastify_ctk.components.toast_host_window import ToastHostWindow


class ToastType(str, Enum):
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"


class ToastManager:
    WIDTH = 280
    HEIGHT = 60

    OFFSET_X = 10
    OFFSET_Y = 10
    SPACING = 10

    THEME = {
        "info": ("ℹ", "#3498DB"),
        "success": ("✓", "#2ECC71"),
        "warning": ("⚠", "#F1C40F"),
        "error": ("✕", "#E74C3C"),
    }

    def __init__(self, root: ctk.CTk):
        self.root = root
        self.toasts: list[ToastHostWindow] = []

        # ✅ IMPORTANT: keep toasts aligned with window movement/resize
        self.root.bind("<Configure>", self._on_root_change)

    # ---------------- PUBLIC ----------------
    def show(self, message: str, toast_type: ToastType, duration: int = 5000):
        if duration <= 0:
            duration = 5000

        icon, color = self.THEME.get(
            toast_type.value,
            self.THEME["info"],
        )

        x, y = self._position(len(self.toasts))

        toast = ToastHostWindow(
            master=self.root,
            message=message,
            icon=icon,
            color=color,
            duration=duration,
            width=self.WIDTH,
            height=self.HEIGHT,
            x=x,
            y=y,
            on_close=self.remove,
        )

        self.toasts.append(toast)

    def remove(self, toast: ToastHostWindow):
        if toast in self.toasts:
            self.toasts.remove(toast)

        self._restack()

    # ---------------- INTERNAL ----------------
    def _on_root_change(self, event=None):
        self._restack()

    def _restack(self):
        self.toasts = [t for t in self.toasts if t.winfo_exists()]

        self.root.update_idletasks()

        for i, toast in enumerate(self.toasts):
            x, y = self._position(i)
            toast.geometry(f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}")

    def _position(self, index: int) -> tuple[int, int]:
        self.root.update_idletasks()

        root_x = self.root.winfo_rootx()
        root_y = self.root.winfo_rooty()
        root_w = self.root.winfo_width()

        x = root_x + root_w - self.WIDTH - self.OFFSET_X

        y = root_y + self.OFFSET_Y + index * (self.HEIGHT + self.SPACING)

        return x, y
import customtkinter as ctk

from src.toastify_ctk.models.toast_model import ToastModel
from src.toastify_ctk.components.toast_window import ToastWindow


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


root = ctk.CTk()
root.geometry("600x400")


def show_success():

    model = ToastModel(
        message="Saved successfully!",
        toast_type="success",
    )

    ToastWindow(root, model)


def show_error():

    model = ToastModel(
        message="Connection failed!",
        toast_type="error",
    )

    ToastWindow(root, model)


ctk.CTkButton(
    root,
    text="Success Toast",
    command=show_success,
).pack(pady=20)

ctk.CTkButton(
    root,
    text="Error Toast",
    command=show_error,
).pack(pady=20)

root.mainloop()
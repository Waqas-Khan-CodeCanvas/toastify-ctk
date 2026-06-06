import customtkinter as ctk
from src.toastify_ctk import Toast

class App:
    def __init__(self) -> None:
        self.root = ctk.CTk()
        self.root.geometry("1000x500")
        self.root.title("Toast Notification Demo.")
        self.root._set_appearance_mode("light")
        
        self.toast = Toast(self.root)
        
        btn_bar = ctk.CTkFrame(self.root , corner_radius=8)
        btn_bar.pack(pady=10)
                
        btns = ["success" , "info" , "warning" , "error"]
        for i ,  text in enumerate(btns):
            ctk.CTkButton(btn_bar , text=text , command=lambda t=text : self.toast.show_toast(t , t)).grid(row=0 , column=i , padx=10 , pady=10)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    App().run()


















# import customtkinter as ctk
# from src.toastify_ctk.core.toast_manager import ToastManager, ToastType

# ctk.set_appearance_mode("dark")

# class App:
#     def __init__(self):
#         self.root = ctk.CTk()
#         self.root.geometry("1000x600")
#         self.root.title("Toastify-CTK Demo")

#         self.manager = ToastManager(self.root)

#         btn_box = ctk.CTkFrame(self.root)
#         btn_box.pack(pady=20)

#         buttons = [
#             ("Success Toast", ToastType.SUCCESS),
#             ("Error Toast", ToastType.ERROR),
#             ("Warning Toast", ToastType.WARNING),
#             ("Info Toast", ToastType.INFO),
#         ]

#         for i, (text, ttype) in enumerate(buttons):
#             ctk.CTkButton(
#                 btn_box,
#                 text=text,
#                 command=lambda m=text, t=ttype: self.toast(m, t),
#             ).grid(row=0, column=i, padx=10)

#     def toast(self, message: str, toast_type: ToastType):
#         self.manager.show(message, toast_type)

#     def run(self):
#         self.root.mainloop()


# if __name__ == "__main__":
#     App().run()
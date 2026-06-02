import customtkinter as ctk
from components.toast_card import ToastCard

ctk.set_appearance_mode("light")


class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("1000x600")
        self.root.title("Toastify Hybrid")

        self.toasts = []
        self.toast_count = 0

        self.show_toast_btn = ctk.CTkButton(
            self.root,
            text="Show Toast",
            command=self.show_toast
        )
        self.show_toast_btn.pack(pady=20)
        self.fm  = ctk.CTkFrame(self.root , height=200 , width=580  , fg_color="blue")
        self.fm.pack()

    def show_toast(self):
        self.toast_count += 1
        self.show(self.toast_count)

    def show(self, index):
        toast = None

        def handle_close() -> None:
            self.remove(toast)

        toast = ToastCard(
            self.root,
            message=f"Operation completed No:{index}",
            icon="✓",
            color="#22C55E",
            duration=5000,
            on_close=handle_close
        )


        toast.place(x=20, y=10 + (len(self.toasts) * 65))
        toast.start()
        self.toasts.append(toast)

    def remove(self, toast):
        if toast not in self.toasts:
            return

        self.toasts.remove(toast)
        toast.destroy_toast()

        self.restack()

    def restack(self):
        for i, toast in enumerate(self.toasts):
            toast.place(x=20, y=10 + (i * 65))

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    App().run()
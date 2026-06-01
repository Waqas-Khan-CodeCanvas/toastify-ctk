class Animator:
    @staticmethod
    def slide_down(
        widget,
        start_y,
        end_y,
        step=5,
        delay=10,
        on_complete=None
    ):
        current_y = start_y

        def animate():
            nonlocal current_y

            if current_y < end_y:
                current_y += step

                widget.geometry(
                    f"+{widget.winfo_x()}+{current_y}"
                )

                widget.after(delay, animate)
            else:
                if on_complete:
                    on_complete()

        animate()
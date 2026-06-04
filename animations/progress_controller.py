


class ProgressController:

    def __init__( self, root, progress_bar, duration, on_complete ):

        self.root = root
        self.bar = progress_bar
        self.duration = duration
        self.on_complete = on_complete

        self.elapsed = 0
        self.running = False
        self.job = None

    def start(self):
        self.running = True
        self._tick()

    def stop(self):
        self.running = False
        if self.job:
            try:
                self.root.after_cancel(self.job)
            except Exception:
                pass

    def _tick(self):
        if not self.running:
            return

        self.elapsed += 50
        ratio = max(0,1 - (self.elapsed / self.duration))

        self.bar.set(ratio)

        if self.elapsed >= self.duration:
            self.running = False
            if self.on_complete:
                self.on_complete()

            return

        self.job = self.root.after( 50, self._tick)
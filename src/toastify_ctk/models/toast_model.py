from dataclasses import dataclass

#  toast model for the toast configurations and key defined values

@dataclass
class ToastModel:
    message: str
    toast_type: str = "info"
    duration: int = 3000
    width: int = 320
    height: int = 90
    show_progress: bool = True
    closable: bool = True
    
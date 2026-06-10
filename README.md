# 🍞 Toastify-CTK

<div align="center">

### Modern Toast Notifications for CustomTkinter 🚀

A lightweight, animated, and easy-to-use toast notification system built for **CustomTkinter** desktop applications in Python. Enhance your UI with clean, non-intrusive feedback messages.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Compatible-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

</div>

---

## 📖 Overview

**Toastify-CTK** is a modern toast notification library designed specifically for **CustomTkinter-based desktop applications**.

It allows developers to display **beautiful, animated, and non-blocking notifications** such as success, error, warning, and info messages with minimal setup.

Perfect for improving **user experience (UX)** in Python GUI applications.

---

## ✨ Features

- 🍞 Lightweight toast notifications
- 🎨 Modern UI compatible with CustomTkinter
- ⚡ Fast and non-blocking popups
- 🧩 Easy integration into existing projects
- 🎯 Multiple notification types (success, error, warning, info)
- 🎬 Smooth animations and transitions
- 📱 Responsive positioning (top-right, bottom, etc.)
- 🔧 Fully customizable design

---

## 🖼️ Preview

> Add your screenshots or GIFs here

```
[Success Toast] ✔ Operation completed successfully
[Error Toast] ❌ Something went wrong
[Info Toast] ℹ New update available
```

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/Waqas-Khan-CodeCanvas/toastify-ctk.git
cd toastify-ctk
```

Install dependencies (if any):

```bash
pip install customtkinter
```

---

## 🚀 Quick Start

```python
from toastify_ctk import Toast

# Create a success toast
Toast.success("Operation completed successfully!")

# Create an error toast
Toast.error("Something went wrong!")

# Create an info toast
Toast.info("New update available")

# Create a warning toast
Toast.warning("Please check your input")
```

---

## 🎨 Toast Types

| Type    | Description                | Example Message              |
|---------|----------------------------|------------------------------|
| Success | Operation completed        | "Saved successfully"        |
| Error   | Something failed           | "Failed to load data"       |
| Info    | General information        | "New update available"      |
| Warning | Caution message            | "Check your input fields"   |

---

## ⚙️ Customization

You can customize toast appearance:

```python
Toast.success(
    message="Saved successfully!",
    duration=3000,
    position="top-right",
    font_size=14
)
```

---

## 📁 Project Structure

```bash
toastify-ctk/
│
├── toastify_ctk/        # Core library
│   ├── __init__.py
│   ├── toast.py
│
├── examples/            # Demo usage
├── assets/              # Icons & UI assets
├── README.md
└── LICENSE
```

---

## 🔍 SEO Keywords

CustomTkinter toast notification, Python GUI notifications, desktop popup messages, tkinter toast system, modern Python UI library, notification system Python, GUI feedback messages

---

## 📈 Use Cases

- Desktop applications built with CustomTkinter
- Login/signup feedback messages
- Form validation alerts
- File upload/download status
- System notifications inside Python apps
- Productivity tools and dashboards

---

## 🤝 Contributing

Contributions are welcome!

```bash
# Fork the repository
# Create your feature branch
git checkout -b feature/NewFeature

# Commit changes
git commit -m "Add new feature"

# Push to branch
git push origin feature/NewFeature
```

Then open a Pull Request.

---

## 📝 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

### Waqas Khan

Full Stack & Python Developer  
GitHub: https://github.com/Waqas-Khan-CodeCanvas

---

<div align="center">

### ⭐ If you like this project, consider giving it a star!

Made with ❤️ for Python developers

</div>

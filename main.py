import tkinter as tk

from system.status import StatusBar
from system.apps import AppsGrid
from system.security import LockScreen
from system.themes import ThemeManager
from system.installer import AppInstaller
from system.taskmanager import TaskManager
from system.recents import RecentsScreen
from system.users import UserManager
from system.cloud import CloudSync


class VortexCore:

    def __init__(self):
        self.theme = ThemeManager()
        self.installer = AppInstaller()
        self.task_manager = TaskManager()
        self.user_manager = UserManager()
        self.cloud = CloudSync()


class VortexLauncher:

    def __init__(self, root):
        self.root = root
        self.root.title("Vortex Launcher 4.0")
        self.root.geometry("360x640")
        self.root.resizable(False, False)

        self.core = VortexCore()

        self.root.configure(bg=self.core.theme.bg)

        # Fade inicial
        self.root.attributes("-alpha", 0)

        # Login
        self.lock = LockScreen(self.root, self.core.theme)

        # Status
        self.status = StatusBar(self.root, self.core.theme)

        # Apps
        self.apps = AppsGrid(
            self.root,
            self.core.theme,
            self.core.task_manager
        )

        # Botão recentes
        self.create_recents_button()

        # Dock
        self.create_dock()

        # Nuvem
        self.core.cloud.connect()

        # Fade animation
        self.fade_in()

    def create_recents_button(self):
        btn = tk.Button(
            self.root,
            text="📂 Recentes",
            bg=self.core.theme.secondary,
            fg="white",
            command=self.open_recents
        )
        btn.pack(side="bottom", pady=5)

    def open_recents(self):
        RecentsScreen(
            self.root,
            self.core.task_manager,
            self.core.theme
        )

    def create_dock(self):
        self.dock = tk.Frame(
            self.root,
            bg=self.core.theme.secondary,
            height=60
        )
        self.dock.pack(side="bottom", fill="x")

        apps = ["📞", "💬", "🌐", "⚙"]

        for app in apps:
            btn = tk.Button(
                self.dock,
                text=app,
                bg=self.core.theme.secondary,
                fg="white",
                bd=0,
                font=("Arial", 16)
            )
            btn.pack(side="left", expand=True)

    def fade_in(self):
        for i in range(0, 11):
            self.root.attributes("-alpha", i / 10)
            self.root.update()
            self.root.after(30)


if __name__ == "__main__":
    root = tk.Tk()
    app = VortexLauncher(root)
    root.mainloop()

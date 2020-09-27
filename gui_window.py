import tkinter as tk


class GuiWindow(tk.Frame):
    root = tk.Tk()
    var = tk.IntVar(
        master=root,
        value=340
    )

    def creat_gui_window(self):
        self.root.title("Device Manager")
        self.scale_widget()
        self.quit_button()
        self.root.mainloop()
        brightness = GuiWindow.var.get()
        return brightness

    def scale_widget(self):
        scale = tk.Scale(
            master=self.root,
            orient="horizontal",
            variable=GuiWindow.var,
            command=self.update_brightness
        )
        scale.pack()

    @staticmethod
    def update_brightness(*args):
        print(GuiWindow.var.get())

    def quit_button(self):
        button = tk.Button(
            master=self.root,
            text="Exit",
            command=self.quit
        )
        button.pack()

    def quit(self):
        self.root.destroy()

import tkinter as tk


class GuiWindow(tk.Frame):
    root = tk.Tk()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.root.title("Hello World")
        self.scale_widget()
        self.root.mainloop()

    def scale_widget(self):
        var = tk.IntVar(
            master=self.root,
            value=340
        )
        scale = tk.Scale(
            master=self.root,
            orient="horizontal",
            variable=var
        )
        scale.pack()

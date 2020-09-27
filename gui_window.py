import tkinter as tk


class GuiWindow:
    """
    creating GUI window & its widgets
    """
    root = tk.Tk()
    var = tk.IntVar(
        master=root
    )

    def creat_gui_window(self, current_value):
        """
        creating window and calling widgets

        :param current_value: scale-bar initial value
        :return: last bar state
        """
        GuiWindow.var.set(current_value)
        self.root.title("Device Manager")
        self.scale_widget()
        self.quit_button()
        self.root.mainloop()
        brightness = GuiWindow.var.get()
        return brightness

    def scale_widget(self):
        """
        setting scale bar

        :return: None
        """
        scale = tk.Scale(
            master=self.root,
            orient="horizontal",
            variable=GuiWindow.var,
            from_=50,
            to=500,
            length=500
        )
        scale.pack()

    def quit_button(self):
        """
        setting Exit button

        :return: None
        """
        button = tk.Button(
            master=self.root,
            text="Exit",
            command=self.quit
        )
        button.pack()

    def quit(self):
        """
        exit brightness setting

        :return: None
        """
        self.root.destroy()

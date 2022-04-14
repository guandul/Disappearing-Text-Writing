import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Little desktop app to practice constant writing


class TextWritingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        text_width = 100
        text_height = 10
        # Pause timer
        self.timer_max = 5
        self.timer = self.timer_max
        self.first_key = False

        # configure the root window
        self.title('Disappearing Text Writing App')
        self.resizable(0, 0)
        self.geometry('1280x600')
        self['bg'] = 'black'

        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure(
            'TLabel',
            background='black',
            foreground='red')

        # label
        self.clock = ttk.Label(
            self,
            text=self.timer,
            font=('Digital-7', 40))

        self.text_write = tk.Text(self, width=text_width, height=text_height, font=("Helvetica", 16))
        self.text_write.bind('<Key>', self.star_timer)
        self.text_write.pack(pady=5)
        self.clock.pack(expand=True)

    def star_timer(self, event):
        self.timer = self.timer_max
        if not self.first_key:
            self.update_window()
            self.first_key = True

    def update_window(self):
        """ update the label every 1 second """
        self.timer -= 1
        self.clock.configure(text=self.timer)

        # schedule another timer
        if self.timer <= 0:
            self.end_app()
        else:
            self.clock.after(1000, self.update_window)

    def end_app(self):
        showinfo(
            title='Time out',
            message=f"You must keep writing"
        )


if __name__ == "__main__":
    app = TextWritingApp()
    app.mainloop()

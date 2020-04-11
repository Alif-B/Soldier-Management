import tkinter as tk
from ttkthemes import themed_tk as thtk
import tkinter.font
from tkinter import ttk
from tkinter import *
from AddSoldier import add_JTF2_popup, add_CSOR_popup
from delete_soldier import delete_soldier_popup
from show_soldiers import view_soldiers


class HomePage(tk.Frame):
    """ GUI for the home page """
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        main_frame = tk.Frame(master=self)
        main_frame.grid(row=0, column=1)

        ttk.Button(main_frame, text='Add JTF2', command=self.add_JTF2_popup, width=20).grid(row=0, column=1)
        ttk.Button(main_frame, text='Add CSOR', command=self.add_CSOR_popup, width=20).grid(row=1, column=1)
        ttk.Button(main_frame, text="Delete Soldier", command=self.delete_soldier_popup, width=20).grid(row=2, column=1)
        ttk.Button(main_frame, text='View Soldiers', command=self.view_soldiers_popup, width=20).grid(row=3, column=1)

    def add_JTF2_popup(self):
        self._popup_win = tk.Toplevel()
        self._popup = add_JTF2_popup(self._popup_win, self.close_window, 'ADD')

    def add_CSOR_popup(self):
        self._popup_win = tk.Toplevel()
        self._popup = add_CSOR_popup(self._popup_win, self.close_window, 'ADD')

    def delete_soldier_popup(self):
        self._popup_win = tk.Toplevel()
        self._popup = delete_soldier_popup(self._popup_win, self.close_window)

    def view_soldiers_popup(self):
        self._popup_win = tk.Toplevel()
        self._popup = view_soldiers(self._popup_win, self.close_window)

    def close_window(self):
        self._popup_win.destroy()


if __name__ == '__main__':
    root = thtk.ThemedTk()

    photo = PhotoImage(file="army.png")
    label = Label(root, image=photo, width=140, height=112).grid(row=1,column=2)

    root.get_themes()
    root.set_theme('equilux')
    root.title('Canadian Armed Forces')
    root.geometry("285x112")
    HomePage(root).grid(row=1,column=1)
    root.mainloop()


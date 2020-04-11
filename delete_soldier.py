import tkinter as tk
from tkinter import ttk
import requests


class delete_soldier_popup(tk.Frame):
    """ Delete soldier popup window """
    def __init__(self, parent, close_window):
        """ Constructor for deleting pop up window """
        tk.Frame.__init__(self, parent, bg="darkseagreen")
        self.grid(row=1, column=1)
        self.close_window = close_window

        tk.Label(self, text="Service Number:", fg="darkolivegreen", bg="darkseagreen").grid(row=1,column=1)
        self._SIN = ttk.Entry(self, width=22)
        self._SIN.grid(row=1,column=2)

        ttk.Button(self, text='Delete', command=self.delete_soldier, width=20).grid(row=3,column=1)
        ttk.Button(self, text='Cancel', command=self.cancel, width=20).grid(row=3,column=2)

    def delete_soldier(self):
        """ Sending request to delete a soldier """
        requests.delete(f"http://127.0.0.1:5000/CAF/soldier/{self._SIN.get()}")
        self.close_window()

    def cancel(self):
        """ Closes the pop up window """
        self.close_window()

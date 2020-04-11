import tkinter as tk
from tkinter import ttk
import requests
from tkinter import messagebox


class add_JTF2_popup(tk.Frame):
    """ Add soldier popup window """
    def __init__(self, parent, close_window, action):
        """ Constructor for the JTF2 pop up window """
        tk.Frame.__init__(self, parent, bg="darkseagreen")
        self.grid(row=1, column=1)
        self.close_window = close_window
        self.action = action

        tk.Label(self, text="SIN:", fg="darkolivegreen", bg="darkseagreen").grid(row=1, column=1)
        self._SIN = ttk.Entry(self)
        self._SIN.grid(row=1, column=2)

        tk.Label(self, text="Rank:", fg="darkolivegreen", bg="darkseagreen").grid(row=2, column=1)
        self._rank = ttk.Entry(self)
        self._rank.grid(row=2, column=2)

        tk.Label(self, text="Last Name:", fg="darkolivegreen", bg="darkseagreen").grid(row=3, column=1)
        self._lname = ttk.Entry(self)
        self._lname.grid(row=3, column=2)

        tk.Label(self, text="First Name:", fg="darkolivegreen", bg="darkseagreen").grid(row=4, column=1)
        self._fname = ttk.Entry(self)
        self._fname.grid(row=4, column=2)

        tk.Label(self, text="Role:", fg="darkolivegreen", bg="darkseagreen").grid(row=5, column=1)
        self._role = ttk.Entry(self)
        self._role.grid(row=5, column=2)

        ttk.Button(self, text='Submit', command=self.add_soldier, width=22).grid(row=7, column=1)
        ttk.Button(self, text='Cancel', command=self.cancel, width=18).grid(row=7,  column=2)

    def add_soldier(self):
        data={}
        data['Service_Number'] = self._SIN.get()
        data['Rank'] = self._rank.get()
        data['Last_Name'] = self._lname.get()
        data['First_Name'] = self._fname.get()
        data['Role'] = self._role.get()
        data['Trainings'] = 'Arctic, Navigation, Weapons, MMA, Navy Seal'

        if self.action == 'ADD':
            requests.post('http://127.0.0.1:5000/CAF/jtf2', json=data)
        elif self.action == 'UPDATE':
            requests.put(f"http://127.0.0.1:5000/CAF/soldier/{self._SIN.get()}", json=data)
        self.close_window()

    def cancel(self):
        self.close_window()


class add_CSOR_popup(tk.Frame):
    def __init__(self, parent, close_window, action):
        """ Constructor for the CSOR pop up window """
        tk.Frame.__init__(self, parent, bg="darkseagreen")
        self.grid(row=1, column=1)
        self.close_window = close_window
        self.action = action

        tk.Label(self, text="SIN:", fg="darkolivegreen", bg="darkseagreen").grid(row=1, column=1)
        self._SIN = ttk.Entry(self)
        self._SIN.grid(row=1, column=2)

        tk.Label(self, text="Rank:", fg="darkolivegreen", bg="darkseagreen").grid(row=2, column=1)
        self._rank = ttk.Entry(self)
        self._rank.grid(row=2, column=2)

        tk.Label(self, text="Last Name:", fg="darkolivegreen", bg="darkseagreen").grid(row=3, column=1)
        self._lname = ttk.Entry(self)
        self._lname.grid(row=3, column=2)

        tk.Label(self, text="First Name:", fg="darkolivegreen", bg="darkseagreen").grid(row=4, column=1)
        self._fname = ttk.Entry(self)
        self._fname.grid(row=4, column=2)

        tk.Label(self, text="Training Pay:", fg="darkolivegreen", bg="darkseagreen").grid(row=5, column=1)
        self._tpay = ttk.Entry(self)
        self._tpay.grid(row=5, column=2)

        tk.Label(self, text="Deployment Pay:", fg="darkolivegreen", bg="darkseagreen").grid(row=6, column=1)
        self._dpay = ttk.Entry(self)
        self._dpay.grid(row=6, column=2)

        tk.Label(self, text="Section Call Sign:", fg="darkolivegreen", bg="darkseagreen").grid(row=7, column=1)
        self._call_sign = ttk.Entry(self)
        self._call_sign.grid(row=7, column=2)

        ttk.Button(self, text='Submit', command=self.add_soldier, width=22).grid(row=8, column=1)
        ttk.Button(self, text='Cancel', command=self.cancel, width=18).grid(row=8, column=2)

    def add_soldier(self):
        data = {}
        data['Service_Number'] = self._SIN.get()
        data['Rank'] = self._rank.get()
        data['Last_Name'] = self._lname.get()
        data['First_Name'] = self._fname.get()
        data['Training_Pay'] = self._tpay.get()
        data['Deployment_Pay'] = self._dpay.get()
        data['Trainings'] = 'BMQ'
        data['Section_Call_Sign'] = self._call_sign.get()

        if self.action == 'ADD':
            r = requests.post('http://127.0.0.1:5000/CAF/csor', json=data)
        elif self.action == 'UPDATE':
            r = requests.put(f"http://127.0.0.1:5000/CAF/soldier/{self._SIN.get()}", json=data)

        if r.status_code != 200:
            tk.messagebox.showerror(r.reason)
        self.close_window()

    def cancel(self):
        self.close_window()

import tkinter as tk
from tkinter import ttk
import requests
from AddSoldier import add_CSOR_popup, add_JTF2_popup


class view_soldiers(tk.Frame):
    """ View soldier popup window """
    def __init__(self, parent, close_window):
        """ Constructor for viewing the soldier window """
        tk.Frame.__init__(self, parent, bg="darkseagreen")
        self.grid(row=1, column=1)
        self.close_window = close_window

        left_frame = tk.Frame(master=self, bg="darkseagreen")
        left_frame.grid(row=1, column=1)
        right_frame = tk.Frame(master=self, bg="darkseagreen")
        right_frame.grid(row=1, column=2)
        bottom_frame = tk.Frame(master=self, bg="darkseagreen")
        bottom_frame.grid(row=2, column=1, columnspan=2)

        tk.Label(left_frame, text="CSOR list:", fg="darkolivegreen", bg="darkseagreen").grid(row=1, column=1)
        self._csor_list = tk.Listbox(left_frame, width=20)
        self._csor_list.grid(row=2, column=1)
        self._csor_list.bind("<<ListboxSelect>>", self._update_textbox_csor)

        tk.Label(right_frame, text="JTF2 list:", fg="darkolivegreen", bg="darkseagreen").grid(row=1, column=1)
        self._jtf2_list = tk.Listbox(right_frame, width=20)
        self._jtf2_list.grid(row=2, column=1)
        self._jtf2_list.bind("<<ListboxSelect>>", self._update_textbox_jtf2)

        tk.Label(master=bottom_frame, text="      [SIN must match existing entry to update]", fg="darkolivegreen", bg="darkseagreen").grid(row=6,
                                                                                                                  column=1)
        self._info_text = tk.Text(master=bottom_frame, height=10, width=40, font=("TkTextFont", 10), fg="darkred")
        self._info_text.grid(row=3, column=1, columnspan=2)

        ttk.Button(left_frame, text="Update CSOR", command=self._update_CSOR, width=17).grid(row=4, column=1)
        ttk.Button(right_frame, text='Update JTF2', command=self._update_JTF2, width=17).grid(row=4, column=1)

        self.update_soldier_list()

    def update_soldier_list(self):
        """ Populates the lists of soldiers """
        r = requests.get("http://127.0.0.1:5000/CAF/soldier/all")
        self._csor_list.delete(0, tk.END)
        self._jtf2_list.delete(0, tk.END)
        for s in r.json()["CSOR"]:
            self._csor_list.insert(tk.END, s['Service_Number'])
        for s in r.json()['JTF2']:
            self._jtf2_list.insert(tk.END, s['Service_Number'])

    def _update_textbox_csor(self, evt):
        """ Updates the textbox with CSOR information """
        selected_values = self._csor_list.curselection()
        selected_index = selected_values[0]
        SIN = self._csor_list.get(selected_index)

        r = requests.get(f"http://127.0.0.1:5000/CAF/soldier/{SIN}")

        self._info_text.delete(1.0, tk.END)

        if r.status_code != 200:
            self._info_text.insert(tk.END, "Error running the request!")

        for k, v in r.json().items():
            self._info_text.insert(tk.END, f"{k.capitalize()}\t\t", "bold")
            self._info_text.insert(tk.END, f"{v}\n")

    def _update_textbox_jtf2(self, evt):
        """ Updates the textbox with JTF2 information """
        selected_values = self._jtf2_list.curselection()
        selected_index = selected_values[0]
        SIN = self._jtf2_list.get(selected_index)

        r = requests.get(f"http://127.0.0.1:5000/CAF/soldier/{SIN}")

        self._info_text.delete(1.0, tk.END)

        if r.status_code != 200:
            self._info_text.insert(tk.END, "Error running the request!")

        for k, v in r.json().items():
            self._info_text.insert(tk.END, f"{k.capitalize()}\t\t", "bold")
            self._info_text.insert(tk.END, f"{v}\n")

    def _update_CSOR(self):
        """ Update CSOR soldier info popup """
        self.new_popup_win = tk.Toplevel()
        self.new_popup = add_CSOR_popup(self.new_popup_win, self.new_close_window, 'UPDATE')

    def _update_JTF2(self):
        """ Update JTF2 soldier info popup """
        self.new_popup_win = tk.Toplevel()
        self.new_popup = add_JTF2_popup(self.new_popup_win, self.new_close_window, 'UPDATE')

    def new_close_window(self):
        """ Close the update info window """
        self.new_popup_win.destroy()





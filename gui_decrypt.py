#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from crypto import Krypton


__author__     = 'Jose Figueredo'
__copyright__  = 'Jose Figueredo'
__credits__    = ['Jose Figueredo']
__license__    = 'Corporative'
__version__    = '1.0.1'
__maintainer__ = 'Jose Figueredo'
__email__      = "josefigueredo@gmail.com"
__status__     = "Development"


'''
+-----------------+
|Deof     |
+-----------------+
|Archivo in: _____|
|Campo: _________v|
|Key: ____________|
|IV: _____________|
|Archivo out: ___ |
+-----------------+
|    Procesar     |
+-----------------+
'''


def find_file():
    filename_in = tk.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("txt files","*.txt"),("all files","*.*")))
    print (filename_in)

def save_file():
    filename_out = tk.filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("txt files","*.txt"),("all files","*.*")))
    print (filename_out)

def makeRow1(root):
    row = tk.Frame(root)
    lab = tk.Label(row, width=15, text='Archivo Origen', anchor='w')
    ent = tk.Button(row, text='Buscar', command=find_file, anchor='w')
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    lab.pack(side=tk.LEFT, )
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    return ent

def makeRow2(root):
    row = tk.Frame(root)
    lab = tk.Label(row, width=15, text='Campo', anchor='w')
    ent = tk.Entry(row)
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    return ent

def makeRow3(root):
    row = tk.Frame(root)
    lab = tk.Label(row, width=15, text='Key', anchor='w')
    ent = tk.Entry(row)
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    return ent

def makeRow4(root):
    row = tk.Frame(root)
    lab = tk.Label(row, width=15, text='IV', anchor='w')
    ent = tk.Entry(row)
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    return ent

def makeRow5(root):
    row = tk.Frame(root)
    lab = tk.Label(row, width=15, text='Archivo Destino', anchor='w')
    ent = tk.Button(row, text='Buscar', command=save_file, anchor='w')
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    lab.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    return ent

def makeform(root):
    entries = []
    btn1 = makeRow1(root)
    entries.append(('file_in', btn1))
    txt1 = makeRow2(root)
    entries.append(('campo', txt1))
    txt2 = makeRow3(root)
    entries.append(('key', txt2))
    txt3 = makeRow4(root)
    entries.append(('iv', txt3))
    btn2 = makeRow5(root)
    entries.append(('file_out', btn2))

    return entries

def makeProgressBAr(root):
    progressbar = ttk.Progressbar(root, length=330, orient="horizontal", mode="determinate")
    progressbar.pack(side=tk.LEFT, padx=5, pady=5)
    progressbar["value"] = 0
    progressbar["maximum"] = 100
    return progressbar

def makeProcessButton(root, ents, progressbar):
    b1 = tk.Button(root, text='Procesar', command=lambda: procesar(ents, progressbar))
    b1.pack(side=tk.RIGHT, padx=5, pady=5)

def procesar(ents, progressbar):
    currentValue = progressbar["value"] + 10
    progressbar.after(270, progress(currentValue))
    progressbar.update()
    key = ents[2][1].get()
    iv = ents[3][1].get()
    krypton = Krypton(key, iv)
    decrypted = krypton.decrypt('+cntYKg0yJkq8lRjwCHpSQ==')
    print('Decrypted: ' + decrypted)

def progress(currentValue):
    progressbar["value"] = currentValue

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('420x210')
    root.title("Fiscar DeOf")
    ents = makeform(root)
    progressbar = makeProgressBAr(root)
    makeProcessButton(root, ents, progressbar)    
    root.mainloop()
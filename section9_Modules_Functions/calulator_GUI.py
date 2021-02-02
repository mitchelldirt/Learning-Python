import tkinter


keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 2), ('/', 1)],
        ]
main_window_padding = 8

main_window = tkinter.Tk()
main_window.title("Calculator")
main_window.geometry('640x480-8-200')
main_window['padx'] = main_window_padding

result = tkinter.Entry(main_window)
result.grid(row=0, column=0, sticky='nsew')

keyPad = tkinter.Frame(main_window)
keyPad.grid(row=1, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

main_window.update()
main_window.minsize(keyPad.winfo_width() + main_window_padding, result.winfo_height() + keyPad.winfo_height())
main_window.maxsize(keyPad.winfo_width() + 100 + main_window_padding, result.winfo_height() + 50 + keyPad.winfo_height())

main_window.mainloop()
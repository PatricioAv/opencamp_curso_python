import tkinter as tk

def main():
    master = tk.Tk()
    master.geometry('300x240+800+400')

    label_titulo = tk.Label(master,
                            text='Top Linux distros en distrowatch.com',
                            foreground='yellow',
                            background='purple')
    label_titulo.pack()
    distowatch_top = ['LinuxMint', 'Ubuntu', 'MX Linux', 'Archlinux', 'Gentoo',
                      'Slackware', 'Debian', 'Fedora', 'OpenSuse', 'CentOS', 
                      'FreeBSD']
    items_listbox = tk.StringVar(value=distowatch_top)
    listbox_toplinux = tk.Listbox(master,
                                  height=len(distowatch_top),
                                  listvariable=items_listbox)
    listbox_toplinux.pack()
    master.mainloop()


if __name__ == "__main__":
    main()

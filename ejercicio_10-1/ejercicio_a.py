import tkinter

def main():

    master = tkinter.Tk()

    def reset():
        """
        Destruye el canvas y llama la función crea_canvas
        """
        canvas.destroy()
        crea_canvas()


    def poblar_canvas(master):
        """
        Crea función para radio_action para mostar en label_seleccion
        la selección del usuario y rellena el canvas con los elementos
        label y radio_buttons
        """

        def radio_action():
            valor = seleccion.get()
            label_seleccion['text'] = valor
        
        
        seleccion = tkinter.StringVar()
        label_titulo = tkinter.Label(
                master,
                text='¿Que tipo de S.O. prefieres?',
                foreground='yellow',
                background='purple'
                )
        label_titulo.pack()
        r1 = tkinter.Radiobutton(
                master,
                text='Linux  ',
                value='Linux',
                variable=seleccion,
                command=radio_action
                )
        r2 = tkinter.Radiobutton(
                master,
                text='MacOS  ',
                value='Mac',
                variable=seleccion,
                command=radio_action
                )
        r3 = tkinter.Radiobutton(
                master,
                text='Windows',
                value='Wondows',
                variable=seleccion,
                command=radio_action
                )
        r1.pack()
        r2.pack()
        r3.pack()
        label_seleccion = tkinter.Label(
                                master,
                                text="    S.O.   ",
                                foreground='white',
                                background='black'
                                )
        label_seleccion.pack()


    def crea_canvas():
        """
        Crea canvas global, llama a función poblar_canvas y agrega botones
        Reset y Salir
        """
        global canvas
        canvas = tkinter.Canvas()
        canvas.pack()
        poblar_canvas(canvas)
        Reset = tkinter.Button(
                canvas, text='Reset',
                command=reset
                ).pack(pady=5, padx=10)
        Salir = tkinter.Button(
                canvas,
                text='Salir',
                command=canvas.quit
                ).pack(pady=5, padx=10) 


    crea_canvas()
    master.mainloop()

if __name__ == "__main__":
    main()

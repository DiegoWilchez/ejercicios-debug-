"""
Muchas especies de tortugas marinas están en peligro de extinción. Por eso, los
biólogos de la conservación y muchos voluntarios recogen cada año los huevos que
depositan las tortugas en las playas y los llevan a incubadoras para protegerlos de
depredadores y humanos. Los huevos de tortuga, como los de todos los reptiles,
son muy sensibles a la temperatura y si se exponen más de 34°C no se desarrollan.
De la misma manera, temperaturas inferiores a 26°C no permiten que se
desarrollen los embriones. Un centro de preservación de tortugas marinas te pide
ayuda Programando una solución de software que les permita mantenerse
informados sobre la temperatura del sitio de incubación; quieren saber si es muy
baja, adecuada o muy alta para el desarrollo de los huevos

Tu programa recogerá los datos emitidos por un dispositivo que detecte la
Temperatura. Dichos datos, por el momento, son introducidos por el operador
manualmente. Además, deberá avisar a los biólogos cuando la temperatura sea muy
baja con un mensaje que diga “T. baja”, cuando la temperatura sea normal “T.
normal”, y cuando la temperatura sea muy alta, “T. alta”. Si quieres, puedes
inventar iconos (en modo texto) que reemplacen los textos pero que resulten
evidentes para quien observa

"""

def temperatura():
    estado_temperatura = float(input("ingrese la temperatura"))
    if estado_temperatura < 26:
        print("T. baja")
    elif estado_temperatura > 34:
        print("T. alta")
    else:
        print("T. normal")
    return estado_temperatura

temperatura()
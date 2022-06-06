#P0 -> Příkaz pro zapnutí/vypnutí funkce odbočení vpravo
#P1 -> Příkaz pro zapnutí/vypnutí funkce odbočení vlevo
#P2 -> Příkaz pro otočení
#LOGO -> Příkaz pro prohození barev (bílá/černá -> 1/0)
#A -> Příkaz nastavení otočky o 180 atd. doleva
#B -> Příkaz nastavení otočky o 180 atd. doprava

def on_pin_pressed_p0():
    radio.send_string("OdbockaP")
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)
def on_pin_pressed_p1():
    radio.send_string("OdbockaL")
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
def on_pin_pressed_p2():
    radio.send_string("Otocka")
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)
def on_logo_event_pressed():
    radio.send_string("ProhodBarvy")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)
def on_button_pressed_a():
    radio.send_string("TurnBackL")
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    radio.send_string("TurnBackR")
input.on_button_pressed(Button.B, on_button_pressed_b)
// P0 -> Příkaz pro zapnutí/vypnutí funkce odbočení vpravo
// P1 -> Příkaz pro zapnutí/vypnutí funkce odbočení vlevo
// P2 -> Příkaz pro otočení
// LOGO -> Příkaz pro prohození barev (bílá/černá -> 1/0)
// A -> Příkaz nastavení otočky o 180 atd. doleva
// B -> Příkaz nastavení otočky o 180 atd. doprava
basic.forever(function on_forever() {
    radio.setGroup(77)
})
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    radio.sendString("OdbockaP")
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    radio.sendString("OdbockaL")
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    radio.sendString("Otocka")
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    radio.sendString("ProhodBarvy")
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("TurnBackL")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString("TurnBackR")
})

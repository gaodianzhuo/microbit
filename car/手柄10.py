def on_button_pressed_a():
    radio.send_string("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_string("AB")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_string("B")
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)
radio.set_transmit_power(7)
basic.show_icon(IconNames.BUTTERFLY)

def on_forever():
    if pins.analog_read_pin(AnalogPin.P2) < 256:
        radio.send_string("A")
    elif pins.analog_read_pin(AnalogPin.P2) < 597:
        radio.send_string("B")
    elif pins.analog_read_pin(AnalogPin.P2) < 725:
        radio.send_string("C")
    elif pins.analog_read_pin(AnalogPin.P2) < 793:
        radio.send_string("D")
    elif pins.analog_read_pin(AnalogPin.P2) < 836:
        radio.send_string("E")
    elif pins.analog_read_pin(AnalogPin.P2) < 938:
        radio.send_string("F")
    if pins.analog_read_pin(AnalogPin.P0) < 400:
        radio.send_string("-X")
    elif pins.analog_read_pin(AnalogPin.P0) > 600:
        radio.send_string("+X")
    if pins.analog_read_pin(AnalogPin.P1) < 400:
        radio.send_string("-Y")
    elif pins.analog_read_pin(AnalogPin.P1) > 600:
        radio.send_string("+Y")
basic.forever(on_forever)

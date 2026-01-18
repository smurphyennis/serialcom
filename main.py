def on_button_pressed_a():
    basic.show_number(pins.analog_read_pin(AnalogReadWritePin.P2))
    basic.show_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string(BR3_Sim_Result)
input.on_button_pressed(Button.B, on_button_pressed_b)

BR3_Sim_Result = ""
serial.redirect_to_usb()
basic.show_icon(IconNames.HEART)

def on_forever():
    serial.write_line("" + str(input.temperature()) + "," + ("" + str(pins.digital_read_pin(DigitalPin.P2))) + "," + BR3_Sim_Result)
basic.forever(on_forever)

def on_forever2():
    global BR3_Sim_Result
    if pins.analog_read_pin(AnalogReadWritePin.P2) >= 750:
        BR3_Sim_Result = "\"Thick Canopy\""
    elif pins.analog_read_pin(AnalogReadWritePin.P2) <= 749 and pins.analog_read_pin(AnalogReadWritePin.P2) > 600:
        BR3_Sim_Result = "\"Medium Canopy\""
    elif pins.analog_read_pin(AnalogReadWritePin.P2) <= 599 and pins.analog_read_pin(AnalogReadWritePin.P2) > 390:
        BR3_Sim_Result = "\"Thin Canopy\""
    else:
        BR3_Sim_Result = "\"No Canopy\""
basic.forever(on_forever2)

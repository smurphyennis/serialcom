input.onButtonPressed(Button.A, function () {
    basic.showNumber(pins.analogReadPin(AnalogReadWritePin.P2))
    basic.showNumber(0)
})
input.onButtonPressed(Button.B, function () {
    basic.showString(BR3_Sim_Result)
})
let BR3_Sim_Result = ""
serial.redirectToUSB()
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    serial.writeLine("" + input.temperature() + "," + ("" + pins.digitalReadPin(DigitalPin.P2)) + "," + BR3_Sim_Result)
})
basic.forever(function () {
    if (pins.analogReadPin(AnalogReadWritePin.P2) >= 750) {
        BR3_Sim_Result = "\"Thick Canopy\""
    } else if (pins.analogReadPin(AnalogReadWritePin.P2) <= 749 && pins.analogReadPin(AnalogReadWritePin.P2) > 600) {
        BR3_Sim_Result = "\"Medium Canopy\""
    } else if (pins.analogReadPin(AnalogReadWritePin.P2) <= 599 && pins.analogReadPin(AnalogReadWritePin.P2) > 390) {
        BR3_Sim_Result = "\"Thin Canopy\""
    } else {
        BR3_Sim_Result = "\"No Canopy\""
    }
})

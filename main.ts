input.onButtonPressed(Button.A, function () {
    while (num < 1023) {
        servos.P0.setAngle(0)
        basic.pause(1500)
        servos.P0.setAngle(180)
        basic.pause(2000)
    }
})
let num = 0
radio.setGroup(88)
num = 433
loops.everyInterval(10000, function () {
    basic.showNumber(num)
    radio.sendNumber(num)
    if (num < 1023) {
        num += randint(50, 100)
    }
})

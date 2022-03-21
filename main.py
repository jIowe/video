def on_button_pressed_a():
    radio.send_string("yes")
    basic.show_string("sent")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    if receivedString == "yes":
        basic.show_icon(IconNames.YES)
        basic.pause(2000)
        basic.clear_screen()
    elif receivedString == "no":
        basic.show_icon(IconNames.NO)
        basic.pause(2000)
        basic.clear_screen()
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("no")
    basic.show_string("sent")
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(88)
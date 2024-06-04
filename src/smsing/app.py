"""
this project is for automating sms verification subscription
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class smsing(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        self.phone_input = toga.TextInput(placeholder='Phone Number', style=Pack(flex=1, padding=5))
        self.message_input = toga.TextInput(placeholder='Message', style=Pack(flex=1, padding=5))
        self.send_button = toga.Button('Send', on_press=self.send_sms, style=Pack(padding=5))

        input_box = toga.Box(style=Pack(direction=ROW, padding=5))
        input_box.add(self.phone_input)
        input_box.add(self.message_input)
        input_box.add(self.send_button)

        main_box.add(input_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def send_sms(self, widget):
        print(f"sms sent to {self.phone_input.value} with the message {self.message_input.value}")

        # Placeholder for the send SMS logic
    # def startup(self):
    #     main_box = toga.Box(style=Pack(direction=COLUMN))

    #     name_label = toga.Label(
    #         "Your name: ",
    #         style=Pack(padding=(0, 5)),
    #     )
    #     self.name_input = toga.TextInput(style=Pack(flex=1))

    #     name_box = toga.Box(style=Pack(direction=ROW, padding=50))
    #     name_box.add(name_label)
    #     name_box.add(self.name_input)

    #     button = toga.Button(
    #         "Say Hello!",
    #         on_press=self.say_hello,
    #         style=Pack(padding=5),
    #     )

    #     main_box.add(name_box)
    #     main_box.add(button)

    #     self.main_window = toga.MainWindow(title=self.formal_name)
    #     self.main_window.content = main_box
    #     self.main_window.show()
    # def say_hello(self, widget):
    #     print(f"Hello, {self.name_input.value}")
def main():
    return smsing()

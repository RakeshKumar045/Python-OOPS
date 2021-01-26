import time
from abc import ABCMeta, abstractstaticmethod


class ICommand(metaclass=ABCMeta):
    """The command interface, which all commands will implement"""

    @abstractstaticmethod
    def execute():
        """The required execute method which all command objects will use"""


class Switch:
    """The Invoker Class"""

    def __init__(self):
        self._commands = {}
        self._history = []

    @property
    def history(self):
        return self._history

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands.keys():
            self._history.append((time.time(), command_name))
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")


class Light:
    """The Receiver"""

    def turn_on(self):
        print("Light turned ON")

    def turn_off(self):
        print("Light turned OFF")


class SwitchOnCommand(ICommand):
    """A Command object, which implements the ICommand interface"""

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()


class SwitchOffCommand(ICommand):
    """A Command object, which implements the ICommand interface"""

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()


if __name__ == "__main__":
    # The Client is the main python app

    # The Light is the Receiver
    LIGHT = Light()

    # Create Commands
    SWITCH_ON = SwitchOnCommand(LIGHT)
    SWITCH_OFF = SwitchOffCommand(LIGHT)

    # Register the commands with the invoker (Switch)
    SWITCH = Switch()
    SWITCH.register("ON", SWITCH_ON)
    SWITCH.register("OFF", SWITCH_OFF)

    # Execute the commands that are registered on the Invoker
    SWITCH.execute("ON")
    SWITCH.execute("OFF")
    SWITCH.execute("ON")
    SWITCH.execute("OFF")

    # For fun, we can see the history
    print(SWITCH.history)

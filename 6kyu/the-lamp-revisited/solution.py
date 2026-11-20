class Lamp:
    def __init__(self, color: str):
        self.color = color
        self.on = False

    def toggle_switch(self):
        self.on = not self.on

    def state(self):
        return "The lamp is on." if self.on else "The lamp is off."


if __name__ == "__main__":
    lamp = Lamp("blue")
    print(lamp.state())
    lamp.toggle_switch()
    print(lamp.state())
    lamp.toggle_switch()
    print(lamp.state())
    lamp.toggle_switch()
    print(lamp.state())




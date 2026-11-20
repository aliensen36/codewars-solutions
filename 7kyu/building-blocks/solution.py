class Block:
    def __init__(self, dimensions):
        self.width, self.length, self.height = dimensions

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        return (2 * (self.width * self.length +
                self.height * self.length +
                self.width * self.height))

if __name__ == "__main__":
    block = Block([2, 4, 6])
    print(f"Ширина блока: {block.get_width()}\n"
          f"Длина блока: {block.get_length()}\n"
          f"Высота блока: {block.get_height()}\n"
          f"Объем блока: {block.get_volume()}\n"
          f"Площадь поверхности блока: {block.get_surface_area()}")

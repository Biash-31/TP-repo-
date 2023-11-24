class Image:
    def __init__(self, channels, fill_value=0):
        self.width = 640
        self.height = 480
        self.fill_value = fill_value

        if channels == 1:
            # Creating a black and white image
            self.data = [fill_value] * (self.width * self.height)
        elif channels == 3:
            # Creating a color (RGB) image
            self.data = [[fill_value] * 3 for _ in range(self.width * self.height)]
        else:
            raise ValueError("Invalid number of channels. Choose 1 for black and white or 3 for color.")


    # Constructor with specified values
    @classmethod
    def from_values(cls, channels, values):
        image = cls(channels)
        if channels == 1:
            image.data = [values] * (image.width * image.height)
        elif channels == 3:
            image.data = [list(values) for _ in range(image.width * image.height)]
        return image



    # Create a new image with the same content
    def copy(self):
        new_image = Image(channels=1 if isinstance(self.data[0], int) else 3)
        new_image.data = [row[:] if isinstance(row, list) else row for row in self.data]
        return new_image



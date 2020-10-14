class Font():
    fonts = {}

    def __init__(self):
        self.fonts = self.read_fonts('font.txt')

    def read_fonts(self, font_file):
        fonts = {}
        with open(font_file, 'r') as file:
            for line in file:
                line_data = line.split("#")
                font_data = line_data[0].split(',')
                fonts[chr(int(line_data[1].strip()))] = [int(data.strip(), 16) for data in font_data]
        return fonts
    
    def get_font(self, char):
        return self.fonts[char]
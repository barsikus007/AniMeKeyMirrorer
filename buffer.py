import os
from pathlib import Path
from functools import partial

from PIL import Image, ImageDraw, ImageFont


# https://blog.joshwalsh.me/asus-anime-matrix/
NATIVE_RESOLUTION = (60, 36)  # btw image size is 35 so y=0 line omtted
# ffmpeg -i *.webm -filter_complex "[0:v]fps=30,scale=66:-1,setpts=0.65*PTS[v]" -map '[v]' -loop 0 bad-apple.gif -y && cp -rf bad-apple.gif ~/.config/rog/
# ffmpeg -i *.webm -filter_complex "[0:v]fps=30,scale=66:-1,setpts=0.645*PTS[v]" -map '[v]' -loop 0 bad-apple.gif -y && cp -rf bad-apple.gif ~/.config/rog/
HORIZONTAL_EMULATED_RESOLUTION = (66, 55)
FONT_COLOR = (255, 255, 255)


class Buffer:
    buffer = ""
    buffer_size = 6
    images = Path("images/")
    images.mkdir(exist_ok=True)
    fonts = Path("fonts/")
    fonts.mkdir(exist_ok=True)
    font_name = "NotoSansMono-SemiBold.ttf"
    # font_name = "DelugiaComplete.ttf"
    # font_name = "ROG Fonts v1.5-Regular.otf"
    font_size = 14
    # font_size = 22
    font = ImageFont.truetype(str(fonts / font_name), font_size)

    def cut(self, line=1, size=buffer_size):
        buf = self.buffer.split("\n")
        print(f"{buf}")
        return buf[-line][-size:] if len(buf) >= line else ""

    def add(self, other):
        self.buffer += other

    def pop(self):
        self.buffer = self.buffer[:-1]

    def clear(self):
        self.buffer = ""

    def show(self):
        type_mode = False
        line_height = 10
        base_line = 18
        # filename = self.images_path / f"{hash(self.cut())}.png")  # for async
        filename = self.images / "frame.png"

        img = Image.new('RGB', NATIVE_RESOLUTION, color=(0, 0, 0))
        d = ImageDraw.Draw(img)
        typer = partial(d.text, fill=FONT_COLOR, font=self.font)
        typer((12, base_line-line_height*2), self.cut(3,4))
        typer((10, base_line-line_height), self.cut(2,6))
        if type_mode:
            typer((8, base_line), f"{self.cut(1, 5)}⎸")
        else:
            typer((8, 18), self.cut())
        img.save(filename)

        os.system(f"asusctl anime pixel-image -p {filename}")  # nosec B605

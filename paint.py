"""
Your friend is developing a small image processing program and has asked for your help
in implementing MS-Paint's “paint bucket”-like functionality. Their program represents
images using arrays of characters, with each array value representing a pixel and letters and
symbols representing different colors. For example, the following 4x6 matrix represents the
letter P in color "#", with background color "." (dot)
.###..
.#..#.
.###..
.#....

Your subroutine should take a pixel and a new color and paint the region of that pixel with
the new color, like MS-Paint's “paint bucket” tool.
Examples:
Pixel (0,1) and new color 'O' Pixel (1,3) and new color 'o' Pixel (1,3) and new color '#'
Before After Before After Before After
.###..
.#..#.
.###..
.#....

.OOO..
.O..#.
.OOO..
.O....

.###.
.#..#.
.###.
.#....

.###..
.#oo#.
.###..
.#....

.###..
.#..#.
.###..
.#....

.###..
.####.
.###..
.#....

"""


from dataclasses import dataclass

image = """.###..
.#..#.
.###..
.#...."""

out1 = """.OOO..
.O..#.
.OOO..
.O...."""

out2 = """.###..
.#oo#.
.###..
.#...."""

out3 = """.###..
.####.
.###..
.#...."""


@dataclass
class Pixel:
    x: int
    y: int
    color: str

    def set_color(self, color: str) -> None:
        self.color = color


@dataclass
class ImageMap:
    width: int
    height: int
    pixels: list[Pixel] | None

    def __init__(self, width, height, pixels):
        if pixels is None:
            pixels = list()
            for i in range(self.width):
                for j in range(self.height):
                    pixels.append(Pixel(i, j, "."))
            self.pixels = pixels
        else:
            self.width = width
            self.height = height
            self.pixels = pixels

    @classmethod
    def map_pixels_from_str(cls, img_str, width=4, height=6):
        pixel_mapping = [list(x) for x in img_str.splitlines()]
        assert len(pixel_mapping) == width
        pixels = []
        for y, line in enumerate(pixel_mapping):
            assert len(line) == height
            for x, color in enumerate(line):
                pixels.append(Pixel(x, y, color))
        return cls(pixels=pixels, width=width, height=height)

    def pixel_to_str(self):
        lines = {}
        for p in self.pixels:
            lines[p.y] = lines[p.y] + p.color if lines.get(p.y) else p.color
        pixel_out = ''
        for chave, valor in lines.items():
            pixel_out += f"{valor}\n"
        return pixel_out[:-1]

    def print_mapped(self):
        print(self.pixel_to_str())

    def _get_pixel(self, x: int, y: int) -> Pixel:
        if x >= 0 and y >= 0:
            list_pixel = list(filter(lambda pixel: pixel.x == x and pixel.y == y, self.pixels))
            if list_pixel:
                return list_pixel[0]

    def _get_nearby(self, pixel: Pixel) -> list[Pixel]:
        x = pixel.x
        y = pixel.y
        return [self._get_pixel(x + 1, y), self._get_pixel(x - 1, y),
                self._get_pixel(x, y + 1), self._get_pixel(x, y - 1)]

    def _get_area(self, pixel: Pixel) -> list[Pixel]:
        if pixel:
            color = pixel.color
            nearby = self._get_nearby(pixel)
            list_pixels = [pixel]
            while nearby:
                nearby = self.remove_repeateds(nearby)
                for p in nearby:
                    nearby = self.remove_repeateds(nearby)
                    if p.color == color:
                        list_pixels.append(p)
                        for px in self._get_nearby(p):
                            if px not in list_pixels:
                                nearby.append(px)
                    nearby.remove(p)

            return list(list_pixels)

    def remove_repeateds(self, pixels: list[Pixel]) -> list[Pixel]:
        cleaned_pixels = []
        for pixel in pixels:
            if pixel not in cleaned_pixels:
                cleaned_pixels.append(pixel)
        return list(filter(lambda px: px, cleaned_pixels))

    def paint_bucket(self, x: int, y: int, color: str):
        selected_pixel = self._get_pixel(x, y)
        area = self._get_area(selected_pixel)
        if area:
            for px in area:
                px.set_color(color)


class TestImageMap:

    def test_case1(self):
        image_map = ImageMap.map_pixels_from_str(image)
        image_map.paint_bucket(1, 0, "O")
        assert image_map.pixel_to_str() == out1

    def test_case_2(self):
        image_map = ImageMap.map_pixels_from_str(image)
        image_map.paint_bucket(3, 1, "o")
        assert image_map.pixel_to_str() == out2

    def test_case3(self):
        image_map = ImageMap.map_pixels_from_str(image)
        image_map.paint_bucket(3, 1, "#")
        assert image_map.pixel_to_str() == out3


if __name__ == "__main__":
    image_map = ImageMap.map_pixels_from_str(image)
    image_map.print_mapped()
    image_map.paint_bucket(0, 1, "o")
    image_map.print_mapped()

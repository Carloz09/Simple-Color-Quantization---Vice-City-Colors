from PIL import Image
def main():
    def isColorAlike(r, g, b):
        colors = [
            (0, 168, 255),
            (2, 102, 200),
            (244, 175, 194),
            (241, 149, 172),
            (178, 139, 192)
        ]

        mostAlike = None
        minDistance = float("inf")

        for color in colors:
            cR, cG, cB = color

            distance = (
                    abs(r - cR) +
                    abs(g - cG) +
                    abs(b - cB)
            )

            if distance < minDistance:
                minDistance = distance
                mostAlike = color

        return mostAlike

    def process_image(input_path, output_path):

        img = Image.open(input_path).convert("RGB")
        width, height = img.size

        pixels = img.load()

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]

                pixels[x, y] = isColorAlike(
                    r, g, b
                )

        img = img.rotate(-90, expand=True)
        img.save(output_path)

    process_image("Input/input.png", "Output/output.png")


if __name__ == "__main__":
    main()
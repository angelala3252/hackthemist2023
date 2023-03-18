""" This file contains the code to convert the input text into a mood ring
Convert the sentiment of the text into a tuple of an RGB colour,
    according to the following scales:
    - Red scale measures how passionate the text is;
        light red is less passionate and dark red is more passionate
    - Green scale measures how rude the text is;
        light green is less rude and dark green is more rude
    - Blue scale measures how sad the text is;
        light blue is less sad and dark red is more sad."""

import pygame
#import pygame.gfxdraw
from PIL import Image, ImageDraw
import data2emotions as emotions

# --- constants ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)

PI = 3.1415


def draw_mood_ring(text: str) -> None:
    """
    Convert the input text into a mood ring with the colours described above.
    """
    # pull RGB vals from data2emotions.py
    red = emotions.give_passion(text)
    green = emotions.give_sentiment(text)
    blue = emotions.give_sadness(text)

    pygame.init()
    screen = pygame.display.set_mode((800,600))

    # - generate PIL image with transparent background -

    pil_size = 300

    pil_image = Image.new("RGBA", (pil_size, pil_size))
    pil_draw = ImageDraw.Draw(pil_image)
    pil_draw.arc([0, 0, pil_size - 1, pil_size - 1], 0, 270, fill=RED)
    pil_draw.pieslice([0, 0, pil_size - 1, pil_size - 1], 0, 240, fill=(red, 0, 0))
    pil_draw.pieslice([0, 0, pil_size - 1, pil_size - 1], 240, 120, fill=(0, blue, 0))
    pil_draw.pieslice([0, 0, pil_size - 1, pil_size - 1], 120, 0, fill=(0, 0, blue))

    # - convert into PyGame image -

    mode = pil_image.mode
    size = pil_image.size
    data = pil_image.tobytes()

    image = pygame.image.fromstring(data, size, mode)

    image_rect = image.get_rect(center=screen.get_rect().center)

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(WHITE)

        screen.blit(image, image_rect)  # <- display image

        pygame.display.flip()

    # - end -

    pygame.quit()

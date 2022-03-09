import pygame, sys

pygame.init()
WINDOW = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 60
clock = pygame.time.Clock()
red_dot = pygame.image.load('Assets/red-dot.jpg')
red_dot = pygame.transform.scale(red_dot, (3, 3))


class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, window):
        if self.image is not None:
            window.blit(self.image, self.rect)
        window.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        return position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom)

    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)


def main():
    # clock = pygame.time.Clock()
    # running = True
    # while running:
    #     clock.tick(FPS)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #     draw_window()
    # pygame.quit()
    menu()


def menu():
    pygame.display.set_caption('PUBG Player Locator')
    running = True
    while running:
        menu_mouse_pos = pygame.mouse.get_pos()
        WINDOW.fill(BLACK)
        font = pygame.font.SysFont('cambria', 30)

        menu_text = font.render("Choose a map", True, WHITE)
        menu_rect = menu_text.get_rect(center=(640, 50))

        map_btns = [
            Button(image=None, pos=(640, 150),
                   text_input="Erangel", font=font, base_color=WHITE, hovering_color=GREEN),
            Button(image=None, pos=(640, 200),
                   text_input="Miramar", font=font, base_color=WHITE, hovering_color=GREEN),
            Button(image=None, pos=(640, 250),
                   text_input="Vikendi", font=font, base_color=WHITE, hovering_color=GREEN),
            Button(image=None, pos=(640, 300),
                   text_input="Sanhok", font=font, base_color=WHITE, hovering_color=GREEN),
            Button(image=None, pos=(640, 350),
                   text_input="Karakin", font=font, base_color=WHITE, hovering_color=GREEN),
            Button(image=None, pos=(640, 400),
                   text_input="Paramo", font=font, base_color=WHITE, hovering_color=GREEN),
            Button(image=None, pos=(640, 450),
                   text_input="Haven", font=font, base_color=WHITE, hovering_color=GREEN),
            Button(image=None, pos=(640, 500),
                   text_input="Taego", font=font, base_color=WHITE, hovering_color=GREEN)
        ]

        WINDOW.blit(menu_text, menu_rect)

        for btn in map_btns:
            btn.change_color(menu_mouse_pos)
            btn.update(WINDOW)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if map_btns[0].check_for_input(menu_mouse_pos):
                    erangel()
                if map_btns[1].check_for_input(menu_mouse_pos):
                    miramar()
                if map_btns[2].check_for_input(menu_mouse_pos):
                    vikendi()
                if map_btns[3].check_for_input(menu_mouse_pos):
                    sanhok()
                if map_btns[4].check_for_input(menu_mouse_pos):
                    karakin()
                if map_btns[5].check_for_input(menu_mouse_pos):
                    paramo()
                if map_btns[6].check_for_input(menu_mouse_pos):
                    haven()
                if map_btns[7].check_for_input(menu_mouse_pos):
                    taego()
        pygame.display.update()


def erangel():
    pygame.display.set_caption('PUBG Player Locator - Erangel')
    running = True
    while running:
        erangel_mouse_pos = pygame.mouse.get_pos()
        WINDOW.fill(BLACK)

        erangel_map = pygame.image.load('Assets/erangel-map.jpg')
        erangel_map = pygame.transform.scale(erangel_map, (1280, 720))
        WINDOW.blit(erangel_map, (0, 0))

        font = pygame.font.SysFont('cambria', 25)
        map_text = font.render("Erangel", True, WHITE)
        map_rect = map_text.get_rect(center=(640, 25))
        WINDOW.blit(map_text, map_rect)

        change_map = Button(image=None, pos=(100, 25),
                            text_input="Change Map", font=font, base_color=WHITE, hovering_color=RED)
        change_map.change_color(erangel_mouse_pos)
        change_map.update(WINDOW)

        WINDOW.blit(red_dot, (300, 200))
        WINDOW.blit(red_dot, (300, 300))
        WINDOW.blit(red_dot, (200, 300))
        WINDOW.blit(red_dot, (200, 200))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if change_map.check_for_input(erangel_mouse_pos):
                    menu()
        pygame.display.update()


def miramar():
    pygame.display.set_caption('PUBG Player Locator - Miramar')
    running = True
    while running:
        miramar_mouse_pos = pygame.mouse.get_pos()
        WINDOW.fill(BLACK)

        miramar_map = pygame.image.load('Assets/miramar-map.jpg')
        miramar_map = pygame.transform.scale(miramar_map, (1280, 720))
        WINDOW.blit(miramar_map, (0, 0))

        font = pygame.font.SysFont('cambria', 25)
        map_text = font.render("Miramar", True, WHITE)
        map_rect = map_text.get_rect(center=(640, 25))
        WINDOW.blit(map_text, map_rect)

        change_map = Button(image=None, pos=(100, 25),
                            text_input="Change Map", font=font, base_color=WHITE, hovering_color=RED)
        change_map.change_color(miramar_mouse_pos)
        change_map.update(WINDOW)

        WINDOW.blit(red_dot, (300, 200))
        WINDOW.blit(red_dot, (300, 300))
        WINDOW.blit(red_dot, (200, 300))
        WINDOW.blit(red_dot, (200, 200))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if change_map.check_for_input(miramar_mouse_pos):
                    menu()
        pygame.display.update()


def vikendi():
    pygame.display.set_caption('PUBG Player Locator - Vikendi')
    running = True
    while running:
        vikendi_mouse_pos = pygame.mouse.get_pos()
        WINDOW.fill(BLACK)

        vikendi_map = pygame.image.load('Assets/vikendi-map.jpg')
        vikendi_map = pygame.transform.scale(vikendi_map, (1280, 720))
        WINDOW.blit(vikendi_map, (0, 0))

        font = pygame.font.SysFont('cambria', 25)
        map_text = font.render("Vikendi", True, WHITE)
        map_rect = map_text.get_rect(center=(640, 25))
        WINDOW.blit(map_text, map_rect)

        change_map = Button(image=None, pos=(100, 25),
                            text_input="Change Map", font=font, base_color=WHITE, hovering_color=RED)
        change_map.change_color(vikendi_mouse_pos)
        change_map.update(WINDOW)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if change_map.check_for_input(vikendi_mouse_pos):
                    menu()
        pygame.display.update()


def sanhok():
    pygame.display.set_caption('PUBG Player Locator - Sanhok')
    running = True
    while running:
        sanhok_mouse_pos = pygame.mouse.get_pos()
        WINDOW.fill(BLACK)

        sanhok_map = pygame.image.load('Assets/sanhok-map.jpg')
        sanhok_map = pygame.transform.scale(sanhok_map, (1280, 720))
        WINDOW.blit(sanhok_map, (0, 0))

        font = pygame.font.SysFont('cambria', 25)
        map_text = font.render("Sanhok", True, WHITE)
        map_rect = map_text.get_rect(center=(640, 25))
        WINDOW.blit(map_text, map_rect)

        change_map = Button(image=None, pos=(100, 25),
                            text_input="Change Map", font=font, base_color=WHITE, hovering_color=RED)
        change_map.change_color(sanhok_mouse_pos)
        change_map.update(WINDOW)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if change_map.check_for_input(sanhok_mouse_pos):
                    menu()
        pygame.display.update()


def karakin():
    pygame.display.set_caption('PUBG Player Locator - Karakin')
    running = True
    while running:
        karakin_mouse_pos = pygame.mouse.get_pos()
        WINDOW.fill(BLACK)

        karakin_map = pygame.image.load('Assets/karakin-map.jpg')
        karakin_map = pygame.transform.scale(karakin_map, (1280, 720))
        WINDOW.blit(karakin_map, (0, 0))

        font = pygame.font.SysFont('cambria', 25)
        map_text = font.render("Karakin", True, WHITE)
        map_rect = map_text.get_rect(center=(640, 25))
        WINDOW.blit(map_text, map_rect)

        change_map = Button(image=None, pos=(100, 25),
                            text_input="Change Map", font=font, base_color=WHITE, hovering_color=RED)
        change_map.change_color(karakin_mouse_pos)
        change_map.update(WINDOW)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if change_map.check_for_input(karakin_mouse_pos):
                    menu()
        pygame.display.update()


def paramo():
    pygame.display.set_caption('PUBG Player Locator - Paramo')
    running = True
    while running:
        paramo_mouse_pos = pygame.mouse.get_pos()
        WINDOW.fill(BLACK)

        paramo_map = pygame.image.load('Assets/paramo-map.jpg')
        paramo_map = pygame.transform.scale(paramo_map, (1280, 720))
        WINDOW.blit(paramo_map, (0, 0))

        font = pygame.font.SysFont('cambria', 25)
        map_text = font.render("Paramo", True, WHITE)
        map_rect = map_text.get_rect(center=(640, 25))
        WINDOW.blit(map_text, map_rect)

        change_map = Button(image=None, pos=(100, 25),
                            text_input="Change Map", font=font, base_color=WHITE, hovering_color=RED)
        change_map.change_color(paramo_mouse_pos)
        change_map.update(WINDOW)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if change_map.check_for_input(paramo_mouse_pos):
                    menu()
        pygame.display.update()


def haven():
    pygame.display.set_caption('PUBG Player Locator - Haven')
    running = True
    while running:
        haven_mouse_pos = pygame.mouse.get_pos()
        WINDOW.fill(BLACK)

        haven_map = pygame.image.load('Assets/haven-map.jpg')
        haven_map = pygame.transform.scale(haven_map, (1280, 720))
        WINDOW.blit(haven_map, (0, 0))

        font = pygame.font.SysFont('cambria', 25)
        map_text = font.render("Haven", True, WHITE)
        map_rect = map_text.get_rect(center=(640, 25))
        WINDOW.blit(map_text, map_rect)

        change_map = Button(image=None, pos=(100, 25),
                            text_input="Change Map", font=font, base_color=WHITE, hovering_color=RED)
        change_map.change_color(haven_mouse_pos)
        change_map.update(WINDOW)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if change_map.check_for_input(haven_mouse_pos):
                    menu()
        pygame.display.update()


def taego():
    pygame.display.set_caption('PUBG Player Locator - Taego')
    running = True
    while running:
        taego_mouse_pos = pygame.mouse.get_pos()
        WINDOW.fill(BLACK)

        taego_map = pygame.image.load('Assets/taego-map.jpg')
        taego_map = pygame.transform.scale(taego_map, (1280, 720))
        WINDOW.blit(taego_map, (0, 0))

        font = pygame.font.SysFont('cambria', 25)
        map_text = font.render("Taego", True, WHITE)
        map_rect = map_text.get_rect(center=(640, 25))
        WINDOW.blit(map_text, map_rect)

        change_map = Button(image=None, pos=(100, 25),
                            text_input="Change Map", font=font, base_color=WHITE, hovering_color=RED)
        change_map.change_color(taego_mouse_pos)
        change_map.update(WINDOW)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if change_map.check_for_input(taego_mouse_pos):
                    menu()
        pygame.display.update()


if __name__ == "__main__":
    main()

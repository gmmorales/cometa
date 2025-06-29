import pygame
from config.constants import FPS

class PygameApp:
    def __init__(self, width, height, name_game, logger):
        self.width = width
        self.height = height
        self.name_game = name_game
        self.logger = logger

        # Inicializar Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name_game)
        self.clock = pygame.time.Clock()
        self.running = True

        # Opciones del menú
        self.menu_options = ["Start", "Options", "Exit"]
        self.current_option = 0

        # Configuración de la fuente
        self.font = pygame.font.Font(None, 74)

        # Cargar imagen de fondo
        self.background_image = pygame.image.load("assets/images/title_screen_background.jpg").convert()

    def run(self):
        while self.running:
            self.handle_events()
            #self.update()
            #self.draw()
            self.draw_title_screen()
            pygame.display.flip()
            self.clock.tick(FPS)
        self.quit()

    def handle_events(self):
        for event in pygame.event.get():
            # logger event
            #self.logger.info(event)
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass  # Lógica de actualización del juego aquí

    def draw(self):
        self.screen.fill((0, 0, 0))  # Dibuja en la pantalla aquí

    def draw_title_screen(self):
        #self.screen.fill((0, 0, 0))  # Draw title screen menu
        # Blitea la imagen de fondo
        self.screen.blit(self.background_image, (0, 0))

        for i, option in enumerate(self.menu_options):
            color = (255, 255, 255) if i == self.current_option else (100, 100, 100)
            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(self.width / 2, self.height / 2 + i * 100))
            self.screen.blit(text, text_rect)


    def quit(self):
        pygame.quit()
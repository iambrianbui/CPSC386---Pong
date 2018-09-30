import pygame.font


class Scoreboard:

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #  Font
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #  Prepare the HUD
        self.prep_score(ai_settings)

    #  Prepare the score on both sides
    def prep_score(self, ai_settings):
        p1score_str = str(self.stats.p1score)
        p2score_str = str(self.stats.p2score)

        self.p1score_image = self.font.render(p1score_str, True, self.text_color, self.ai_settings.bg_color)
        self.p2score_image = self.font.render(p2score_str, True, self.text_color, self.ai_settings.bg_color)

        #  Display the score at the top center
        self.p1score_rect = self.p1score_image.get_rect()
        self.p1score_rect.y = 20
        self.p1score_rect.x = (ai_settings.screen_width/2) - 64

        self.p2score_rect = self.p2score_image.get_rect()
        self.p2score_rect.y = 20
        self.p2score_rect.x = (ai_settings.screen_width/2) + 64

    #  Actually display the score
    def show_score(self):
        self.screen.blit(self.p1score_image, self.p1score_rect)
        self.screen.blit(self.p2score_image, self.p2score_rect)
        self.dashed_line()

    def dashed_line(self):
        pygame.draw.line(self.screen, self.text_color, [600, 0], [600, 800], 3)



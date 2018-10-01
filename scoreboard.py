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
        self.bg = (0, 0, 0)

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

        self.rect = pygame.Rect(0, 0, 128, 64)
        self.rect.center = [self.screen_rect.centerx, self.screen_rect.bottom - 64]

        msg = "Play to " + str(self.ai_settings.score_limit)

        self.put_image = self.font.render(msg, True, self.text_color, self.bg)
        self.put_image_rect = self.put_image.get_rect()
        self.put_image_rect.center = self.rect.center

        self.screen.fill(self.bg, self.rect)
        self.screen.blit(self.put_image, self.put_image_rect)



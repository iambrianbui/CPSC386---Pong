import pygame.ftfont


class TitleScreen:

    def __init__(self, ai_settings, screen, msg):
        #  Init button attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #  Set the dimensions and properties of the button
        self.width, self.height = 250, 64
        self.title_color = (0, 100, 50)
        self.white = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 72)
        self.smallfont = pygame.font.SysFont(None, 48)

        #  Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = [self.screen_rect.centerx, self.screen_rect.centery - 200]

        #  Difficulty text
        self.diffrect = pygame.Rect(0, 0, 196, 64)
        self.diffrect.center = [self.screen_rect.centerx - 300, self.screen_rect.centery + 100]

        self.easyrect = pygame.Rect(0, 0, 128, 64)
        self.easyrect.center = [self.screen_rect.centerx - 138, self.screen_rect.centery + 100]

        self.medrect = pygame.Rect(0, 0, 128, 64)
        self.medrect.center = [self.screen_rect.centerx - 10, self.screen_rect.centery + 100]

        self.hardrect = pygame.Rect(0, 0, 128, 64)
        self.hardrect.center = [self.screen_rect.centerx + 118, self.screen_rect.centery + 100]

        self.vrect = pygame.Rect(0, 0, self.width, self.height)
        self.vrect.center = [self.screen_rect.centerx, self.screen_rect.centery]

        #  Play upto
        self.playuptorect = pygame.Rect(0, 0, 196, 64)
        self.playuptorect.center = [self.screen_rect.centerx - 300, self.screen_rect.centery + 200]

        self.put5rect = pygame.Rect(0, 0, 128, 64)
        self.put5rect.center = [self.screen_rect.centerx - 138, self.screen_rect.centery + 200]

        self.put9rect = pygame.Rect(0, 0, 128, 64)
        self.put9rect.center = [self.screen_rect.centerx - 10, self.screen_rect.centery + 200]

        self.put15rect = pygame.Rect(0, 0, 128, 64)
        self.put15rect.center = [self.screen_rect.centerx + 118, self.screen_rect.centery + 200]

        self.put21rect = pygame.Rect(0, 0, 128, 64)
        self.put21rect.center = [self.screen_rect.centerx + 246, self.screen_rect.centery + 200]

        self.prep_msg(msg, "Difficulty: ", "Easy", "Medium", "Hard", "Play up to:  ", "5", "9", "15", "21")

    def prep_msg(self, msg, diff, easy, med, hard, put, put5, put9, put15, put21):
        #  Turn the msg into a rendered image and center the text
        self.msg_image = self.font.render(msg, True, self.white, self.title_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

        self.diff_image = self.smallfont.render(diff, True, self.white, self.title_color)
        self.diff_image_rect = self.diff_image.get_rect()
        self.diff_image_rect.center = self.diffrect.center

        self.easy_image = self.smallfont.render(easy, True, self.white, self.title_color)
        self.easy_image_rect = self.easy_image.get_rect()
        self.easy_image_rect.center = self.easyrect.center

        self.med_image = self.smallfont.render(med, True, self.white, self.title_color)
        self.med_image_rect = self.med_image.get_rect()
        self.med_image_rect.center = self.medrect.center

        self.hard_image = self.smallfont.render(hard, True, self.white, self.title_color)
        self.hard_image_rect = self.hard_image.get_rect()
        self.hard_image_rect.center = self.hardrect.center

        self.put_image = self.smallfont.render(put, True, self.white, self.title_color)
        self.put_image_rect = self.put_image.get_rect()
        self.put_image_rect.center = self.playuptorect.center

        self.put5_image = self.smallfont.render(put5, True, self.white, self.title_color)
        self.put5_image_rect = self.put5_image.get_rect()
        self.put5_image_rect.center = self.put5rect.center

        self.put9_image = self.smallfont.render(put9, True, self.white, self.title_color)
        self.put9_image_rect = self.put9_image.get_rect()
        self.put9_image_rect.center = self.put9rect.center

        self.put15_image = self.smallfont.render(put15, True, self.white, self.title_color)
        self.put15_image_rect = self.put15_image.get_rect()
        self.put15_image_rect.center = self.put15rect.center

        self.put21_image = self.smallfont.render(put21, True, self.white, self.title_color)
        self.put21_image_rect = self.put21_image.get_rect()
        self.put21_image_rect.center = self.put21rect.center

    def draw_title(self):
        #  Draw blank button and then draw message
        self.screen.fill(self.title_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

        self.screen.fill(self.title_color, self.diffrect)
        self.screen.blit(self.diff_image, self.diff_image_rect)

        self.screen.fill(self.title_color, self.easyrect)
        self.screen.blit(self.easy_image, self.easy_image_rect)

        self.screen.fill(self.title_color, self.medrect)
        self.screen.blit(self.med_image, self.med_image_rect)

        self.screen.fill(self.title_color, self.hardrect)
        self.screen.blit(self.hard_image, self.hard_image_rect)

        self.screen.fill(self.title_color, self.playuptorect)
        self.screen.blit(self.put_image, self.put_image_rect)

        self.screen.fill(self.title_color, self.put5rect)
        self.screen.blit(self.put5_image, self.put5_image_rect)

        self.screen.fill(self.title_color, self.put9rect)
        self.screen.blit(self.put9_image, self.put9_image_rect)

        self.screen.fill(self.title_color, self.put15rect)
        self.screen.blit(self.put15_image, self.put15_image_rect)

        self.screen.fill(self.title_color, self.put21rect)
        self.screen.blit(self.put21_image, self.put21_image_rect)

    def show_victory(self, winnermsg):
        self.victory_image = self.font.render(winnermsg, True, self.white, self.title_color)
        self.victory_image_rect = self.victory_image.get_rect()
        self.victory_image_rect.center = self.vrect.center

        self.screen.fill(self.title_color, self.vrect)
        self.screen.blit(self.victory_image, self.victory_image_rect)

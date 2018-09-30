import pygame


class P2Paddle():

    def __init__(self, ai_settings, screen):
        super(P2Paddle, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #  Load the paddle image and get its rect
        self.image = pygame.image.load('images/paddle.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right - 64

        self.center = float(self.rect.centery)

        #  Load the upper and lower paddles and get its rect
        self.upimage = pygame.image.load('images/wallpaddle.png')
        self.uprect = self.upimage.get_rect()

        self.uprect.centerx = self.screen_rect.centerx + (ai_settings.screen_width / 4)
        self.uprect.top = self.screen_rect.top + 32

        self.downimage = pygame.image.load('images/wallpaddle.png')
        self.downrect = self.downimage.get_rect()

        self.downrect.centerx = self.screen_rect.centerx + (ai_settings.screen_width / 4)
        self.downrect.top = self.screen_rect.bottom - 32

        self.upcenter = float(self.uprect.centerx)
        self.downcenter = float(self.downrect.centerx)

        #  Movement flag
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.upimage, self.uprect)
        self.screen.blit(self.downimage, self.downrect)

    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.paddle_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.paddle_speed_factor
        if self.moving_right and self.uprect.right < self.screen_rect.centerx:
            self.upcenter += self.ai_settings.paddle_speed_factor
            self.downcenter += self.ai_settings.paddle_speed_factor
        if self.moving_left and self.uprect.left > self.screen_rect.left:
            self.upcenter -= self.ai_settings.paddle_speed_factor
            self.downcenter -= self.ai_settings.paddle_speed_factor

        self.rect.centery = self.center
        self.uprect.centerx = self.upcenter
        self.downrect.centerx = self.downcenter

    def ai_update(self, ai_settings, ball):
        if ball.y < self.rect.y and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.paddle_speed_factor * (ai_settings.ai_difficulty - 0.1)
        if ball.y > self.rect.y and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.paddle_speed_factor * (ai_settings.ai_difficulty - 0.1)
        if ball.x > self.uprect.x and self.uprect.right < self.screen_rect.right:
            self.upcenter += self.ai_settings.paddle_speed_factor * ai_settings.ai_difficulty
            self.downcenter += self.ai_settings.paddle_speed_factor * ai_settings.ai_difficulty
        if ball.x < self.uprect.x and self.uprect.left > self.screen_rect.centerx:
            self.upcenter -= self.ai_settings.paddle_speed_factor * ai_settings.ai_difficulty
            self.downcenter -= self.ai_settings.paddle_speed_factor * ai_settings.ai_difficulty

        self.rect.centery = self.center
        self.uprect.centerx = self.upcenter
        self.downrect.centerx = self.downcenter

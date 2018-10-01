class Settings:

    def __init__(self):
        #  Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        #  Paddle settings
        self.paddle_speed_factor = 1

        #  AI Paddle tracking speed
        #  0.7 = Easy, 0.9 = Medium, 1.0 = Hard
        self.ai_difficulty = 0.9

        #  Ball settings
        self.ball_speed_factor = 1
        self.ball_width = 16
        self.ball_height = 16
        self.ball_color = 255, 255, 255

        #  Ball direction
        self.ball_x_direction = -1              # 1 = moving to the right
        self.ball_y_direction = 1               # 1 = moving down

        #  Max score
        self.score_limit = 15

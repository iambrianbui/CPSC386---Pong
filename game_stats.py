class GameStats:

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        #  Set the game to active
        self.game_active = False
        self.victor = ""

    def reset_stats(self):
        self.p1score = 0
        self.p2score = 0
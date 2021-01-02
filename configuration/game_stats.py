class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        self.high_score = 0
        # 游戏活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化状态"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

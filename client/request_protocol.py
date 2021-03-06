from config import *


class RequestProtocol(object):

    @staticmethod
    def request_login_result(username, password):
        """0001|user1|myPass """
        return DELIMITER.join([REQUEST_LOGIN, username, password])

    @staticmethod
    def request_register_result(username, password):
        """0002|user1|myPass """
        return DELIMITER.join([REQUEST_REGISTER, username, password])

    @staticmethod
    def request_show_rule_result():
        """0003"""
        return DELIMITER.join([REQUEST_SHOW_RULE])

    @staticmethod
    def request_play_game_result():
        """0004"""
        return DELIMITER.join([REQUEST_PLAY_GAME])

    @staticmethod
    def request_send_score(score):
        """0006|myScore"""
        return DELIMITER.join([REQUEST_SEND_SCORE, score])

    @staticmethod
    def request_high_scores():
        """0007"""
        return DELIMITER.join([REQUEST_HIGH_SCORES])

    @staticmethod
    def request_send_difficulty(difficulty):
        """0008"""
        return DELIMITER.join([REQUEST_SEND_DIFFICULTY, difficulty])
    

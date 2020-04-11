import os

class score_handler():
    def __init__(self):
        self.high_scores = self.read_scores_from_file()

    def is_high_score(self, new_score):
        pass

    def get_high_scores(self):
        pass
    
    def format_high_scores(self, scores_count_to_keep=5):
        l = [15,2,0,150,3,7]
        l.sort(reverse=True)
        l = l[:scores_count_to_keep]
        print(l)

    def read_scores_from_file(self, filename = "game_saves/high_scores.bear"):
        pass

    def write_scores_to_file(self, scores, write_mode = "w", filename = "game_saves/high_scores.bear"):
        pass


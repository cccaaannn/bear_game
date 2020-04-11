import os
class score_handler():
    def __init__(self, scores_count_to_use=5, save_path = "game_saves/high_scores.bear"):
        self.scores_count_to_use = scores_count_to_use
        self.save_path = save_path
        
        self.high_scores = []
        self.__read_scores_from_file()

    def is_best_score(self, new_score):
        if(new_score > self.high_scores[0]):
            return True
        else:
            return False

    def get_high_scores(self):
        return self.high_scores

    def check_and_add_new_score(self, new_score):
        self.high_scores.append(new_score)
        self.high_scores = sorted(self.high_scores,reverse = True)[:self.scores_count_to_use]
        self.__write_scores_to_file(self.high_scores)

    def __read_scores_from_file(self):
        """read scores from file and pad with zeros if not exists return zeros"""
        try:
            with open(self.save_path,'r', encoding='utf-8') as file:
                scores = file.read()

            scores = scores.split()
            self.high_scores = [int(score) for score in scores]

            # pad with zero
            if(len(self.high_scores) > self.scores_count_to_use):
                self.high_scores = sorted(self.high_scores,reverse = True)[:self.scores_count_to_use]
            elif(len(self.high_scores) < self.scores_count_to_use):
                for i in range(self.scores_count_to_use):
                    self.high_scores.append(0)
                self.high_scores = sorted(self.high_scores, reverse = True)[:self.scores_count_to_use]

        # return full zeros if error occurs
        except (OSError, IOError) as e:
            self.high_scores = []
            for i in range(self.scores_count_to_use):
                self.high_scores.append(0)


    def __write_scores_to_file(self, scores, write_mode = "w"):
        
        # create path 
        only_save_path, _ = os.path.split(self.save_path)
        if(not os.path.exists(only_save_path)):
            os.makedirs(only_save_path)
        
        # write to file
        try:
            with open(self.save_path, write_mode, encoding='utf-8') as file:
                for score in scores:
                    file.write(str(score))
                    file.write("\n")
        except (OSError, IOError) as e:
            print(e, "COULD NOT WRITE HIGH SCORES")




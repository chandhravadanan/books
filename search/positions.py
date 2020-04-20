
class WordPositions:
    
    def __init__(self, pos):
        self.pos_list = [pos]

    def append(self, pos):
        self.pos_list.append(pos)

    def word_count(self):
        return len(self.pos_list)

    def get_positions(self):
        return self.pos_list
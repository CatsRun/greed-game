from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!


class Artifact(Actor):
    """ Add comment here*********
    """
    def __init__(self):
        super().__init__()
        # self._message = ''
        self._position = 0

    # def set_message(self, message):
    #     self._message = message

    # def get_message(self):
    #     return self._message


    #artifact calculate score based on what it is
    def calculate_points(self):
        points = 0

        if (self.get_text() == '*'):
            points = 1
        else:
            points = -1
        
        return points

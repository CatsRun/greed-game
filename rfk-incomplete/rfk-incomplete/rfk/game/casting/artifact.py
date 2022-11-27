from game.casting.actor import Actor

class Artifact(Actor):
    """Calculates points based on what object is gathered.

    This class is child to Actor class.

    Attributes:
        _position
    """
    def __init__(self):
        super().__init__()        
        

    #artifact calculate score based on what it is
    def calculate_points(self):
        points = 0

        if (self.get_text() == '*'):
            points = 1
        else:
            points = -1
        
        return points

class Init():
    def __init__(self, animation):
        self.animation = animation

    def register(self, callback):
        callback(self)

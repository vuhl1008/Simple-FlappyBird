from Pipe import Pipe

class ListPipe(list):

    def __init__(self):
        super().__init__()


    def append(self,pipe):
        super().append(pipe)
       # print(len(self.pipes))


    def move_pipe(self):
        for pipe in self:
            pipe.move()

    def draw_pipes(self,screen):
        for pipe in self:
            pipe.draw(screen)


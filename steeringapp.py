from MathLib import Vector2
import pygame
from agent import Agent
import constants


from gametemplate import GameTemplate


class SteeringApp(GameTemplate):
    
    '''need documentation'''

    def __init__(self, name):
        '''need documentation'''
        super(SteeringApp, self).__init__()
        self._name = name
        self._gameobjects = []
        self.targetagent = Agent(Vector2(0,0), 0 )
        self._func = None

    def addtobatch(self, gameobject):
        '''need documentation'''
        self._gameobjects.append(gameobject)

    def update(self):
        '''need documentation'''
        if not super(SteeringApp, self)._update():
            return False 
        for gameobject in self._gameobjects:
            gameobject.update(self._deltatime, self.targetagent)
        return True

    def draw(self):
        '''draw all gameobjects added to this game'''
        self._background.fill((255, 255, 255))

        super(SteeringApp, self)._draw()
        for gameobject in self._gameobjects:
            if gameobject._choice_ is 1:
                super(SteeringApp, self).draw_text("s = Seek \n")

            if gameobject._choice_ is 2:
                super(SteeringApp, self).draw_text("F = Flee \n")

            if gameobject._choice_ is 3:
                super(SteeringApp, self).draw_text("w = Wander \n")
            pygame.draw.circle(self._screen, constants.BLACK, [int(gameobject.position.GetX()), int(gameobject.position.GetY())], 40)
    def run(self):
        '''need documentation'''
        if super(SteeringApp, self)._startup():
            while self.update():
                for event in self._events:
                    if event.type == pygame.KEYDOWN:
                        if pygame.key.get_pressed()[pygame.K_s]:
                            for gameobject in self._gameobjects:
                                gameobject._choice_ = 1
                            print "S KEY PRESSED"
                            self.draw_text("SEEKING")
                        if pygame.key.get_pressed()[pygame.K_w]:
                            for gameobject in self._gameobjects:
                                gameobject._choice_ = 3
                                print "W KEY PRESSED"
                                self.draw_text("WANDERING")
                        if pygame.key.get_pressed()[pygame.K_f]:
                            for gameobject in self._gameobjects:
                                gameobject._choice_ = 2
                            print "F KEY PRESSED"
                            self.draw_text("FLEEING")
                        if pygame.key.get_pressed()[pygame.K_i]:
                            for gameobject in self._gameobjects:
                                gameobject._choice_ = 0
                            print "S KEY PRESSED"
                        if pygame.key.get_pressed()[pygame.K_SPACE]:
                            self.addtobatch(Agent(Vector2(0,0), 100))
                self.targetagent.position = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                self.draw()
        super(SteeringApp, self)._shutdown()

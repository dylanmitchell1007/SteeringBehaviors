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
        self.targetagent = Agent(Vector2(0, 0), 0)
        self._func = None
        self._agentmode = 0
        self.helpbar = pygame.font.Font(None, 44)

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
        self._background.fill((0, 0, 0))
        # self.draw_text("I = Idle, F = Flee, W = Wander, S = Seek")

        letmesee = self.helpbar.render(
            "I = Idle  |  F = Flee  |  W = Wander  |  S = Seek  |  Esc = Exit", 0, (0, 255, 0))
        self._screen.blit(letmesee, (0, 0))

        
        if self._agentmode is 1:
            super(SteeringApp, self).draw_text("S = Seek (Selected)")
        if self._agentmode is 2:
            super(SteeringApp, self).draw_text("F = Flee (Selected)")
        if self._agentmode is 3:
            super(SteeringApp, self).draw_text("W = Wander (Selected)")
        if self._agentmode is 0:
            super(SteeringApp, self).draw_text("I = Idle (Selected)")
        if self._agentmode is 4:
            super(SteeringApp, self).draw_text("Agent Spawned!")
        for gameobject in self._gameobjects:
            gameobject.draw(self._screen)

        super(SteeringApp, self)._draw()

    def run(self):
        '''need documentation'''

        if super(SteeringApp, self)._startup():
            while self.update():
                for event in self._events:
                    if event.type == pygame.KEYDOWN:
                        if pygame.key.get_pressed()[pygame.K_s]:
                            self._agentmode = 1
                            self.draw_text("SEEKING")
                        if pygame.key.get_pressed()[pygame.K_w]:
                            self._agentmode = 3
                            self.draw_text("WANDERING")
                        if pygame.key.get_pressed()[pygame.K_f]:
                            self._agentmode = 2
                            self.draw_text("FLEEING")
                        if pygame.key.get_pressed()[pygame.K_i]:
                            self._agentmode = 0
                        if pygame.key.get_pressed()[pygame.K_t]:
                            self._agentmode = 3
                        if pygame.key.get_pressed()[pygame.K_SPACE]:
                            self.addtobatch(Agent(Vector2(500, 500), 100))

                for gameobject in self._gameobjects:
                    gameobject._choice_ = self._agentmode
                self.targetagent.position = Vector2(
                    pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                self.draw()
        super(SteeringApp, self)._shutdown()

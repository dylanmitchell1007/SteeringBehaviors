'''game.py'''

import pygame
from constants import *


class GameTemplate(object):
    '''pygame object'''

    def __init__(self):
        '''abc'''
        self._name = ""
        pygame.display.init()
        pygame.font.init()
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._clock = pygame.time.Clock()
        self._fps = 60
        self._playtime = 0.0
        self._background = pygame.Surface(
            (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

        self._background.fill((255, 255, 255))
        self._gamestates = {}
        self._gamestates["init"] = ["running"]
        self._gamestates["running"] = ["pause", "quit"]
        self._gamestates["pause"] = ["running", "quit"]
        self._gamestates["quit"] = []
        self._currentstate = "init"
        self._events = pygame.event.get()
        self.font = pygame.font.SysFont('mono', 24, bold=True)
        self._deltatime = 0.0

    def _set_state(self, value):
        '''set state of the game'''
        if value in self._gamestates[self._currentstate]:
            print "newstate =>", self._currentstate, "to", value
            self._currentstate = value
        else:
            print "can not go from ", self._currentstate, "to", value

    def _get_state(self):
        return self._currentstate

    gamestate = property(_get_state, _set_state)

    def _startup(self):
        pygame.display.set_caption(self._name)
        self._set_state("running")
        return True

    def _update(self):
        '''input and time'''
        if self._get_state() == "quit":
            return False
        milliseconds = self._clock.tick(self._fps)
        self._deltatime = milliseconds / 1000.0
        self._playtime += self._deltatime
        self._events = pygame.event.get()
        for event in self._events:
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.constants.K_e]:
                    self.gamestate = "pause"
                if keystate[pygame.constants.K_r]:
                    self.gamestate = "running"
                if keystate[pygame.constants.K_ESCAPE]:
                    self._set_state("quit")
            if event.type == pygame.constants.QUIT:
                self._set_state("quit")

        return True

    def _draw(self):
        '''need docstring'''
        self.draw_text("FPS: {:6.6}{}PLAYTIME: {:6.6} SECONDS".format(
            self._clock.get_fps(), " " * 5, self._playtime))

        pygame.display.flip()
        self._screen.blit(self._background, (0, 0))

    def _shutdown(self):
        '''shutdown the game properly'''
        pygame.quit()

    def draw_text(self, text):
        """Center text in window"""
        surface = self.font.render(text, True, (0, 0, 0))
        self._screen.blit(surface, (25, 25))
from pygame.sprite import Sprite as sp
import os.path
import pygame.image


class Entity(sp):
    def __init__(self, path: str, x: float, y: float, width: int, height: int, max_hp: int) -> None:
        super().__init__()
        self._x = x
        self._y = y 
        self._width = width
        self._height = height
        self._max_hp = max_hp
        
        # ATRIBUTOS DE ANIMACAO
        self._animation = []
        self._blit_animation(path)
        self._index = 0
        self._tick_anim = 0
        self._sum_tick = 0.3
            # ATRIBUICAO E MANIPULACAO DE SPRITES
        self.image = self._animation[self._index]
                # REDIMENSIONANDO SPRITE
        self.image = pygame.transform.scale(self.image, (self._width*2,self._height*2))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self) -> None:
        print('UPDATE DA ENTIDADE')
        
    def render(self) -> None:
        self._animate()
        print('RENDER DA ENTIDADE')
        pygame.display.get_surface().blit(self.image, self.rect)
        
    def _animate(self):
        self._tick_anim += self._sum_tick
        if self._tick_anim >= 1:
            self._tick_anim = 0
            if self._index + 1 < len(self._animation):
                self._index += 1
            else:
                self._index = 0
            self.image = self._animation[self._index]
            self.image = pygame.transform.scale(self.image, (self._width*2,self._height*2))
            self.mask = pygame.mask.from_surface(self.image)
        
    def _blit_animation(self, path) -> None:
        pre_path = 'CAMINHO PARA A PASTA DO SPRITESHEET'
        pre_path = os.path.join(pre_path,'MONTAGEM DO CAMINHO')
        path = os.path.join(pre_path, path)
        
        try:
            self.sprite = pygame.image.load(path).convert_alpha()
            wid = int(self.sprite.get_width()/self._width)
            for i in range(wid):
                self.animation.append(self.sprite.subsurface((self._width*i,0),(self._width, self._height)))
        except Exception as e:
            print(e)
            exit()

    def set_pos(self, x, y):
        self.__x = x
        self.__y = y
        self.rect.topleft = self.__x,self.__y

    def get_x(self) -> float:
        return self._x
    
    def get_width(self) -> int:
        return self._width
    
    def get_y(self) -> float:
        return self._y
            
    def get_hp(self) -> int:
        return self._hp
    
    def get_max_hp(self) -> int:
        return self._max_hp
            
    
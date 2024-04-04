import pygame


class GameLoop:
    
    def __init__(self) -> None:
        self.__width = 800
        self.__height = 600
        
        self.__screen = pygame.display.set_mode((self.__width,self.__height))
        pygame.display.set_caption('LOL_Clone')
        
        self.__in_loop = True
        self.__fps = 60
        self.__bg_color = (0,0,0)
        self.__clock = pygame.time.Clock()
        
        # EXEMPLO DE SOM
        self.__hit_ost = pygame.mixer.Sound("assets/sounds/effects/Hit_Hurt4.wav")
        self.__hit_ost.set_volume(0.3)
        
    def main_loop(self):
        while self.__in_loop:
            self.__update()
            self.__render()
        
    def __update(self):
        self.__clock.tick(self.__fps)
        #BLOCO DE COMANDS DE UPDATE
        self.__get_input()
    
    def __render(self):
        self.__screen.fill(self.__bg_color)
        #BLOCO DE COMANDOS DE RENDER
        pygame.display.update()
        
    def __get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__in_loop = False
                quit()
        keys = pygame.key.get_pressed()
        self.__get_key_down(keys)
        
    def __get_key_down(self, keys):
        if keys[pygame.K_a]:
            print('Botao pressionado "A"')
from PIL import Image


class NewLevel:
    
    def __init__(self, path: str) -> None:
        self.general_path = path
        self.sprite = ''
        self.get_level_map()
        self.tile_list = []
        # ERASE THIS BELOW
        self.enemy_list = []
        
    def get_level_map(self):
        try:
            self.sprite = Image.open(self.general_path).convert('RGB')
        except Exception as e:
            print(e)
            exit()
        
    # FUNCAO QUE CRIA UMA LISTA DE TILES QUE FORMARAO O MAPA DO JOGO
    def create_level_map(self):
        width = self.sprite.width
        height = self.sprite.height
        
        try:
            for y in range(height):
                for x in range(width):
                    pixel = self.get_pixel_color(x,y)
                    if pixel == {255}:
                        print("COR PRETA")
                    elif pixel == {151,138}:
                        print('COR BRANCA')
                        #self.tile_list.append(WallForest(x * 64, y * 64, 64, 64,'wall_forest.png'))
                    elif pixel == {91, 110, 225}:
                        print("COR AZUL")      
                    
        except Exception as e:
            print(e)
            exit()
        return self.tile_list
    
    #FUNCAO QUE CRIA A LISTA DE INIMIGOS
    def enemy_list_temp(self):
        width = self.sprite.width
        height = self.sprite.height
        
        try:
            for y in range(height):
                for x in range(width):
                    pixel = self.get_pixel_color(x,y)
                    if pixel == {208, 29}:
                        print("CRIACAO DE INIMIGOS POR COR")
                        # self.enemy_list.append(Slime(x*64, y*64))       
                    
        except Exception as e:
            print(e)
            exit()
        return self.enemy_list

    # FUNCAO QUE IDENTIFICA A COR DO PIXEL
    def get_pixel_color(self, x, y):
        r, g, b = self.sprite.getpixel((x,y))
        return {r, g, b}

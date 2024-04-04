import pygame.display


class Camera:
    
    def __init__(self) -> None:
        self.offset = pygame.math.Vector2()
        self.x = 10
        self.y = 10
        self.world_width = 0
        self.tmp_w = 0
        self.world_height =0
        self.tmp_h = 0 
    
    # EXEMPLO DE USO DA CAMERA PARA RENDERIZAR AS ENTIDADES DO JOGO
    def render(self, player, tiles, enemys):
        self.center_camera(player)
        osffset_pos = (player.x - self.offset.x, player.y - self.offset.y)
        player.make_offset(osffset_pos)
        if enemys:
            for enemy in enemys:
                enemy.make_offset(osffset_pos)
        for tile in tiles:
            tile.make_offset(self.offset)
            self.verify_world_size(tile)
    
    # FUNCAO PARA VERIFICAR O TAMANHO MAXIMO DO MUNDO PELOS TILES 
    def verify_world_size(self,tile):
        if not self.world_width:
                if self.tmp_w <= tile.x:
                    self.tmp_w = tile.x
                else:
                    self.world_width = self.tmp_w + 64
        if not self.world_height:
            if self.tmp_h <= tile.y:
                self.tmp_h = tile.y
            else:
                self.world_height = self.tmp_h +100
    
    # FUNCAO PARA CENTRALIZAR A CAMERA NO JOGADOR SEM SAIR DAS BORDAS DO MUNDO
    def clamp_camera(self, x_atual, x_min, x_max):
        if x_atual < x_min:
            x_atual = x_min
        if x_atual > x_max:
            x_atual = x_max
        return x_atual
    
    # FUNCAO PARA CENTRALIZAR A CAMERA NO JOGADOR
    def center_camera(self, player):
        self.offset.x = self.clamp_camera((player.x - (pygame.display.get_surface().get_width()/2)),0,(self.world_width)-pygame.display.get_surface().get_width())
        self.offset.y = self.clamp_camera((player.y - (pygame.display.get_surface().get_height()/2)),0,(self.world_height)-pygame.display.get_surface().get_height())
        
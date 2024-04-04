

class Collision:
    
    #EXEMPLO DE COLISAO DE PIXEL PERFECT ENTRE UMA ENTIDADE E UMA LISTA DE ENTIDADES
    def entities_collision(self, entity, entities):
        for e in entities:
            if e.mask.overlap(entity.mask,(entity.rect[0]-e.rect[0],entity.rect[1]-e.rect[1])):
                return True
        return False
    
    #EXEMPLO DE COLISAO DE PIXEL PERFECT ENTRE DUAS ENTIDADES
    def single_entities_collision(self, entity1, entity2):
        if entity1.mask.overlap(entity2.mask,(entity2.rect[0]-entity1.rect[0],entity2.rect[1]-entity1.rect[1])):
            return True
        return False
    
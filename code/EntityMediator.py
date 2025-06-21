# Módulo que gerencia as interações entre os objetos do jogo como as colisões

from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Explosion import Explosion
from code.Player import Player
from code.PlayerShot import PlayerShot

class EntityMediator:
    # Método estático que verifica colisões entre entidades e com as bordas da janela
    @staticmethod
    def verify_collision(entity_list: list[Entity], sounds):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2, sounds)

    # Método estático que verifica se a entidade saiu da tela e marca para remoção se necessário
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    # Método estático que verifica colisão entre duas entidades específicas e aplica dano
    @staticmethod
    def __verify_collision_entity(ent1, ent2, sounds):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name
                sounds['damage'].play()

    # Método estático que atribui pontuação ao jogador que causou o dano final no inimigo
    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    # Método estático que verifica a vida das entidades, remove as com vida zero e cria explosão
    @staticmethod
    def verify_health(entity_list: list[Entity], sounds):
        for ent in entity_list[:]:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                # Adição da explosão na posição central da entidade
                explosion = Explosion(f'Explosion{ent.name}', ent.rect.center)
                entity_list.append(explosion)
                entity_list.remove(ent)
                sounds['explosion'].play()
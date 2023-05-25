""" Program that creates waves of enemies for the game. Bing chilling"""
from config.settings.general_config import Spawn_probs, Special_waves, Wave_function

from random import choices

def create_wave(wave_function:Wave_function , wave:int) -> list:
    """ Create a wave of enemies"""
    number_of_enemies = int(wave_function(wave))
    enemies = []
    if wave in Special_waves.boss_wave:
        wave_difficulty = Spawn_probs.only_boss
    elif wave in Special_waves.camo_wave:
        wave_difficulty = Spawn_probs.only_camo
    elif wave in Special_waves.speedrun_wave:
        wave_difficulty = Spawn_probs.casual_speeder
    elif wave in Special_waves.hard_wave:
        wave_difficulty = Spawn_probs.hard
    elif wave < 10:
        wave_difficulty = Spawn_probs.only_casual
    elif wave < 20:
        wave_difficulty = Spawn_probs.casual_speeder
    elif wave < 30:
        wave_difficulty = Spawn_probs.normal
    elif wave < 40:
        wave_difficulty = Spawn_probs.hard
    elif wave < 50:
        wave_difficulty = Spawn_probs.harder
    else:
        wave_difficulty = Spawn_probs.impossible
    
    for i in range(number_of_enemies): # je potřeba tenhle loop? 
        for enemy_type in wave_difficulty:
            for j in range(int(number_of_enemies*wave_difficulty[enemy_type])):
                enemies.append(enemy_type)

    #print("Enemies: ", enemies, 2*"\n")
    return choices(enemies, k=number_of_enemies)
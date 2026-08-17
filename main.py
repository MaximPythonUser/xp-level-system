DEFAULT_LEVEL_EXPERIENCE = 200


def is_leveled_up(current_experience: int, gained_experience: int ) -> bool:
    #Проверяет хватает ли опыта для повышения уровня

    total_experience = current_experience + gained_experience
    level_up = False

    if total_experience >= DEFAULT_LEVEL_EXPERIENCE:
       level_up = True

    return level_up


  #Примеры использования
print(is_leveled_up(current_experience=150, gained_experience=60))  #True
print(is_leveled_up(current_experience=10, gained_experience=60))  #False

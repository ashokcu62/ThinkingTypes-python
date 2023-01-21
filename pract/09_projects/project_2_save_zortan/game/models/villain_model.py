from game.schemas.villain import Villain


class VillainModel:
    def __init__(self) -> None:
        self.all:list[Villain]=self._get_all_villains()

    def __str__(self) -> str:
        name:list[str]=[]
        for villan_name in self.all:
            name.append(villan_name.name)
        return f"{name}"

        
    def _get_all_villains(self) -> list[Villain]:
        """Returns a list of all Villains"""
        # Super Villains
        thanos = Villain(name="Thanos", attack_power=400, life=1500)
        redskull = Villain(name="Redskull", attack_power=300, life=800)
        proxima = Villain(name="Proxima", attack_power=320, life=800)

        # All Villains
        villains = [thanos, redskull, proxima]

        return villains


    def get_villain(self,index: int) -> Villain | None:
        """Returns a single villain from the given index"""
        
        if index < len(self.all):
            return self.all[index]
        else:
            return None

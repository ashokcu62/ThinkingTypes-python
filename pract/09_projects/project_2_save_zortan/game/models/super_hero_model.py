from game.schemas.super_hero import SuperHero


class SuperHeroModel:
    def __init__(self) -> None:
        self.all: list[SuperHero] = self._get_all_superheros

    def __str__(self) -> str:
        name:list[str]=[]
        for superhero in self.all:
            name.append(superhero.name)
        return f"{name}"

    def _get_all_superheros(self) -> list[SuperHero]:
        """Return a list of all Superheros"""
        ironman = SuperHero(name="Ironman", attack_power=250, life=1000)
        blackwidow = SuperHero(name="Blackwidow", attack_power=180, life=800)
        spiderman = SuperHero(name="Spiderman", attack_power=190, life=700)
        hulk = SuperHero(name="Hulk", attack_power=300, life=1100)

        # All Superheros
        superheros = [ironman, blackwidow, spiderman, hulk]

        return superheros

    def get_superhero(self, index: int) -> SuperHero | None:
        """Returns superhero from the given index."""
        
        if index < len(self.all):
            return self.all[index]
        else:
            return None

from pyminion.game import Game
from pyminion.expansions.base import copper, mine
from pyminion.players import Human


def test_mine_no_treasures(human: Human, game: Game, monkeypatch):
    human.hand.add(mine)
    human.play(mine, game)
    assert len(game.trash) == 0
    assert len(human.discard_pile) == 0


def test_mine_gain_valid(human: Human, game: Game, monkeypatch):
    human.hand.add(copper)
    human.hand.add(mine)
    assert len(human.discard_pile) == 0
    assert len(game.trash) == 0

    responses = iter(["copper", "silver"])
    monkeypatch.setattr("builtins.input", lambda input: next(responses))

    human.play(mine, game)
    assert len(human.playmat) == 1
    assert human.state.actions == 0
    assert game.trash.cards[0].name == "Copper"
    assert human.hand.cards[-1].name == "Silver"

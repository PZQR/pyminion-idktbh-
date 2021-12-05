from pyminion.bots import OptimizedBot
from pyminion.expansions.base import artisan, silver, village
from pyminion.game import Game
from pyminion.players import Human


def test_artisan_valid_gain_same_topdeck(human: Human, game: Game, monkeypatch):
    human.hand.add(artisan)
    assert len(game.supply.piles[1]) == 40
    assert len(human.hand) == 1

    responses = iter(["silver", "silver"])
    monkeypatch.setattr("builtins.input", lambda input: next(responses))

    human.hand.cards[0].play(human, game)
    assert len(human.hand) == 0
    assert human.deck.cards[-1] is silver
    assert len(human.playmat) == 1
    assert human.state.actions == 0
    assert len(game.supply.piles[1]) == 39


def test_artisan_invalid_gain(human: Human, game: Game, monkeypatch):
    human.hand.add(artisan)
    assert len(game.supply.piles[1]) == 40
    assert len(human.hand) == 1

    responses = iter(["gold", "silver", "silver"])
    monkeypatch.setattr("builtins.input", lambda input: next(responses))

    human.hand.cards[0].play(human, game)
    assert len(human.hand) == 0
    assert human.deck.cards[-1] is silver
    assert len(human.playmat) == 1
    assert human.state.actions == 0
    assert len(game.supply.piles[1]) == 39


def test_artisan_valid_gain_diff_topdeck(human: Human, game: Game, monkeypatch):
    human.hand.add(artisan)
    human.hand.add(artisan)
    assert len(game.supply.piles[1]) == 40
    assert len(human.hand) == 2

    responses = iter(["silver", "artisan"])
    monkeypatch.setattr("builtins.input", lambda input: next(responses))

    human.hand.cards[0].play(human, game)
    assert len(human.hand) == 1
    assert human.deck.cards[-1] is artisan
    assert len(human.playmat) == 1
    assert human.state.actions == 0
    assert len(game.supply.piles[1]) == 39

from pyminion.expansions.base import estate
from pyminion.expansions.seaside import island
from pyminion.game import Game
from pyminion.human import Human
from pyminion.player import Player


def test_island_multiple_cards(human: Human, game: Game, monkeypatch):
    assert len(human.hand) == 0
    assert human.get_victory_points() == 3

    human.hand.add(island)
    human.hand.add(island)
    human.hand.add(estate)
    assert human.get_victory_points() == 8

    responses = ["estate"]
    monkeypatch.setattr("builtins.input", lambda _: responses.pop(0))

    human.play(island, game)
    assert len(responses) == 0
    assert human.state.actions == 0
    assert len(human.playmat) == 0
    mat = human.get_mat("Island")
    assert len(mat) == 2
    mat_names = set(card.name for card in mat)
    assert "Island" in mat_names
    assert "Estate" in mat_names
    assert human.get_victory_points() == 8


def test_island_one_card(player: Player, game: Game, monkeypatch):
    player.hand.add(island)
    player.hand.add(estate)
    assert len(player.hand) == 2

    player.play(island, game)
    assert player.state.actions == 0
    assert len(player.playmat) == 0
    mat = player.get_mat("Island")
    assert len(mat) == 2
    mat_names = set(card.name for card in mat)
    assert "Island" in mat_names
    assert "Estate" in mat_names
    assert player.get_victory_points() == 6


def test_island_no_cards(player: Player, game: Game, monkeypatch):
    player.hand.add(island)
    assert len(player.hand) == 1

    player.play(island, game)
    assert player.state.actions == 0
    assert len(player.playmat) == 0
    mat = player.get_mat("Island")
    assert len(mat) == 1
    assert mat.cards[0].name == "Island"
    assert player.get_victory_points() == 5

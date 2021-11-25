from pyminion.game import Game
from pyminion.expansions.base import Bandit, Gold, Silver, bandit, copper, gold, silver


def test_bandit_gains_gold(multiplayer_game: Game):
    player = multiplayer_game.players[0]
    player.hand.add(bandit)
    assert len(player.hand) == 6
    player.hand.cards[-1].play(player, multiplayer_game)
    assert len(player.hand) == 5
    assert len(player.playmat) == 1
    assert type(player.playmat.cards[0]) is Bandit
    assert len(player.discard_pile) == 1
    assert type(player.discard_pile.cards[0]) is Gold
    assert player.state.actions == 0
    assert player.state.money == 0
    assert player.state.buys == 1


def test_bandit_trash_one_silver(multiplayer_game: Game):
    player = multiplayer_game.players[0]
    opponent = multiplayer_game.players[1]
    player.hand.add(bandit)
    opponent.deck.add(silver)
    assert len(opponent.discard_pile) == 0
    assert len(multiplayer_game.trash) == 0
    player.hand.cards[-1].play(player, multiplayer_game)
    assert len(multiplayer_game.trash) == 1
    assert type(multiplayer_game.trash.cards[0]) is Silver
    assert len(opponent.discard_pile) == 1


def test_bandit_trash_silver_over_gold(multiplayer_game: Game):
    player = multiplayer_game.players[0]
    opponent = multiplayer_game.players[1]
    player.hand.add(bandit)
    opponent.deck.add(silver)
    opponent.deck.add(gold)
    assert len(opponent.discard_pile) == 0
    assert len(multiplayer_game.trash) == 0
    player.hand.cards[-1].play(player, multiplayer_game)
    assert len(multiplayer_game.trash) == 1
    assert type(multiplayer_game.trash.cards[0]) is Silver
    assert len(opponent.discard_pile) == 1
    assert type(opponent.discard_pile.cards[0]) is Gold


def test_bandit_discard_two_non_treasure(multiplayer_game: Game):
    player = multiplayer_game.players[0]
    opponent = multiplayer_game.players[1]
    player.hand.add(bandit)
    opponent.deck.add(copper)
    assert len(opponent.discard_pile) == 0
    assert len(multiplayer_game.trash) == 0
    player.hand.cards[-1].play(player, multiplayer_game)
    assert len(multiplayer_game.trash) == 0
    assert len(opponent.discard_pile) == 2

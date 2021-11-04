from pyminion.models.core import Player
from pyminion.game import Game
from pyminion.models.base import Market
from pyminion.expansions.base import market


def test_market(player: Player, game: Game):
    player.hand.add(market)
    assert len(player.hand) == 1
    player.hand.cards[0].play(player, game)
    assert len(player.hand) == 1
    assert len(player.playmat) == 1
    assert type(player.playmat.cards[0]) is Market
    assert player.state.actions == 1
    assert player.state.money == 1
    assert player.state.buys == 2

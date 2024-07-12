from money import Money, Wallet
import calcs, report

class Format:
    pass


def premier_draft_report():
    wins_payout = [Wallet([Money("gems", x)]) for x in [50, 100, 250, 1000, 1400, 1600, 1800, 2200]]
    payout = [ [ wins_payout[w] for _ in range(4) ] for w in range(8) ]
    max_wins = 7
    max_losses = 3
    wr = 0.5
    report.generate_report(payout, lambda wr_in: calcs.chances_max_wins_losses(max_wins, max_losses, wr_in), lambda i, j: i >= max_wins or j >= max_losses)

def premier_draft():
    wins_payout = [Wallet([Money("gems", x)]) for x in [50, 100, 250, 1000, 1400, 1600, 1800, 2200]]
    wins_payout[-1].add(Money("kiss on the lips", 1))
    payout = [ [ wins_payout[w] for _ in range(4) ] for w in range(8) ]
    max_wins = 7
    max_losses = 3
    wr = 0.5
    edge_conditional = lambda i, j: i == max_wins or j == max_losses

    chances = calcs.chances_max_wins_losses(max_wins, max_losses, wr)
    premier_ev = calcs.ev(chances, payout, edge_conditional)
    # wins, losses = calcs.average_wins_losses(chances, edge_conditional)
    # print(premier_ev, wins, losses)
    print(chances, premier_ev)

def traditional_draft():
    wins_payout = [100, 250, 1000, 2500]
    payout = [ [ wins_payout[w] for _ in range(4) ] for w in range(4) ]
    max_games = 3
    wr = 0.5

    chances = calcs.chances_max_matches(max_games, wr)
    traditional_ev = calcs.ev(chances, payout, lambda i, j: i + j == max_games)
    wins, losses = calcs.average_wins_losses(chances, lambda i, j: i + j == max_games)
    # print(traditional_ev, wins, losses)
    print(chances)

    def ev_func(wr):
        chances = calcs.chances_max_matches(max_games, wr)
        premier_ev = calcs.ev(chances, payout, lambda i, j: i + j == max_games)
        return premier_ev - 1500
    app_wr = calcs.approximate_even_ev(ev_func, 0.01)
    # print(app_wr)

def test():
    wins_payout = [50, 100, 250, 1000, 1400, 1600, 1800, 2200]
    payout = [ [ wins_payout[w] for _ in range(4) ] for w in range(8) ]
    max_wins = 7
    max_losses = 3

    def ev_func(wr):
        chances = calcs.chances_max_wins_losses(max_wins, max_losses, wr)
        premier_ev = calcs.ev(chances, payout, lambda i, j: i == max_wins or j == max_losses)
        return premier_ev - 1500

    app_wr = calcs.approximate_even_ev(ev_func, 0.01)

    print(app_wr)

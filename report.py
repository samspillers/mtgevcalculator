import calcs

WRS = [0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7]

def generate_report(payout, chances_func, edge_conditional):
    chances = chances_func(0.5)

    # chances of getting each record if 50% wr
    records = {}
    for i, e in enumerate(chances):
        for j, f in enumerate(e):
            if edge_conditional(i, j):
                records[(i, j)] = f
    print("records", records)

    # evs and average wins for wrs of 30%, 40%, 45%, 50%, 55%, 60%, and 70%
    wr_stats = {}
    for wr in WRS:
        chances = chances_func(wr)
        ev = calcs.ev(chances, payout, edge_conditional)
        wins, losses = calcs.average_wins_losses(chances, edge_conditional)
        wr_stats[wr] = (ev, wins, losses)

    print("wr_stats", wr_stats)

    # wr needed to go even
    pass
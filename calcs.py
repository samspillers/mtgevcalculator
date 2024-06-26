

def chances_max_wins_losses(max_wins: int, max_losses: int, wr: float):
    chances = [ [ 0 for _ in range(max_losses + 1) ] for _ in range(max_wins + 1) ]

     
    old = calc_chances(chances, max_wins + max_losses - 1, wr, lambda wins, losses: wins < max_wins and losses < max_losses)
    new = calc_chances_new(chances, max_wins + max_losses - 1, wr, lambda wins, losses: wins < max_wins and losses < max_losses)
    print("old", old)
    print("new", new)
    return new


def chances_max_matches(max_matches: int, wr: float):
    chances = [ [ 0 for _ in range(max_matches + 1) ] for _ in range(max_matches + 1) ]

    old = calc_chances(chances, max_matches, wr, lambda wins, losses: wins + losses < max_matches)
    new = calc_chances_new(chances, max_matches, wr, lambda wins, losses: wins + losses < max_matches)
    print("old", old)
    print("new", new)
    return new

# Returns chances matrix
def calc_chances(chances: list[list[float]], max_matches: int, wr: float, edge_conditional):
    chances[0][0] = 1

    for games_played in range(max_matches):
        for wins in range(games_played + 1):
            losses = games_played - wins
            if edge_conditional(wins, losses):
                curr_chance = chances[wins][losses]
                chances[wins + 1][losses] += curr_chance * wr
                chances[wins][losses + 1] += curr_chance * (1 - wr)
    
    sanity_check(chances, edge_conditional)
    return chances


# Returns chances matrix
def calc_chances_new(chances: list[list[float]], max_matches: int, wr: float, edge_conditional):
    chances[0][0] = 1

    for diagonal in range (len(chances) + len(chances[0]) - 1):
        for wins in range(diagonal):
            losses = diagonal - wins
            if edge_conditional(wins, losses):
                curr_chance = chances[wins][losses]
                chances[wins + 1][losses] += curr_chance * wr
                chances[wins][losses + 1] += curr_chance * (1 - wr)
    
    sanity_check(chances, edge_conditional)
    return chances

# two parameters should have same dimensions
def ev(chances: list[list[float]], payout: list[list[float]], edge_conditional):
    total_ev = 0
    for i, e in enumerate(chances):
        for j, f in enumerate(e):
            if edge_conditional(i, j):
                total_ev += f * payout[i][j]
    return total_ev


def average_wins_losses(chances: list[list[float]], edge_conditional):
    wins = 0
    losses = 0
    for i, e in enumerate(chances):
        for j, f in enumerate(e):
            if edge_conditional(i, j):
                wins += f * i
                losses += f * j
                # print(i,j, f, wins, losses)
    return wins, losses



# ev_func should take only wr and should already have negative ev included
def approximate_even_ev(ev_func, precision: float):
    min_ev = 0
    max_ev = 1

    while (max_ev - min_ev) / 2 > precision:
        guess = (min_ev + max_ev) / 2
        ev = ev_func(guess)
        if ev > 0:
            max_ev = guess
        elif ev < 0:
            min_ev = guess
        else:
            break
    
    return (min_ev + max_ev) / 2


def sanity_check(chances: list[list[float]], edge_conditional):
    edge = 0
    for i, e in enumerate(chances):
        for j, f in enumerate(e):
            if not edge_conditional(i, j):
                edge += f
    print(chances, edge)
    assert abs(edge - 1) < 0.000001


def print_win_loss_obj(object):
    for i, e in enumerate(object):
        print("wins ", i, ": ", e)
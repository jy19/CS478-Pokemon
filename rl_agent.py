import json

class PokemonState:
    def __init__(self, self_poke, opp_poke):
        self.typing = self_poke.typing
        self.opp_typing = opp_poke.typing
        # todo be able to generalize well..

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

# choose move/switch based on rewards
# move: attack or status
# switch: greedy switch based on type match ups, probably

class RLAgent:
    def __init__(self):
        self.q_vals = {}
        self.actions = []

    def get_q(self, state, action):
        return self.q_vals.get((state, action), 0.0)

    def choose_action(self, state):
        q_values = [self.get_q(state, a) for a in self.actions]
        q = max(q_values)

        a_index = q_values.index(q)
        action = self.actions[a_index]

        return action

# todo learn:
# simulate the move
# give rewards for dmg done, hp gotten, status inflicted on opp or self, stat mods

def get_pokes():
    gen1_mons = []
    with open('data/pokegen1.json') as fn:
        poke_data = json.load(fn)

    for poke in poke_data:
        movesets = [info["moveslots"] for info in poke["strategies"][0]["movesets"]]
        curr_poke = {"name": poke["pokemon"], "moveset": movesets}
        gen1_mons.append(curr_poke)

    return gen1_mons

def main():
    pokemons = get_pokes()


if __name__ == "__main__":
    main()

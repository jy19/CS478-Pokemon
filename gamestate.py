import pickle
from simulator import Action
from type import get_multiplier
from data import MOVES
import logging
import arff

logging.basicConfig()


class GameState:
    def __init__(self, teams):
        self.teams = teams
        self.rocks = [False, False]
        self.spikes = [0, 0]
        self.turn = 0

    def dump(self, path):
        with open(path, 'wb') as fp:
            pickle.dump(self, fp)

    def create_gamestate_arff(self, who):
        user = self.get_team(who)
        opp = self.get_team(1 - who)
        n_user_stats = {k: v / 255.0 for k, v in user.primary().stats.items()}
        n_opp_stats = {k: v / 255.0 for k, v in opp.primary().stats.items()}

        obj = {
            'description': '',
            'relation': 'Game state instance at turn {0}'.format(self.turn),
            'attributes': [('user-type-normal', 'REAL'),
                           ('user-type-grass', 'REAL'),
                           ('user-type-fire', 'REAL'),
                           ('user-type-water', 'REAL'),
                           ('user-type-poison', 'REAL'),
                           ('user-type-bug', 'REAL'),
                           ('user-type-psychic', 'REAL'),
                           ('user-type-ghost', 'REAL'),
                           ('user-type-rock', 'REAL'),
                           ('user-type-ground', 'REAL'),
                           ('user-type-fighting', 'REAL'),
                           ('user-type-flying', 'REAL'),
                           ('user-type-electric', 'REAL'),
                           ('user-type-ice', 'REAL'),
                           ('user-type-dragon', 'REAL'),
                           ('user-baseHP', 'REAL'),
                           ('user-baseattack', 'REAL'),
                           ('user-basedefense', 'REAL'),
                           ('user-basespeed', 'REAL'),
                           ('user-basespecial', 'REAL'),
                           ('user-curHP', 'REAL'),
                           ('user-status-par', 'REAL'),
                           ('user-status-frz', 'REAL'),
                           ('user-status-slp', 'REAL'),
                           ('user-status-brn', 'REAL'),
                           ('user-status-psn', 'REAL'),
                           ('user-attackMod', 'REAL'),
                           ('user-defenseMod', 'REAL'),
                           ('user-speedMod', 'REAL'),
                           ('user-specialMod', 'REAL'),
                           ('user-accuracyMod', 'REAL'),
                           ('user-evasionMod', 'REAL'),
                           ('opponent-type-normal', 'REAL'),
                           ('opponent-type-grass', 'REAL'),
                           ('opponent-type-fire', 'REAL'),
                           ('opponent-type-water', 'REAL'),
                           ('opponent-type-poison', 'REAL'),
                           ('opponent-type-bug', 'REAL'),
                           ('opponent-type-psychic', 'REAL'),
                           ('opponent-type-ghost', 'REAL'),
                           ('opponent-type-rock', 'REAL'),
                           ('opponent-type-ground', 'REAL'),
                           ('opponent-type-fighting', 'REAL'),
                           ('opponent-type-flying', 'REAL'),
                           ('opponent-type-electric', 'REAL'),
                           ('opponent-type-ice', 'REAL'),
                           ('opponent-type-dragon', 'REAL'),
                           ('opponent-baseHP', 'REAL'),
                           ('opponent-baseattack', 'REAL'),
                           ('opponent-basedefense', 'REAL'),
                           ('opponent-basespeed', 'REAL'),
                           ('opponent-basespecial', 'REAL'),
                           ('opponent-curHP', 'REAL'),
                           ('opponent-status-par', 'REAL'),
                           ('opponent-status-frz', 'REAL'),
                           ('opponent-status-slp', 'REAL'),
                           ('opponent-status-brn', 'REAL'),
                           ('opponent-status-psn', 'REAL'),
                           ('opponent-attackMod', 'REAL'),
                           ('opponent-defenseMod', 'REAL'),
                           ('opponent-speedMod', 'REAL'),
                           ('opponent-specialMod', 'REAL'),
                           ('opponent-accuracyMod', 'REAL'),
                           ('opponent-evasionMod', 'REAL')],
            'data': [
                [int('Normal' in user.primary().typing), int('Grass' in user.primary().typing),
                 int('Fire' in user.primary().typing), int('Water' in user.primary().typing),
                 int('Poison' in user.primary().typing), int('Bug' in user.primary().typing),
                 int('Psychic' in user.primary().typing), int('Ghost' in user.primary().typing),
                 int('Rock' in user.primary().typing), int('Ground' in user.primary().typing),
                 int('Fighting' in user.primary().typing), int('Flying' in user.primary().typing),
                 int('Electric' in user.primary().typing), int('Ice' in user.primary().typing),
                 int('Dragon' in user.primary().typing), n_user_stats['hp'], n_user_stats['patk'],
                 n_user_stats['pdef'], n_user_stats['spe'], n_user_stats['spatk'],
                 float(user.primary().health / user.primary().final_stats['hp']), int(user.primary().status == 'paralyze'),
                 int(user.primary().status == 'freeze'), int(user.primary().status == 'sleep'),
                 int(user.primary().status == 'burn'), int(user.primary().status == 'poison'),
                 user.primary().stages['patk'], user.primary().stages['pdef'], user.primary().stages['spe'],
                 user.primary().stages['spatk'], user.primary().stages['acc'], user.primary().stages['eva'],
                 int('Normal' in user.primary().typing), int('Grass' in user.primary().typing),
                 int('Fire' in user.primary().typing), int('Water' in user.primary().typing),
                 int('Poison' in opp.primary().typing), int('Bug' in opp.primary().typing),
                 int('Psychic' in opp.primary().typing), int('Ghost' in opp.primary().typing),
                 int('Rock' in opp.primary().typing), int('Ground' in opp.primary().typing),
                 int('Fighting' in opp.primary().typing), int('Flying' in opp.primary().typing),
                 int('Electric' in opp.primary().typing), int('Ice' in opp.primary().typing),
                 int('Dragon' in opp.primary().typing), n_opp_stats['hp'], n_opp_stats['patk'],
                 n_opp_stats['pdef'], n_opp_stats['spe'], n_opp_stats['spatk'],
                 float(opp.primary().health / opp.primary().final_stats['hp']), int(opp.primary().status == 'paralyze'),
                 int(opp.primary().status == 'freeze'), int(opp.primary().status == 'sleep'),
                 int(opp.primary().status == 'burn'), int(opp.primary().status == 'poison'),
                 opp.primary().stages['patk'], opp.primary().stages['pdef'], opp.primary().stages['spe'],
                 opp.primary().stages['spatk'], opp.primary().stages['acc'], opp.primary().stages['eva']
                 ]
            ],
        }
        with open('sample.arff', 'wb') as fp:
            arff.dump(obj, fp)

    def print_readable_data(self, who):
        my_team = self.get_team(who)
        print "curr team:", who
        print my_team.primary()
        for poke in my_team.poke_list:
            poke_info = "{0}: status-{1}, stats-{2}, moves-{3}, health-{4}, type-{5}, boosts-{6}".format(
                poke.name, poke.status, poke.stats, poke.moveset.moves, poke.health, poke.typing, poke.stages)
            print poke_info

    @staticmethod
    def load(path):
        with open(path, 'rb') as fp:
            gs = pickle.load(fp)
        return gs

    def deep_copy(self):
        state = GameState([x.copy() for x in self.teams])
        state.rocks = self.rocks[:]
        state.spikes = self.spikes[:]
        return state

    def set_rocks(self, who, rock_bool):
        self.rocks[who] = rock_bool

    def add_spikes(self, who):
        self.spikes[who] += 1

    def get_team(self, team):
        return self.teams[team]

    def to_tuple(self):
        return (tuple(x.to_tuple() for x in self.teams), (self.rocks[0], self.rocks[1], self.spikes[0], self.spikes[1]))

    @staticmethod
    def from_tuple(tupl):
        return GameState([team.from_tuple() for team in tupl[0]])

    def evaluate(self, who):
        win_bonus = 0
        my_team = self.get_team(who)
        opp_team = self.get_team(1 - who)
        if self.is_over():
            if my_team.alive():
                win_bonus = 10000
            else:
                win_bonus = -10000
        my_team_health = sum([x.health / x.final_stats['hp'] for x in my_team.poke_list])
        opp_team_health = sum([x.health / x.final_stats['hp'] for x in opp_team.poke_list])
        my_team_death = len([x for x in my_team.poke_list if not x.alive])
        opp_team_death = len([x for x in opp_team.poke_list if not x.alive])
        my_burn, opp_burn = 0, 0
        my_rocks, opp_rocks = 0, 0
        spikes = 0
        if self.is_over():
            my_team_stages, opp_team_stages = 0, 0
        else:
            my_poke = my_team.primary()
            opp_poke = opp_team.primary()
            my_team_stages = my_poke.stages['spatk'] + my_poke.stages['patk']
            opp_team_stages = opp_poke.stages['spatk'] + opp_poke.stages['patk']
            opp_rocks = 0.75 if self.rocks[1 - who] else 0
            my_rocks = -1.0 if self.rocks[who] else 0
            if self.spikes[1 - who] == 1:
                spikes = 0.3
            elif self.spikes[1 - who] == 2:
                spikes = 0.6
            elif self.spikes[1 - who] == 3:
                spikes = 1
            opp_burn = 0.75 if (
                opp_poke.status == "burn" and opp_poke.final_stats['patk'] > 245 and opp_poke.ability != "Guts") else 0
            my_burn = -1.5 if (
                my_poke.status == "burn" and my_poke.final_stats['patk'] > 250 and my_poke.ability != "Guts") else 0
        return win_bonus + my_team_health - opp_team_health - 0.5 * my_team_death + 0.5 * opp_team_death + opp_rocks + my_rocks + opp_burn + my_burn + spikes  # + 0.07 * (my_team_stages - opp_team_stages)

    def is_over(self):
        return not (self.teams[0].alive() and self.teams[1].alive())

    def switch_pokemon(self, switch_index, who, log=False, hazards=True):
        my_team = self.get_team(who)
        opp_team = self.get_team(1 - who)
        if my_team.primary().name == "Meloetta":
            my_team.primary().meloetta_reset()
        my_team.set_primary(switch_index)
        my_poke = my_team.primary()
        my_poke.reset_taunt()
        my_poke.reset_disabled()
        my_poke.reset_last_move()
        my_poke.reset_encore()
        opp_poke = opp_team.primary()
        if log:
            print (
                "%s switched in." % my_poke
            )
        if my_poke.ability == "Intimidate":
            if log:
                print ("%s got intimidated." % opp_poke)
            opp_poke.decrease_stage('patk', 1)
        if self.rocks[who] and hazards:
            type = 1.0
            type_multipliers = [get_multiplier(x, "Rock") for x in my_poke.typing]
            for x in type_multipliers:
                type *= x
            damage = 1.0 / 8 * type
            d = my_poke.damage_percent(damage)
            if log:
                print "%s was damaged %f due to rocks!" % (my_poke, d)
            if self.spikes[who] > 0 and "Flying" not in my_poke.typing and my_poke.ability != "Levitate":
                if self.spikes[who] == 1:
                    d = my_poke.damage_percent(1.0 / 8)
                elif self.spikes[who] == 2:
                    d = my_poke.damage_percent(1.0 / 6)
                elif self.spikes[who] == 3:
                    d = my_poke.damage_percent(1.0 / 4)
                if log:
                    print "%s was damaged %f due to spikes!" % (my_poke, d)

    def get_legal_actions(self, who, log=False):
        my_team = self.get_team(who)
        my_poke = my_team.primary()
        opp_team = self.get_team(1 - who)
        opp_poke = opp_team.primary()

        pokemon = range(len(my_team.poke_list))
        valid_switches = [i for i in pokemon if my_team.poke_list[i].alive and i != my_team.primary_poke]
        valid_backup_switches = valid_switches + [my_team.primary_poke]
        if len(valid_switches) == 0:
            valid_switches = [None]

        moves = []
        switches = []
        for move_index in range(len(my_poke.moveset.moves)):
            move_name = my_poke.moveset.moves[move_index]
            mega = my_poke.can_evolve()
            if my_poke.choiced:
                if move_name != my_poke.move_choice:
                    continue
            if move_name == "U-turn" or move_name == "Volt Switch":
                for j in valid_switches:
                    for k in valid_backup_switches:
                        if j is None:
                            moves.append(
                                Action(
                                    "move",
                                    move_index=move_index,
                                    mega=mega,
                                    volt_turn=j,
                                    backup_switch=None
                                )
                            )
                        elif j is not None and k is not None and j != k:
                            moves.append(
                                Action(
                                    "move",
                                    move_index=move_index,
                                    volt_turn=j,
                                    backup_switch=k,
                                    mega=mega
                                )
                            )
            else:
                moves.extend([
                                 Action("move", move_index=move_index, mega=mega, backup_switch=j)
                                 for j in valid_switches
                                 ])
        switches.extend(
            [Action("switch", switch_index=i, backup_switch=j) for i in valid_switches for j in valid_backup_switches if
             j != i and i is not None])

        if opp_poke.ability == "Magnet Pull" and "Steel" in my_poke.typing and "Ghost" not in my_poke.typing:
            switches = []
        elif opp_poke.ability == "Shadow Tag" and "Ghost" not in my_poke.typing:
            switches = []
        elif opp_poke.ability == "Arena Trap" and "Ghost" not in my_poke.typing and "Flying" not in my_poke.typing:
            switches = []
        if my_poke.taunt:
            moves = [move for move in moves if MOVES[my_poke.moveset.moves[move.move_index]].category != "Non-Damaging"]
        if my_poke.disabled is not None:
            moves = [move for move in moves if my_poke.moveset.moves[move.move_index] != my_poke.disabled]
        if my_poke.encore:
            moves = [move for move in moves if my_poke.moveset.moves[move.move_index] == my_poke.last_move]

        return moves + switches

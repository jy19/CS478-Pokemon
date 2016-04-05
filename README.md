## Running the simulator ##
* Run `python game.py team1 team2` where `team1` and `team2` are pokemon team files. See examples under `teams/` subfolder.

### Human Agent ###
* Not much error handling, if using a human agent, input like so:

 `move move_index backup mega_evolve volt_switch`

 where `move`: `move` or `switch`

 `move_index`: index of the move

 `backup`: index of the pokemon in team to switch into if current one faints

 `mega_evolve`: `True` or `False`
 
 `volt_switch`: index of the pokemon to switch into if using moves like volt switch or u turn

* make sure there are at least 4 arguments or there will be an error...

* Simulator code mostly from [here](https://github.com/vasumv/pokemon_ai), simplifying for class project testing purposes.
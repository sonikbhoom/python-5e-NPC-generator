""" Generate NPC character stats in python """
import random
import sys
from collections import OrderedDict

class Colors:
    """ print formatting class """
    c_header = '\033[95m'
    ok_blue = '\033[94m'
    ok_green = '\033[92m'
    c_warning = '\033[93m'
    c_fail = '\033[91m'
    end_c = '\033[0m'

    def disable(self):
        """ self """
        self.c_header = ''
        self.ok_blue = ''
        self.ok_green = ''
        self.c_warning = ''
        self.c_fail = ''
        self.end_c = ''

char_maps = {}
char_maps['archer']    = ['dex','con','wis','cha','int','str'] # Assuming Dex based Fighter
char_maps['barbarian'] = ['str','con','dex','wis','cha','int']
char_maps['bard']      = ['cha','dex','con','int','wis','str']
char_maps['cleric']    = ['wis','con','dex','str','int','cha']
char_maps['druid']     = ['wis','con','dex','int','str','cha']
char_maps['eknight']   = ['str','con','int','wis','cha','dex'] # Assuming Dex based Fighter
char_maps['fighter']   = ['str','con','wis','cha','int','dex'] # Assuming Strength-Based Melee
char_maps['monk']      = ['dex','con','wis','str','int','cha']
char_maps['paladin']   = ['str','cha','con','wis','int','dex']
char_maps['pal_dex']   = ['str','cha','con','wis','int','dex']
char_maps['ranger']    = ['dex','con','wis','int','str','cha']
char_maps['rogue']     = ['dex','con','wis','int','str','cha']
char_maps['srocerer']  = ['cha','con','dex','int','wis','str']
char_maps['warlock']   = ['cha','con','dex','int','wis','str']
char_maps['wizard']    = ['int','con','dex','wis','cha','str']

STAT_MAX = 108

def character_ordered(_stats, _stats_map):
    """ load character model with primary ordered stats """
    _character = OrderedDict()
    for stat in _stats_map:
        _character[stat] = _stats.pop(0)
    return _character

def genstats():
    """ main stats generator function; the main math! """
    stats = sorted(([sum(sorted([random.randint(1,6) for _ in range (4)])[1:]) for _ in range(6)]),reverse=True)
    return stats

def nice_print(character):
    """ pretty up the presentation of the character stats """
    limiter = ''
    stat_total = (character['str'] + character['dex'] + character['con'] + character['int'] + character['wis'] + character['cha'])
    if stat_total <= 64:
        limiter = 'weak'
    elif (stat_total > 64) and (stat_total < 80):
        limiter = 'medium'
    elif stat_total >= 80:
        limiter = 'strong'
    elif stat_total > 100:
        limiter = 'epic'
    print("%sSTR%s : %s%s%s" % (Colors.ok_blue,Colors.end_c,Colors.ok_green,character['str'],Colors.end_c))
    print("%sDEX%s : %s%s%s" % (Colors.ok_blue,Colors.end_c,Colors.ok_green,character['dex'],Colors.end_c))
    print("%sCON%s : %s%s%s" % (Colors.ok_blue,Colors.end_c,Colors.ok_green,character['con'],Colors.end_c))
    print("%sINT%s : %s%s%s" % (Colors.ok_blue,Colors.end_c,Colors.ok_green,character['int'],Colors.end_c))
    print("%sWIS%s : %s%s%s" % (Colors.ok_blue,Colors.end_c,Colors.ok_green,character['wis'],Colors.end_c))
    print("%sCHA%s : %s%s%s" % (Colors.ok_blue,Colors.end_c,Colors.ok_green,character['cha'],Colors.end_c))
    print("Total Points : %s" % (stat_total))
    print("%sStats Rating%s : %s%s%s" % (Colors.ok_blue,Colors.end_c,Colors.ok_green,limiter,Colors.end_c))
    print("")

def main(character_type):
    """ generate character stats """
    character_stats = genstats()

    try:
        character = character_ordered(character_stats,char_maps[character_type])

    except KeyError:
        print ("%s%s%s %s%s" % (Colors.ok_green, character_type, Colors.ok_blue,"class not found. assuming wizard\n",Colors.end_c))
        character_type = 'wizard'
        character = character_ordered(character_stats,char_maps[character_type])

    print(Colors.ok_blue + "Stats created for" + Colors.ok_green, character_type, Colors.end_c)
    nice_print(character)

if __name__ == '__main__':
    print ("%s%s%s" % (Colors.c_header,"Generate stats for NPC with class",Colors.end_c))
    print ("%s%s%s" % (Colors.c_header,"Version: 0.6  Author: Nim Turen\n",Colors.end_c))
    try:
        _character_type = sys.argv[1].lower()
    except IndexError as e_error:
        # print ('error finding character type:' + str(e_error) +'\n')
        print ("%s%s%s%s%s%s" % (Colors.c_header,"usage:",sys.argv[0].lower()," <character type>",Colors.end_c,"\n\nValid types are:"))
        for char_type in char_maps:
            print ("%s%s%s%s" % (Colors.ok_green,char_type," ",Colors.end_c), end="")
        print ("\n")
        sys.exit()

    main(_character_type)
#EOF

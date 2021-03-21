import random
import json
import sys
from collections import OrderedDict

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

char_maps = {}
char_maps['archer']    = ['dex','con','wis','cha','int','str'] # Assuming Dex based Fighter
char_maps['barbarian'] = ['str','con','dex','wis','cha','int']
char_maps['bard']      = ['cha','dex','con','int','wis','str']
char_maps['cleric']    = ['wis','con','dex','str','int','cha']
char_maps['druid']     = ['wis','con','dex','int','str','cha']
char_maps['eknight']   = ['str','con','int','wis','cha','dex'] # Assuming Dex based Fighter with tweak
char_maps['fighter']   = ['str','con','wis','cha','int','dex'] # Assuming Strength-Based Melee
char_maps['monk']      = ['dex','con','wis','str','int','cha']
char_maps['paladin']   = ['str','cha','con','wis','int','dex']
char_maps['pal_dex']   = ['str','cha','con','wis','int','dex']
char_maps['ranger']    = ['dex','con','wis','int','str','cha']
char_maps['rogue']     = ['dex','con','wis','int','str','cha']
char_maps['srocerer']  = ['cha','con','dex','int','wis','str']
char_maps['warlock']   = ['cha','con','dex','int','wis','str']
char_maps['wizard']    = ['int','con','dex','wis','cha','str']

stat_max = 108
stat_total = 0

# character model with primary stats ordered
def character_ordered(_stats, _stats_map):
    _character = OrderedDict()
    for stat in _stats_map:
        _character[stat] = _stats.pop(0)
    return _character

def genstats():
    stats = sorted(([sum(sorted([random.randint(1,6) for _ in range (4)])[1:]) for _ in range(6)]),reverse=True)
    return stats

def nice_print(character):
    # pretty up the presentation of the character stats
    # print(character)
    stat_total = (character['str'] + character['dex'] + character['con'] + character['int'] + character['wis'] + character['cha'] )
    print("%sSTR%s : %s%s%s" % (bcolors.OKBLUE,bcolors.ENDC,bcolors.OKGREEN,character['str'],bcolors.ENDC))
    print("%sDEX%s : %s%s%s" % (bcolors.OKBLUE,bcolors.ENDC,bcolors.OKGREEN,character['dex'],bcolors.ENDC))
    print("%sCON%s : %s%s%s" % (bcolors.OKBLUE,bcolors.ENDC,bcolors.OKGREEN,character['con'],bcolors.ENDC))
    print("%sINT%s : %s%s%s" % (bcolors.OKBLUE,bcolors.ENDC,bcolors.OKGREEN,character['int'],bcolors.ENDC))
    print("%sWIS%s : %s%s%s" % (bcolors.OKBLUE,bcolors.ENDC,bcolors.OKGREEN,character['wis'],bcolors.ENDC))
    print("%sCHA%s : %s%s%s" % (bcolors.OKBLUE,bcolors.ENDC,bcolors.OKGREEN,character['cha'],bcolors.ENDC))
    print("%sTotal Points%s : %s%s%s" % (bcolors.OKBLUE,bcolors.ENDC,bcolors.OKGREEN,stat_total,bcolors.ENDC))
    print("")

def main(character_type):

    # generate character stats
    character_stats = genstats()

    # TODO: allow for class variants (e.g. Heavy armour cleric, and dex based paldin)

    try:
        character = character_ordered(character_stats,char_maps[character_type])

    except KeyError:    
        # assign stats to character abilities
        print ("%s%s%s %s%s" % (bcolors.OKGREEN, character_type, bcolors.OKBLUE,"class not found. assuming wizard\n",bcolors.ENDC))
        character_type = 'wizard'
        character = character_ordered(character_stats,char_maps[character_type])

    print(bcolors.OKBLUE + "Stats created for" + bcolors.OKGREEN, character_type, bcolors.ENDC)
    nice_print(character)

if (__name__ == '__main__'):
    print (bcolors.HEADER + "Generate stats for NPC with class" + bcolors.ENDC)
    print (bcolors.HEADER + "Version: 0.6  Author: Nim Turen\n" + bcolors.ENDC)
    try:
        _character_type = sys.argv[1].lower()
    except Exception as e:
        # print ('error finding character type:' + str(e) +'\n')
        print (bcolors.HEADER + "usage:", sys.argv[0].lower() + " <character type>" +bcolors.ENDC + "\n\nValid types are:")
        for char_type in char_maps.keys():
            print (bcolors.OKGREEN + char_type + " " + bcolors.ENDC, end="")
        print ("\n")
        sys.exit()

    main(_character_type)
#EOF

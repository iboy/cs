# script1501.py - Display Bird immutable data via Accessors
# Written by Blum and Bresnahan
#
############ Import Modules  ##################
#
# Birds object file
from Birds import Bird
#
# Barn Swallow object file
from BarnSwallow import BarnSwallow
#
# South Africa Cliff Swallow object file
from SouthAfricanCliffSwallow import SouthAfricanSwallow
#
def main ():
	###### Create Variables & Object Instances ###
	#
	sex='unknown'  #Male, female, or unknown
	flock_size='0'
	#
	bird=Bird(sex)
	barn_swallow=BarnSwallow(sex,flock_size)
	sa_cliff_swallow=SouthAfricanSwallow(sex,flock_size)
	#
	########## Show Bird Characteristics ########
	#
	print("A bird has",end=' ')
	if bird.get_feathers() == 'yes':
    		print("feathers,", end=' ')
	print("bones that are", bird.get_bones(), end=' ')
	print("and", bird.get_eggs(), "eggs.")
	#
	###### Show Barn Swallow Characterstics #####
	#
	print()
	print("A barn swallow is a bird that", end=' ')
	if barn_swallow.get_migratory() == 'yes':
    		print("is migratory.")
	else:
    		print("is not migratory.")
	#
	######## Show Cliff Swallow Characterstics ######
	#
	print()
	print("A cliff swallow is a bird that", end=' ')
	if sa_cliff_swallow.get_migratory() == 'yes':
    		print("is migratory.")
	else:
    		print("is not migratory.")
#########################################################
#
########## Call the main function #######################
main()






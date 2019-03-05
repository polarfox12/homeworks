players = {}
#ships_locations_player1 = {}
#ships_locations_player2 = {}
#shouts_player1 = {}
#shouts_player2 = {}


class Player(object):
	ochered = list()
	def __init__(self, name):
		self.name = name
		if ochered == []:
		    self.ochered = 1
		    ochered.append(self.name)
		else:
		    self.ochered = 2
		    ochered.append(self.name)
        
        self.ships = {
	    'линкор': 1,
	    'крейсер': 2,
	    'эсминец': 3,
	    'катер': 4
	    }

	    self.ships_locations = {}
	    self.shouts = {}		  

class Field(object):
    def __init__(self):
        self.size = 
        {
        'a':list(range(1, 11)),
        'b':list(range(1, 11)),
        'c':list(range(1, 11)),
        'd':list(range(1, 11)), 
        'e':list(range(1, 11)),
        'f':list(range(1, 11)),
        'g':list(range(1, 11)),
        'h':list(range(1, 11)),
        'i':list(range(1, 11)),
        'j':list(range(1, 11))
        }

        '''
for key, value in field.items():
    l = list()
    for i in value:
        
        i = '*'
        l.append(i)
    value = l    
    print(l)
'''
             
        


                                                                                               # Дописать создание кораблей. Разбить по классам по необходимости
class Ships(object):
	
	def __init__(self, name_ship, player):
		if name_ship[0] == 'линкор' and player.ships['линкор'] > 0:
			self.name = name_ship[0]
			self.size = 4
			if name_ship[2] == 'up':
			    i = name_ship[1]

			    self.location = {i[0]: int(i[1])} 
		elif name_ship[0] == 'крейсер' and player.ships['крейсер'] > 0:
		    self.name = name_ship[0]
		    self.size = 3
		    self.location = 0
		elif name_ship[0] == 'эсминец' and player.ships['эсминец'] > 0:
		    self.name = name_ship[0]
		    self.size = 2
		    self.location = 0    	
		elif name_ship[0] == 'катер' and player.ships['катер'] > 0:
		    self.name = name_ship[0]
		    self.size = 1
		    self.location = 0


class Shout(object):		    	
		
     def __init__(self, player, shout_input):
     	self.player = player.name
     	self.location = shout_input
     	self.headshot = False


def create_field(field, ships_locations, shouts):



def create_ships(player):
	ship = input('Введите название , координаты начала и направление корабля (up/down/left/right) (например: линкор b4 down): /n')
    ship = ship.split(' ')
    ship = Ships.__init__(ship, player):




def main:
	#Создать поле
	field = Field.__init__()
	#Создать двух игроков
	name = input('Введите имя первого игрока ')
	player1 = Player.__init__(name)
	name = input('Введите имя второго игрока ')
	player2 = Player.__init__(name)
	#Создать корабли
    



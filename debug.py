from lib.animal import *
from lib.zoo import *

# code here

# e.g.  
micke_grove = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )

a1 = Animal( 'Tiger', 75, 'Luke', micke_grove )
a2 = Animal( 'Tiger', 32, 'Leia', micke_grove )


bronx_zoo = Zoo( 'Bronx Zoo', 'The Bronx' )
bronx_zoo = Zoo( "Sam's Spot", 'The Bronx' )

a3 = Animal( 'Tiger', 157, 'Homer', bronx_zoo )
Animal( 'Tiger', 51, 'Tony', bronx_zoo )
Animal( 'Snake', 12, 'Jake', bronx_zoo )

# Animal.find_by_species( 'Tiger' ) 
import ipdb; ipdb.set_trace()

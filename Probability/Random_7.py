# Use random 5 generate random 7
# random5 range: 1 - 5
#   random5 * random5 = 1-25 > 7*3, so if a number less than 21 generated, 
#   since it has the equal probability to map to 1 - 7
#   1-7,8-14,15-21 all uniformly distributed
import random
def generate():
    #initially assign a max value to random number
    random_num =float('inf') 
    #if random number greater than or equal to 21, need to resample
    while random_num>=21:
        x =random.randint(1,5)
        y =random.randint(1,5)
        random_num=(x-1)*5+ y-1
    #map 0-20 to 1-7
    return random_num%7+1
 
for i in range(2):
  print(generate())

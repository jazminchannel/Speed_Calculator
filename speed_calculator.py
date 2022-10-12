def ask_for_distance(name):
   return float(input(f'How far did {name} run (in feet)? '))

def ask_for_min(name, distance1):
   return float(input(f'How many minutes did {name} take to run {distance1} feet? '))

def compute_speed(minutes, distance):
   speed = distance / (minutes * 60)
   return speed
   

def main():
   names = ['peter', 'jane']
   for name in names:
     distance1 = ask_for_distance(name)
     min1 = ask_for_min(name, distance1)
     speed = compute_speed (min1, distance1)
     if name == 'peter':
       peter_speed = speed
     else:
       jane_speed = speed

   if jane_speed > peter_speed:
      print(f'Jane was the fastest at {jane_speed} f/s')
   elif peter_speed > jane_speed:
      print(f'Peter was the fastest at {peter_speed} f/s')
   else:
      print(f'The race was a tie at {peter_speed} f/s')
   print('Well done Peter and Jane!')
  
main()
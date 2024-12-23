      ## X Co ordinates
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original x position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
   x_increment = 1
elif alien_0['speed'] == 'medium':
   x_increment = 2
else:
   # This must be a fast alien.
   x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x position: {alien_0['x_position']}")
  ## Y Co ordinates
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f"Original y position: {alien_0['y_position']}")
if alien_0['speed'] == 'slow':
   y_increment = 1
elif alien_0['speed'] == 'medium':
   y_increment_increment = 2
else:
   # This must be a fast alien.
   y_increment_increment = 3
alien_0['y_position'] = alien_0['y_position'] + y_increment_increment
print(f"New y position: {alien_0['y_position']}")
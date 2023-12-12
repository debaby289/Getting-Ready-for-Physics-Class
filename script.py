# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8

# Write your code below: 

#Temperature Change Formula to C
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

#Testing Formula for F input
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

#Temperature Change Formula to F
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

#Temperature Change Formula to C
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

#get_force function
def get_force(mass,acceleration):
  return mass * acceleration

#Test get_force
train_force = get_force(train_mass,train_acceleration)
print(train_force)

#Task 7 - Print Statement
print("The GE train supplies",train_force, "Newtons of force.")

#get_energy function
def get_energy(mass,c):
  return mass * (c ** 2)

#Test get_energy
bomb_energy = get_energy(bomb_mass,c)
print(bomb_energy)

#Task 10 - Print Statement
print("A 1kg bomb supplies", bomb_energy, "Joules.")

#get_work function
def get_work(mass,acceleration,distance):
  return mass * acceleration * distance

#Test get_work
train_work = get_work(train_mass,train_acceleration,train_distance)
print(train_work)

#Task 13 - Print Statement
print("The GE train does",train_work,"Joules of work over",train_distance,"meters.")

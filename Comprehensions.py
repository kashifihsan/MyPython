primes = [2, 3, 5, 7, 11]

for prime in primes:
	print(prime, "is prime number..")

# -------------
# for i in range (20):
# print(range(10))	

my_friends = {
	'kashif': 6,
	'imran': 10,
	'atif' : 6
}

# for name in my_friends:
# 	print(name, my_friends[name])
# items() introduced in python 3
for name, days in my_friends.items():
	print(f'\nI saw {name} after {days} days.')

print('\n', my_friends.items(),'\n')	

for t in [('kashif', 6), ('imran', 10), ('atif', 6)]:
	# print(t)
	n, v = t
	print(n)
	print(v)
print('\n')


for name, days in my_friends.items():
	if name == 'imran':
		print('I know imran')

who_do_i_know = 'atif'
if who_do_i_know in my_friends:
	print('I also know atif..')
print('\n')

# Break and Continue keywords..
cars = ['ok', 'ok', 'ok', 'faulty', 'ok', 'ok']
for car_status in cars:
	if car_status == 'faulty':
		print('stop production.')
		break
	print(f'This car is {car_status}')
print('\n')
# What range does---------
# for num in range(2,10):
# 	print(num)
# --------------------------
for num in range(2,10):
	if num % 2 == 0:
		print(f'{num} is an even number')
		continue
	print(f'{num} is odd.')
print('\n')	
# --------------------------
for n in range(2,10):
	for x in range(2, n):
		if n % x == 0:
			print(f'{n} equals {x} * {n//x} so its not a prime number')
			break
	else:
		print(f'{n} is a prime number')	

print('\n')	
# -------------------------
# -------------------------
# Appending prime numbers in a list..
# What is a Prime number:
# 1- A prime number has to be a positive integer
# 2- Divisible by exactly 2 integers (1 and itself)
# 3- 1 is not a prime number

primes = []
for possibePrime in range(2,21):
	isPrime = True
	for num in range(2, possibePrime):
		if possibePrime % num == 0:
			isPrime = False
	if isPrime:
		primes.append(possibePrime)
		print(possibePrime)
		print(primes)
			
print('------')

primes = []
for possibePrime in range(2,21):
	for num in range(2, possibePrime):
		if possibePrime % num == 0:
			break	
	else:
		primes.append(possibePrime)
		# print(possibePrime)
print(primes)
print('\n')

# --------------------------
# List Comprehesion---------
numbers = list(range(10))
doubled_numbers = [n*2 for n in numbers]
print(doubled_numbers)

phrases = [f'I am {age} years old.' for age in doubled_numbers]
print(phrases)
print('\n')
# -------------------------
names_list = ['Kashif', 'Hina', 'Irha']
print(names_list)
lowercase_names = [name.lower() for name in names_list]
print(lowercase_names)
print('\n')
# List Comprehesion with conditional-----
evens = [n for n in numbers if n % 2 == 0] 
print(evens)
print('\n')

# Matching 2 Lists-----------------------
friends = ['ibrahim', 'moosa', 'Eesa']
guests = ['Ibrahim', 'mustafa', 'eesa', 'Yahya']
lower_friends = [n.lower() for n in friends]

present_friends = [name for name in guests if name.lower() in lower_friends]
print(present_friends)
print('\n')
# Sets and Dictionary Comprehesion--------
friends = {'ibrahim', 'moosa', 'Eesa'}
guests = {'Ibrahim', 'mustafa', 'eesa', 'Yahya'}
lower_friends_names = {f.lower() for f in friends}
lower_guests_names = {f.lower() for f in guests}

present_friends = {name for name in  lower_friends_names & lower_guests_names}
print(present_friends)
print('\n')
# ----------------------------------------
# Construct Dictionary from 2 Lists ------
names = ['Ali', 'Amjad', 'Qasim']
time_last_seen = [10, 15, 7]

friends_last_seen = {names[i]: time_last_seen[i] for i in range(len(names))}
print(friends_last_seen)
print('\n')
# A better way to do this-----------------
friends_last_seen = dict(zip(names, time_last_seen))
print(friends_last_seen)
print('\n')
# fire = zip(names, time_last_seen)
# print(dict(fire))
new = [('wali', 10), ('ali', 15), ('kash', 25)]
print(dict(new))




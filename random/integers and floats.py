num = 3
print(type(num))
num = 3.14
print(type(num))

# Arthimetic operatores:
# Addition:..........3 + 2
# Substraction:......3 - 2
# Multiplication:....3 * 2
# Division:..........3 / 2
# Floor Division:....3 // 2
# Exponent:..........3 ** 2
# Modulus:...........3 % 2
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3**2)  # power 3^2
print(3 % 2)  # reminder after division
print(4 % 2)  # if modulus of 2 is 0 then it is even
print(5 % 2)  # if modulus of 2 is 1 then it is odd
# python follows BODMAS format
print(3 * 2 + 1)  # gives 7
print(3 * (2 + 1))  # gives 9
##
num = 1
num = num + 1
print(num)
# increment
num = 1
num += 1
print(num)
# multiply
num = 1
num *= 10
print(num)
# absolute
print(abs(-3))
# round
print(round(3.75))
print(round(3.75, 1))

# Comparisons:
# Equal:............. 3==2
# NOt Equal:......... 3!=2
# Greater Than:...... 3 > 2
# Less Than:......... 3 < 2
# Greater or Equal:.. 3 >= 2
# Less or Equal:..... 3 <= 2
##
i = 4

print(i)

num_1 = 3
num_2 = 2
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

num_1 = "100"  # takes as string
num_2 = "200"
print(num_1 + num_2)  # concatinates strings

# casting
num_1 = "100"  # takes as string
num_2 = "200"
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)

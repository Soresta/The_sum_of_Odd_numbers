# sum of the odd numbers:
# The program that finds the sum of the odd ones out of 10 numbers entered from the keyboard.
# Klavyeden girilen 10 sayıdan tek olanların toplamını bulan program.


counter = 0
total = 0

while counter < 10:
    num = int(input("Enter integer: "))

    episode = num // 2
    remainder = num - episode * 2

    if remainder == 1:
        total = total + num
    counter += 1

print(total)

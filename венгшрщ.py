word=str(input("Введіть слово: "))
ascii_sum=sum(ord(char)for char in word)
print ("Sum of ASCII codes of symbols = ", ascii_sum)
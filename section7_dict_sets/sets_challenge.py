vowels = frozenset("aeiou")
answer = input("Please enter some text ").lower()
result = sorted(set(answer).difference(vowels))
print(result)
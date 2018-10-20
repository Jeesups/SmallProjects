import random

slowa = ("python","gdansk","dlaczego","gdynia","wsb")
word = random.choice(slowa)

poprawnie = word
pomie = ""

while word:
    position = random.randrange(len(word))
    pomie += word[position]
    word = word[:position] + word[(position+1):]


print("""
    Witaj w grze 'Wymieszane litery'!
    Uporządkuj litery, aby odtworzyć prawidłowe słowo.
    (Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
""")

print("Zgadnij, jakie to słowo: %s" %(pomie))

zgaduj = input("\n Twoja odpowiedź: ")
while zgaduj != poprawnie and zgaduj != "":
    print("Niestety to nie to słowo.")
    zgaduj = input("Twoja odpowiedź: ")
if zgaduj == poprawnie:
    print("Zgada się! Zgadłeś!\n")
print("Dziękuję za udział w grze")
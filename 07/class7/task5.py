# Wykorzystaj plik zawierający fragment Pana Tadeusza.
# Znajdź najdłuższe słowo występujące w zadanym fragmencie.

with open('tekst.txt', 'r', encoding="utf-8") as fopen:
  lines = fopen.readlines()
  print(lines)
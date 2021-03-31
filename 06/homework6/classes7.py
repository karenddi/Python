filename = 'tekst.txt'

with open(filename, 'r', encoding="utf-8") as f:
  content = f.read()
  print(content)


#Error
filename = 'text.txt'

try:
    with open(filename, 'r') as file:
      content = file.readlines()
      print(content)
except FileNotFoundError:
    print('Error - no such file')
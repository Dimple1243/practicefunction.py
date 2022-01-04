# def add(a,b):
#     d=a+b
#     return d
# x=int(input("enter the num "))
# y=int(input("enter the num "))
# z=add(x,y)
# print(z)

def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))

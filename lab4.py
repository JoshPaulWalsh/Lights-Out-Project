import random

square = [
        [u"\u25A1",u"\u25A1",u"\u25A1",u"\u25A1",u"\u25A1"],
        [u"\u25A1",u"\u25A1",u"\u25A1",u"\u25A1",u"\u25A1"],
        [u"\u25A1",u"\u25A1",u"\u25A1",u"\u25A1",u"\u25A1"],
        [u"\u25A1",u"\u25A1",u"\u25A1",u"\u25A1",u"\u25A1"],
        [u"\u25A1",u"\u25A1",u"\u25A1",u"\u25A1",u"\u25A1"],
]
coloredBox=random.choice(['white','black'])
if coloredBox=='black':
    print(u"\u25A1")
if coloredBox=='white':
    print(u"\u25A0")

#for i in range(5):
#    print(square[i])
#for i in range(5):
#    print(u"\u25A1", end=" ")
#for i in range(5):
#    print(u"\u25A1", end=" ")
#for i in square:
#    Square = [[print(u"\u25A1")]*5 for i in range(5)]
#25A0 is white square
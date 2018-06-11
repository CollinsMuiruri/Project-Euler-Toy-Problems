# Just a simple height viewer to start off and ease the pressure

import emoji

print("Input your height:")
height = int(input())
if height > 30 :
    print(emoji.emojize("You tall bastard :Troll_face:", use_aliases=True))
elif height > 20 :
    print("Just the right size for marriage")
    print(emoji.emojize('Your height is :+1:', use_aliases=True))
else:
    print(emoji.emojize("Such a short kid you are!! :kiss: :kiss: ", use_aliases=True))

COLOUR_LIST=["Red","Green","White","Black","Pink","Yellow"]    #original list
print(COLOUR_LIST)

del COLOUR_LIST[3]
print(COLOUR_LIST)      #list obtained after deleting colour black

COLOUR_LIST=["Red","Green","White","Black","Pink","Yellow"]
COLOUR_LIST[3]=COLOUR_LIST[4]="Purple"
print(COLOUR_LIST)       #list obtained after replacing 4th and 5th element with pink colour


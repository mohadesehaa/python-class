subject=['math','computer science','statistic','phisic','chemical']
name=input('enter a name pf subject you dont like it:')
t=subject.index(name)
del(subject[t])
print(subject)


import operator
import re

def change_char(s, p, r):
    return s[:p] + r + s[p + 1:]


CipherdText = "QHNABKZTAPNDGJOENAYNOIANLTIBJAUZYBTVYZDVTNYTYBTQHNABEZJOYENVNIZMYBTNUNRZOANOINYHNOYJANVTNYWNVYBTACETVUNOJANOTMETVJUTOYJOHNPZVNYZVSQHNABYTNUAWJYBPNYUNONOIDSPZVKYZVTAYZVTYBTYJUTHJOT"
highfrechar = ['a','t','e']
wordsintext = ["atlantis", "experiment", "laboratory", "timeline","flash","goes","back","and","super"]

charfreq = {}
for i in range(0,26):
    x=chr(i+65)
    charfreq[x]=0

lenght = len(CipherdText)

for i in range(0,lenght):
    charfreq[CipherdText[i]]=charfreq[CipherdText[i]]+1

sortedcharfreq = sorted(charfreq.items(), key=operator.itemgetter(1))
sortedcharfreq.reverse()

orginalcharmap = {}
charsequence = []
markedchar = []

for i in range(0,26):
   charsequence.append(sortedcharfreq[i][0])
for i in range(0,3):
    orginalcharmap[charsequence[i]] = highfrechar[i]
    markedchar.append(highfrechar[i])
    CipherdText = CipherdText.replace(charsequence[i],highfrechar[i])

for i in range(0,len(wordsintext)):

    currentstring = wordsintext[i]

    pattern=""
    for j in range(0,len(currentstring)):
        pattern+="#"
    lenght1 = len(pattern)
    # making pattern
    for j in range(0,len(markedchar)):
        for k in range(0,lenght1):
            if currentstring[k] == markedchar[j] :
                pattern = change_char(pattern,k,markedchar[j])

    for j in range(0,lenght-lenght1):
        ok = 1
        for k in range(0,lenght1):
            if pattern[k] == '#':
                continue
            if pattern[k] !=  CipherdText[j+k] :
                ok = 0

        if ok == 1:
            for k in range(0, lenght1):
                if pattern[k] == '#':
                    if CipherdText[j+k] not in markedchar :
                        orginalcharmap[CipherdText[j+k]] = currentstring[k]
                        markedchar.append(currentstring[k])
                        CipherdText = CipherdText.replace(CipherdText[j+k], currentstring[k])


print(CipherdText)




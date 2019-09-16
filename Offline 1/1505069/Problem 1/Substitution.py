import operator

def change_char(s, p, r):
    return s[:p] + r + s[p + 1:]
for fileno in range (1,91):
    if fileno<=60 and fileno>=31:
        continue
    filename = "Input/substitution-" + str(fileno) + ".txt"

    file = open(filename, "r")

    CipherdText = file.readline()
    CipherdText = CipherdText[0:-1]

    file.readline()
    highchar = file.readline()
    highchar = highchar[0:-1]
    highfrechar = highchar.split(", ")

    file.readline()
    words = file.readline()
    words = words[0:-1]
    wordsintext = words.split(", ")
    wordsintext.append("flash")
    wordsintext.append("super")
    wordsintext.append("goes")
    wordsintext.append("and")
    wordsintext.append("back")
    wordsintext.append("save")
    wordsintext.append("amazon")
    wordsintext.append("war")

    # wordsintext = ["atlantis", "experiment", "laboratory", "timeline","flash","goes","back","and","super"]

    charfreq = {}
    for i in range(0, 26):
        x = chr(i + 65)
        charfreq[x] = 0

    lenght = len(CipherdText)

    for i in range(0, lenght):
        charfreq[CipherdText[i]] = charfreq[CipherdText[i]] + 1

    sortedcharfreq = sorted(charfreq.items(), key=operator.itemgetter(1))
    sortedcharfreq.reverse()

    orginalcharmap = {}
    charsequence = []
    markedchar = []

    for i in range(0, 26):
        charsequence.append(sortedcharfreq[i][0])
    for i in range(0, len(highfrechar)):
        orginalcharmap[charsequence[i]] = highfrechar[i]
        markedchar.append(highfrechar[i])
        CipherdText = CipherdText.replace(charsequence[i], highfrechar[i])

    for i in range(0, len(wordsintext)):

        currentstring = wordsintext[i]

        pattern = ""
        for j in range(0, len(currentstring)):
            pattern += "#"
        lenght1 = len(pattern)
        # making pattern
        for j in range(0, len(markedchar)):
            for k in range(0, lenght1):
                if currentstring[k] == markedchar[j]:
                    pattern = change_char(pattern, k, markedchar[j])

        for j in range(0, lenght - lenght1):
            ok = 1
            for k in range(0, lenght1):
                if pattern[k] == '#':
                    continue
                if pattern[k] != CipherdText[j + k]:
                    ok = 0

            if ok == 1:
                for k in range(0, lenght1):
                    if pattern[k] == '#':
                        if currentstring[k] in markedchar:
                            continue
                        if CipherdText[j + k] not in markedchar :
                            orginalcharmap[CipherdText[j + k]] = currentstring[k]
                            markedchar.append(currentstring[k])
                            CipherdText = CipherdText.replace(CipherdText[j + k], currentstring[k])

    file.close()
    filename = "Output/substitution-" + str(fileno) + ".txt"
    file = open(filename, "w")
    file.write(CipherdText)
    file.write("\n\n")
    for k, v in orginalcharmap.items():
        file.write(str(k) + ' >>> ' + str(v) + '\n')
    file.write("\n")
    accuracy = (((len(orginalcharmap)) / 26.0) * 100.0)
    file.write("Accuracy : " + str(accuracy))
    file.write("\n")
    file.close()






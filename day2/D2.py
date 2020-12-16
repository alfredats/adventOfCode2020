
def getReqs(reqstr):

    (nums, char) = reqstr.split()
    n = nums.split('-')

    return (int(n[0]), int(n[1])), char


def p1CheckReqs(p, checkChar, numlims):

    charCount = 0
    for char in p:
        if char == checkChar:
            charCount += 1

    if charCount >= numlims[0] and charCount <= numlims[1]:
        return True
    else:
        return False


def p2CheckReqs(p, checkChar, indices):

    fp, sp = indices
    f = False
    s = False

    if p[fp] == checkChar:
        f = True
    if p[sp] == checkChar:
        s = True

    return f != s


def p1(indata):

    count = 0
    for record in indata:
        (req, pwStr) = record.split(':')
        lims, char = getReqs(req)

        if len(char) != 1:
            print('More than 1 char to check for')
        if lims[0] > lims[1]:
            print('limits are errorneous')

        if p1CheckReqs(pwStr, char, lims):
            count += 1

    return count


def p2(indata):

    count = 0
    for record in indata:
        (req, pwStr) = record.split(':')
        lims, char = getReqs(req)

        if len(char) != 1:
            print('More than 1 char to check for')
        if lims[0] > lims[1]:
            print('limits are errorneous')

        if p2CheckReqs(pwStr, char, lims):
            count += 1

    return count


if __name__ == "__main__":
    with open("pw.txt", 'r') as f:
        data = f.readlines()

    for i in range(len(data)):
        data[i] = data[i].rstrip()

    print(p1(data))
    print(p2(data))

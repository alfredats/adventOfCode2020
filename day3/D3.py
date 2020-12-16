
def p1Move(xP, yP, rows, rs = 3, ds = 1):

    xP = (xP + rs) % len(rows[0])
    yP += ds
    if rows[yP][xP] == '#':
        return True, (xP, yP)

    return False, (xP, yP)


def countTrees(rows, rstep=3, dstep=1):

    treeCount = 0
    x_pos = 0
    y_pos = 0

    while y_pos != len(rows) - 1:

        gotTree, (x_pos, y_pos) = p1Move(x_pos, y_pos,
                                         rows, rstep, dstep)
        
        if gotTree:
            treeCount += 1

    return treeCount


if __name__ == '__main__':

    with open("trees.txt", 'r') as f:
        topo = f.readlines()

    for i in range(len(topo)):
        topo[i] = topo[i].rstrip()
    
    print("Puzzle 1:")
    print(countTrees(topo))
    
    print()
    print("Puzzle 2:")
    cumsum = 1
    for (r, d) in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        foo = countTrees(topo, r, d)
        print("R{}, D{} : {}".format(r, d, foo))
        cumsum = cumsum * foo
    
    print(cumsum)

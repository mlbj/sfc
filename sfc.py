import sys

# recursive function that returns a (2^n) x (2^n) 2d list filled with the nth iteration on the procedure that generates the hilbert curve
# optimized using dynamic programming memoization 
def HilbertTable(n: int, memo={}):# -> List[List[int]]:
    if n in memo:
        return memo[n]
    if n == 1:
        return [[1,2],[0,3]]
    
    expn = int(2**n)
    expnm1o2 = int((2**(n-1))**2)
    expn2 = int(expn//2)
    
    tablePrevious = HilbertTable(n-1)
    ans = [[None for j in range(expn)] for i in range(expn)]
    
    # [0,0] quadrant
    for i in range(expn2):
        for j in range(expn2):
            ans[i][j] = expnm1o2 + tablePrevious[i][j]
            
    # [0,1] quadrant
    for i in range(expn2):
        for j in range(expn2):
            ans[i][expn2 + j] = 2*expnm1o2 + tablePrevious[i][j]
    
    # [1,1] quadrant
    # this flips filledPreviousOrder pi/2 counter clockwise
    rotFlipi_tablePrevious = list(zip(*tablePrevious))
    for i in range(expn2):
        for j in range(expn2):
            ans[expn2 + i][expn2 + j] = 3*expnm1o2 + rotFlipi_tablePrevious[i][j]
    
    # [1,0] quadrant
    # this rotates rotatedFilledPreviousOrder pi/2 clockwise
    rotFlipj_tablePrevious = list(zip(*rotFlipi_tablePrevious))[::-1]
    rotFlipj_tablePrevious = list(zip(*rotFlipj_tablePrevious))[::-1]
    
    for i in range(expn2):
        for j in range(expn2):
            ans[expn2 + i][j] = rotFlipj_tablePrevious[i][j]
    

    memo[n]=ans
    return ans
    
# Transform an input 2d list containing the indexes of a space filling curve into an ordered list containing the points in which that space filling curve should be drawn, in the correct ordering.
def TableToList(table):
    ni = len(table)
    nj = len(table[0])
    ans = [None]*(ni*nj)

    for i in range(ni):
        for j in range(nj):
            ans[table[i][j]] = [i,j]
    
    return ans

# this method returns a string containing a tikz drawing of the list described in points
def draw(points: int):
    ans = ''
    preamble = '\\documentclass[tikz]{standalone} \n'
    preamble +='\\usepackage{tikz} \n'
    preamble += '\\begin{document} \n '
    ans += preamble
    
    postamble = '\\end{document}'


    ans += '\\begin{tikzpicture}[auto,rotate=270] \n'
    for idx in range(len(points)-1):
        pointA = '(' + str(points[idx][0]) + ',' + str(points[idx][1]) + ')'
        pointB = '(' + str(points[idx+1][0]) + ',' + str(points[idx+1][1]) + ')'
        # ans += '\draw ' + pointA + ' node[draw] {a' + str(idx) + '} -- ' + pointB + ' node {b' + str(idx) + '};'
        ans += '\draw ' + pointA  + ' -- ' + pointB + ';'
        ans += '\n'
    
    ans += '\\end{tikzpicture}'
    ans += postamble

    return ans


# temporary main method
def main():
    n = int(sys.argv[1])
    points = TableToList(HilbertTable(n))
    validRange = [1,13]
    errMessage = 'ERROR: n must be an integer in {'+str(validRange[0])+',...,'+str(validRange[1])+'}\n'
    errMessage += 'ERROR: received n = '+str(n)


    if isinstance(n, int): 
        if n>=validRange[0] and n<=validRange[1]:
            print(draw(points))
        else:
            print(errMessage)
    else:
        print(errMessage)

if __name__ == "__main__":
    main()



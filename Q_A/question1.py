"""
Question A
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on
the x-axis and returns whether they overlap. As an example, (1,6) and (8,6) overlaps but not (1,5) and (6,8).
"""

# checks if two lines overlap
def are_overlap(x1,x2,x3,x4):

    # make sure the coordinates are ordered (by swapping)
    if x1>x2:
        x1, x2 = x2, x1
    if x3>x4:
        x3, x4 = x4, x3

    """
    now we just need to check if x2>=x3 and x4>=x1 for an overlap
    this is because:
    if x2<x3 -> x1,x2 coordinates are to the left of x3,x4
    if x4<x1 -> x3, x4 coordinates are to the left of x1,x2
    and thus lines dont overlapps
    """
    return (x2>=x3) and (x4>=x1)


if __name__ == '__main__':

    # keeps taking input until correct input is given
    while 1:

        # handle exception for when input entered in a wrong format
        try:
            print("What are the x coordinates of the 1st line in x1,x2 format ( for example: 3,4 ) ?")
            x1, x2 = tuple(int(x.strip()) for x in input().split(','))

            print("What are the x coordinates of the 2nd line in x1,x2 format ( for example: 3,4 ) ?")
            x3, x4 = tuple(int(x.strip()) for x in input().split(','))

            result = are_overlap(x1, x2, x3, x4)
            print(result)
            break

        except Exception as e:
            print("Check your input - Must be in x1,x2 format")
            print (e)

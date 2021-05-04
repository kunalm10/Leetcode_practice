"""

On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.


Example 1:


Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
Time from [1,1] to [3,4] = 3 seconds
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
Example 2:

Input: points = [[3,2],[-2,2]]
Output: 5


Constraints:

points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000

"""


def time_between_two_nodes(node_end, node_start):
    move_in_x = abs(node_end[0] - node_start[0])
    move_in_y = abs(node_end[-1] - node_start[-1])
    # diagonal_time = abs(move_in_x - move_in_y)
    total_time = min(move_in_x, move_in_y) + abs(move_in_x - move_in_y)
    return int(total_time)


def minTimeToVisitAllPoints(points):
    min_time = 0

    # Method 1
    for i, j in zip(points[0:], points[1:]):
        min_time += time_between_two_nodes(i, j)

    # Method 2
    # for i in range(len(points) - 1):
    #     min_time += time_between_two_nodes(points[i + 1], points[i])
    return min_time


if __name__ == '__main__':
    node_end, node_start = [3, 4], [-1, 0]
    print(time_between_two_nodes(node_end, node_start))
    points = [[1, 1], [3, 4], [-1, 0]]
    print(minTimeToVisitAllPoints(points))
    points = [[3, 2], [-2, 2]]
    print(minTimeToVisitAllPoints(points))
    points = [[559, 511], [932, 618], [-623, -443], [431, 91], [838, -127], [773, -917], [-500, -910], [830, -417],
              [-870, 73], [-864, -600], [450, 535], [-479, -370], [856, 573], [-549, 369], [529, -462], [-839, -856],
              [-515, -447], [652, 197], [-83, 345], [-69, 423], [310, -737], [78, -201], [443, 958], [-311, 988],
              [-477, 30], [-376, -153], [-272, 451], [322, -125], [-114, -214], [495, 33], [371, -533], [-393, -224],
              [-405, -633], [-693, 297], [504, 210], [-427, -231], [315, 27], [991, 322], [811, -746], [252, 373],
              [-737, -867], [-137, 130], [507, 380], [100, -638], [-296, 700], [341, 671], [-944, 982], [937, -440],
              [40, -929], [-334, 60], [-722, -92], [-35, -852], [25, -495], [185, 671], [149, -452]]
    print(minTimeToVisitAllPoints(points))

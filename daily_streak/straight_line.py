"""
To determine if a set of coordinates forms a straight line, we need to check if the slopes between consecutive points are equal. If the slopes are equal, it indicates that all the points lie on the same line. We can use this property to solve the problem.

Approach
Take the first two points from the given coordinates and store their coordinates as (x1, y1) and (x2, y2) respectively. These two points will serve as reference points for slope comparison.

Iterate through the remaining points starting from the third point.

For each point (x, y) in the iteration:

Calculate the left-hand side of the equation: (y - y1) * (x2 - x1)
Calculate the right-hand side of the equation: (y2 - y1) * (x - x1)
Compare the left-hand side and right-hand side of the equation. If they are not equal, return false immediately, as the points do not form a straight line.
If the loop completes without returning false, return true, indicating that all the points form a straight line.

By comparing the products of differences (instead of directly dividing), we can avoid the risk of division by zero error. This is important because directly dividing by (x2 - x1) can lead to an error when the points are vertically aligned.

Using this approach, we can efficiently determine whether a set of coordinates forms a straight line or not.


"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        else:
            x0, y0 = coordinates[0]
            x1, y1 = coordinates[1]

            for coordinate in coordinates[2:]:
                x2, y2 = coordinate
                lhs = (y0 - y1)*(x2 - x1)
                rhs = (y2 - y1)*(x0 - x1)
                if lhs != rhs:
                    return False

            return True



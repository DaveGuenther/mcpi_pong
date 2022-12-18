import numpy as np



class CollisionHandler:
    def __init__(self, colliders, collidables):
        self.__colliders = colliders[0]
        self.__collidables = collidables[0]

    def __edgeFacingHeading(self, heading, edge_normal):
        val = np.dot(heading, edge_normal)
        return True if val<0 else False

    def testCollisions(self):
        for ball in self.__colliders:
            heading = ball.getHeadingUnitVec()
            for this_rectangle in self.__collidables:
                for edge in this_rectangle.getSegments():
                    normal = edge.getNormal()
                    if self.__edgeFacingHeading(heading, normal):
                        intersection_point = ball.getHeadingSegment().interceptWith(edge.getSegment())
                        if (type(intersection_point)!=bool):
                            ball.collide(edge, intersection_point)
                            this_rectangle.collide()        


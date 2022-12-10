import numpy as np

class LineSegment:

    def orderPoints(self, axis):
        """
        Orders the points p[0] and p[1] ascending first by axis ascending
        """
        if axis=='x':
            if((self.__p[0][0] > self.__p[1][0])):
                p_temp=self.__p[1]
                self.__p[1]=self.__p[0]
                self.__p[0]=p_temp
        if axis=='y':
            if ((self.__p[0][1]>self.__p[1][1])):
                p_temp=self.__p[1]
                self.__p[1]=self.__p[0]
                self.__p[0]=p_temp            

    def __calcSlope(self):
        """
        Calculates the slope of the line segment
        """
        if self.__p[0][0]!=self.__p[1][0]:
            self.__slope=(self.__p[1][1]-self.__p[0][1])/(self.__p[1][0]-self.__p[0][0])
        else:
            self.__slope='vertical'

    def __calcIntercept(self):
        """
        Calculates the y intercept at x=0
        """
        if self.__p[0][0]!=self.__p[1][0]:
            self.__intercept=self.__p[0][1]-(self.__slope*self.__p[0][0])
        else:
            self.__intercept='vertical'

    def setPoints(self, p0, p1):
        """
        Given two points p0, and p1, this function sets the new line segment data, orders the points, and calculates slope/intercept for the segment
        
        p0      np.array()      Array with x,y positions of first point in segment
        p1      np.array()      Array with x,y positions of the second point in segment        
        """
        self.__p[0]=p0
        self.__p[1]=p1
        self.orderPoints('x')
        self.__calcSlope()
        self.__calcIntercept()

    def getPoints(self):
        return self.__p

    def __init__(self, p0, p1):
        """
        LineSegment Class is responsible for containing data and formula around definining a linesegment, determining it's slope, intercept, and also whether it collides with another segment.

        p0          np.array()      Array with x,y positions of first point in segment
        p1          np.array()      Array with x,y positions of the second point in segment (only appli)
        heading     np.array()      Array with x,y positions reflecting the normal vector of the line segment
        """
        self.__p=[p0, p1]
        self.setPoints(p0, p1)

    def getSlope(self):
        return self.__slope

    def getIntercept(self):
        return self.__intercept

    def interceptWith(self,other):
        """
        Returns the point at which both segments intercept if the intercept (np.array([x,y])), otherwise returns False if they do not intercept
        """
        x = self.__xInterceptWith(other)
        y = self.__yInterceptWith(other, x)
        if ((x!='invalid') & (y!='invalid')):
            return np.array([x,y])
        else: 
            return False

    def __xInterceptWith(self, other):
        """
        Calculates the x intercept with the other segment or returns False if the segments don't intercept

        other       LineSegment         This is an instance of an other line segment by which to test for intersection with this one.
        """
        self.orderPoints('x')
        other.orderPoints('x')
        if (self.getSlope()!=other.getSlope()): # make sure line segments are not parallel
            if (self.getSlope()=='vertical'): # this line segment is a vertical line
                if other.getSlope()==0: #other line segment is horizontal
                    other_point = other.getPoints()
                    if ((other_point[0][0] <= self.__p[0][0]) & 
                        (self.__p[0][0] <= other_point[1][0])): # test if this vertical line intersects with other horizontal line
                        
                        # Sort by y values and check if line intersects
                        other.orderPoints('y')
                        other_point = other.getPoints()
                        if ((self.__p[0][1] <= other_point[0][1])&
                            (other_point[0][1] <= self.__p[1][1])):
                            return self.__p[0][0]
                        else:
                            return 'invalid'
                    else:
                        return 'invalid'
                else: #other horizontal segment isn't horizontal
                    return self.getPoints()[0][0] # for a vertical line segment, x1=x2, so return either point's x value
            elif (other.getSlope()=='vertical'): # other line segment is a vertical line
                if self.getSlope()==0: #this line segment is horizontal
                    other_point = other.getPoints()
                    if ((self.__p[0][0] <= other_point[0][0]) & 
                        (other_point[0][0] <= self.__p[1][0])): # test if this vertical line intersects with other horizontal line
                        
                        # Sort by y values and check if line intersects
                        other.orderPoints('y')
                        other_point = other.getPoints()
                        if ((other_point[0][1]<=self.__p[0][1])&
                            (self.__p[1][1] <= other_point[0][1])):
                            return other_point[0][0]
                        else:
                            return 'invalid'
                    else:
                        return 'invalid'
                else: #other horizontal segment isn't horizontal                
                    if ((self.__p[0][0]<=other.getPoints()[0][0])&
                        (other.getPoints()[0][0] <= self.__p[1][0])):
                        return other.getPoints()[0][0] # for a vertical line segment x1=x2, so return either point's x value
                    else: return 'invalid'
            else: #neither line is vertical and we calculate a standard intercept
                x=(other.getIntercept()-self.getIntercept())/(self.getSlope()-other.getSlope())
                return x
        else:
            return 'invalid'

    def __yInterceptWith(self, other, x):
        """
        Meant to be called after __xInterceptWith() passing in the x value argument retrieved from that function

        other:      LineSegment     The other line segment that you are testing intersection with
        x:          float           This is the return value from __xInterceptWith()
        """
        if self.__slope=='vertical':
            other_point = other.getPoints()
            if ((other_point[0][0] <= self.__p[0][0]) & 
                (self.__p[0][0] <= other_point[1][0])): # test if this vertical line intersects with other line
                if (other_point[0][1]==other_point[1][1]):
                    return other_point[0][1] # other line is horizontal
                else:
                    return other.getYfromX(x) # other line is not horizontal
            else: 
                return 'invalid'
        elif x!='invalid':
            return self.getYfromX(x)
        else:
            return 'invalid'



    def getYfromX(self, x):
        """
        Given an x value on the line defined by this line segment, this function returns the respective y value at that x location
        """
        if self.__slope=='vertical':
            # line segment is vertical  
            return 'invalid'
        else: # line segment is not a vertical line
            return self.__slope*x + self.__intercept

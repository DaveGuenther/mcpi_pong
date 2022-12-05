class LineSegment:

    def __orderPoints(self):
        """
        Orders the points p[0] and p[1] ascending first by x, then by y
        """
        if((self.__p[0].x > self.__p[1].x)|(self.__p[0].y>self.__p[1].y)):
            p_temp=self.__p[1]
            self.__p[1]=self.__p[0]
            self.__p[0]=p_temp

    def __calcSlope(self):
        """
        Calculates the slope of the line segment
        """
        self.__slope=(self.__p[1].y-self.__p[0].y)/(self.__p[1].x-p[0].x)

    def __calcIntercept(self):
        """
        Calculates the y intercept at x=0
        """
        self.__intercept=self.__p[0].y/(self.__slope*self.__p[0].x)

    def setPoints(self, p0, p1):
        """
        Given two points p0, and p1, this function sets the new line segment data, orders the points, and calculates slope/intercept for the segment
        
        p0      np.array()      Array with x,y positions of first point in segment
        p1      np.array()      Array with x,y positions of the second point in segment        
        """
        self.__p[0]=p0
        self.__p[1]=p1
        self.__orderPoints(self)
        self.__calcSlope(self)
        self.__calcIntercept(self)


    def __init__(self, p0, p1):
        """
        LineSegment Class is responsible for containing data and formula around definining a linesegment, determining it's slope, intercept, and also whether it collides with another segment.

        p0      np.array()      Array with x,y positions of first point in segment
        p1      np.array()      Array with x,y positions of the second point in segment
        """
        self.__p=[p0, p1]
        setPoints(self, p0, p1)

    def getSlope(self):
        return self.__slope

    def getIntercept(self):
        return self.__intercept

    def xInterceptWith(self, other:LineSegment):
        """
        Calculates the x intercept with the other segment or returns False if the segments don't intercept
        """
        if (self.getSlope()!=other.getSlope()):
            x=(other.getIntercept()-self.getIntercept())/(self.getSlope()-other.getSlope())
            return x

    def getYfromX(self, x):
        """
        Given an x value on the line defined by this line segment, this function returns the respective y value at that x location
        """
        return self.__slope*x + self.__intercept
        
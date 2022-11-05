import ellipse

class Circle(Ellipse):
    """An ellipse with the same alpha and beta or just a circle"""

    def __init__(self, a: float, b: float, radius: float ) -> None:
        """
        Init a circle  object. The parameters come from
        (position[0]-self.a)**2+(position[0]-self.b)**2 = radius**2
        """
        super.__init__(a,radius,b,radius)

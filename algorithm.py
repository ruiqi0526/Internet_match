class Distinguish:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
    
    @property
    def func(self) -> float:
        '''
        Discriminant Analysis Function
        Logistic regression equation'''
        y_0 = -0.013 * self.a - 0.002 * self.b - 0.011 * self.c + 4.974
        return y_0
    
    @property
    def func1(self) -> float:
        '''The first kind of initial bayesian function'''
        y_1 = 0.088 * self.a + 0.013 * self.b + 0.045 * self.c - 13.367
        return y_1
    
    @property
    def func2(self) -> float:
        '''The second kind of initial bayesian function'''
        y_2 = 0.073 * self.a + 0.011 * self.b + 0.028 * self.c - 8.585
        return y_2
    
    @property
    def func1_1(self) -> float:
        '''The first kind of standardized bayesian function'''
        y_1_1 = self.func1 / ( self.func1 + self.func2 )
        return y_1_1
    
    @property
    def func2_1(self) -> float:
        '''The second kind of standardized bayesian function'''
        y_2_1 = self.func1 / ( self.func1 + self.func2 )
        return y_2_1
    
    @property
    def func1_1_1(self) -> float:
        '''The finally discriminant function  the first class'''
        X = 306.255 * self.func + 6.976 * self.func1_1 - 93.99
        return X
    
    @property
    def func2_1_1(self) -> float:
        '''The finally discriminant function  the second class'''
        Y = 27.975 * self.func + 3.421 * self.func2_1 - 4.235
        return Y
    
    @property
    def get_result(self) -> str:
        '''Judge the result according to the analysis'''
        if self.func1_1_1 > self.func2_1_1:
            return 'healthy'
        else:
            return 'ill'

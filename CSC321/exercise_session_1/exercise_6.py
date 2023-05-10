class mathSeries():
    
    def fib(self, n):
        if(n == 0):
            return 0
        if(n == 1):
            return 1
        
        return self.fib(n-1) + self.fib(n-2)
    
    
    def fib_with_max(self, n,  _max):
        if(_max < 1):
            return 0
        if(n == 0 or _max == 0):
            return 0
        if(n == 1  or _max == 1):
            return 1
        
        return fib_with_max(n-1, _max - 1) + fib_with_max(n-2, _max - 2)
    
    
    def prime(self, n):
        res = []
        
        for i in range(2, n):
            for j in range(2, (i//2)+1):
                if (i % j) == 0:
                    break
            else:
                res.append(i)
        return res
    
    
    def factorial(self, n):
        if(n == 0):
            return 0
        if(n == 1):
            return 1
        
        return n * self.factorial(n-1)
    
    
    def geometric(self, n):
        res = []
        for i in range(1, n):
            res.append(1/(2**i))
        return res
    
    
    def harmonic(self, n):
        res = []
        for i in range(1, n):
            res.append(1/i)
        return res
    
    
    def other_series1(self, n):
        res = []
        for i in range(1, n):
            res.append(((-1)**(i+1))/i)
        return res
    
    
    def other_series2(self, n):
        res = []
        for i in range(1, n):
            res.append(((-1)**(i+1))*4/(2*i)-1)
        return res
    
    
    def other_series3(self, n):
        res = [2]
        for i in range(1, n):
            k = i * 2
            res.append(k*k/(k - 1) * (k + 1))
        return res
    
    
    def other_series4(self, n):
        res = []
        for i in range(1, n):
            res.append(((-1)**i)/self.factorial(i))
        return res

mathy = mathSeries()
print(mathy.fib(5))
print(mathy.fib(20, 10))
print(mathy.prime(20))
print(mathy.factorial(5))
print(mathy.geometric(5))
print(mathy.harmonic(5))
print(mathy.other_series1(5))
print(mathy.other_series2(5))
print(mathy.other_series3(5))
print(mathy.other_series4(5))


    
    
    

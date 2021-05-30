import math
""" Note: Numerators and Denominators might become constant after ceratin number of iterations """
def Farey_Algorithm(n:float,iterations:int)->tuple:
    """[Gives approximate fractional representation of a irrational number]
    Args:
        n ([float]): [float number(assumed irrational) which is entered whose fraction is returned]
    """
    decimal,integer=math.modf(n)
    start_num=0;start_den=1;end_num=1
    end_den=1;avg_num=0;avg_den=1
    for i in range(iterations):
        avg_num=start_num+end_num
        avg_den=start_den+end_den
        avg=avg_num/avg_den
        
        if decimal<avg:
            end_num=avg_num
            end_den=avg_den    
        
        elif decimal>avg:
            start_num=avg_num
            start_den=avg_den
    
    numerator=avg_num+int(avg_den*integer)
    denominator=avg_den
    return (numerator,denominator)

#Test
num,denom=Farey_Algorithm(math.pi,100)
print("Fraction is: {n}/{d}".format(n=num,d=denom))

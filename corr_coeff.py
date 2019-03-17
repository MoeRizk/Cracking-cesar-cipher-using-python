
import math


def corr_Coeff (X, Y):
    sumX = sumY = sumXY = squrSumX = squrSumY = i = 0

    while i < len ( X ):
        sumX += X[ i ]
        sumY += Y[ i ]
        sumXY += X[ i ] * Y[ i ]
        squareSumX = 0
        squareSumY = 0
        squareSumX += X[ i ] * X[ i ]
        squareSumY += Y[ i ] * Y[ i ]
        i += 1

    corr = (float) ( len ( X ) * sumXY - sumX * sumY ) / (float) ( math.sqrt ( (len ( X ) * squareSumX - sumX * sumX) * (len ( X ) * squareSumY - sumY * sumY) ) )

    return corr

#
# X = [ 20 , 21 , 36 , 19 , 23 ]
# Y = [ 22 , 27 , 31 , 56 , 32 ]
#
# print(abs(corr_Coeff( X , Y )))

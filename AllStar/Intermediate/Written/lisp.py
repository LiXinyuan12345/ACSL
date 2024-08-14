def CDR(ary):
    result =  ary[1:]
    print("CDR({}) ==>  {}".format(ary, result) )
    return result

def CAR(ary):
    result = ary[0]
    print("CAR({}) ==>  {}".format(ary, result) )
    return result

def REVERSE(ary):

    src = ary
    ary.reverse()
    print("REVERSE({}) ==>  {}".format(src, ary) )
    return ary

#M = [1,[2,3], [4,[5],[6,7]]]
#print(  CDR( REVERSE(CAR(REVERSE(CDR(M))))))
    
#M = [ ['a','b',['d']], ['b',['c','a'],'d'], [ ['a','b'],['b'],'d'] ]
#print(  CAR(CDR(CDR(M))) )
   
#M = [ 'P' ,['R','O'],['G',['R','A'],['M','M'],'I'],['N','G'] ]
#print( CDR(CDR(CAR(CDR(CDR(M))))) )
        
Z = [ 'C' ,['O','N'],['N',['E','C'],'T'],['I',['C',['U'],'T']] ]
Y = CAR(REVERSE(CDR(CDR(Z))))
print( CAR(CDR(CAR(CDR(Y)))))

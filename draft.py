
#put the borders
# map=arange_borders(map)

def arange_borders(m):
    #up border
    for i in range(15):
        if(m[i]!='B'):
            m[i]='-'
    #down border
    for i in range(165,180):
        if(m[i]!='B'):
            m[i]='-'
    #left border
    for i in range(12):
        if(m[i*15]!='B'):
            m[i*15]='-'
    #right border
    for i in range(1,12):
        if(m[i*15-1]!='B'):
            m[i*15-1]='-'

    return m

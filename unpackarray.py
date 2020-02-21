def unpack(data):
    
    goodlist=[]
    for stuff in data: 
        
        if type(stuff) is list:
            asd=unpack(stuff)
            for i in asd:
                goodlist.append(i)
            
        else:

            goodlist.append(stuff)
        
    return goodlist
        

a=[[1,[2,3],4],5,6,[[]],[7,6,7],['asdfasf','drerewrwr'],'kjkjkjkj']

b=unpack(a)

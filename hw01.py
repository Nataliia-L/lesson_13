import random
a = (min, max, sum, len)
func = random.choice (a)
print ('Function:', func)

def get_result (*args):
    print ('List of arguments:', args)
    var_new = [float (i) for i in args]
    var_new = []
    for i in args:
        var_new.append(float(i))
    return func (var_new)
    
var_new = get_result(1, 2, 5.1, 8, '5')
print ('Result:', var_new) 

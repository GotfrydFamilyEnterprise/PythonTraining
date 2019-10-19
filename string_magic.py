def string_together(v1,v2):
    # print(f" variable1: {v1}, variable2: {v2}")
    # result = v1 + v2
    result = "".join([v1,v2])
    # print (result)
    return result

def string_apart(vcool):
    result = vcool.split(" ")
    return result

def string_replace_words(phrase,old,new):
    import ipdb; ipdb.set_trace()
    return phrase
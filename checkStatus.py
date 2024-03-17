def check_status(a, b, flag):
    if (a >= 0) ^ (b >= 0) and flag == False:
        return True
    elif a <= -1 and b <= -1 and flag == True:
        return True
    else:
        return False
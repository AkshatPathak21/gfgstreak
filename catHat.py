def cat_hat(str):
  ##your code here##
  ##You need to write complete code this time 
    ccnt = 0
    hcnt = 0
    for i in range(len(str)-2):
          if str[i:i+3] == 'cat':
            ccnt+=1
          if str[i:i+3] == 'hat':
            hcnt += 1
    if ccnt == hcnt:
        return True
    else:
        return False
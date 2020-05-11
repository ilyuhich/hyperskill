def heading(hsym, hnum=1):
    if hnum <= 1:
        hnum = 1
    elif hnum >= 6:
        hnum = 6
    return '#' * hnum + ' ' + hsym


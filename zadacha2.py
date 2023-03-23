for x in True, False:
    for y in True, False:
        for z in True, False:
            print(f'{x = }; {y = }; {z = }    RESULT: {not(x or y or z) == (not x and not y and not z)}')
        

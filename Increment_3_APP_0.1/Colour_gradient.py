


def colour_1 (canvas):
    global r1, g1, b1, r2, g2, b2, steps, rdelta, bdelta, gdelta, r6, r7, rdelta4
    r1 = 135
    g1 = 0
    b1 = 0
    r2 = 0
    g2 = 0
    b2 = 0
    steps = 336
    rdelta = (r1 - r2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    gdelta = (g1 - g2)/ float(steps/10)
    r6 = 200#i2&i7&i1&i8
    r7 = 0
    rdelta4 = (r6 - r7)/ float(steps/10)#new
    
    for i in range((steps/12) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
    
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
        
        color4 = '#%02x%02x%02x' % (int(r6), int(g1), int(b1))

        r6 -= rdelta4#new
        g1 -= gdelta#new
        b1 -= bdelta#new
    
        ia = steps/12 -i
        canvas.create_rectangle(0 , ia , 100 , ia + 6, fill = color, outline = "")
        i0 = steps/12 +i
        canvas.create_rectangle(0 , i0 , 100 , i0 + 6, fill = color, outline = "")
        i1  = (steps/4)- i 
        canvas.create_rectangle(0 , i1 , 100 , i1 + 6, fill = color4, outline = "")
    
        i2  = (steps/4)+ i
        canvas.create_rectangle(0 , i2 , 100 , i2 + 6, fill = color4, outline = "")
        i7 = (float(steps/1.33333333))- i
        canvas.create_rectangle(0 ,i7 , 100 , i7 + 6, fill = color4, outline = "")
        
        i8 = (float(steps/1.33333333))+ i
        canvas.create_rectangle(0 ,i8 , 100 , i8 + 6, fill = color4, outline = "")
        i9 = (float(steps/1.090909091))- i
        canvas.create_rectangle(0 , i9  ,100 , i9 + 6, fill = color, outline = "")
    
        ilast = (float(steps/1.090909091))+ i
        canvas.create_rectangle(0 ,ilast ,100 ,ilast + 6, fill = color, outline = "")
        
        
    r3 = 175#new
    r4 = 250#new
    rdelta2 = (r3 - r4)/ float(steps/10)#new
    r5 = 175
    r6 = 0
    rdelta3 = (r5 - r6)/ float(steps/10)#new
    for a in range((steps/12) + 1):#new
        
        color2 = '#%02x%02x%02x' % (int(r3), int(g1), int(b1))#new
        r3 -= rdelta2#new
        g1 -= gdelta#new
        b1 -= bdelta#new
    
        i3  = (float(steps/2.4))+ a
        canvas.create_rectangle(0  ,i3  ,100  ,i3 + 6,  fill = color2, outline = "")
        i6 = (float(steps/1.7142857))- a
        canvas.create_rectangle(0 , i6  ,100  , i6 + 6, fill = color2, outline = "")
    
        color3 = '#%02x%02x%02x' % (int(r5), int(g1), int(b1))#new
        r5 -= rdelta3#new
        g1 -= gdelta#new
        b1 -= bdelta#new
    
        i4 = (float(steps/2.4))- a
        canvas.create_rectangle(0 ,i4 + 5, 100 , i4 + 6, fill = color3, outline = "")
        i5 = (float(steps/1.7142857))+ a
        canvas.create_rectangle(0 , i5 + 5, 100  ,i5 +6 , fill = color3, outline = "")





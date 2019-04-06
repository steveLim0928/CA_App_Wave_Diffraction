
def colour_1 (canvas):
    r1 = 0
    g1 = 0
    b1 = 0
     
    r2 = 200
    g2 = 0
    b2 = 0
    
    steps = 340
    rdelta = (r1 - r2)/ float(steps/10) 
    gdelta = (g1 - g2)/ float(steps/10)
    bdelta = (b1 - b2)/ float(steps/10)
    
    
    color1 = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
    for i in range((steps/14) + 1):
        
        color = '#%02x%02x%02x' % (int(r1), int(g1), int(b1))
        
        r1 -= rdelta
        g1 -= gdelta
        b1 -= bdelta
    
        canvas.create_rectangle(0, i, 340, i + 1, fill = color1, outline = "")
        i1  = (steps/7)- i
        canvas.create_rectangle(0,i1, 340, i1+ 1 , fill = color1, outline = "")
        i2  = (steps/7)+ i
        canvas.create_rectangle(0,i2, 340, i2 + 1, fill = color, outline = "")
        i3  = float((steps/3.5))- i
        canvas.create_rectangle(0, i3, 340, i3 + 1,fill = color, outline = "")
        i4 = float((steps/3.5))+ i
        canvas.create_rectangle(0, i4, 340,i4 + 1, fill = color, outline = "")
        i5 = float((steps/2.33333333))- i
        canvas.create_rectangle(0, i5, 340, i5 + 1, fill = color, outline = "")
        i6 = float((steps/2.33333333))+ i
        canvas.create_rectangle(0, i6 , 340, i6 +1, fill = color, outline = "")
        i7 = float((steps/1.75))- i
        canvas.create_rectangle(0, i7 , 340, i7+1,fill = color, outline = "")
        i8 = float((steps/1.75))+ i
        canvas.create_rectangle( 0, i8 , 340,i8+1, fill = color, outline = "")
        i9 = float((steps/1.4))- i
        canvas.create_rectangle( 0, i9 , 340,i9+1, fill = color, outline = "")
        i10 = float((steps/1.4))+ i
        canvas.create_rectangle( 0, i10 , 340,i10+1, fill = color, outline = "")
        i11 = float(steps/1.166666666667)- i
        canvas.create_rectangle( 0, i11 ,340,i11+1, fill = color, outline = "")
        i12 = float(steps/1.166666666667)+ i
        canvas.create_rectangle( 0, i12 ,340,i12+1, fill = color1, outline = "")
        i13 = steps - i
        canvas.create_rectangle( 0, i13 ,340,i13+1, fill = color1, outline = "")
    


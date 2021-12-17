from PIL import Image

class BreakOutOfALoop(Exception): pass

x_axis = 1000
y_axis = 1000

fractalImage = Image.new('RGB', (x_axis, y_axis), "white") 
fractal_pixels = fractalImage.load() 

fractalImage_path = "C:/Users/dinok/OneDrive/Bilder/Fraktale"  
areaImage_path = fractalImage_path + "/area"

X0 = -2.5
Y0 = 1.j * 1       # the area verticies
X1 = 1
Y1 = -1.j * 1
area_list = []

def fractal(n, X0, Y0, X1):      # searching for new branch
    branch = []          
    k = (X1 - X0) / x_axis      # pixel size
    b = 20             # the number of black points int the set i am looking for
    
    for y in range(y_axis):         
        try:
            for x in range(x_axis):                                                 
                c = X0 + k * x + Y0 - k * y * 1.j    # new c     
                z = c

                for m in range(n):                
                    if abs(z) <= 2:
                        z = z * z + c                  # new z
                    else:
                        break
                if abs(z) <= 2:                                          
                    branch.append((x,y))                # the coordinates for those points   
                else:                                      
                    if b < len(branch) < 50: 
                        raise BreakOutOfALoop       # break if a branch was found
                    branch = []
        except BreakOutOfALoop:
            break
    return branch, k
                           
def new_area(branch, X0, Y0, X1, k):    # calculating new area        
    X0 = X0 + k * branch[0][0]
    Y0 = Y0 - k * branch[0][1]
    X1 = X1 + k * branch[-1][0]              # new area verticies  
    return X0, Y0, X1

def create_picture(n, X0, Y0, X1):       # calculating final image and draw
    
          
    k = (X1 - X0) / x_axis        
    r = 1

    for y in range(y_axis): 
        # if y % 50 == 0:
        #     print(y)         
        for x in range(x_axis):                                           
                                                         
            c = r * (X0 + k * x + Y0 - k * y * 1.j)          
            z = c
            v = 511
            
            for m in range(n):
                if abs(z) <= 2:
                    z = z * z + c                    
                    v = v - 1           
                else:
                    break
            if abs(z) <= 2:                      
                fractal_pixels[x, y] = (0, 0, 0)              
            else:                                          # coloring
                if v <= 255:

                    fractal_pixels[x,y] = (0, 0, v)
                if v <= 511:
                    fractal_pixels[x,y] = (0, v - 255, 255)   
p = 3
n = 511

for i in range(p): 
    
    areaImage = Image.new('RGB', (x_axis,y_axis), "white")
    area_pixels = areaImage.load()                              # image load

    branch, k = fractal(n,X0, Y0, X1) 
    X0, Y0, X1 = new_area(branch, X0, Y0, X1, k)    
         
    file_name = "/" + str(i) + "_" + str(n) + "_" + str(x_axis) + "_" + str(y_axis) + ".png"                    # image save
    areaImage = areaImage.save(f"{areaImage_path}{file_name}")           

create_picture(n, X0, Y0, X1)
          
file_name = "/" + str(p) + "_" + str(n) + "_" + str(x_axis) + "_" + str(y_axis) + ".png"                   # image save
fractalImage = fractalImage.save(f"{fractalImage_path}{file_name}")
# Mandelbrot-zoom
Variablen:
n = Anzahl der Iterationen
c = aktuelle Komplexe Zahl
z = aktuelle Wert der Folge
x_axis = x Koordinate des aktuellen Pixels
y_axis = y Koordinate des aktuellen Pixels
X0 = x Koordinate des Punktes an dem der aktuelle Bereich beginnt
Y0 = y Koordinate des Punktes an dem der aktuelle Bereich beginnt
X1 = x Koordinate des Punktes an dem der aktuelle Bereich aufhört
branch_length =  Anzahl der Punkte, die ohne Unterbrechung der Menge zugeordnet werden
branch =  Punkte, die der Menge in einer Spalte oder Reihe zugeordnet wurden
v = input für den Farbwert des aktuellen Punktes
number_of_zooms = Anzahl der zooms
areaImage = Bild des aktuellen Bereichs
fractalImage = Bild des finalen Bereichs

Variablen aus dem Update:
branch_X/Y =  Punkte die in einer Reihe/Spalte der Menge zugeordnet wurden
pixelsize = Länge eines Pixels im aktuellen Bereich
branch_points = alle Punkte, die der Menge zegeordnet wurden
lowest_x = kleinste x Koordinate eines der Menge zugeordneten Punktes
lowest_y = kleinste y Koordinate eines der Menge zugeordneten Punktes
highest_x = größte x Koordinate eines der Menge zugeordneten Punktes
highest_y = größte y Koordinate eines der Menge zugeordneten Punktes
lowest_branch_x = kleinste x Koordinate eines Punktes aus der Liste branch_X
lowest_branch_y = kleinste y Koordinate eines Punktes aus der Liste branch_Y
highest_branch_x = größte x Koordinate eines Punktes aus der Liste branch_X
highest_branch_y = größte y Koordinate eines Punktes aus der Liste branch_Y
count = Anzahl  der Stellen an denen gilt Breite > branch_length

Ich möche die Mandelbrot Menge visualisieren. Anfangs hatte ich nur die Funktion create Picture und habe X0, Y0 und pixelsize manuel eingegeben. Es hat funktioniert, aber das Problem war, neue interessante Bereiche zu finden in denen man auch etwas sehen kann. Die Idee ist jetzt, dass ich die Punkte speicher, die der Menge zugeordnet wurden, dann einen Bereich berechne (new_area) in dem die Punkte liegen und dann diesen Bereich als neuen Ausgangspunkt nehme. Dann wiederhole ich das Ganze bis ich number_of_zooms erreiche.

branch_Y und das was dazu gehört habe ich noch nicht weiter gemacht, sollte aber ähnlich wie branch_X funktionieren

https://stackoverflow.com/q/69716125/17109058

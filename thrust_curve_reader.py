from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

infile = "curve1.png"
outfile = "curve1.csv"
#the graph axes
x_size = 20
y_size = 5

plot = Image.open(infile)
plot = plot.convert("RGB")
#plot.show()
print(plot.size)
imarr = np.asarray(plot)
print(imarr.shape)
binimg = np.empty(plot.size[::-1])
for i,row in enumerate(imarr):
    for j,px in enumerate(row):
        #print(px)
        yellow = px[1] > 100
        binimg[i,j] = yellow
print(binimg.shape)
#transpose to average the rows (which averages the columns)
tran = binimg.T
yvals = []
for row in tran:
    line_spots = np.argwhere(row==1)
    if len(line_spots) > 0:
        center = sum(line_spots) / len(line_spots)
    yvals.append(y_size * (1 - (center / len(row)))[0])
xvals = [x_size * i / plot.size[0] for i in range(plot.size[0])]
#plt.imshow(tran,cmap = 'gray')
plt.ylim(0,y_size)
plt.xlim(0,x_size)
plt.plot(xvals,yvals)
plt.show()
with open(outfile,"w") as f:
    for pair in zip(xvals,yvals):
        f.write(str(pair[0]) + "," + str(pair[1]) + "\n")

import tkinter as tk
from tkinter import messagebox, ttk, simpledialog, filedialog
import subprocess
import ipaddress
import sys
import os
import re
import base64
from io import BytesIO
from PIL import Image, ImageTk

# ========= base64 아이콘 문자열 =========
ICON_BASE64 = """
iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAYAAABccqhmAAAl9ElEQVR42u2deZRdVZ3vv7+9zzl3
qOGmMpI5gUBIBQFtEGSwgkoHfe30tGJ4PNS2G9SOhIhtqy2+Sj3t1dj9mikgELVpxQFSos9lK9og
Ia1MBoHkkRIiJKkiZKokNd/pnL1/749zb6US01BJ3anu/X3WqoWLhXVq33t+3/2b9m8DgiAIgiAI
giAIgiAIgiAIgiAIgiBUGVRby2WSr1x4/VcEABGLAEzYL5AJK6DQ/Bi1YBk2dYLRjPALbScrb7gw
po2iLbSNFkBtAoD8e9QOBqpHICa+ALSxQicIzSC0w7zel3PqtYcTgVaKPGbODog3IBxtDF4jc4yo
+6ZJva/7H7ayRvNjBCyzE10QaMIaPaCOZ/CLvjQwLUiml7BSpxFF59kgebZSTpNlo4ixFEQaYHnb
heP7/6QBNi8z1BCBfVbOZmX8HtaxrU68/uVXtmMPOsgc/T5udNDZw+hotRNNDGhCufYdUFiBoz7k
U1cn5xnKnEdElzLMxcx8hnKiCdIeoDRgA4BDz5+DDBgM2fqF100BaC/cJwBAuQBbsPXBQToJUruI
1NNM6jcunKdn10e2b2qnYOQXbGCNbeCJEm7SxNntj3zI8z430Azm95C1HwT4XOXG41AabLJgkwFM
YAEwA0w0ao0MJdYvjMEsbN5LZB7JHCsorUh7IB0BANjsoCFS2xn0cyb6SferjU+PeAetHCrIsd6C
CMAJxva5D3Dh6n0z2Kt/H0zwcWb7VhVpdNhkwUEKYGPCrZ0IYAWQmLlQFDcUDM4JBIFIkxMFOTGw
nwTAncyqA8T3d93c+OJRSekKFQKq2Cx+7gObs/rQWVq7HwPM1cprmMEmC/aHwcwBicEL5Y4YmBmA
BaDJjRE5UdjsUAakNyjQfTtvbnh4lCdbcZUoqqi/pZWPMnxH6RuYcJXy6j3ODsKarCEQhTu9OPNC
xW1eFmAGaa0ijWHewAQPK+J/3nnzpIdHQoMOVEyykCrG3c8p45xPds92Yo1fZcJVyq3zbKYv3O0B
nTN8QZgAnoG1AJGKNChmC2Z+mALzlV23JZ4+IgTlDwvKb1BtGx20Xxbgz+5xF7R85FMM50blRqbb
dB/A1oCUkt1emMBaYMAgFWlUbLM+W75bp3q+tuPuRQfCja+8fQTlM6y2NgWsBdrJLrj+4AWsI7cp
N3oBZ4dgjR9QWIcRwxeqJTwwINIqOgnsp/Yw28913TLp/nJ7A+UxsFELXrDmcBtI30jadUx20BBI
iasvVK0MMBvleA7pGNik789mXvvMnjubD6GNndGl7uoVgJzxz1uzayZR4l4daVxuUodDVwn57gtB
qGYZsAwiq6KTtfWTf2Sb+svuW2c8Xo6QgEqc7HPQTsGC6/cvh47cS05spk33ByBoKeUJNVg0CJQb
d5g5gDGf77qt6dZSlwupZKerWsPa/rzrD1yjvcb1bNLgIGNASnZ9oZa9AQtSpONTyaQOfbPr1qnX
HlsZm+ACkDta2U52wZpDt5ATW2P9pAWHVRJ5AwSBGYBRkYRj/fSvON13Zfdd83tLIQJUqp1//pqD
63VsyjUmedBI954gHD8kcOLTHJMZ3MzpvuWlEAFV9J0/b/zRydeYZI8PsMT7gnC83ZiUE6R6fOXG
zqfopF/N+3RXE9rJjuQFJo4HwNTSBr2pnYIjxn8wAJEjX7MgvLEnoKNNjvWHNxsMXrG7cW4fgKIk
BqmY2f55q/ff4tRNXxPu/OTKVysIJyACsSmOSfc/1X3blIvAnLPWwpYIVVHq/O0UzLt+3zXKa1hj
kocCALLzC8IJhgM2dSjQkcYL5685eA+IGK2Ft1dVjCafuateu1x5k9azn7SAlZhfEE5KBZRjMn2+
jk+5Zv51+9eig0xLGzsVGgKwAsALV++fbnVkC4Gms8mylPoEYbwlQmXIjTkm1ffnr945++FCnh0o
nHFuCMXEKvc+5dbNYJOxYvyCMP5gAGwVbMDKi9+3cPW+GeE8gcJUBgryS1raNjpYQWbB6v3/S0Wb
LjfpvkA6/AShcAkBDtJWuXUzrNL3AcT5Dbf8IUCuUWH+dQfeDC/2NExWgY00+ghC4aOBQMWmOCZ5
4DPd62beWYhQQI272acT1NLGDiv6tiLtgg3E+AWhKF07mrMDhty6f5y3Zt+p2IBxNwmNTwBybb47
Dx/4pI42vdlmB+VIryAUMRawJgvlxBrIqq+DiNE5Pi+expX1Z/D8VQdmIOJ2ElSCbZZk9xeE4o8Z
I69RI92/fNe6Gf8xnlBAjWP3JxAxNN+kvMYmazIsxi8IJRk5SrABW61vX3Td9kh4+e3J3XytTjrx
1wG74PqexXDjK226z1I4vFMQhFJUBfxhq71JiwNKrEQ72ZPtEjw5o+0EAcTM5u+VE4swG5YBnoJQ
WhVgk2ar9Jea29jDBtiT8QLUye7+868/uARO7CM2MyC7vyCUzQtILB7uO/Q/TvaswAn/H1oAldv9
/1q59RFmY2X3F4TyNAnC+gw2qwAgzAUUtQoQuhgzr90zxY1HtylS09j6UvcXBJTv3DC5cXCQemfX
bdMeO9GKwIl5AG3QAHEkFv2gjiSmW5O1YvyCUM6CACzpiGLCtQDQ2lpMD6CNFbAW8/pWPand+vOt
P2Sl8UcQynydNmkwMIxscHrXN2bsCz31sQ0OUSfU+NNOduHBVYtIeedafxhi/IJQAd2B1ljlNdbD
xRUA0NIGXfAQoKUt/G/Zofcrr8FjZiMfviBURi4QbMFAKwBsAmzBBWATYNG6QVvmD8FkQCSZf0Go
EBT7wyByL5m7qmtWODx0bD0BaszZ/3ayc+a84xRSzps4SBV5pLggCCfUFMSBIbeuUem6CwBgrD0B
asyn/gBoy+eTG48zGyPZf0FAJQ0OY1IaIG4BgJZmFM4DOPLL7DJSDpjB8pELQiWNCoCCyQKwl6CN
1aa1MAUTgE1rYdCy0QHUJTCZ8GGCIFSSAhAHKYDcM2cdeG02iHgscwPVmOJ/Ij51yZmTmXA6mwwg
CUBBqLw8gDWWnFid68SWjhzZH7cA5OJ/o73TlI7VszHS/ScIFdsV6IGUPWeseYA3FoD8L3HMEtKe
4vAqY0EQKlIFLJi5GQCmL33jXJ0aw+m/vIuxAOHdniIAglCZDUEENmCi+QDQsa0AApDvKmLCUlhf
GoAEoYI1gE0GABYu/sQfGtD+xqPCxp7Nt3aqbP6CUOG1ALYAkEhF4s5YDgSNvROQFIsACMLEkAHf
OLoAfQBhC/D863clCFjKQUZagAWhoucE+lbpWCISc5sBvGFL8JiMmbOKmOGIByAIE+JacbKGnIKe
BiQS6xeEiXSncGmvBxcEYcIhAiAIIgCCINQiTi0uWuWuMKXC9F/DMkrSIK0o/EHt9bjnz7yHP2K3
IgDjMfxkhpEJAGPH/yo5ihDzCBG3uEJABCSzjFS29l5/R4ftp44GPIfg6NB1LaX4igBMcLQKDcgP
gOY5Di441cWsyWpcd6QzgBf3BHj6FR9dPRYNMYKjwpey0MKVzDKWLfFw4SIXlmvLE/jDngC9w4ze
YYtdPQZ9SYZvAEcBMY/g5d5iY8WgRQCOu0sDfSlG8ywHX3xfHO9cGkGkgCs/OGjx42cy+D8/H8ZQ
mhHzqKAvo8p5LcuWePjUO2M1+7JaC+zps3jlQIDndoXCu7U7wJ4+C0cBdRGCViIEIgDHGH9vknHh
Ihff/5sEJsVpZLfgwoxiwtQGhWsvi+GC01x8ZF0/BlIWUZcK6gnkQ4DAAoEN11VTmWoClALmTFaY
M9lDy5keAGBvn8WmF7P46e8zeHy7j4FhRkOM4KrwcxJqWAAUAYMZxlvmO/jBqgQSMUJgwlhSq4IO
ZERggXPmOdiwOoEP3dqHTBA+o5DxqaIjhu+oGk0Gci7uz30eMycprLwwipUXRtH5WoBvP5bCg5sz
ODTESMTFI6jpMqDl0FBuvbohNH4bGj+KkKBzNeAb4Oy5Dv7+/XUYSFlokheswIMvQRQKq6NCAWDO
eXMMNM928C9XNeBXX2jCX7ZEwQz0JRlayfXVNScAWgFDacZlSzwsnePAlMBtzicAP3heFAunaaR9
GZ5WiltxtMrdlJ0Tg8UzNW6+qgH/97OT8I5mD73DDIvCen0iABNgtwgs48/PjoBLNMaIKHzOpDjh
bad7SGa5Juv25Qz5tDoiBG9e4KBjdQL/dGU9rAWGM1wUD1AEoELdf88hnHGKDl3H0l3QAAZw5kwN
Y1lczzILgbXAXy+L4SefTeC06RqHh7gm8yc12wpsuTzeh5HmlIoQApWrBpy30MUvPt+EK872cHiY
JRyoFQGgGnuugOPmZowFEnHCD1YlcM1lMfQMWAkHavUsgFB75EMCZuDrK+tBAL7xSBLTG1VN9wuI
AAg1FRJwrgnsppX1YADrH01hSj3VrAhIJCSg1sqGKlcyvGllPZYtcdGXqt2cgAiAUJMiAABg4FvX
NGJuk0LKr82j1iIAQs2GA5aBKfUKd3y8EcbU5qV3IgACajkxGFjg4jNcfOl9dehL2prrERABEGpb
BHKewGcuj+Pc+S4GMwylRAAEoWbyAczhIbH//eH6MAxgEQBBqKlQwDBw6WIX71zqYaCGqgIiAIKA
I7v+6uXxkWPGIgCCUGOdgm9b5OLyN3kYSNeGFyACIAijTnIC4elB8QAEATXYKszA20538aa5DpKZ
6m8OkrMAwrh2TFuEizoIR1p2UeKKQGCBqEtY/iYPz+0aRl1EleVIuXgAQkUbvrFHz+cr5I9WRzr1
Sm18ec159zkR1EWo6uc6iAcg4EQHrCgKG2gODlq8sDvAC7sD+KYwMxAshzP9zpzl4LTp+qhnlioM
AIDFszTmTdHoPmQRcau3KiACIIwZY8Pd+cCAxT//exL/8UIGuw/b3FTewlmIVoTJdYSLzvBww7vj
OHe+M/LsUoQBhoGYSzh3voPt+zLhRS8iAIIYP7D11QBX39WPXT0GjTGFSXHK7fxU0JJ8YIF/fy6D
R17I4OarGrDybdGSiQBzuJyz57m4/8k0qIrnO4kACGNyy7UCtnYHWLGuH33DdmSSTjEv3ZhcT/AD
4DPfGQQIWHlhaUQgb+5LZ2s4DkkSUEDN18YPDFh89O5+9CYt6mME3xQ/Lg5MaOz1UcJn/m0Qv33J
L8lNP/k8wBmzHExrUPBt9d7vIAIgjCnpd8tDSezoMUhEw+vVSu19aAWs/fEQTAkTgnWR8LZnFg9A
qNXdXyugZ9DiF1sySMTC3bAc+Ye6COGF3QGe2O6HiTpb/KMBngZmJBQCU71TnkUAhDe8U6Fzd4Dd
hy08p3y7oSIglWU8vj07+uxOUY8IR13CKZMUfMMSAgg1e0AOL+wOyn7LEQNwNaHzteCoOL3YBLa6
73gQARDekJRfOXFwyodc8CICIJSSyXUEpco/KIc5/FtQW0N7RAAElPV6szfNdeBqKqsXkL/t+aw5
zlHlyVK1BosACDV7k07zbAdnnKLLOjvfMNAYI7zrrEjRX1zmMBE4lGHsOGDgudXbDCQCILxuNtzm
SnBXvi2GoVR5xma7GuhLMi5r9rBklg57E0rQDcgMJDNc1V6ACIAwpgs0rn1HDO86y8OBQYZXwgZy
RwNDacYpCYWv5qf2lqj6cXDQYijD0CIAQi17AZQzxHs/mcDFZ7jY12/h6rBJqBi2QTnh8RygP8lI
xBUeuC6B+VM1uARxeV5k/vBagN4kV3U3oAiAMObGmElxwg9WJfAX50ZwYMBiIMUIbGiQhfyxHDb9
7OuzOP0UjQ2rEzh7bngkuBTueN7Wt71mYKq4CUhOAwonHAokYqEI/Oh3afzodxls6Q7QN2zDhhkq
jPUl4oTFMx184LwoPnpJFPVRKtlR4NGzAZ/v8sPqB0QABOGoefkffmsUH35rFIeGLF7ZbwrWMWcZ
WDBVY2aTGtnt8weCUKJeA0VAf4qxbXeAqFfdx4FFAISTulo7745PqVeYUl8c6zSjwguU+PTjszt9
vNZr0RAVARAEHO8ijdGTgQvefEMo28UcBOAXz2fgG4YiEQBBeF2PoFrKZJzrLzg8zHhkWxb1EVX1
U4GlCiAIo7oNCcDD/y+DnT0GUbf67wgUARCEUcm/bACsfzSFqFvdrr8IgCDgT5N/P3sug2d3+aiP
iAAIQs3s/vlrwe58OIlIjez+IgCCMGr3/+ETaTzfFaAuIgIgCLVj/Ao4NMS46WfDiNeQ8YsACCIA
ucz/jR2D2NdnEXWqP/MvAiAICGN+RwH3/mcKP3gijaY6QmAhI8EEATVw16GjgOe6AnylYwhNddXf
9CMCIAijLjo9PMz4+D39sJwbeioCIAi1YfwDKcbVd/Vjb59FzAtHn0GmAgtCbRj/lXf044k/+mjM
zRqAjAUXhOo3/p4Biyvv7McTL/uYWl97ST/IaUABNdbllx8o8vudPv7qmwPY02sxpT684rzWEQEQ
qn7X1wR867EU2n88DGMZDbHSXnEuAiAIJbxE1OYNXwH7ByzWPjiEHz6ZxqS4gqtrO+YXARCq3tXX
CvANcN9vU7j5oST29lpMrVcwtvDTi0QABKHMRg8ccfV9Azy4OY31j6bwfFeAuEc12eEnAiBUlVsP
Dv/JuX/mh4Xmx5H1DFr8amsW925K4dldASIu0FQXHuwR4xcBEMZpgOXskssPCSXgqNnjvcOMzTt8
/HJrBo9uy2LXQYuoC0yuD28yllhfBEBAYabklvN2nFSWkfaBQ0MWL+0N0PmawfNdPl7YHWBPb3gp
SV2EMLU+3PHF8EUABBRuUEbn7gA3/mgIsTJdkrGrx2AwzUhlGb3DDGsZjiZEXUJDlMJbjMXVFwEQ
inBJJoWHZh7amkVDmYZleA6gFUFRGNcTwuu6bD4JKJl9EQChiC+JCi8GLdegzJFninsvAiCUJwlo
LKSODjkMJAiCCIAgCCIAgiCIAAiCIAIgCIIIgCAIIgCCIIgACIIgAiAIggiAIAgiAIIgiAAIgiAC
IAiCCACKNs2mWp5LNfYZCiIAKMQd8NXy3GpaiyACUPRBkhmf8VyXD6B0Q2NUbrt8rsuHq6kgz2UA
rqaRtSgq4TTe3FoyPpfsuYIIwLixAKIu4efPZ8BcGjc2f8X07sMWT73so65AE3Qsh0Mvn3rZx+7D
9qhnFdv1ZwZ+/nwGUZcgjoAIwMQRgNyk2Gd2BHhoS3bktphiYnJDNNc/msShIYajCzNOmxlwNHBo
iLH+0SQUhc8qJr4JL9t4aEsWz+wIQjETBRABwAQbZRX1CDd8fxBbXw3g6vDFLuRYq/y4rMACrgbu
fzKNex5NYVK8sHfQGRvO5bvn0RTufzINV4fPNLaw4Y3l8DNyNbD11QA3fH8QUY9k7qYIwMScahtx
gP6kxUfW9eOZnT5cfSSGzk+VHc8PIdwpHQV87/E0rvvuIGJe8QKOmEe47ruD+N7jaTi5e/CoQGvJ
5xdcDTyz08dH1vWjP2kRccp7MYgAGQo6np0zHiEMpBitt/fjY5dGseKCKBbPdKALIH/JLOOZHQHu
ezyFnz6TQV0knFNfDINhDi/oqIsQbvjeIDa9mMXVF8dw3qkO4gUQHWOBl/YG2PB0Gt/5TRrZIPzs
CunJCCIAZRGBiBPGzbf+Mol7N6Vx+ika0xrHrwBdBw12HDDwAyARD6+kKuZumU9o1kcJP/5dBj97
NoNTp2vMn6rH/bt7Biz+uM+gP2WRiKvwMxPjFwFAtdxyA2BqvUJggRd2BwhMYS6tiHmEukjpjIVz
QjApd/nlrh6D7XvHvxhHh5UTuUpbBKBqk4L5ppa4RwW5787mdnzD5fFsACDiEmJe4a7blsYfEYCa
8AiqJbVdLgESIFUAQRBEAARBEAEQBEEEQBAEEQBBEEQABEEQARAEAdIHULkDRBQd6bIb/e8ZRxp+
ZJ2yThGAKoFyL4mxwFCakQkYriYodaR1MBsAWoedg55zpFtO1inrFAGYwGgVvgxDaUYiTrh0sYu3
LvJwzjwHjTECITwXv6Xbx/PdAZ54ycf+AYuIC9R5NGHaZWWd1bVOEYBCLFoBvcOMaY0Ka66I471v
ieCMU45/mu7tZ7oAgL19Fo92ZnHPr5PY0h1gSr36E/dS1inrrLKp2UwA8bxPdzWRF3+FlNPE1s+d
Sp+giyWgb5jx7nM8/MOKeiycpo+a7EPHOUCUjycBYDDN+PrPhvHNjSm4DsHTledCyjqra504sYMh
lrx6xZnhd3Stm7YRrazRQUaqALmXJZ1lrLkijh+sSmDhNI3AHJnsk5+wM/rHUbnEEYcvVEOU8LXW
eqz7aAOibnhyTpGsU9YJKQNWtNuvgUODFl94bx3a/nsdgtx5d0eP7QsnCl8gzs3MW3FhFP/2yQTS
Wa6oQ4WyzupapwhAgWLEQ4OMqy6OYs0V8XDiLZ2c0lNuZp5vgEvOcHHTynr0DduCjBeTdco6RQAK
UArS6kic52ggEwALpil8rbUBjNwgzXG6ea4OXchPtMTwnnMjGEjxyMDRcvzIOou7zvw7JVWASlYz
BWR9YDgTfnnIfXkDKcZtVycwpT4s9zgFkr38+/C11nr854uH0TvMoVtZpsYXWWfx1ukHCEuGVTYk
1ammuv5gmjFzksLfvCuGSxZ7cDQADhs/zj/VDS/YUIUVHAawcJrGL/+uCYeHeeSZKMO4M61knQVf
Z+7fvbA7wANPprGlO0BjjKqmecipFuMfSDEuOM3Ft69pxIyEKmkpigEsneNUfb24ltd50ekuPvH2
GL7cMYT1G1OYXFcdnoBTDT3fySxj8UyN769KIBEj+OZP47ViJnUIldNbLusszjqZw2d+fWU9+pMW
Hb/LFPz2JxGAk0z6pbOM65fHR4zf1eURIlRhkkjWiaOmMGsCvvDeOjy0JVsVHoCa6MafNcApCY2W
JV7BY0JBONbrsAzMn6rx5gUOkhme8OVCVQ3jvWNeeIUVkbykQmm8g8YYiQeACpiH7xDQl2IcHLRy
xlsoCYENDxO5zsS/NXnCewBuriX0p7/PQBEQiAAIRSKfXH52p48t3QHiHmAlCVheDAOJmMKdDydx
2RIPZ89zYOyflqg1FfcMo7E576PMYYisszjrpNxm059i3NgxVDVdgU41XIvl6LAJ6Mo7+3HHxxpw
WbNXVWUpVFgirFbXuX2fwWe/N4jf7wqqogRYNY1AloGYS+hPhSJw0ekuLjrDC7u4OOzw+kRLDPUR
GqkeFPS6bgLu+20a+/stXKd8eQgiWWeh1+nkSsrbdgf49bYshjNcNcZfVa3AlkMXzdWE377k49Ft
PhhhmaZ3mBEY4HPviYe941Q4N1Er4LfbfXz63oGwBEnlMQxZZ3HX6WhCfYTkLEClhwMAUB+lXIwW
lgab6oBbfzmMd5/joXm2M/JFj1dwiIBUlvHF+weRiCvURcqXFJJ1FnedjPB/V9sAUVWtV38HNvzx
c8OQsgGw+ruD6E8xlMK4VDw/SVYRcGPHELa9ZhBzw2fkn1vqH1lncdd5vMSyCMAEwdiwcWPzDh9/
98NB2NyOcTIvjc29CI4C1m9M4ZsbU5hSVxlTZWWd1bXOihEAmyXiCS4WvgGmNSg8+LsMPnRbH3oG
7Ehr50jJ53V2CJPbBfJHRr/4wBC+9MAQpjWqinpZZJ3Vtc6TjZOYxmavNAb/iFrWQu/q63lCufXn
2+yQBZGa6EeHZzcptH+4Hu9/S+So0IH5aFdPHTNq6rmuAF/eMISnXvYxKV6558JlndW1zrEGM0QO
GBhyMsmlr9w151WAFUD25AWgjRXayc6//uAjyqt/p80OGIA0JniNN+0zsgHwrrM8fODPInj7mR5m
Tjq+rg2lGU/80cfPn8/gp7/PYDjDSMQq302UdVbXOsckAMoltn6vTg0u3LH+tP78aH+MvwpgbTXl
BCIOIeIAj7yQxS+3ZDG7SeHM2Q7OnhveJAOEyZ8tXT627zN4Zb+B5TD2bJwgL4uss7rWOfZpBiow
sclUkBCgpY2dTe0ULLj+4D9StOmLJnUoICKn2jq+skG4i/gG4FwASSA4Ony5ot7RSSNZp6yzAj0A
o7wGbbNDj3fdNvVStIHQTrZQfQB7wRbVNg4inzl2NNDoUG5xdNQMunxiSdYp66x8B0CBmfcDxOhk
Ne5GoE2doUAyeCusD6rSeTDM4cGiakfWWdVrZpADpbAVAFqaQZsw3jJgRygA5Ps7OUgnSWmCnLoX
hEqs/hHbAMS6c/TmPc4+ALIAU7zn8F62/m7SHgEQARAEVN7NGByksgy7dfTmPe5GoNYNUJ0dZ2WJ
6EnoKJhh5cMWhIoKAKxyIsQmuzO+Z//OXPnPFkQADmzLx/3qsTH3DwiCUMr430JHQYSnOjvOyrZu
GJttj6kKsKk93PEpk37SKierSLksUYAgVFoDwMgmfWTTLshhoFwe4FDfTjbZneRECbmaoCAIlTCp
WCnrD2dVYJ8YvWkX7DRgSxt0mAfAz+BIHkAQKqkBiNw4sck8t3PqnS+j7fX7/09KAEZKCtY+yH7K
Ekiu4BCESqn/aw+K1INob7ctJ2DXYzfiDjIAU92+g8/aILVDuVElYYAgVEL9n7TNDgUU8E9PxP0/
8YEgI2EAfR9OTMIAQaiM/n9im/3Nibr/Jy4AOWWx1t5nskNpRUpLU5AglHkOJmkQ07dO1P0/iZFg
ZFs3sH513YxXYDI/oUiCmNnI1yAIZWr+cWPKpvt2oH/ox2CmTe0wKOZMwI6OfNyh1nN4OEiSgYJQ
lt2fmZw4Efi7Xd9ZmMZa6Ncb/nFyE4FeZ0rQvNX7N+pIYlk1TAkShAk4/QfM9nA2mT5z7/pZh3Im
zcWfCtwZCgeRag8jAOkMFoQSx/6GvEaCCe7Yu372QWyAOlHjP3kB6CCDNlZdt017zPpDm5TXqAHJ
BQhCqcxfaU/ZTF+vb6PrwExYcXIVufHH76w+Z00myEUAUhEQhOLbvyWvQTGCr+y5M3EIK05u9x//
qb5W1uggM3/1vjtUbOoqmzpkEJYGBUEoTuLfKq9eWT/57IJJUy/YBFi0g09WAMbnAXTAoo0V+9Gv
2MzAAdIRBZbuQEFA8Wb+MYOgDK/Z1E5BmI8jLtPVYMToBHXfNamXTOY6cuN0Il1IgiCc0O4fqOhk
bTMD39h5x/Tf5D1wlPVuwA4yrRtY71o3c4PN9HWoWJPDbAP5tgShsK4/uXWOzfbviA3rL6KNFTrG
34pfkCaejhVhKGBU+lM2O7RDuXENtuIJCEKhin7KYbA1CIaveulfpw2eTM2/iLcDh3/I7lvmHUYw
eBWYLZRjZXqwIBSEQEUmafaTf9u1bu5TaGHnjS78KP314O1k0cZO17q5T7Gf/Fsdm+yAIb0BgjC+
il+gY9Ncmz78YNe6U25taWMHmygo8ByxAtLGDtopmL+6Z72KJq6x6d4ApBz5KgXhhON+Q16DZpPZ
zOmB5d3T5/WPp+RXXA/gyJHhsEvw9mnX2szgIzo+zWFYX75NQTgRrCG3TrPJ9OjUob/ovmt+b6Hi
/uIKQP4PbGPlB6mVJtO/WUeaXKkMCMKYZ3xY0jEN5l5jUv9tx92LDqCVdaHi/iILQC4fAGDPnXMO
cXpgufVTm3VUyoOCMCa334krgHqD1ODy3bfP2lyIen9pBeBIUlB13zW/l9N9oQjEpogICMLrGb9b
p0eM/65Zm9HGTrGMv7gCcFwRGHpcRyc7AHwpEQrCMV1+XoMGeG+Q6j1i/O0UlOA2kSKTGyCClo3O
/Def8w0da7rGJA8aMBNIxosLtT7Xh40Tn+6YTN9mHu5/f/f6BXuL6faXXgBGiwCABWsOt0F7a8EG
HKTlBKFQs+29IKVUtAnWH95g+l/99O5vn3W4VMZfhks+mdAGQjvZBdfvXw4duZec2Eyb7g8AaBDJ
aCGhZhp8lBt3mDkAm8933dJ067EbZRUKwNHNQnNXdc1SXuO/Kq9hOWf6YW1gSLwBodp3fRBUbLKy
QWo7m+Qnum+d8Xi468MWus5fmQIAYLSbs2DN4etYuV9VTiRh070WIEhuQKi2UB9gS169BgMMs04P
9nxlx/rT+kuR7Ks8AcgNNsXaMCRYeMOBMxjRdmh3JWwA9pMGIEkSChM/xwcYpV2HvAZYP/k0B5kv
d98+7dflcPkrSwBGQoKNDtovCwBg/uf63w2Lf1Ju/Cw26ZwQgEBKhECYUEE+A3bE8IP0fuLgH3YN
PXA31n/SL5fLX5kCkFdCAGgn29z6gjc8d/b/BKvPKjd2FtsAnB1kADb0CCRZKFSm2QNswQC5UU1O
HNYf3g/G3cqk7tp5+yn7jw1/y03lGdKoDycvBMT6r6DoInKisJkBwBqT+8tFDIQKMHpYZmYicpRX
D5AG+6kXGXjgOIZvK2l6doUaDxNaoUar5MIb+i63UFeD7fuVG28EM6w/DHBgwOCwhMgiCELxDZ6Z
w9mXTCDS5NaBtAubHQ4A2kjA95yg8YGX11FmJMRdu8yAqOK6XyvcWPJCcCRWmn3dwTmO414O8AfA
vEy58UYoBTZZcJAGbGAZZCkclkpgIhBT/kZDeX+FMd65G+7TFM7dYw7fJIA0OVGQjgAAbHbQAOpp
UuonlugX3f/S2DnyazawRitsJRr+BBGAY0IDAKO9gtnXHZzjeN5bydhLGeZiAEuVG49DuQBbgE0o
DPlJ5ca38nILb+jRK0eBFAgEciIAKYAcwAaw/pAB6ZeI1NNM6jcM+/RRRs9M6IAKb+qhij/vMvF2
xLY2BSxTwDJ7bPnktBuSc421S5iT5xPpRSBnnrWZRUS6ga1Ryo0niBQ4J+2CcKzxEynY7FASoAyY
DZTTyTY4qJS7lR13K5R+seu8yHasGJ3EY0IbNABbzpJebQjAsWLQuZbQ/BihfZk5nuLO+SzHVATR
YHBAeU5mKStXI5ATycJ/gROFQ9mX/ZQechqt3fH1yf3/pUfa/BgdbyMSAShnKbET1NIM2tQJRjN4
In85QoW9U0vB2AYu9Fw+EYBiJxLzX9UKSDOR8MY0r2W0r+VizOATBEEQBEEQBEEQBEEQBEEQBEEQ
BEEoMv8f7ApSWQimidoAAAAASUVORK5CYII=
"""

# ========= 유효한 서브넷 마스크 =========
VALID_MASKS = {
    "255.0.0.0", "255.128.0.0", "255.192.0.0", "255.224.0.0",
    "255.240.0.0", "255.248.0.0", "255.252.0.0", "255.254.0.0",
    "255.255.0.0", "255.255.128.0", "255.255.192.0", "255.255.224.0",
    "255.255.240.0", "255.255.248.0", "255.255.252.0", "255.255.254.0",
    "255.255.255.0", "255.255.255.128", "255.255.255.192", "255.255.255.224",
    "255.255.255.240", "255.255.255.248", "255.255.255.252"
}

root = tk.Tk()
root.title("네트워크 IP 설정 by 최승훈")

# ========= 아이콘 적용 =========
icon_data = base64.b64decode(ICON_BASE64)
image = Image.open(BytesIO(icon_data))
icon_img = ImageTk.PhotoImage(image)
root.iconphoto(False, icon_img)

root.geometry("550x600")

# ========= 함수 =========
def decode_output(data):
    # netsh는 실행 환경에 따라 UTF-8 또는 cp949로 출력한다
    try:
        return data.decode('utf-8')
    except UnicodeDecodeError:
        return data.decode('cp949', errors='replace')

def run_command(cmd):
    result = subprocess.run(cmd, capture_output=True)
    result.stdout = decode_output(result.stdout)
    result.stderr = decode_output(result.stderr)
    return result

def get_interfaces():
    result = run_command(['netsh', 'interface', 'show', 'interface'])
    interfaces = []
    for line in result.stdout.splitlines():
        if "Connected" in line or "연결됨" in line or "Disconnected" in line or "연결 끊김" in line:
            # 칸 구분은 공백 두 칸 이상이다. 상태값과 어댑터 이름에는 띄어쓰기가 있을 수 있다
            parts = re.split(r'\s{2,}', line.strip())
            if len(parts) >= 4:
                interfaces.append(parts[-1])
    return interfaces

def toggle_ip_fields():
    state = 'normal' if ip_mode.get() == "manual" else 'disabled'
    for entry in ip_entries + subnet_entries + gateway_entries:
        entry.config(state=state)

def toggle_dns_fields():
    state = 'normal' if dns_mode.get() == "manual" else 'disabled'
    for entry in dns1_entries + dns2_entries:
        entry.config(state=state)

def validate_octet(text):
    return text.isdigit() and 0 <= int(text) <= 255 if text else True

def auto_move(event, entry_list, index):
    if event.char == '.' and index < len(entry_list) - 1:
        entry_list[index + 1].focus_set()
        return "break"
    elif event.keysym == 'BackSpace' and event.widget.get() == '' and index > 0:
        entry_list[index - 1].focus_set()

def check_entries_filled(entries, label):
    for e in entries:
        if not e.get().strip():
            messagebox.showerror("입력 오류", f"{label} 입력칸이 비어 있습니다.")
            return False
    return True

def join_octets(entries):
    values = [e.get().strip() for e in entries]
    return '.'.join(values) if any(values) else ''

def validate_and_run():
    interface = combo_interface.get().strip()
    if not interface:
        messagebox.showerror("입력 오류", "인터페이스를 선택하세요.")
        return

    if ip_mode.get() == "manual":
        if not check_entries_filled(ip_entries, "IP 주소"):
            return
        if not check_entries_filled(subnet_entries, "서브넷 마스크"):
            return
        if not check_entries_filled(gateway_entries, "기본 게이트웨이"):
            return

        ip = '.'.join(e.get() for e in ip_entries)
        subnet = '.'.join(e.get() for e in subnet_entries)
        gateway = '.'.join(e.get() for e in gateway_entries)

        try:
            ipaddress.IPv4Address(ip)
            ipaddress.IPv4Address(gateway)
            if subnet not in VALID_MASKS:
                messagebox.showerror("입력 오류", f"서브넷 마스크 값이 유효하지 않습니다: {subnet}")
                return
        except ValueError as ve:
            messagebox.showerror("입력 오류", f"IP/게이트웨이 입력 오류: {ve}")
            return

        cmd_ip = ['netsh', 'interface', 'ip', 'set', 'address', interface, 'static', ip, subnet, gateway]
    else:
        cmd_ip = ['netsh', 'interface', 'ip', 'set', 'address', interface, 'dhcp']

    if dns_mode.get() == "manual":
        if not check_entries_filled(dns1_entries, "기본 DNS 서버"):
            return
        dns1 = '.'.join(e.get() for e in dns1_entries)
        dns2 = join_octets(dns2_entries)
        try:
            ipaddress.IPv4Address(dns1)
            if dns2.strip():
                ipaddress.IPv4Address(dns2)
        except ValueError as ve:
            messagebox.showerror("입력 오류", f"DNS 입력 오류: {ve}")
            return
        cmds_dns = [['netsh', 'interface', 'ip', 'set', 'dns', interface, 'static', dns1, 'primary']]
        if dns2.strip():
            cmds_dns.append(['netsh', 'interface', 'ip', 'add', 'dns', interface, dns2, 'index=2'])
    else:
        cmds_dns = [['netsh', 'interface', 'ip', 'set', 'dns', interface, 'dhcp']]

    try:
        result_ip = run_command(cmd_ip)
        result_dns = None
        for cmd_dns in cmds_dns:
            result_dns = run_command(cmd_dns)
            if result_dns.returncode != 0:
                break
        if result_ip.returncode == 0 and (result_dns is None or result_dns.returncode == 0):
            messagebox.showinfo("성공", "설정 적용 완료")
        else:
            error_msg = (result_ip.stderr.strip() or result_ip.stdout.strip() or
                         (result_dns.stderr.strip() if result_dns else '') or
                         (result_dns.stdout.strip() if result_dns else '') or
                         "명령어 실패 (cmd 확인)")
            messagebox.showerror("명령어 실패", error_msg)
    except Exception as e:
        messagebox.showerror("실행 오류", str(e))

def save_settings():
    try:
        interface = combo_interface.get().strip()
        if not interface:
            messagebox.showerror("입력 오류", "인터페이스를 선택하세요.")
            return

        if ip_mode.get() == "manual":
            if not check_entries_filled(ip_entries, "IP 주소"):
                return
            if not check_entries_filled(subnet_entries, "서브넷 마스크"):
                return
            if not check_entries_filled(gateway_entries, "기본 게이트웨이"):
                return

        if dns_mode.get() == "manual":
            if not check_entries_filled(dns1_entries, "기본 DNS 서버"):
                return

        # 자동으로 받는 항목은 빈 값으로 저장한다
        ip = subnet = gateway = dns1 = dns2 = ""

        try:
            if ip_mode.get() == "manual":
                ip = '.'.join(e.get() for e in ip_entries)
                subnet = '.'.join(e.get() for e in subnet_entries)
                gateway = '.'.join(e.get() for e in gateway_entries)
                ipaddress.IPv4Address(ip)
                ipaddress.IPv4Address(gateway)
                if subnet not in VALID_MASKS:
                    messagebox.showerror("입력 오류", f"서브넷 마스크 값이 유효하지 않습니다: {subnet}")
                    return
            if dns_mode.get() == "manual":
                dns1 = '.'.join(e.get() for e in dns1_entries)
                dns2 = join_octets(dns2_entries)
                ipaddress.IPv4Address(dns1)
                if dns2.strip():
                    ipaddress.IPv4Address(dns2)
        except ValueError as ve:
            messagebox.showerror("입력 오류", f"저장 실패 - 입력값 검증 실패: {ve}")
            return

        filename = simpledialog.askstring("파일 이름 입력", "저장할 파일 이름 입력 (확장자 제외):")
        if not filename:
            return

        current_path = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__))
        save_path = os.path.join(current_path, filename + ".txt")

        with open(save_path, "w", encoding="utf-8") as f:
            f.write(f"인터페이스:{interface}\n")
            f.write(f"IP 주소:{ip}\n")
            f.write(f"서브넷 마스크:{subnet}\n")
            f.write(f"기본 게이트웨이:{gateway}\n")
            f.write(f"기본 DNS 서버:{dns1}\n")
            f.write(f"보조 DNS 서버:{dns2}\n")

        messagebox.showinfo("저장 완료", f"{save_path}에 저장되었습니다.")
    except Exception as e:
        messagebox.showerror("저장 실패", str(e))

def load_settings():
    try:
        filepath = filedialog.askopenfilename(title="설정 파일 선택",
                                              filetypes=[("텍스트 파일", "*.txt")])
        if not filepath:
            return
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        def parse_value(line):
            parts = line.strip().split(':', 1)
            return parts[1].strip() if len(parts) == 2 else ""

        interface_val = parse_value(next((l for l in lines if l.startswith("인터페이스")), "인터페이스:"))
        ip_val = parse_value(next((l for l in lines if l.startswith("IP 주소")), "IP 주소:"))
        subnet_val = parse_value(next((l for l in lines if l.startswith("서브넷 마스크")), "서브넷 마스크:"))
        gateway_val = parse_value(next((l for l in lines if l.startswith("기본 게이트웨이")), "기본 게이트웨이:"))
        dns1_val = parse_value(next((l for l in lines if l.startswith("기본 DNS 서버")), "기본 DNS 서버:"))
        dns2_val = parse_value(next((l for l in lines if l.startswith("보조 DNS 서버")), "보조 DNS 서버:"))

        # 이 PC에 실제로 있는 인터페이스만 선택되도록 파일 값을 검증한다
        combo_interface.set(interface_val if interface_val in combo_interface['values'] else "")

        def fill_entries(val, entries):
            parts = val.split(".")
            for i in range(4):
                entries[i].delete(0, tk.END)
                entries[i].insert(0, parts[i] if i < len(parts) else "")

        # 입력칸이 잠겨 있으면 값을 넣을 수 없으므로 먼저 수동으로 풀어 둔다
        ip_mode.set("manual")
        dns_mode.set("manual")
        toggle_ip_fields()
        toggle_dns_fields()

        fill_entries(ip_val, ip_entries)
        fill_entries(subnet_val, subnet_entries)
        fill_entries(gateway_val, gateway_entries)
        fill_entries(dns1_val, dns1_entries)
        fill_entries(dns2_val, dns2_entries)

        # 값이 없는 항목은 자동으로 받는 설정이다
        ip_mode.set("manual" if ip_val.strip('. ') else "auto")
        dns_mode.set("manual" if dns1_val.strip('. ') else "auto")
        toggle_ip_fields()
        toggle_dns_fields()

        messagebox.showinfo("불러오기 완료", "설정값이 불러와졌습니다.")
    except Exception as e:
        messagebox.showerror("불러오기 실패", str(e))

# ========= UI =========
vcmd = (root.register(validate_octet), '%P')

tk.Label(root, text="네트워크 인터페이스 선택:", font=("맑은 고딕", 12)).pack(pady=5)
interfaces = get_interfaces()
combo_interface = ttk.Combobox(root, values=interfaces, state='readonly', font=("맑은 고딕", 11))
combo_interface.pack(pady=5)

ip_frame = tk.LabelFrame(root, text="IP 주소 설정", font=("맑은 고딕", 12))
ip_frame.pack(fill="x", padx=10, pady=10)

ip_mode = tk.StringVar(value="auto")
tk.Radiobutton(ip_frame, text="자동으로 IP 주소 받기", variable=ip_mode, value="auto", command=toggle_ip_fields, font=("맑은 고딕", 11)).pack(anchor='w')
tk.Radiobutton(ip_frame, text="다음 IP 주소 사용", variable=ip_mode, value="manual", command=toggle_ip_fields, font=("맑은 고딕", 11)).pack(anchor='w')

def create_ip_entry_row(parent, label_text):
    row = tk.Frame(parent)
    tk.Label(row, text=label_text, width=14, anchor='w', font=("맑은 고딕", 11)).pack(side=tk.LEFT)
    entries = []
    for i in range(4):
        entry = tk.Entry(row, width=5, validate='key', validatecommand=vcmd, justify='center', font=("맑은 고딕", 11))
        entry.pack(side=tk.LEFT)
        entries.append(entry)
        if i < 3:
            tk.Label(row, text='.', font=("맑은 고딕", 11)).pack(side=tk.LEFT)
        entry.bind('<KeyPress>', lambda e, l=entries, idx=i: auto_move(e, l, idx))
    row.pack(anchor='w', padx=20, pady=2)
    return entries

ip_entries = create_ip_entry_row(ip_frame, "IP 주소:")
subnet_entries = create_ip_entry_row(ip_frame, "서브넷 마스크:")
gateway_entries = create_ip_entry_row(ip_frame, "기본 게이트웨이:")

dns_frame = tk.LabelFrame(root, text="DNS 서버 주소 설정", font=("맑은 고딕", 12))
dns_frame.pack(fill="x", padx=10, pady=10)

dns_mode = tk.StringVar(value="auto")
tk.Radiobutton(dns_frame, text="자동으로 DNS 서버 주소 받기", variable=dns_mode, value="auto", command=toggle_dns_fields, font=("맑은 고딕", 11)).pack(anchor='w')
tk.Radiobutton(dns_frame, text="다음 DNS 서버 주소 사용", variable=dns_mode, value="manual", command=toggle_dns_fields, font=("맑은 고딕", 11)).pack(anchor='w')

dns1_entries = create_ip_entry_row(dns_frame, "기본 DNS 서버:")
dns2_entries = create_ip_entry_row(dns_frame, "보조 DNS 서버:")

btn_frame = tk.Frame(root)
btn_frame.pack(fill="x", padx=10, pady=20)
tk.Button(btn_frame, text="확인", width=12, command=validate_and_run, font=("맑은 고딕", 11)).pack(side=tk.RIGHT, padx=5)
tk.Button(btn_frame, text="취소", width=12, command=root.quit, font=("맑은 고딕", 11)).pack(side=tk.RIGHT, padx=5)
tk.Button(btn_frame, text="저장", width=12, command=save_settings, font=("맑은 고딕", 11)).pack(side=tk.RIGHT, padx=5)
tk.Button(btn_frame, text="불러오기", width=12, command=load_settings, font=("맑은 고딕", 11)).pack(side=tk.RIGHT, padx=5)

toggle_ip_fields()
toggle_dns_fields()

root.mainloop()

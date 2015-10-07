##Notes

#### install lib to sandbox to check compiling:
export PYTHONPATH='/home/adam/sandbox/python-test//lib/python2.7/site-packages/'&& python setup.py install --prefix /home/adam/sandbox/python-test/
python -c 'import image_doctor'


#### Install OpenCV
http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/


#### white papers:
on cylindrical projects: https://www.maa.org/sites/default/files/pdf/upload_library/22/Ford/apostol388.pdf    
computer vision w/ python textbook: http://www.bogotobogo.com/python/files/pytut/Computer_Vision_with_Python.pdf    
python opencv book: https://homepages.thm.de/~hg11237/Start/OpenCV/Mastering%20OpenCV%20with%20Practical%20Computer%20Vision%20Projects%20%5BeBook%5D.pdf
p 85: piecewise affine transformation: http://programmingcomputervision.com/downloads/ProgrammingComputerVision_CCdraft.pdf
Shi & Malik, 2000, on segmentation via eigenvector solution(seminal):http://repository.upenn.edu/cgi/viewcontent.cgi?article=1101&context=cis_papers

#### Courses:

UC Davis, Image processing and recognition: https://www.youtube.com/playlist?list=PLA64AFAE28B8DD0FD


#### algo:
1) find ellipse -> bottle top
2) find parallel lines -> bottle end
3) measure ellipse on bottle top, calculate even sized offsets around can(ellipse angle -> point = center.x + (x-axis * theta ), center.y + (y-axis * theta))
4) given 

t = seq(from=0,to=pi/2, length=1000)
df = data.frame(x=cos(t),y=sin(t))
dev.off()
plot(x=df$x,y=df$y,asp=1)
seglen = tapply(INDEX=rep(1:10,each=100,length=length(df$x)),rev(df$x),FUN=min)
plot(x=c(df$x,seglen),y=c(df$y,rep(max(df$y), length=length(seglen)) ),asp=1)

4) create grid from can ellipse, sides. 

import cv2

# Videoyu oku
vidcap = cv2.VideoCapture('a.mp4')

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        # Her frame'i bir resim dosyası olarak kaydet
        cv2.imwrite("frame"+str(count)+".jpg", image)
    return hasFrames

sec = 0
frameRate = 0.5 # Bu, 0.5 saniyede bir frame çekmek için // Değiştirilebilir
count=1
success = getFrame(sec)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

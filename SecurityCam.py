import cv2
import time
import dropbox
import random
name = 1
startTime = time.time()



def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = 'img'+ str(number) + '.jpg'
        cv2.imwrite(imageName, frame)
        startTime=time.time()
        result = False
    return imageName        
    print("Snapshot is taken.")    

    videoCaptureObject.release()
    cv2.destrolAllWindows()

def uploadFiles(imageName):
    access_token = 'sl.A10XTYR3zfWs149wOw7WDfWCts4E8xPagzXASbroXos7161u4EvW3W6GC15r29XrlKYiAwqNUIYbrFcrc_MJMkkR355Vz1c_dFDfo2bSSA93K8ynvPrBCyrv31mMjMYas6bVBaE'
    file = imageName
    file_from = file
    file_to = '/NewFolder/' + imageName
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if time.time()-startTime >=5:
            name = take_snapshot()
            uploadFiles(name)
main()            



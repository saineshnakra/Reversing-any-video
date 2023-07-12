import cv2

cap = cv2.VideoCapture(0)
opened = cap.isOpened()

#fourcc
fourcc = cv2.VideoWriter_fourcc(*'MJPG')


height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width =  cap.get(cv2.CAP_PROP_FRAME_WIDTH)

fps = cap.get(cv2.CAP_PROP_FPS)


# video writer 
out = cv2.VideoWriter('jj_exp.avi',fourcc,fps,(int(width), int(height)))
print(height)
print("FPS is : {}".format(fps))

if(opened):
    while(cap.isOpened()):
        ret , frame = cap.read()
        if(ret==True):
            cv2.imshow('Test video frame', frame)
            if(cv2.waitKey(5000)==32):
                out.write(frame)
            if(cv2.waitKey(2)==27):
                break

out.release()
cap.release()
cv2.destroyAllWindows()
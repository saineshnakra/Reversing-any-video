import cv2

cap = cv2.VideoCapture('sample.mp4')

#Frame count -> for last index, fps, height and width for writing the video 

frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

fps = cap.get(cv2.CAP_PROP_FPS)

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

#Initiated the output writer for video
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#Scaled the video to increase the speed
out = cv2.VideoWriter('reverse.avi',fourcc,fps,(int(width*0.75),int(height*0.75)))

print('No of frames are : {}'.format(frames))
print('FPS is {}'.format(fps))


#Reach to the last index of the video
frame_index = frames-1

if(cap.isOpened()):
    while(frame_index!=0):
        #capture instance set for a property -> position
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
        ret, frame = cap.read()

        frame = cv2.resize(frame,(int(width*0.75),int(height*0.75)))

        out.write(frame)

        frame_index = frame_index - 1

        if(frame_index%100==0):
            print(frame_index)

out.release()
cap.release()
cv2.destroyAllWindows()



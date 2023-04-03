import cv2
cap = cv2.VideoCapture(0)
while True:
	ret,frame = cap.read()

	height, width, _ = frame.shape
	quarter_height, quarter_width = int(height/2), int(width/2)
	top_left = frame[0:quarter_height, 0:quarter_width]
	top_right = frame[0:quarter_height, quarter_width:width]
	bottom_left = frame[quarter_height:height, 0:quarter_width]
	bottom_right = frame[quarter_height:height, quarter_width:width]

	top_left = cv2.cvtColor(top_left,cv2.COLOR_BGR2GRAY)
	top_right = cv2.cvtColor(top_right, cv2.COLOR_BGR2HSV)
	bottom_left = cv2.cvtColor(bottom_left, cv2.COLOR_BGR2LAB)
	bottom_right = cv2.cvtColor(bottom_right, cv2.COLOR_BGR2YUV)

	cv2.imshow('top_left', top_left)
	cv2.imshow('top_right', top_right)
	cv2.imshow('bottom_left', bottom_left)
	cv2.imshow('bottom_right', bottom_right)

	if cv2.waitKey(1) == 27:
		break

cap.release()
cv2.destroyAllWindows()
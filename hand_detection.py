import cv2
import mediapipe as mp

class LandmarkCoordinates(object):
    def __init__(self,x,y,z):
        self.X = x
        self.Y = y
        self.Z = z

    def __add__(self,other):
        return [self.X + other.X, self.Y + other.Y, self.Z + other.Z]

    def __str__(self):
        return(str(self.X)+", "+str(self.Y)+", "+str(self.Z))
        
    def getXYZ(self):
        return [self.X,self.Y,self.Z]

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def getZ(self):
        return self.Z


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For static images:
IMAGE_FILES = ["B\\B3.jpg"]
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5) as hands:

    for idx, file in enumerate(IMAGE_FILES):
        one_image = []
        class_one_image = []
        # Read an image, flip it around y-axis for correct handedness output (see
        # above).
        image = cv2.flip(cv2.imread(file), 1)
        # Convert the BGR image to RGB before processing.
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if not results.multi_hand_landmarks:
            continue
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                one_image.append([landmark.x,landmark.y,landmark.z])
        print(one_image)
        wristToThumbBase = [one_image[0],one_image[1]]
        wristToIndexBase = [one_image[0],one_image[5]]
        wristToLittleBase = [one_image[0],one_image[17]]
        thumbBaseToThumbTip = [one_image[1],one_image[4]]
        indexBaseToIndexTip = [one_image[5],one_image[8]]
        middleBaseToMiddleTip = [one_image[9],one_image[12]]
        ringBaseToRingTip = [one_image[13],one_image[16]]
        littleBaseToLittleTip = [one_image[17],one_image[20]]

        
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                class_one_image.append(LandmarkCoordinates(landmark.x,landmark.y,landmark.z))
        
        wristToThumbBase = [class_one_image[0]+class_one_image[1]]
        wristToIndexBase = [class_one_image[0]+class_one_image[5]]
        wristToLittleBase = [class_one_image[0]+class_one_image[17]]
        thumbBaseToThumbTip = [class_one_image[1]+class_one_image[4]]
        indexBaseToIndexTip = [class_one_image[5]+class_one_image[8]]
        middleBaseToMiddleTip = [class_one_image[9]+class_one_image[12]]
        ringBaseToRingTip = [class_one_image[13]+class_one_image[16]]
        littleBaseToLittleTip = [class_one_image[17]+class_one_image[20]]

        # fingercoords = []
        # for i in range (5):
        #     changesx = one_image[0][0]+one_image[i*4+1][0]+one_image[i*4+2][0]+one_image[i*4+3][0]+one_image[i*4+4][0]
        #     changesy = one_image[0][1]+one_image[i*4+1][1]+one_image[i*4+2][1]+one_image[i*4+3][1]+one_image[i*4+4][1]
        #     changesz = one_image[0][2]+one_image[i*4+1][2]+one_image[i*4+2][2]+one_image[i*4+3][2]+one_image[i*4+4][2]
        #     fingercoords.append([changesx,changesy,changesz])
        # print(fingercoords)







# import cv2
# import mediapipe as mp
# cap = cv2.VideoCapture(0)
# mpHands = mp.solutions.hands
# hands = mpHands.Hands()
# mpDraw = mp.solutions.drawing_utils
# while True:
#     sucess, image = cap.read()
#     imageRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#     results = hands.process(imageRGB)
#     if results.multi_hand_landmarks:
#         for handLms in results.multi_hand_landmarks:
#             for id, lm in enumerate(handLms.landmark):
#                 h,w,c = image.shape
#                 cx,cy = int(lm.x * w), int(lm.y * h)
#             mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
#             cv2.imshow("Output", image)
#             print(results.multi_hand_landmarks)
#             cv2.waitKey(1)

# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_hands = mp.solutions.hands

# # For static images:
# IMAGE_FILES = ["archive\\asl_alphabet_train\\asl_alphabet_train\\B\\B3.jpg","archive\\asl_alphabet_train\\asl_alphabet_train\\B\\B659.jpg"]
# with mp_hands.Hands(
#     static_image_mode=True,
#     max_num_hands=1,
#     min_detection_confidence=0.5) as hands:

#     for idx, file in enumerate(IMAGE_FILES):
#         one_image = []
#         # Read an image, flip it around y-axis for correct handedness output (see
#         # above).
#         image = cv2.flip(cv2.imread(file), 1)
#         # Convert the BGR image to RGB before processing.
#         results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

#         # Print handedness and draw hand landmarks on the image.
#         print('Handedness:', results.multi_handedness)
#         if not results.multi_hand_landmarks:
#             continue
#         for hand_landmarks in results.multi_hand_landmarks:
#             for landmark in hand_landmarks.landmark:
#                 one_image.append([landmark.x,landmark.y,landmark.z])
#         print(one_image)
#         image_height, image_width, _ = image.shape
#         annotated_image = image.copy()
#         for hand_landmarks in results.multi_hand_landmarks:
#             print('hand_landmarks:', hand_landmarks)
#             print(
#                 f'Index finger tip coordinates: (',
#                 f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
#                 f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
#             )
#             mp_drawing.draw_landmarks(
#                 annotated_image,
#                 hand_landmarks,
#                 mp_hands.HAND_CONNECTIONS,
#                 mp_drawing_styles.get_default_hand_landmarks_style(),
#                 mp_drawing_styles.get_default_hand_connections_style())


    
#     cv2.imwrite(
#         '/tmp/annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))
#     # Draw hand world landmarks.
#     if not results.multi_hand_world_landmarks:
#         continue
#     for hand_world_landmarks in results.multi_hand_world_landmarks:
#         mp_drawing.plot_landmarks(
#             hand_world_landmarks, mp_hands.HAND_CONNECTIONS, azimuth=5)
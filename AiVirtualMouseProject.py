import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy
import math
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CoInitialize, CoUninitialize, CLSCTX_ALL

##########################
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 7
#########################

# Initialize volume control
try:
    CoInitialize()
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volRange = volume.GetVolumeRange()
    minVol = volRange[0]
    maxVol = volRange[1]
    volume_control_available = True
except Exception as e:
    print(f"Warning: Volume control not available: {e}")
    volume_control_available = False
    minVol = -65.25
    maxVol = 0.0
    volume = None

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

# Additional variables for new features
click_count = 0
last_click_time = 0
drag_mode = False
prev_y = 0
scroll_sensitivity = 20

# Try different camera indices
cap = None
for i in range(3):  # Try camera indices 0, 1, 2
    print(f"Trying camera index {i}...")
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        ret, test_frame = cap.read()
        if ret and test_frame is not None:
            print(f"Camera found at index {i}")
            break
        cap.release()
    cap = None

if cap is None:
    print("Error: No camera found!")
    exit()

print("Camera initialized successfully")

cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
print(f"Screen size: {wScr} x {hScr}")

def draw_gesture_info(img, fingers):
    """Draw gesture information on the screen"""
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    for i, finger in enumerate(fingers):
        color = (0, 255, 0) if finger == 1 else (0, 0, 255)
        cv2.putText(img, f'{finger_names[i]}: {"UP" if finger == 1 else "DOWN"}', 
                   (10, 200 + i*25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    return img

def draw_mode_indicator(img, mode):
    """Draw current mode indicator"""
    cv2.putText(img, f'Mode: {mode}', (wCam - 200, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
    return img

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    
    # Check if frame is captured successfully
    if not success or img is None:
        print("Failed to capture frame from camera")
        continue
    
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Get finger positions
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Index finger tip
        x2, y2 = lmList[12][1:]  # Middle finger tip
        x3, y3 = lmList[16][1:]  # Ring finger tip
        x4, y4 = lmList[20][1:]  # Pinky finger tip
        x_thumb, y_thumb = lmList[4][1:]  # Thumb tip

        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
        
        # Draw finger status
        img = draw_gesture_info(img, fingers)

        # 4. MOUSE MOVEMENT MODE - Only Index Finger Up
        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            img = draw_mode_indicator(img, "MOUSE MOVE")
            
            # Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            
            # Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Move Mouse
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

        # 5. LEFT CLICK MODE - Index and Middle Fingers Up
        elif fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
            img = draw_mode_indicator(img, "LEFT CLICK")
            
            # Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            
            # Click mouse if distance is short
            if length < 40:
                current_time = time.time()
                if current_time - last_click_time < 0.5:  # Double click within 0.5 seconds
                    autopy.mouse.click()
                    autopy.mouse.click()  # Double click
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (255, 255, 0), cv2.FILLED)
                    cv2.putText(img, "DOUBLE CLICK", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                else:
                    autopy.mouse.click()  # Single click
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, "SINGLE CLICK", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                last_click_time = current_time
                time.sleep(0.3)  # Prevent multiple clicks

        # 6. RIGHT CLICK MODE - Index, Middle, and Ring Fingers Up
        elif fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 0:
            img = draw_mode_indicator(img, "RIGHT CLICK")
            
            # Find distance between index and ring finger
            length, img, lineInfo = detector.findDistance(8, 16, img)
            
            if length < 50:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 0, 255), cv2.FILLED)
                cv2.putText(img, "RIGHT CLICK", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                autopy.mouse.click(autopy.mouse.Button.RIGHT)
                time.sleep(0.3)        # 7. SCROLL MODE - Index and Pinky Up
        elif fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1:
            img = draw_mode_indicator(img, "SCROLL")
            
            current_y = lmList[8][2]  # Index finger y position
            if prev_y != 0:
                if current_y < prev_y - scroll_sensitivity:  # Moved up
                    # Use win32api for scrolling if available, otherwise skip
                    try:
                        import win32api
                        import win32con
                        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 120, 0)
                        cv2.putText(img, "SCROLL UP", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                    except ImportError:
                        cv2.putText(img, "SCROLL UP (WIN32 NOT AVAILABLE)", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                elif current_y > prev_y + scroll_sensitivity:  # Moved down
                    try:
                        import win32api
                        import win32con
                        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -120, 0)
                        cv2.putText(img, "SCROLL DOWN", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                    except ImportError:
                        cv2.putText(img, "SCROLL DOWN (WIN32 NOT AVAILABLE)", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            prev_y = current_y

        # 8. DRAG AND DROP MODE - Thumb and Index Up
        elif fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            if not drag_mode:
                # Start dragging
                drag_mode = True
                autopy.mouse.toggle(autopy.mouse.Button.LEFT, True)  # Mouse down
                cv2.putText(img, "DRAG START", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
            
            img = draw_mode_indicator(img, "DRAG MODE")
            
            # Continue moving while dragging
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
            
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY        # 9. VOLUME CONTROL - Thumb and Pinky Up
        elif fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1:
            if volume_control_available and volume is not None:
                img = draw_mode_indicator(img, "VOLUME CONTROL")
                
                # Find distance between thumb and pinky
                length, img, lineInfo = detector.findDistance(4, 20, img)
                
                # Convert distance to volume (50-200 pixel range)
                vol = np.interp(length, [50, 200], [minVol, maxVol])
                volBar = np.interp(length, [50, 200], [400, 150])
                volPer = np.interp(length, [50, 200], [0, 100])
                
                # Set volume
                volume.SetMasterVolumeLevel(vol, None)
                
                # Draw volume bar
                cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
                cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
                cv2.putText(img, f'{int(volPer)}%', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
            else:
                img = draw_mode_indicator(img, "VOLUME UNAVAILABLE")

        # 10. Stop dragging when no drag gesture is detected
        elif drag_mode:
            drag_mode = False
            autopy.mouse.toggle(autopy.mouse.Button.LEFT, False)  # Mouse up
            cv2.putText(img, "DRAG END", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

        # 11. IDLE MODE - No specific gesture
        else:
            img = draw_mode_indicator(img, "IDLE")

    # 12. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    # 13. Instructions
    cv2.putText(img, "Press 'q' to quit", (20, hCam - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # 14. Display
    cv2.imshow("AI Virtual Mouse", img)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
CoUninitialize()
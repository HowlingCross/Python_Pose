import cv2
from ultralytics import YOLO
import numpy as np
import video_sources

# --- FÜGGVÉNYEK ---
def calculate_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    if angle > 180.0: angle = 360-angle
    return angle

# --- FŐ PROGRAM ---
# 1. Videó kiválasztása
print("\n--- ELÉRHETŐ VIDEÓK ---")
for key, path in video_sources.video_list.items():
    print(f"[{key}] -> {path}")
choice = input("\nVálassz videót (szám): ")
video_path = video_sources.video_list.get(choice, list(video_sources.video_list.values())[0])

# Automatikus módválasztás a fájlnév alapján
if "front" in video_path.lower():
    MODE = "FRONT"
    print(f"\nMOD: FRONT (Szemből nézet érzékelve: {video_path})")
else:
    MODE = "SIDE"
    print(f"\nMOD: SIDE (Oldalnézet érzékelve: {video_path})")

model = YOLO('yolov8n-pose.pt')
cap = cv2.VideoCapture(video_path)

counter = 0 
direction = 0 # 0: Fent, 1: Lent
feedback = "START"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    if MODE == "SIDE":
    conf = result.keypoints.conf.cpu().numpy()[0]
    
    # Bal csukló (9) és Jobb csukló (10) megbízhatóságának összehasonlítása
    if conf[9] > conf[10]:
        idx_s, idx_e, idx_w = 5, 7, 9   # Bal oldal
        side_label = "BAL"
    else:
        idx_s, idx_e, idx_w = 6, 8, 10  # Jobb oldal
        side_label = "JOBB"
    
    shoulder, elbow, wrist = kp[idx_s], kp[idx_e], kp[idx_w]
    val = calculate_angle(shoulder, elbow, wrist)
    
    # Kiírjuk, melyik oldalt figyeli a rendszer 
    cv2.putText(frame, f"OLDAL: {side_label} (conf:{conf[idx_w]:.2f})", (50, 80), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
    # Kép átméretezése
    frame = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4)

    results = model(frame, verbose=False)
    
    for result in results:
        # 1. HIBAKERESÉS: Rajzoljuk ki a csontvázat!
        frame = result.plot() 

        if result.keypoints is not None:
            kp = result.keypoints.xy.cpu().numpy()[0]
            
            if len(kp) > 10:
                # --- OLDALNÉZET (SIDE) LOGIKA ---
                if MODE == "SIDE":
                    # Bal oldal (5,7,9) vagy Jobb oldal (6,8,10) - Automata döntés
                    # Azt az oldalt választjuk, ahol a csukló jobban látszik (conf)
                    idx_s, idx_e, idx_w = (5, 7, 9) if kp[9][0] > 0 else (6, 8, 10)
                    
                    shoulder, elbow, wrist = kp[idx_s], kp[idx_e], kp[idx_w]
                    val = calculate_angle(shoulder, elbow, wrist) # Ez a szög
                    
                    # Logika
                    if val <= 90: # Kicsit engedékenyebb (85 helyett 90)
                        if direction == 0:
                            direction = 1
                            feedback = "LENT (OK)"
                    
                    if val >= 150: # Kicsit engedékenyebb (160 helyett 150)
                        if direction == 1:
                            counter += 1
                            direction = 0
                            feedback = "FENT (OK)"

                    # Kiírjuk az értéket a fejed fölé
                    cv2.putText(frame, f"SZOG: {int(val)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

                # --- SZEMBŐL (FRONT) LOGIKA ---
                elif MODE == "FRONT":
                    # Váll és Könyök Y (magasság) különbsége
                    l_sh, r_sh = kp[5], kp[6]
                    l_el, r_el = kp[7], kp[8]
                    
                    avg_sh_y = (l_sh[1] + r_sh[1]) / 2
                    avg_el_y = (l_el[1] + r_el[1]) / 2
                    
                    val = avg_el_y - avg_sh_y # Ez a távolság pixelben
                    
                    # Logika (határértékek)
                    if val < 50: # Ha a vállad majdnem egyvonalban van a könyökkel -> LENT
                        if direction == 0:
                            direction = 1
                            feedback = "LENT (OK)"
                    
                    if val > 100: # Ha a vállad magasan van -> FENT
                        if direction == 1:
                            counter += 1
                            direction = 0
                            feedback = "FENT (OK)"

                    # Kiírjuk az értéket
                    cv2.putText(frame, f"TAVOLSAG: {int(val)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

                # --- SZÁMLÁLÓ ---
                cv2.rectangle(frame, (0, 0), (300, 120), (255, 255, 255), 2) # Fehér keret
                cv2.putText(frame, f"DB: {counter}", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
                cv2.putText(frame, feedback, (150, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow('Pushup Debugger', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'): break # Lassítottam kicsit (20ms), hogy lásd

cap.release()
cv2.destroyAllWindows()

import cv2
import time
import os
import numpy as np
import datetime

duration_hours = 1  #cứ cách một giờ chuyển sang tệp khác để lưu
log = 1

def capture_images(output_folder, duration_hours):
    # Mở webcam
    cap = cv2.VideoCapture(0)

    # Kiểm tra xem webcam có được mở không
    if not cap.isOpened():
        print("Error opening webcam.")
        return
    
    check = 1   #check =1 nghia la chua ghi anh
    start_time = time.time()
    end_time = start_time + duration_hours * 60 * 60  # Tính thời điểm kết thúc sau một số giờ
    # Bắt đầu quay và ghi video
    while 1:
        ret, frame = cap.read()
        # Kiểm tra xem frame có được đọc đúng không
        if not ret:
            print("Error in retrieving frame.")
            break

        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # lay thoi gian de tao ten thu muc
        if (check == 1) or time.time() >= end_time:
            time_start_for_folder = current_time
            output_folder_path = f'{output_folder}/image_{time_start_for_folder}'
            if not os.path.exists(output_folder_path):
                os.makedirs(output_folder_path)
            check = 0

        if time.time() >= end_time:
            end_time += duration_hours*60*60    

        output_file = f'{output_folder_path}/image_{current_time}.PNG'

        # Hiển thị thời gian trên ảnh
        cv2.putText(frame, current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # Lưu ảnh vào thư mục
        cv2.imwrite(output_file, frame)

        # Hiển thị ảnh trong cửa sổ
        cv2.imshow('Captured Image', frame)

        # Kiểm tra phím 'q' để thoát
        if (cv2.waitKey(1) == ord('q')) or (log == 0):
            cap.release
            cv2.destroyAllWindows
            break    


output_folder = 'output_images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Gọi hàm để chụp ảnh và ghi lại mỗi giờ
while log:
    capture_images(output_folder, duration_hours)



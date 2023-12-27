import imageio.v2 as imageio  
import os
from natsort import natsorted
import cv2

def create_video_from_images(input_folder, output_video_path, fps=20):
    images = []
    
    # Đọc tất cả các tệp trong thư mục hình ảnh với định dạng .PNG và sắp xếp chúng theo thứ tự tự nhiên
    image_files = natsorted(os.listdir(input_folder))
    for filename in image_files:
        if filename.lower().endswith('.png'):
            img_path = os.path.join(input_folder, filename)
            images.append(img_path)

    # Lấy kích thước của ảnh đầu tiên để cài đặt kích thước video
    img = imageio.imread(images[0])
    height, width, _ = img.shape

    # Tạo VideoWriter để ghi video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Ghi các ảnh vào video
    for image in images:
        img = imageio.imread(image)
        out.write(img)

    # Đóng VideoWriter khi đã xong
    out.release()

# Đặt đường dẫn thư mục chứa ảnh và đường dẫn của video đầu ra
input_image_folder = 'output_images'
output_video_path = 'output_video.avi'

# Gọi hàm để tạo video từ ảnh
create_video_from_images(input_image_folder, output_video_path)

# 从人脸图像文件中提取人脸特征存入 CSV

import os
import dlib
from skimage import io
import csv
import cv2
import numpy as np

# 要读取人脸图像文件的路径
path_images_from_camera = "C:\\Users\\ASUS\\Desktop\\Elderly-Care\\Data\\data_faces_from_camera\\"

# 1. Dlib 正向人脸检测器
# detector = dlib.get_frontal_face_detector()
# OpenCV DNN face detector
detector = cv2.dnn.readNetFromCaffe("C:\\Users\\ASUS\\Desktop\\Elderly-Care\\Data\\data_opencv\\deploy.prototxt.txt",
                                    "C:\\Users\\ASUS\\Desktop\\Elderly-Care\\Data\\data_opencv\\res10_300x300_ssd_iter_140000.caffemodel")

# 2. Dlib 人脸 landmark 特征点检测器
predictor = dlib.shape_predictor('C:\\Users\\ASUS\\Desktop\\Elderly-Care\\Data\\data_dlib\\shape_predictor_68_face_landmarks.dat')

# 3. Dlib Resnet 人脸识别模型，提取 128D 的特征矢量
face_reco_model = dlib.face_recognition_model_v1("C:\\Users\\ASUS\\Desktop\\Elderly-Care\\Data\\data_dlib\\dlib_face_recognition_resnet_model_v1.dat")


# 返回单张图像的 128D 特征
def return_128d_features(path_img):
    img_rd = io.imread(path_img)
    (h, w) = img_rd.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img_rd, (300, 300)), 1.0,
                                 (300, 300), (104.0, 177.0, 123.0))
    detector.setInput(blob)
    faces = detector.forward()

    print("%-40s %-20s" % ("检测到人脸的图像 \ Image with faces detected:", path_img), '\n')

    # 因为有可能截下来的人脸再去检测，检测不出来人脸了
    # 所以要确保是 检测到人脸的人脸图像 拿去算特征
    if faces.shape[2] != 0:
        box = faces[0, 0, 0, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        rect = dlib.rectangle(startX, startY, endX, endY)
        shape = predictor(img_rd, rect)
        face_descriptor = face_reco_model.compute_face_descriptor(img_rd, shape)
    else:
        face_descriptor = 0
        print("no face")

    return face_descriptor


# 将文件夹中照片特征提取出来, 写入 CSV
def return_features_mean_personX(path_faces_personX):
    features_list_personX = []
    photos_list = os.listdir(path_faces_personX)
    if photos_list:
        for i in range(len(photos_list)):
            # 调用return_128d_features()得到128d特征
            print("%-40s %-20s" % ("正在读的人脸图像 \ Image to read:", path_faces_personX + "/" + photos_list[i]))
            features_128d = return_128d_features(path_faces_personX + "/" + photos_list[i])
            #  print(features_128d)
            # 遇到没有检测出人脸的图片跳过
            if features_128d == 0:
                i += 1
            else:
                features_list_personX.append(features_128d)
    else:
        print("文件夹内图像文件为空  \ Warning: No images in " + path_faces_personX + '\ ', '\n')

    # 计算 128D 特征的均值
    # personX 的 N 张图像 x 128D -> 1 x 128D
    if features_list_personX:
        features_mean_personX = np.array(features_list_personX).mean(axis=0)
    else:
        features_mean_personX = np.zeros(128, dtype=int, order='C')

    return features_mean_personX


# 获取已录入的最后一个人脸序号 / get the num of latest person
person_list = os.listdir("C:\\Users\\ASUS\\Desktop\\Elderly-Care\\Data\\data_faces_from_camera\\")
person_num_list = []
for person in person_list:
    person_num_list.append(int(person.split('_')[-1]))
person_cnt = max(person_num_list)

with open("C:\\Users\\ASUS\\Desktop\\Elderly-Care\\Data\\features_all.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for person in range(person_cnt):
        # Get the mean/average features of face/personX, it will be a list with a length of 128D
        print(path_images_from_camera + "person_" + str(person + 1))
        features_mean_personX = return_features_mean_personX(path_images_from_camera + "person_" + str(person + 1))
        writer.writerow(features_mean_personX)
        print("特征均值 \ The mean of features:", list(features_mean_personX))
        print('\n')
    print("所有录入人脸数据存入 \ Save all the features of faces registered into: data\\features_all.csv")

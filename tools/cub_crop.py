'''
crop birds from bounding boxes
'''

import os
import cv2

if __name__ == '__main__':

    image_list = 'CUB_200_2011/images.txt'
    bbox_list = 'CUB_200_2011/bounding_boxes.txt'
    img_dir = 'CUB_200_2011/images_train'
    #img_dir = 'CUB_200_2011/images_test'
    # where to save
    save_dir = 'CUB_200_2011/images_test_cropped'

    id_to_name = {}
    with open(image_list, 'r') as rf:
        for line in rf:
            id, name = line.split()
            id_to_name[id] = name


    with open(bbox_list, 'r') as rf2:
        valid_num = 0
        for k, line2 in enumerate(rf2):
            id2, bbox_str = line2.split(maxsplit=1)
            cur_img_name = id_to_name[id2]
            cur_img_dir = os.path.join(img_dir, cur_img_name)
            cur_img = cv2.imread(cur_img_dir)
            if cur_img is None:
                continue
            cropped_img_name = os.path.join(save_dir, cur_img_name)
            cropped_img_dir = os.path.dirname(cropped_img_name)
            if not os.path.exists(cropped_img_dir):
                os.mkdir(cropped_img_dir)

            bbox = [round(float(x)) for x in bbox_str.split()]
            cropped_img = cur_img[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]
            valid_num += 1
            print('{}/{} processing {}'.format(valid_num, k, cur_img_name))
            cv2.imwrite(cropped_img_name, cropped_img)

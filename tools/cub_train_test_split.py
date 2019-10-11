'''
split cub dataset into train and test

'''

import os


if __name__ == '__main__':
    image_list = 'CUB_200_2011/images.txt'
    train_test_list = 'CUB_200_2011/train_test_split.txt'
    # original image
    img_dir = 'CUB_200_2011/images'
    # where to save
    test_dir = 'CUB_200_2011/images_test'

    if not os.path.exists(test_dir):
        os.mkdir(test_dir)

    for folder in os.listdir(img_dir):
        test_folder = os.path.join(test_dir, folder)
        os.mkdir(test_folder)

    id_to_name = {}
    with open(image_list, 'r') as rf:
        for line in rf:
            id, name = line.split()
            id_to_name[id] = name

    with open(train_test_list, 'r') as rf2:
        test_num = 0
        for line2 in rf2:
            id2, is_train = line2.split()
            if is_train == '0':
                test_num += 1
                move_img = id_to_name[id2]
                img_path = os.path.join(img_dir, move_img)
                move_to = os.path.join(test_dir, move_img)
                print('test num: {}, moving {}'.format(test_num, move_img))
                os.rename(img_path, move_to)




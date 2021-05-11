import cv2
import json
from skimage import io
import numpy as np


def find_best_bounding_box(filename):
    """
    Function to get the best bounding box out of the good ones

    Parameters
    ----------
    filenames : The output file after running the function find_good_bounding_boxes.py
    Please call the function with river-oaks/results.json to get the final results of the river oaks region.
    Then call the function with greater-heights/results.json to get the final results of the greater heights region.
    """

    result_dict = dict()
    with open(filename, 'r') as f:
        file = json.load(f)
        for img_url in file:
            all_bboxes = file[img_url]

            if len(all_bboxes) == 0:
                continue

            images = []
            for index, bboxes in enumerate(all_bboxes):
                img = io.imread(img_url)
                for bbox in bboxes:
                    x, y, h, w, label = bbox['left'], bbox['top'], bbox['height'], bbox['width'], bbox['label']
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(img, label, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
                cv2.putText(img, str(index), (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                images.append(img)
            concat_img = np.concatenate(images, axis=1)
            cv2.imshow('Image', concat_img)
            while True:
                k = cv2.waitKey(0)
                if k == ord('n'):
                    # do nothing here as we do not want this image
                    print('Image deleted')
                    break
                elif k == ord('0'):
                    result_dict[img_url] = all_bboxes[0]
                    print('0 Chosen')
                    break
                elif k == ord('1'):
                    result_dict[img_url] = all_bboxes[1]
                    print('1 Chosen')
                    break
                elif k == ord('2'):
                    result_dict[img_url] = all_bboxes[2]
                    print('2 Chosen')
                    break
                else:
                    result_dict[img_url] = all_bboxes[3]
                    print('3 Chosen')
                    break
    directory = filename.split('/')[0]
    with open(directory + '/final.json', 'w') as f:
        json.dump(result_dict, f)


# find_best_bounding_box('river-oaks/results.json') # comment this when running greater-heihts 

# After running this with river-oaks, please run with greater-heights
find_best_bounding_box('greater-heights/results.json') #uncomment this after running river-oaks

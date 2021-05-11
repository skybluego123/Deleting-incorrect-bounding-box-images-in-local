import csv
import cv2
from skimage import io
import json


def review_goodness_of_bounding_box(*filenames):
    """
    Function to review whether the bounding boxes drawn by the participants are complete and good

    Parameters
    ----------
    filenames : The output of the bounding box task from mturk
    Please call the function with river-oaks/Batch_4363955_batch_results.csv to get the results of the river oaks region.
    Then call the function with greater-heights/ to get the results of the greater heights region.
    """

    result_dict = dict()

    for filename in filenames:
        print(filename)
        with open(filename, 'r', newline='') as csvfile:
            f = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
            _ = next(f)
            for index, row in enumerate(f):
                img_url = row[27]

                if img_url not in result_dict:
                    result_dict[img_url] = []

                assign_id = row[14]
                img = io.imread(img_url)
                bboxes = json.loads(row[28])
                for bbox in bboxes:
                    height, label, left, top, width = bbox['height'], bbox['label'], bbox['left'], bbox['top'], bbox[
                        'width']
                    cv2.rectangle(img, (left, top), (left + width, top + height), (0, 255, 0), 2)
                    cv2.putText(img, label, (left, top-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

                cv2.imshow('Image', img)
                while True:
                    k = cv2.waitKey(0)
                    if k == ord('y'):
                        result_dict[img_url].append(bboxes)
                        print('Yes')
                        break
                    elif k == ord('n'):
                        print('No')
                        break
                # uncomment to perform only sample images    
                # if index == 7:
                #     break
    directory = filenames[0].split('/')[0]
    print(directory)
    with open(directory + '/results.json', 'w') as f:
        json.dump(result_dict, f)


# review_goodness_of_bounding_box('river-oaks/Batch_4363955_batch_results.csv') # comment this when running greater-heihts 

# After running this with river-oaks, please run with greater-heights
review_goodness_of_bounding_box('greater-heights/Batch_4363963_batch_results.csv') #uncomment this after running river-oaks

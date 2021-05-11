import cv2
import json
from skimage import io


def view_bounding_boxes(filename):
    with open(filename, 'r') as f:
        file = json.load(f)
        for image_url in file:
            bboxes = file[image_url]
            img = io.imread(image_url)
            for bbox in bboxes:
                x, y, h, w, label = bbox['left'], bbox['top'], bbox['height'], bbox['width'], bbox['label']
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, label, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

            cv2.imshow('Image', img)
            k = cv2.waitKey(0)

# view_bounding_boxes('river-oaks/results.json')
view_bounding_boxes('greater-heights/results.json')


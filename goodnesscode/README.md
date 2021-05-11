# Instructions

- First activate the conda environment using `conda activate ve1`
- Run `python find_good_bounding_boxes.py`
    a. Make sure line 59 is `review_goodness_of_bounding_box('river-oaks/Batch_4363955_batch_results.csv')`
- After completing this task, a new file called `results.json` will be creaed in the folder `river-oaks`
- Now run `python find_best_bounding_box.py`
    a. Make sure line 65 is `find_best_bounding_box('river-oaks/results.json')`
- After completing this task, a new file called `final.json` will be created in the folder `river-oaks`
- Now we can do the same with greater-heights
- For this, first comment line 59 in `find_good_bounding_boxes.py` file and line 65 in `find_best_bounding_box.py`
- Now uncomment line 62 in `find_good_bounding_boxes.py` file and line 68 in `find_best_bounding_box.py`
- Run `python find_good_bounding_boxes.py`
- After completing this task, a new file called `results.json` will be created in the folder `greater-heights`
- Now run python `find_best_bounding_box.py`
- After completing this task, a new file caled `final.json` will be created in the folder `greater-heights`

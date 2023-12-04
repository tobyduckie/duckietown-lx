from typing import Tuple


def DT_TOKEN() -> str:
    # TODO: change this to your duckietown token
    dt_token = "dt1-3nT7FDbT7NLPrXykNJW6pwkBovivhmH8yTicMqz4S8beXFJ-43dzqWFnWd8KBa1yev1g3UKnzVxZkkTbfR1jDBc6BLdiPaUMy4s1Ue5SaoxJHzxsi1"
    return dt_token


def MODEL_NAME() -> str:
    # TODO: change this to your model's name that you used to upload it on google colab.
    # if you didn't change it, it should be "yolov5n"
    return "yolov5n"


def NUMBER_FRAMES_SKIPPED() -> int:
    # TODO: change this number to drop more frames
    # (must be a positive integer)
    return 3


def filter_by_classes(pred_class: int) -> bool:
    """
    Remember the class IDs:

        | Object    | ID    |
        | ---       | ---   |
        | Duckie    | 0     |
        | Cone      | 1     |
        | Truck     | 2     |
        | Bus       | 3     |


    Args:
        pred_class: the class of a prediction
    """
    # Right now, this returns True for every object's class
    # TODO: Change this to only return True for duckies!
    if pred_class == 0:
        state = True
    else:
        state = False

    # In other words, returning False means that this prediction is ignored.
    return state


def filter_by_scores(score: float) -> bool:
    """
    Args:
        score: the confidence score of a prediction
    """
    # Right now, this returns True for every object's confidence
    # TODO: Change this to filter the scores, or not at all

    # (returning True for all of them might be the right thing to do!)
    return True


def filter_by_bboxes(bbox: Tuple[int, int, int, int]) -> bool:
    """
    Args:
        bbox: is the bounding box of a prediction, in xyxy format
                This means the shape of bbox is (leftmost x pixel, topmost y, rightmost x, bottommost y)
    """
    print('leftmost x pixel = ', bbox[0])
    print('rightmost x pixel = ', bbox[2])
    print('bottommost y = ', bbox[3])
    #if bbox[0] >= 250 and bbox[3]>=250 and bbox[2]-bbox[0]>=30:
    if bbox[0] >= 100 and bbox[3]>=300 and bbox[2]-bbox[0]>=50:
        state = True
    else:
        state = False
    
    # TODO: Like in the other cases, return False if the bbox should not be considered.

    return state

# Names: Zachary Kim, Keegan Sand
# Lab: Lab5 (Multimodal AI with Ollama)
# Date: 10/3/25

## 3.2 Compare this to zero-shot. Does adding guidelines help? In what situations do the guidelines seem to matter most?

* Yes, adding guidelines improved classification accuracy. Without guidelines, the model misidentified leisure and work. All 3 examples were identified differently when the examples were given. Adding guidelines changed the definitions as we would expect, except for the Yoga_Class.jpg, which classified the image as work, when we would say it is leisure:

```
Image: Sergio_Ottolina_1964.jpg
Basic classification:  LEISURE
With guidelines:       WORK
Different result:      YES ✓

Image: Arles_Busker_IMG_8299.jpg
Basic classification:  LEISURE
With guidelines:       WORK
Different result:      YES ✓

Image: Yoga_Class.jpg
Basic classification:  LEISURE
With guidelines:       WORK
Different result:      YES ✓
```

* Images with explicit context are the easiest to classify, and images with implied context are significantly more difficult to classify.

## 4.1 - Does the object count seem accurate?

* No, the object count, circle count, nor descriptions are accurate. Only the item type, dice, was correctly identified:

```
Object Detection
==================================================

Detected objects: Dice, white, red, green, white
Circle count: 21
```

* We would expect:
  * Detected objects: Dice, blue, red, green, yellow
  * Circle count: ~40
  * Running the model multiple times yields the same results. The model is confidently incorrect.

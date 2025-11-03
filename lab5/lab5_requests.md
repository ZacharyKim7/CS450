# Names: Your name and your lab partner's name
# Lab: Lab5 (Multimodal AI with Ollama)
# Date: Today's date

## 1. Image Understanding

* Yes, the image descriptions were very accurate.

* The model covered the subject, background, colors, environment, and animal position in a way that it clearly referring to the source image.

* The model describes the mood of the image and the feelings the viewer would invoke, which was unecessary and not very accurate.

## 2. Classification Performance

* The zero-shot classification prompting performed quite well, selecting the correct category. However, the model had a tendancy to ignore the options and return what it believes is the best answer:

```
Image: https://upload.wikimedia.org/wikipedia/commons/a/a8/Tour_Eiffel_Wikimedia_Commons.jpg
Categories: ['home', 'box', 'cat tower', 'cabinet']
Classification: Eiffel Tower
```

* Yes, adding guidelines improved classification accuracy. Without guidelines, the model misplaced leisure and work. Adding guidelines changed the definitions as we would expect, except for the Yoga_Class.jpg, which classified the image as work, when I would say it is leisure:

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
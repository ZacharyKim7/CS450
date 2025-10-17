# Name: Zachary Kim
# Lab: Lab3 (Advanced Prompt Engineering)
# Date: 17 October 2025

## Task 3.2: Read the problem statement here: https://en.wikipedia.org/wiki/Wolf,_goat_and_cabbage_problem 

Q. Look at the problem statement in the prompt above. Do you notice any difference? Did the LLM provide an *efficient* response?

A. The prompts are different in that we only ask to save the goat, not all 3 as is in the original prompt. No, the LLM did not provide an efficient response: We gave it a well known puzzle, but only asked to save the goat, not all 3. The LLM gave instructions on how to save all 3 according to the original problem. While the solution is technically correct in that it does show how to save the goat, it used more instructions than what was needed, demonstrating that its bias towards commonly seen solutions outweighed our explicit instructions.

## Task 6.1.2

Q. Run the new Snake game. How is it different from the first version?

A. snake2.py includes around 40 additional lines of code in order to support two new features: changing game speed with a speed boost, and a shield that prevents death on collision; both of the power ups appear on the screen as the fruit would, and can be collected by the player to receive the effects for 10 seconds.
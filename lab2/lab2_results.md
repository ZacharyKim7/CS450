1. Zero-Shot and Few-Shot:

    * When would you choose zero-shot?
   
        * Zero-shot prompting is useful if the task is straightfoward and doesn't need extra context to be completed correctly, if you desire speed and simplicity, if you are asking for open-ended questions that value creativity, or when the output does not need strict formatting.
          
    * When is few-shot worth the extra effort?
      
        * few-shot is valuable when the output of the task needs to follow a strict style or format (eg. JSON), then the output is not standard (eg. using bullets instead of paragraphs or numbers instead of bullets), to prevent hallucination, or to control the output tone.
       
    * How did the classification output change from Task 3.11 Task 3.12
   
        * Changing the classifications of the example messages had a surprisingly low impact on message like "important" or "normal", remaining as their correct classification even when changing the examples to be incorrect. We were able to change the classification of spam messages to be important or normal though, indiciating that the model has some sort of pre-existing bias that makes the model classify the inputs the same regardless of what we say they are.
   
    * How did the generated code change from Task 3.21 to Task 3.22?
      
        * The generated code became less concise and more verbose in that 3.22 included documentation and more variation, while the 3.21 code gneration stuck to clean 1 line solutions like the examples.
     
    


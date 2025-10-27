# Names: Zachary Kim, Josh Garbi
# Lab: Lab4 (Retrieval Augmented Generation)
# Date: 10/27/25

## 5.1.1 - Does the structure of the questions seem to matter?

 * Yes, very short questions without question marks or broader context confuse the LLM, as demonstrated by:

 ```
 Q: Instructor: 
 A: I don't know.

 Q: Tell me about the CS450 instructor:
 A: The CS450 course is taught by Chiké Abuah. He can be reached via email at chike.abuah@wallawalla.edu and has an office located in KRH 329.
 ```

 * Putting two separate concepts into the same question seems to confuse the LLM, as demonstrated by:

 ```
Q: What is the CS450 Week of Worship?
A: I don't know.

Q: Tell me about the Week of Worship
A: The Week of Worship is a scheduled event that may cause adjustments to our class meeting times during the second week of the quarter.
 ```

 * Unrelated topics in the question can confuse the LLM into searching for more exact matches; in this case, CS450 + Week of Worship. CS450 and Week of Worship are understood independently with the source data, but there is no clear data on matching an answer for both.

## 5.1.2 - Would you say that RAG has limitations based on this exercise?

 * Yes. You need to understand your data well enough to know if the LLM has confidently given you a wrong answer, and ask clear questions that well match the answers found in the source data.

## 5.1.3 - Did you notice anything about the course name in the questions? Is that course name actually in the context? What does this demonstrate?

 * Yes, the course name in the questions is "CS450" while the actual course name is "CPTR450".

 * While the questions had the wrong course name, the LLM was still able to answer the properly worded questions correctly, indicating that the LLM can infer what we mean if we input similar words; CS### is a commonly used naming convention for similar courses. It demonstrates how LLMs are able to handle slight mismatches like typos or alternative naming schemes.

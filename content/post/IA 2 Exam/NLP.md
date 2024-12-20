---
title: NLP for IA 2 Exam
date: 2024-10-07
---
# Assignment

![NLP Assiginment](https://i.imgur.com/OTEBXxw.png)


![NLP Syllabus](https://i.imgur.com/JOO0Ukg.png)


# Module 4 : 

## Sementic analysis


### Defination
Semantic analysis in Natural Language Processing (NLP) is the process of understanding the meaning and interpretation of words, phrases, and sentences in a way that mimics how humans comprehend language. 

or

Semantic analysis is the process of finding the meaning of text.
It can direct computers to understand and interpret sentences, paragraphs or
whole documents by analyzing their grammatical structure and identifying the
relationships between individual words of sentence in a particular context.

### Goal
to capture not just the individual meanings of words, but also how they combine to form coherent and meaningful ideas in a larger context.

The aim of semantic analysis is to draw exact meaning or dictionary meaning
from the text.

### Example

The purpose of this analyzer is to check the text for ==meaningfulness, most==
==important task is to get the proper meaning of sentence.== E.g. “Govind is great”
in this sentence the speaker is talking about lord Govind or about a person
whose name is Govind.

### Uses
This analysis is used in extracting the important information from achieving
human level accuracy from the computers.

It is used in tools like Machine Translations, chatbots, search engines and text
analysis.

### Syntactic & Semantic Analysis:

- Syntactic analysis determines and checks whether the instance of the language is “well formed” and analyze its grammatical structure.
- Semantic analysis analyses its meaning & find out whether it “makes sense”.
- Syntactic analysis depends on the types of words, but not on their meaning.
###  Semantic analysis in NLP
- Semantic analysis is the subfield of NLP & ML
- It tries to clear the context of any text and makes one realize the emotions inherent in the sentence.

![](https://i.imgur.com/ZKqQ3ym.png)

[Understand Sementic analysis](Sementic_analysis_in_hindi )


##  Lexical Seantic

### 1. **Definition**:

Lexical semantics is the branch of linguistics and Natural Language Processing (NLP) that deals with the meaning of words and the relationships between them. It involves understanding how words convey meaning in different contexts and how they are related to one another in terms of synonyms, antonyms, hyponyms, and more.

### 2. **Aim / Goal**:

The main aim of lexical semantics is to:
- Analyze and understand the meaning of individual words.
- Establish relationships between words, like similarity, opposition, or inclusion.
- Help machines and algorithms in NLP to correctly interpret the meaning of words in different contexts.
- Enable computers to perform tasks like text summarization, sentiment analysis, and machine translation by understanding word meanings.

### 3. **Applications**:

Lexical semantics has wide applications in NLP and related areas:
- **Machine Translation**: To accurately translate text by understanding word meanings in context.
- **Information Retrieval**: Enhances search engines by improving search result relevance based on word meaning.
- **Text Summarization**: Helps summarize long texts by understanding the key words and their meanings.
- **Sentiment Analysis**: Understands the sentiment (positive, negative, neutral) behind words used in reviews, social media, etc.
- **Chatbots and Virtual Assistants**: Helps AI understand user queries by interpreting word meanings.

### 4. **Features**:

- **Word Relationships**: Lexical semantics identifies various relationships like synonyms (similar words), antonyms (opposite words), and hyponyms (specific terms under a broader term).
- **Context Sensitivity**: The meaning of words changes based on the context in which they are used.
- **Polysemy and Homonymy**: Identifies words with multiple meanings (polysemy) and words that sound or are spelled the same but have different meanings (homonymy).
- **Word Similarity**: Determines how similar or different words are based on their meanings.
  
### 5. **Advantages**:

- **Improved Understanding**: It allows machines to process text more naturally, understanding word meaning and context just like humans.
- **Better Translation**: Ensures more accurate translations by capturing the nuances of word meaning.
- **Enhanced Search**: Improves search engine results by considering synonyms and related terms.
- **Contextual Relevance**: Helps in applications like text summarization and sentiment analysis by capturing the meaning of words in context.
  
### 6. **Disadvantages / Limitations**:

- **Ambiguity**: Some words have multiple meanings (polysemy), making it difficult for systems to always determine the correct meaning.
- **Lack of World Knowledge**: Machines struggle to understand word meanings in real-world scenarios without having external, world knowledge.
- **Complexity in Large Texts**: When dealing with large corpora of text, the variety of meanings can increase complexity.
- **Dependency on Language Data**: For effective lexical analysis, systems need large, diverse datasets. Without them, the results can be inaccurate.

### 7. **Examples**:

- **Word Sense Disambiguation**: In the sentence, "I went to the bank," lexical semantics helps determine if "bank" refers to a financial institution or the side of a river.
- **Hyponymy**: Understanding that "rose" is a type of "flower" helps in classifying and organizing words.
- **Synonymy in Search Engines**: Searching for "buy car" also retrieves results for "purchase automobile" because lexical semantics helps relate these words.

You can use this structure in your exam to give a complete and clear explanation of lexical semantics.


Here's a detailed breakdown of the given topics related to **Lexical Semantics**, corpus studies, dictionaries like WordNet and BabelNet, and word relations.

---

##  **Corpus Study**:

A **corpus** is a large and structured collection of texts, often used in linguistics for studying language. In NLP, a **corpus study** helps analyze real-world language usage by examining patterns, meanings, and relationships in a massive body of texts. 

#### Key Points:
- **Purpose**: To analyze word usage, frequency, and meaning in natural language.
- **Application**: Used in training NLP models for tasks like translation, sentiment analysis, etc.
- **Examples of Corpora**: British National Corpus (BNC), Penn Treebank, Google Books Corpus.
- **Importance**: It helps in understanding linguistic structures and provides data for language processing algorithms.

---

## **Study of Language Dictionaries**:

#### a) **WordNet**:
- **WordNet** is a large lexical database of English where words are grouped into sets of synonyms called **synsets**.
- Each synset represents a distinct concept, and the words within a synset are interchangeable in some contexts.
  
  **Relations in WordNet**:
  - **Synonymy**: Words with similar meanings.
  - **Antonymy**: Words with opposite meanings.
  - **Hyponymy**: Specific terms under a broader category (e.g., "dog" is a hyponym of "animal").
  - **Meronymy**: Part-whole relationships (e.g., "wheel" is a part of "car").
  
  **Usage**: Widely used in NLP applications like word sense disambiguation and text classification.

#### b) **BabelNet**:
- **BabelNet** is a multilingual lexical network that integrates information from WordNet and Wikipedia, covering multiple languages.
- It links words and concepts across different languages, making it useful for tasks like **machine translation** and **cross-lingual information retrieval**.

  **Relations in BabelNet**:
  - **Multilingual Synsets**: Words in different languages that refer to the same concept.
  - **Conceptual Relations**: Similar to WordNet, but extended across languages.

  **Usage**: It is used in cross-linguistic NLP tasks, multilingual semantic analysis, and machine translation.

---

## **Relations Among Lexemes & Their Senses**:
Lexical semantics studies the relationships between **lexemes** (words) and their **senses** (meanings). Here are the key relations:

#### a) **Homonymy**:
- Words that share the same spelling or pronunciation but have **different and unrelated meanings**.
- Example: 
  - "Bat" (cricket bat) vs. "Bat" (flying mammal).
  
  **Types**:
  - **Homophones**: Words that sound the same but have different meanings (e.g., "bare" vs. "bear").
  - **Homographs**: Words that are spelled the same but have different meanings (e.g., "lead" as a metal vs. "lead" as to guide).

#### b) **Polysemy**:
- A word has **multiple related meanings**.
- Example: 
  - "Head" (body part) vs. "Head" (leader of a group).
  
  **Importance**: Polysemy is common in natural languages, and disambiguating such meanings is crucial for NLP applications.

#### c) **Synonymy**:
- Words that have **similar or identical meanings**.
- Example: 
  - "Happy" and "Joyful".
  
  **Usage**: Understanding synonyms helps in improving search engines and text processing by recognizing words with similar meanings.

#### d) **Hyponymy**:
- A relationship where a word represents a **subtype** of a broader category.
- Example:
  - "Dog" is a hyponym of "Animal", and "Rose" is a hyponym of "Flower".
  
  **Importance**: Hyponymy is useful for organizing information hierarchically and understanding taxonomies in NLP.

---

## **Semantic Ambiguity**:
Semantic ambiguity occurs when a word, phrase, or sentence can have **multiple meanings**. There are two main types of semantic ambiguity:

#### a) **Lexical Ambiguity**:
- Ambiguity in the meaning of a single word.
- Example: 
  - "Bank" can refer to a financial institution or the side of a river.

#### b) **Structural Ambiguity**:
- Ambiguity that arises from the structure or grammar of a sentence.
- Example: 
  - "Visiting relatives can be annoying." (It is unclear whether "visiting" is an action or describes the relatives).
  
  **Impact on NLP**: Ambiguity complicates tasks like machine translation, question answering, and semantic analysis because the system needs to understand which meaning is intended based on context.

![Ambiguities](https://i.imgur.com/N0Zf0Rq.png)

---

### Summary:
1. **Corpus Study**: Involves analyzing large text collections to understand language patterns.
2. **WordNet**: A lexical database that groups words into synsets based on meanings and relationships.
3. **BabelNet**: A multilingual lexical network linking words across languages.
4. **Relations**:
   - **Homonymy**: Same spelling or pronunciation, different meanings.
   - **Polysemy**: Multiple related meanings for a word.
   - **Synonymy**: Words with similar meanings.
   - **Hyponymy**: Specific words under broader categories.
5. **Semantic Ambiguity**: Ambiguity in word or sentence meaning that complicates text understanding.

This detailed understanding of these concepts is essential for tackling tasks in NLP, such as machine translation, word sense disambiguation, and semantic analysis.


**Word Sense Disambiguation (WSD)** is the process of determining which meaning (or **sense**) of a word is intended in a given context. In natural language processing (NLP), many words have multiple meanings (polysemy), so it is crucial to accurately identify the correct sense of the word to understand the overall meaning of the text.

## 1. **Word Sense Disambiguation (WSD)**:
- **Definition**: WSD is the task of identifying which sense of a word is used in a sentence, especially when the word has multiple meanings.
- **Example**: The word "bank" could mean either a financial institution or the side of a river. In WSD, the goal is to determine which meaning is intended based on the surrounding context.
  
---

## 2. **Knowledge-based Approach (Lesk's Algorithm)**:
Knowledge-based approaches use pre-existing lexical resources (like dictionaries or thesauruses) to determine the meaning of words.

#### **Lesk's Algorithm**:
- **Lesk's Algorithm** is a **knowledge-based WSD method** that disambiguates words by comparing the dictionary definitions (or glosses) of each possible sense of a word to the context in which the word appears.
  
  **Working**:
  - For each sense of an ambiguous word, Lesk's algorithm calculates how much **overlap** there is between the dictionary definition of that sense and the words in the surrounding context.
  - The sense with the highest overlap is selected as the most likely meaning.

  **Example**:
  - In the sentence, "I went to the bank to fish," Lesk’s algorithm would check the glosses of the word "bank" (both financial institution and riverbank) and find that "riverbank" overlaps with the word "fish," thus selecting the riverbank meaning.

  **Limitation**:
  - Lesk’s algorithm heavily depends on the quality and detail of the dictionary definitions, and it may not work well if glosses are short or vague.

---

## 3. **Supervised Approaches**:
Supervised methods for WSD rely on labeled datasets where each word is manually tagged with the correct sense. These methods learn to disambiguate words based on training data and predict the correct sense for new instances.

#### a) **Naïve Bayes Classifier**:
- Naïve Bayes is a probabilistic classifier based on **Bayes' theorem**. It assumes that the features (context words) are independent of each other.
  
  **How it works**:
  - For each possible sense of the ambiguous word, the classifier computes the probability that the given context fits that sense using previously learned probabilities from training data.
  - The sense with the highest probability is selected.

  **Example**: Given a word like "bass" in a sentence, Naïve Bayes would calculate the probability of "bass" meaning "fish" or "musical instrument" based on the nearby words (e.g., "lake" vs. "guitar").

#### b) **Decision List Algorithm**:
- A **Decision List** algorithm learns a set of **if-then rules** from training data. These rules rank different features (like surrounding words) by their ability to disambiguate a word.

  **How it works**:
  - During training, the algorithm creates a ranked list of features (e.g., specific words or part-of-speech tags in the context).
  - When testing, the highest-ranked rule that applies is used to assign the word’s sense.

  **Example**: The rule "If 'fish' appears near 'bass', then choose the sense 'fish'" would take precedence over other possible senses of "bass."

---

## 4. **Semi-supervised Approach (Yarowsky's Algorithm)**:
Semi-supervised methods use both labeled and unlabeled data. **Yarowsky's algorithm** is a classic semi-supervised approach to WSD.

#### **Yarowsky's Algorithm**:
- It relies on two key principles:
  1. **One Sense Per Collocation**: A word tends to have a consistent meaning in similar contexts.
  2. **One Sense Per Discourse**: A word usually keeps the same sense throughout a document.

  **How it works**:
  - **Initial Labeled Data**: Yarowsky starts with a small set of labeled examples (where the correct senses are already known).
  - **Bootstrapping**: It uses these labeled examples to classify unlabeled examples based on their similarity to the labeled ones.
  - As more data is labeled, the system iteratively improves its model without needing much human intervention.

  **Example**: If the algorithm sees "bass" near "lake" labeled as "fish," it will begin labeling similar contexts as "fish" without needing more manual labels.

---

## 5. **Unsupervised Approach (HyperLex)**:
Unsupervised methods do not require labeled training data. They use clustering or similarity measures to infer word senses from the data itself.

#### **HyperLex Algorithm**:
- **HyperLex** is an unsupervised WSD approach that uses **distributional similarity** between words. It clusters word occurrences based on their contexts and then assigns word senses based on the clusters.
  
  **How it works**:
  - Words that appear in similar contexts are assumed to have similar meanings. HyperLex creates clusters of word senses by analyzing the **distributional properties** of words in large corpora.
  - It uses **vector-space models** to represent words and their contexts and applies clustering algorithms to group different usages into distinct senses.

  **Example**: HyperLex might analyze the occurrences of "bass" and cluster it into "fish-related" and "music-related" groups based on context words like "lake" and "guitar."

  **Limitation**:
  - Unsupervised methods can struggle to identify highly nuanced word senses because they rely purely on statistical patterns without external knowledge.

---

### Summary of Approaches:

| **Approach**            | **Type**            | **Algorithm**             | **Key Features**                               |
|-------------------------|---------------------|---------------------------|------------------------------------------------|
| **Knowledge-based**      | Dictionary-driven   | **Lesk's Algorithm**       | Uses gloss overlap to select word senses.      |
| **Supervised**           | Labeled Data        | **Naïve Bayes, Decision List** | Uses labeled training data, probabilistic models, and rule-based approaches. |
| **Semi-supervised**      | Labeled + Unlabeled | **Yarowsky's Algorithm**   | Bootstraps from a small labeled set using context consistency. |
| **Unsupervised**         | No Labeled Data     | **HyperLex**               | Clusters word usages based on context distribution. |

---

### Conclusion:
Word Sense Disambiguation is crucial for many NLP tasks like machine translation, information retrieval, and text understanding. Different approaches (knowledge-based, supervised, semi-supervised, and unsupervised) use varying strategies to resolve word meaning ambiguity. Each method has its own strengths and limitations, making them suitable for different types of tasks and data availability.

---
## **Dictionary-Based Approach for Word Sense Disambiguation (WSD)**:

A **dictionary-based approach** to Word Sense Disambiguation (WSD) leverages predefined lexical resources (like dictionaries, thesauruses, or semantic networks) to resolve the ambiguity of word meanings. It identifies the correct sense of a word based on **word definitions (glosses)** and the **context** in which the word is used.

Unlike supervised methods, dictionary-based approaches do not require large amounts of labeled data. Instead, they rely on external lexical resources such as WordNet or other dictionaries to identify word meanings.

### Key Concepts:

1. **Dictionary/Thesaurus as Knowledge Source**:
   - **Dictionary**: Provides word meanings (glosses), synonyms, antonyms, and usage examples.
   - **Semantic Network**: Resources like **WordNet** offer a more structured representation of words, linking them based on semantic relationships (synonymy, hyponymy, etc.).

2. **Gloss**: The **definition** or **explanation** of a word found in a dictionary. In dictionary-based approaches, the gloss is compared with the words in the sentence to determine which sense of the word fits best.

---

### Types of Dictionary-Based Approaches:

#### 1. **Lesk’s Algorithm**:
The **Lesk algorithm** is one of the most famous dictionary-based methods for WSD. It disambiguates words by comparing the dictionary definitions (glosses) of each potential sense of a word with the surrounding words in the context.

##### **How Lesk’s Algorithm Works**:
- **Input**: An ambiguous word and its surrounding context.
- **Step 1**: For each sense of the word, retrieve the corresponding gloss from a dictionary (e.g., WordNet).
- **Step 2**: Compare the glosses of each sense with the words in the sentence.
- **Step 3**: Count the **overlapping words** (common words) between the gloss and the context.
- **Step 4**: The sense with the highest overlap is selected as the correct one.

##### **Example**:
- Sentence: "I went to the **bank** to fish."
- Senses of **bank** (from a dictionary):
  1. **Financial institution**: "An establishment that provides financial services."
  2. **Riverbank**: "The land alongside a river."

  - Context words: "I", "went", "fish".
  - Overlap check:
    - Financial institution gloss: No overlap.
    - Riverbank gloss: Overlap with the word "fish" (associated with rivers).

  In this case, the **riverbank** sense would be selected due to the overlap with "fish."
 

#### 4. **Graph-Based Approach (WordNet)**:
Using **WordNet** or similar lexical resources, dictionary-based WSD methods can create a **graph of word senses** and their relationships (e.g., synonymy, hyponymy). The graph is then analyzed to find the best sense based on **connectedness** to other senses or words in the context.

##### **How it Works**:
- **WordNet** provides a network of related words and senses.
- The **target word** is mapped to its possible senses in the WordNet graph.
- Context words are also mapped to their senses in WordNet.
- The algorithm selects the sense of the target word that is most closely related to the senses of the surrounding words in the context.

##### **Example**:
- Sentence: "The **apple** fell from the tree."
  - WordNet senses:
    - Apple (fruit).
    - Apple (company).
  
  By analyzing the **relationship** between "tree" and "apple" in the WordNet graph, the algorithm identifies "apple" as **fruit**, as it is closely related to "tree" (through a **hypernymy** relation: "tree" → "plant" → "fruit").

---

### Advantages of Dictionary-Based Approaches:
- **No Training Data Required**: These methods do not require labeled corpora for training, making them highly scalable.
- **Utilization of External Knowledge**: Leverage rich linguistic resources like dictionaries, WordNet, and other semantic networks.
- **Simple and Fast**: Easy to implement, and works well with small-scale or resource-limited environments.

### Disadvantages of Dictionary-Based Approaches:
- **Dependence on Gloss Quality**: The accuracy of the method depends heavily on the quality and comprehensiveness of the glosses in the dictionary.
- **Gloss Overlap Limitations**: Words with similar meanings but no exact overlap in the glosses may be poorly disambiguated.
- **Scalability Issues**: In large corpora with complex sentence structures, the method may struggle to maintain accuracy.
- **Ambiguity in Glosses**: Some glosses can be too vague, and different dictionaries may define the same sense in different ways.

### Example Applications:
- **Machine Translation**: WSD ensures that the correct word sense is translated into the target language.
- **Information Retrieval**: Enhances search engines by correctly interpreting ambiguous words in search queries (e.g., "bank" financial institution vs. "bank" riverbank).
- **Text Summarization**: Ensures that ambiguous words are correctly interpreted when summarizing text.

### Conclusion:
**Dictionary-based approaches** for WSD, such as **Lesk’s Algorithm** and its variations, are effective methods that use **pre-existing lexical knowledge** to resolve word ambiguities. These methods are easy to implement and do not require large amounts of labeled data, making them ideal for certain NLP tasks where annotated datasets are unavailable. However, their performance depends on the richness of the dictionary or lexical resource used and may struggle with complex language scenarios.


# module 5

## Discourse in NLP

Discourse in NLP is nothing but coherent groups of sentences. When we are dealing with Natural Language Processing, the provided language consists of structured, collective, and consistent groups of sentences, which are termed discourse in NLP.

The relationship between words makes the training of the NLP model quite easy and more predictable than the actual results.

### usage:

Discourse Analysis is extracting the meaning out of the corpus or text.
Discourse Analysis is very important in Natural language Processing and helps train the NLP model better.

![](https://i.imgur.com/LBNRADJ.png)


![](https://i.imgur.com/DWx0o1B.png)


### **Reference Resolution**:

- Identifying what or who a word (like a pronoun) refers to in the text.
- **Example**: "John went to the store. **He** bought apples." ("He" refers to John).
### **Reference Phenomena**:

- **Anaphora**: Refers back to an earlier entity (e.g., "he", "she").
- **Cataphora**: Refers to something mentioned later in the text.
### **Syntactic & Semantic Constraints on Coherence**:

- **Syntactic Constraints**: Structure of sentences must be clear and consistent for proper reference (e.g., "He" should refer to an understandable noun).
- **Semantic Constraints**: Words must be **meaningfully connected** across sentences.
### **Anaphora Resolution**:

- The task of identifying the correct antecedent (who/what a pronoun refers to).
### **Algorithms for Anaphora Resolution**:

- **Hobbs’ Algorithm**: Uses syntactic structure (parse trees) to resolve pronouns.
- **Centering Algorithm**: Focuses on coherence between sentences by tracking discourse entities.

## Coreference 

- Coreference refers to the linguistic phenomenon where two or more expressions in a text refer to the same entity.

- The primary goal of coreference resolution is to establish the links between these expressions, allowing for a coherent understanding of the text.

![](https://i.imgur.com/NGSzkoJ.png)

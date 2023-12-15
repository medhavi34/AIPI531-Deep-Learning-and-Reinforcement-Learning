
# LLM-Based Item Recommendation Project


## Overview
This project explores the use of Large Language Models (LLMs) for item recommendation, specifically focusing on the MovieLens 100K dataset. The project aims to:
1. Utilize prompt engineering to teach LLMs for item recommendation.
2. Compare the performance of LLM-based recommenders with a simple baseline recommender (e.g., most popular items).

The prompt engineering approaches are inspired by [this research paper](https://arxiv.org/pdf/2304.03153.pdf), with custom improvements for enhanced performance.

## Dataset
The primary dataset used is the MovieLens 100K dataset. Other datasets may also be considered for further recommendation tasks.

## Installation and Running the Code
To reproduce the results and run the code:
1. **Clone the Repository**: Clone this GitHub repository to your local machine.
2. **Install Dependencies**: Ensure that all required libraries are installed. (Include a `requirements.txt` file or specify the libraries in the README).
3. **Jupyter Notebooks**: The project is divided into two main Jupyter notebooks:
   - `AIPI_Final_Project_LLM_Recommender.ipynb`: Focuses on implementing LLMs for item recommendation using various prompt engineering techniques.
   - `CollaborativeFiltering.ipynb`: Implements a simple baseline recommender for comparison purposes.
4. **Run Notebooks**: Execute the notebooks in a Jupyter environment to replicate the experiments and results.

## Experimentation and Findings
Based on the summary and findings you've provided, here's an elaborated explanation for the "Experimentation and Findings" section of your README.md:

---

## Experimentation and Findings

### Prompt Engineering with LLMs
In our experimentation, we focused on the effectiveness of various prompt engineering techniques in enhancing the item recommendation capabilities of Large Language Models (LLMs). Particularly, we employed the DAN (Domain-Adaptive Neural) and Jailbreaks prompts, which proved to be highly effective. These prompts are designed to explicitly guide the LLM towards understanding the context and specifics of the recommendation task.

The key to our success was the clarity and precision of our prompts. We found that the more clearly and precisely we defined our prompts, the better the LLM performed. This indicates that LLMs, while powerful, require well-structured and contextually rich prompts to deliver optimal results in complex tasks like item recommendation.

### Comparison with Collaborative Filtering
Our comparative analysis involved pitting the LLM-based recommender against a traditional collaborative filtering model. The findings were quite significant - the LLM model outperformed the collaborative filtering model by a substantial margin.

Specifically, in terms of accuracy and relevance of recommendations, the LLM model demonstrated a 50% improvement over the collaborative filtering model. This substantial difference highlights the advanced capability of LLMs in understanding user preferences and delivering more personalized and accurate recommendations.

### Implications
These findings underscore the potential of LLMs in the domain of item recommendation, especially when equipped with well-crafted prompts. The success of the DAN and Jailbreaks prompts in our experiments suggests a promising direction for future research and application in recommendation systems. Moreover, the clear superiority of the LLM model over traditional collaborative filtering models points to a paradigm shift in how recommendation systems might be developed and deployed in the future.

## Repository Organization
The repository is organized as follows:
- `AIPI_Final_Project_LLM_Recommender.ipynb`: Notebook for LLM-based recommendations.
- `CollaborativeFiltering.ipynb`: Notebook for baseline recommender implementation.
- `ml_100k.json`: MovieLens 100K dataset used for the recommendation tasks.
- `README.md`: Overview and instructions for the project.
- Additional resources (if any).

## Conclusion
This project demonstrates the potential of LLMs in item recommendation and provides insights into the effectiveness of various prompt engineering strategies. The comparison with a baseline recommender highlights the advanced capabilities of LLMs in understanding and catering to user preferences.

---

## Work Distribution

This project was a collaborative effort between Thwisha Nahender and Medhavi Darshan, with each contributing to different aspects of the work to ensure the success and effectiveness of the item recommendation system.

### Thwisha Nahender
Thwisha focused on implementing and fine-tuning the collaborative filtering model. This involved working with the MovieLens 100K dataset, selecting appropriate algorithms for collaborative filtering, and optimizing the model to ensure accurate and relevant item recommendations. Thwisha's work was crucial in establishing a baseline for comparing the performance of the LLM-based recommender.

### Medhavi Darshan
Medhavi was responsible for the development and implementation of the LLM model. This task required in-depth knowledge of Large Language Models, especially in crafting effective prompts to guide the model in making item recommendations. Medhavi's expertise was instrumental in leveraging the LLM's capabilities to surpass traditional recommendation methods.

### Joint Efforts
Both Thwisha and Medhavi collaborated extensively on the aspect of prompt engineering. This joint effort was key to enhancing the LLM's performance, as they experimented with various prompt strategies such as DAN and Jailbreaks prompts. Additionally, they worked together on parsing the output from GPT into a format suitable for recommendation purposes, ensuring that the final output was both user-friendly and relevant to the task at hand.

### Conclusion
The synergy between Thwisha's expertise in collaborative filtering and Medhavi's skills in working with LLMs was a cornerstone of this project's success. Their collaborative work on prompt engineering further strengthened the project, leading to innovative approaches in item recommendation.


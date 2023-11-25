# AIPI531: HW3
## Author: Medhavi Darshan

Link to GitHub repo: https://github.com/medhavi34/AIPI531-Deep-Learning-and-Reinforcement-Learning

Objectives:

Train different session (contextual, sequential) based product recommendation recommenders for E-commerce use cases and compare the performances of the recommenders.

Include item and/or user features as side information for cold items/users.

Methodology:

We have adapted the source code to enable the inclusion of item properties/features. Thus, we compute cross-entropy logits when using only item numbers (original) and only item features/properties (addition). Following prof Ma's recommendation, we incorporate both cross-entropy logits by computing a weighted average of the two and introducing a new hyper-parameter lambda (lam) that acts as the weight. Lambda takes values from 0 to 1. lam=0 means that only the original item numbers are included. lam=1 on the contrary means that only the new item features are included. Values in between are a weighted average of the two.

Please, see SNQN_Features.py and SA2C_Features for the modified version of the original code within SA2C. 

Please, see Colab notebook for implementation and output: 
https://colab.research.google.com/drive/1SjzV3IAhzhFbY-Gacyd7JNnpQZk_eiuB?usp=sharing 


# AIPI 531 - Homework 1 Solutions

This repository contains the solutions for Homework 1 of the AIPI 531 course, focusing on reinforcement learning using Stable Baselines3 (SB3). The tasks include training an agent to play a game using the A2C algorithm and comparing various advantage estimation methods.

## Homework Question 2: A2C Agent for Donkey Kong

### Overview
In this task, an agent is trained to play the Donkey Kong game using the A2C algorithm implemented in SB3. The process involves setting up the necessary dependencies, training the agent, and implementing TensorBoard for training visualization.

### Key Features
- **Game Selection**: The chosen game for this task is Donkey Kong.
- **TensorBoard Integration**: For visualizing training curves.
- **Video Recording**: The final evaluation video is recorded to demonstrate the agent's performance.
- **Model Management**: Procedures for saving and loading the trained RL model are implemented.

### Usage
1. **Install Dependencies**: Instructions for setting up Stable Baselines3 and other necessary libraries.
2. **Training the Agent**: Step-by-step guide on how to train the agent on the Donkey Kong game.
3. **TensorBoard Setup**: Details on how to setup and view training progress using TensorBoard.
4. **Recording and Evaluation**: How to record the final performance of the agent and evaluate it.
5. **Model Saving/Loading**: Instructions on saving and loading the trained model.

## Homework Question 3: Comparison of Advantage Estimation Methods in A2C

### Overview
This task involves a comparative study of different advantage estimation methods within the A2C algorithm framework, specifically comparing the vanilla advantage, n-step advantage, Monte Carlo (MC) advantage, and Generalized Advantage Estimation (GAE).

### Key Observations
- **MC Advantage Performance**: The Monte Carlo Advantage method showed superior performance in terms of mean rewards, likely due to its effectiveness in capturing long-term dependencies within the environment.
- **Comparative Analysis**: A detailed comparison is provided between the mentioned advantage methods, highlighting their strengths and weaknesses in different scenarios.

### Usage
1. **Initial Setup**: Instructions for setting up the necessary dependencies and imports.
2. **Advantage Method Implementations**: Guide on how to implement and compare different advantage estimation methods in A2C.
3. **Results and Analysis**: Detailed analysis of the comparative performance of each method.

## Getting Started

Follow the instructions in each notebook (`AIPI_531_Homework_1_Q2.ipynb` and `AIPI_531_Homework_1_Q3.ipynb`) to replicate the experiments and understand the methodologies used.

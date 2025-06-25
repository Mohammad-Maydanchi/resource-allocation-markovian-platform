# Resource Allocation Markovian Platform
This project applies a Markov Decision Process (MDP) to optimize imperfect inspection in a genetic manufacturing system, where rework is not allowed. It provides a structured framework for decision-making in high-cost, low-volume manufacturing environments.

# Project Overview
The goal is to minimize total expected inspection and failure costs by dynamically allocating resources to inspection tasks, taking into account:

Imperfect inspection (false positives and false negatives)

State transitions driven by process stages

Cost trade-offs between inspection, passing, and failures

This model is particularly relevant to systems where each unit has high value and there is no opportunity for rework (e.g., biomanufacturing, aerospace, semiconductors).

# Methodology
Framework: Discrete-time finite-horizon MDP

States: Defined by inspection history and stage in the process

Actions: Allocate inspection or skip at each stage

Rewards: Based on inspection cost, process cost, and failure penalties

Solution Approach: Backward induction via dynamic programming


# Application
This platform is adaptable for:

Genetic manufacturing systems

High-value, low-rework environments

Scenarios requiring confidence-based inspection decisions

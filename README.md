# Enterprise

## Overview

This project implements an Enterprise Retrieval-Augmented Generation (RAG) Governance System that manages organizational policies safely.
The system retrieves the most relevant policy for a user query and includes governance mechanisms to protect the enterprise memory.
The pipeline ensures that policies are validated, filtered, updated safely, and monitored using audit logs.

---

## Features

R1 – Noise Injection Test  
Detects and rejects meaningless or random policy text that may corrupt the policy memory.

R2 – Policy Filtering  
Filters unsafe or malicious policies containing restricted words like hack, steal, illegal, or attack.

R3 – Update / Replace Strategy  
Allows safe updating or replacing of policies in the memory database.

R4 – Conflict Handling  
Detects contradictions between new policies and existing policies.

R5 – Memory Audit Log  
Records all important system actions such as policy updates, filtering, and conflict detection.

---
## How to Run

1. Open `enterprise.py` in Python or VS Code.

2. Install the required library:

pip install scikit-learn

3. Run the script:

python enterprise.py

---

## Technologies Used

Python

Scikit-learn

TF-IDF Vectorization

Cosine Similarity

Retrieval-Augmented Generation (RAG)

---
## Authors

Surya Praba

Kaviya Sree

---

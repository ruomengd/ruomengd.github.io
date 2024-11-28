---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
<!-- {% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %} -->



<span class='anchor' id='about-me'></span>

Hi, I am a Master's student specializing in Computer Science at Georgia Institute of Technology. Previously, I earned my bachelor’s degrees from Tianjin University. I am fortunate to collaborate with researchers of Georgia Tech, UIUC, Microsoft Research, Microsoft Research Asia, NEC Laboratories America, and Tianjin University. [[Resume]](http://ruomengd.github.io/files/Resume_RuomengDing.pdf)


My research interests focus on **Trustworthy AI**, **Foundation Models**, and **Reinforcement Learning (RL)**:

* **Reliability**: integrating external knowledge and tools to enhancing the reasoning and planning capabilities of foundation models; 
* **Robustness**: advancing RL/RLHF for improved generalization and trustworthiness under distribution shift; 
* **Applications** of RL and LLMs in specific domains including AIOps, AI4SE, *.etc*. 

<!-- For more information, please check out my Research Statement. -->

**<font color="red"> I am actively seeking PhD positions for Fall 2025. If you have or know of any opportunities that align with my interests, I would be grateful if you could contact me at <font color="blue">rmding@gatech.edu</font>. I am very interested in discussing any potential opportunities. Thank you!</font>**



# 🔥 News
- *Sep, 2024*: &nbsp;🎉🎉 Our paper, "Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs", has been accepted by NeurIPS 2024! [[paper]](https://arxiv.org/pdf/2406.10216) 
- *May, 2024*: &nbsp;🎉🎉 Our paper, "Everything of Thoughts: Defying the Law of Penrose Triangle for Thought Generation", has been accepted by ACL 2024 as a long paper finding! [[paper]](https://arxiv.org/pdf/2311.04254.pdf) [[code]](https://github.com/microsoft/Everything-of-Thoughts-XoT)
- *Apr, 2024*: &nbsp;🎉🎉 I am thrilled to announce that I will be joining Microsoft Redmond as a Research Intern this summer. I am excited for the journey ahead and can't wait to be in Seattle!


# 📝 Publications 

<!-- ------------------------------- -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2024</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Everything of thoughts: Defying the law of penrose triangle for thought generation](https://arxiv.org/pdf/2311.04254)

**Ruomeng Ding**, Chaoyun Zhang, Lu Wang, Yong Xu, Minghua Ma, Wei Zhang, Si Qin, Saravan Rajmohan, Qingwei Lin, Dongmei Zhang

[**[paper]**](https://arxiv.org/pdf/2311.04254) [**[code]**](https://github.com/microsoft/Everything-of-Thoughts-XoT) 
- Findings of the Association for Computational Linguistics (ACL), 2024.
- Incorporate external domain knowledge into thoughts using RL and Monte Carlo Tree Search (MCTS), enhancing LLMs' capabilities and enabling them to efficiently generalize to unseen problems.
</div>
</div>
<!-- ------------------------------- -->

<!-- ------------------------------- -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://arxiv.org/pdf/2311.04254)

Rui Yang, **Ruomeng Ding**, Yong Lin, Huan Zhang, Tong Zhang

[**[paper]**](https://arxiv.org/pdf/2406.10216) [**[code]**](https://github.com/YangRui2015/Generalizable-Reward-Model) 
- Neural Information Processing Systems (NeurIPS), 2024.
- Enhance the reward model's generalization ability against distribution shifts by regularizing the hidden states.
</div>
</div>
<!-- ------------------------------- -->

<!-- ------------------------------- -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ESEC/FSE 2023</div><img src='images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TraceDiag: Adaptive, Interpretable, and Efficient Root Cause Analysis on Large-Scale Microservice Systems](https://arxiv.org/pdf/2311.04254)

**Ruomeng Ding**, Chaoyun Zhang, Lu Wang, Yong Xu, Minghua Ma, Xiaomin Wu, Meng Zhang, Qingjun Chen, Xin Gao, Xuedong Gao, Hao Fan, Saravan Rajmohan, Qingwei Lin, Dongmei Zhang

[**[paper]**](https://arxiv.org/pdf/2311.04254) 
- Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE), 2023.
- A end-to-end RCA framework for large-scale microservice systems. It utilizes reinforcement learning to automatically eliminate redundant components, improving RCA efficiency.
</div>
</div>
<!-- ------------------------------- -->

- `KDD 2023` [Root cause analysis for microservice systems via hierarchical reinforcement learning from human feedback](https://dl.acm.org/doi/abs/10.1145/3580305.3599934), Lu Wang, Chaoyun Zhang, **Ruomeng Ding**, Yong Xu, Qihang Chen, Wentao Zou, Qingjun Chen, Meng Zhang, Xuedong Gao, Hao Fan, Saravan Rajmohan, Qingwei Lin, Dongmei Zhang [[paper]](https://dl.acm.org/doi/abs/10.1145/3580305.3599934) 
- `UDM-AAAI 2023` [Detecting Multi-Label Out-of-Distribution Nodes on Graphs](https://charliezhaoyinpeng.github.io/UDM-AAAI23/assets/papers/Ding/CameraReady/AAAI23_UDM_MLVC_CameraReady.pdf), **Ruomeng Ding**, Xujiang Zhao, Chen Zhao, Minglai Shao [[paper]](https://charliezhaoyinpeng.github.io/UDM-AAAI23/assets/papers/Ding/CameraReady/AAAI23_UDM_MLVC_CameraReady.pdf) 
- `VLDB 2023` [Imdiffusion: Imputed diffusion models for multivariate time series anomaly detection](https://dl.acm.org/doi/abs/10.1145/3580305.3599934), Yuhang Chen, Chaoyun Zhang, Minghua Ma, Yudong Liu, **Ruomeng Ding**, Bowen Li, Shilin He, Saravan Rajmohan, Qingwei Lin, Dongmei Zhang [[paper]](https://arxiv.org/pdf/2307.00754) [[code]](https://github.com/17000cyh/IMDiffusion) 
- `TCYB 2023` [Exploring temporal community structure via network embedding](https://ieeexplore.ieee.org/abstract/document/9768181), Tianpeng Li, Wenjun Wang, Pengfei Jiao, Yinghui Wang, **Ruomeng Ding**, Huaming Wu, Lin Pan, Di Jin [[paper]](https://ieeexplore.ieee.org/abstract/document/9768181) 



# 📖 Educations
- *2022.08 - 2025.05 (Estimated)*, **M.S. in Computer Science**, **Georgia Institute of Technology**
  - GPA: 4.0/4.0, Specialization: Machine Learning.
  - Both in Atlanta and Shenzhen Campus, pursuing a dual master’s degree at Tianjin University. Expected to graduate with separate M.S. degrees from both institutions in May 2025.
- *2018.08 - 2022.05*, **Bachelor in Computer Science and Technology**, **Tianjin University** 
  - GPA: 3.75/4.0, Rank: 11/169 (6.5%).
 

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

# 💻 Internships
- *2024.05 - 2024.08*, Microsoft Research, Redmond, WA.
- *2022.11 - 2023.08*, Microsoft Research Asia, Beijing, China.

# 🎖 Honors and Awards
- *2023* National Scholarship, TOP 1%, Tianjin University.
- *2022* Merit Scholarship, TOP 5%, Georgia Institute of Technology (Shenzhen Campus)
- *2020* People’s Scholarship, TOP 1%, Tianjin University
- *2019* Merit Scholarship, TOP 5%, Tianjin University

# 🛠️ Services
- *2024*, Reviewer, ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)
- *2023*, Reviewer, KDD Workshop on Uncertainty Reasoning and Quantification in Decision Making (UDM-KDD), 2023
- *2023*, Reviewer, Journal of Information Processing and Management

# 🔦 Miscellaneous

- Practiced synchronized swimming during my teens—our team earned 2nd place at the National Youth Competition. Now I swim just for fun. 🏊‍♀️
- Played the flute in orchestras throughout school and performed in benefit concerts. 🎶
- Took up piano in 2022—progress is slow, but it’s all about the journey. 🎹
- A big fan of novels and musicals, especially Les Misérables. 🎭
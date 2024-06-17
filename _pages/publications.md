---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
<!-- 
{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %} -->



## 2024:

### [ERegularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://arxiv.org/pdf/2406.10216) 

* Rui Yang, **Ruomeng Ding**, Yong Lin, Huan Zhang, Tong Zhang
* *arXiv*  [[paper]](https://arxiv.org/pdf/2406.10216)
* <font color="grey">Our study proposes a novel approach to enhance the reward model's generalization ability against distribution shifts by regularizing the hidden states. Specifically, we retain the base model's language model head and incorporate a suite of text-generation losses to preserve the hidden states' text generation capabilities, while concurrently learning a reward head behind the same hidden states.

### [Everything of thoughts: Defying the law of penrose triangle for thought generation](https://arxiv.org/pdf/2311.04254.pdf) 

* **Ruomeng Ding**, Chaoyun Zhang, Lu Wang, Yong Xu, Minghua Ma, Wei Zhang, Si Qin, Saravan Rajmohan, Qingwei Lin, Dongmei Zhang
* *Findings of the Association for Computational Linguistics* **(ACL)**, 2024 [[paper]](https://arxiv.org/pdf/2311.04254.pdf) [[code]](https://github.com/microsoft/Everything-of-Thoughts-XoT) 
* <font color="grey">Everything of Thoughts (XoT) incorporates external domain knowledge into thoughts using pretrained reinforcement learning and Monte Carlo Tree Search (MCTS), enhancing LLMs' capabilities and enabling them to efficiently generalize to unseen problems. XoT outperforms existing approaches in challenging multi-solution problem-solving tasks and showcases its proficiency in addressing complex problems across diverse domains.</font> 

## 2023:

### [TraceDiag: Adaptive, Interpretable, and Efficient Root Cause Analysis on Large-Scale Microservice Systems](https://arxiv.org/pdf/2310.18740.pdf) 

* **Ruomeng Ding**, Chaoyun Zhang, Lu Wang, Yong Xu, Minghua Ma, Xiaomin Wu, Meng Zhang, Qingjun Chen, Xin Gao, Xuedong Gao, Hao Fan, Saravan Rajmohan, Qingwei Lin, Dongmei Zhang 
* *Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering* **(ESEC/FSE)**, 2023 [[paper]](https://arxiv.org/pdf/2310.18740.pdf)
* <font color="grey">This paper introduces TraceDiag, an end-to-end RCA framework for large-scale microservice systems. It utilizes reinforcement learning to automatically eliminate redundant components, improving RCA efficiency. The framework is evaluated on real data traces from the Microsoft Exchange system and shows superior performance compared to existing approaches, resulting in improved system reliability and reduced human effort for RCA.</font> 

### [Root cause analysis for microservice systems via hierarchical reinforcement learning from human feedback](https://dl.acm.org/doi/abs/10.1145/3580305.3599934) 

* Lu Wang, Chaoyun Zhang, **Ruomeng Ding**, Yong Xu, Qihang Chen, Wentao Zou, Qingjun Chen, Meng Zhang, Xuedong Gao, Hao Fan, Saravan Rajmohan, Qingwei Lin, Dongmei Zhang 
* *Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining* **(KDD)**, 2023 [[paper]](https://dl.acm.org/doi/abs/10.1145/3580305.3599934)
* <font color="grey">This paper proposes a framework that utilizes Hierarchical Reinforcement Learning from Human Feedback (HRLHF) to address the challenges of identifying root causes of anomalies in microservice systems. Evaluations demonstrate superior performance compared to state-of-the-art methods, and the framework has been integrated into Microsoft M365 Exchange service.</font> 

### [Imdiffusion: Imputed diffusion models for multivariate time series anomaly detection](https://arxiv.org/pdf/2307.00754.pdf)

* Yuhang Chen, Chaoyun Zhang, Minghua Ma, Yudong Liu, **Ruomeng Ding**, Bowen Li, Shilin He, Saravan Rajmohan, Qingwei Lin, Dongmei Zhang
* *Proceedings of the VLDB Endowment* **(VLDB)**, 2023 [[paper]](https://arxiv.org/pdf/2307.00754.pdf) [[code]](https://github.com/17000cyh/IMDiffusion)
* <font color="grey">The ImDiffusion framework combines imputation and diffusion models to achieve accurate and robust anomaly detection in multivariate time series data. It outperforms existing approaches by leveraging neighboring values and capturing complex dependencies. ImDiffusion has been integrated into Microsoft's production system.</font> 


### [Detecting Multi-Label Out-of-Distribution Nodes on Graphs](https://charliezhaoyinpeng.github.io/UDM-AAAI23/ap/) 

* **Ruomeng Ding**, Xujiang Zhao, Chen Zhao, Minglai Shao 
* *AAAI Workshop on Uncertainty Reasoning and Quantification in Decision Making (UDM)* **(UDM-AAAI)**, 2023 
* <font color="grey">This paper proposes an Evidence-Based Out-of-Distribution Detection method for multi-label graphs using Evidential Deep Learning (EDL) and Multi-Label Evidential Graph Neural Networks (ML-EGNNs) with Beta Loss. The model is effective and efficient in detecting Out-of-Distribution (OOD) nodes in multi-label settings.</font> 


## 2022:

### [Exploring temporal community structure via network embedding](https://ieeexplore.ieee.org/abstract/document/9768181) 

* Tianpeng Li, Wenjun Wang, Pengfei Jiao, Yinghui Wang, **Ruomeng Ding**, Huaming Wu, Lin Pan, Di Jin
* *IEEE Transactions on Cybernetics*, 2022  [[paper]](https://ieeexplore.ieee.org/abstract/document/9768181)
* <font color="grey">This paper presents an innovative unsupervised dynamic community detection model using network embedding. By incorporating the Gaussian mixture model (GMM) and utilizing a variant of the gated recurrent unit (GRU), the model successfully identifies temporal communities and models dynamic networks. Experimental results demonstrate that the proposed model enhances the accuracy of dynamic community detection.</font> 

## 2021:

### [Action unit detection with joint adaptive attention and graph relation](https://arxiv.org/pdf/2107.04389.pdf) 

* Chenggong Zhang, Juan Song, Qingyang Zhang, Weilong Dong, **Ruomeng Ding**, Zhilei Liu
* *arXiv preprint arXiv:2107.04389*, 2021 [[paper]](https://arxiv.org/pdf/2107.04389.pdf)
* <font color="grey">This paper proposes an approach for facial action unit (AU) detection in the ABAW 2021 competition. The method uses a pre-trained JAA model to extract features and applies graph convolution to consider the correlation between AUs. The model achieves an accuracy of 0.674 on the Aff-Wild2 database.</font> 

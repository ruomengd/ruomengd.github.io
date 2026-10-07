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

<br>

<span class='anchor' id='about-me'></span>

Hi, I am a second-year Ph.D. student at <img class="intro-logo" style="width: 19px; padding-bottom: 5px;" src="/images/unc.jpeg"> UNC-Chapel Hill advised by [Prof. Zhun Deng](https://www.zhundeng.org/home). Currently, I study how LLM agents learn and improve through interaction, with a focus on eliciting human preferences and developing reliable evaluation methods. I have been particularly interested in AI4AI—using AI systems to automate data engineering, evaluation, and model improvement. Please feel free to reach out if you are interested in collaborating.

Before joining UNC, I completed my Master’s degree in Computer Science at <img class="intro-logo" style="width: 19px; padding-bottom: 5px;" src="/images/gatech.svg"> Georgia Tech. I am also fortunate to collaborate with researchers at <img class="intro-logo" style="width: 19px; padding-bottom: 5px;" src="/images/uiuc.png"> UIUC, <img class="intro-logo" style="width: 19px; padding-bottom: 5px;" src="/images/Microsoft.png"> Microsoft, and <img class="intro-logo" style="width: 19px; padding-bottom: 3px;" src="/images/nec.png"> NEC Laboratories America.

Research interests: LLM Agents & Reasoning · Preference Learning & Elicitation · Reliable LLM Evaluation · AI4AI

[[Resume]](/files/Resume_RuomengDing.pdf) [[Google Scholar]](https://scholar.google.com/citations?user=aPlu2rYAAAAJ&hl=en)
 

 <font color="red"> I am actively seeking 2027 summer internships. If you have or know of any opportunities that align with my interests, please contact me at <font color="blue">ruomeng@cs.unc.edu</font>.</font>

# 🔥 News
- **[10/2026]** 🚀 New arXiv preprint: *Speculative Evaluation of Stochastic LLMs*. [[paper]](https://arxiv.org/pdf/2609.28560) [[code]](https://github.com/ShenQianli/SpecEval)
- **[09/2026]** 🎉 Three papers accepted at NeurIPS 2026 workshops: [WAPA](https://openreview.net/forum?id=GiRtUYmJvF) @ [FLLMPT](https://www.fllmpt-work.shop/), [ADE](https://openreview.net/forum?id=bTVUsrguDi) @ [AutoMLR](https://automlr.com/), and [SpecEval](https://openreview.net/forum?id=IvzVKsdcH9) @ [TAE](https://tai-eval.github.io/). ArXiv versions will be released soon.
- **[09/2026]** I will serve as a reviewer for ICLR 2027.
- **[07/2026]** 🎉 One paper accepted at COLM 2026.
- **[07/2026]** I will serve as a reviewer for AAAI 2027.
- **[05/2026]** 🎉 One paper accepted at ICML 2026. See you in Seoul! 🇰🇷
- **[05/2026]** I will serve as a reviewer for NeurIPS 2026.
- **[04/2026]** I will join <img class="intro-logo" style="width: 19px; vertical-align: middle; margin-right: 4px;" src="/images/tongyi.jpeg">Alibaba Tongyi Lab as a research intern in Summer 2026.
- **[03/2026]** 🎉 Two papers accepted at ICLR 2026 Workshops [ICBINB](https://sites.google.com/view/icbinb-2026/home) & [AIMS](https://alimama-tech.github.io/aims-2026/#). See you in Rio! 🇧🇷
- **[02/2026]** 🚀 New arXiv preprint: *Rubrics as an Attack Surface: Stealthy Preference Drift in LLM Judges*. [[paper]](https://arxiv.org/pdf/2602.13576) [[code]](https://github.com/ZDCSlab/Rubrics-as-an-Attack-Surface)
- **[02/2026]** 🚀 New arXiv preprint: *Whom to Query for What: Adaptive Group Elicitation via Multi-Turn LLM Interactions*. [[paper]](https://arxiv.org/pdf/2602.14279) [[code]](https://github.com/ZDCSlab/Group-Adaptive-Elicitation)
<!-- - **[01/2026]** I will serve as a reviewer for AIMS @ ICLR 2026. -->
- **[01/2026]** I will serve as a reviewer for ICML 2026.
- **[01/2026]** I will serve as a reviewer for KDD 2026.
- **[11/2025]** 🎉 One paper accepted at AAAI 2026 (Oral).

<!-- - *Dec, 2024*: &nbsp;🎉🎉 One paper is accepted by SDM 2025. 
- *Sep, 2024*: &nbsp;🎉🎉 Our paper, "Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs", has been accepted by NeurIPS 2024. [[paper]](https://arxiv.org/pdf/2406.10216) [[code]](https://github.com/YangRui2015/Generalizable-Reward-Model) 
- *May, 2024*: &nbsp;🎉🎉 Our paper, "Everything of Thoughts: Defying the Law of Penrose Triangle for Thought Generation", has been accepted by ACL 2024 as a long paper finding. [[paper]](https://arxiv.org/pdf/2311.04254.pdf) [[code]](https://github.com/microsoft/Everything-of-Thoughts-XoT)
- *Apr, 2024*: &nbsp;🎉🎉 I am thrilled to announce that I will be joining Microsoft Redmond as a Research Intern this summer. I am excited for the journey ahead and can't wait to be in Seattle! -->



# 📝 Selected Publications

\* Equal contribution.

<details class="publication-category" markdown="1" open>
<summary>LLM Agents &amp; Reasoning</summary>

- <span class="pub-tag pub-tag--workshop">AutoMLR Workshop @NeurIPS 2026</span> [Agentic Data Engineering for LLMs: System Design and a Controlled Empirical Study](https://openreview.net/forum?id=bTVUsrguDi), **Ruomeng Ding**, Qianli Shen, ZhaoYang Han, Meixin Chen, Daoyuan Chen, Yaliang Li [[paper]](https://openreview.net/forum?id=bTVUsrguDi)

- <span class="pub-tag pub-tag--conference">AAAI 2026</span> <span class="pub-tag pub-tag--highlight">Oral</span> [SkillGen: Learning Domain Skills for In-Context Sequential Decision Making](https://arxiv.org/pdf/2511.14670), **Ruomeng Ding**, Wei Cheng, Minglai Shao, Chen Zhao [[paper]](https://arxiv.org/pdf/2511.14670) [[code]](https://github.com/ruomengd/SkillGen)

- <span class="pub-tag pub-tag--conference">ACL 2024</span> [Everything of thoughts: Defying the law of penrose triangle for thought generation](https://arxiv.org/pdf/2311.04254), **Ruomeng Ding**, Chaoyun Zhang, Lu Wang, Yong Xu, Minghua Ma, Wei Zhang, Si Qin, Saravan Rajmohan, Qingwei Lin, Dongmei Zhang [[paper]](https://arxiv.org/pdf/2311.04254) [[code]](https://github.com/microsoft/Everything-of-Thoughts-XoT)

</details>

<details class="publication-category" markdown="1" open>
<summary>Preference Learning &amp; Elicitation</summary>

- <span class="pub-tag pub-tag--workshop">FLLMPT Workshop @NeurIPS 2026</span> [Who Should We Listen to More? Welfare-Aware Preference Acquisition for Pluralistic Alignment](https://openreview.net/forum?id=GiRtUYmJvF), **Ruomeng Ding**, Tianwei Gao, Lianrui Geng, and Zhun Deng [[paper]](https://openreview.net/forum?id=GiRtUYmJvF)

- <span class="pub-tag pub-tag--conference">ICML 2026</span> [Whom to Query for What: Adaptive Group Elicitation via Multi-Turn LLM Interactions](https://arxiv.org/pdf/2602.14279), **Ruomeng Ding**\*, Tianwei Gao\*, Thomas P. Zollo, Eitan Bachmat, Richard Zemel, and Zhun Deng [[paper]](https://arxiv.org/pdf/2602.14279) [[code]](https://github.com/ZDCSlab/Group-Adaptive-Elicitation)

</details>

<details class="publication-category" markdown="1" open>
<summary>Reliable LLM Evaluation</summary>

- <span class="pub-tag pub-tag--workshop">TAE Workshop @NeurIPS 2026</span> <span class="pub-tag pub-tag--preprint">Preprint</span> [Speculative Evaluation of Stochastic LLMs](https://arxiv.org/pdf/2609.28560), Qianli Shen, Xiang Li, **Ruomeng Ding**, Yanxi Chen, Daoyuan Chen, Yaliang Li [[paper]](https://arxiv.org/pdf/2609.28560) [[code]](https://github.com/ShenQianli/SpecEval)

- <span class="pub-tag pub-tag--conference">COLM 2026</span> [Rubrics as an Attack Surface: Stealthy Preference Drift in LLM Judges](https://arxiv.org/pdf/2602.13576), **Ruomeng Ding**\*, Yifei Pang\*, He Sun, Yizhong Wang, Zhiwei Steven Wu, and Zhun Deng [[paper]](https://arxiv.org/pdf/2602.13576) [[code]](https://github.com/ZDCSlab/Rubrics-as-an-Attack-Surface)

- <span class="pub-tag pub-tag--conference">NeurIPS 2024</span> [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://arxiv.org/pdf/2406.10216), Rui Yang, **Ruomeng Ding**, Yong Lin, Huan Zhang, Tong Zhang [[paper]](https://arxiv.org/pdf/2406.10216) [[code]](https://github.com/YangRui2015/Generalizable-Reward-Model)

</details>

<details class="publication-category" markdown="1" open>
<summary>Reliable Machine Learning &amp; Applications</summary>

- <span class="pub-tag pub-tag--conference">SDM 2025</span> [Evidence-Based Out-of-Distribution Detection on Multi-Label Graphs](), **Ruomeng Ding**, Xujiang Zhao, Chen Zhao, Minglai Shao, Zhengzhang Chen, Haifeng Chen

- <span class="pub-tag pub-tag--conference">ESEC/FSE 2023</span> [TraceDiag: Adaptive, Interpretable, and Efficient Root Cause Analysis on Large-Scale Microservice Systems](https://arxiv.org/pdf/2310.18740), **Ruomeng Ding**, Chaoyun Zhang, Lu Wang, Yong Xu, Minghua Ma, Xiaomin Wu, Meng Zhang, Qingjun Chen, Xin Gao, Xuedong Gao, Hao Fan, Saravan Rajmohan, Qingwei Lin, Dongmei Zhang [[paper]](https://arxiv.org/pdf/2310.18740)

- <span class="pub-tag pub-tag--conference">KDD 2023</span> [Root cause analysis for microservice systems via hierarchical reinforcement learning from human feedback](https://dl.acm.org/doi/abs/10.1145/3580305.3599934), Lu Wang, Chaoyun Zhang, **Ruomeng Ding**, Yong Xu, Qihang Chen, Wentao Zou, Qingjun Chen, Meng Zhang, Xuedong Gao, Hao Fan, Saravan Rajmohan, Qingwei Lin, Dongmei Zhang [[paper]](https://dl.acm.org/doi/abs/10.1145/3580305.3599934)

- <span class="pub-tag pub-tag--conference">VLDB 2023</span> [ImDiffusion: Imputed diffusion models for multivariate time series anomaly detection](https://dl.acm.org/doi/abs/10.1145/3580305.3599934), Yuhang Chen, Chaoyun Zhang, Minghua Ma, Yudong Liu, **Ruomeng Ding**, Bowen Li, Shilin He, Saravan Rajmohan, Qingwei Lin, Dongmei Zhang [[paper]](https://arxiv.org/pdf/2307.00754) [[code]](https://github.com/17000cyh/IMDiffusion)

</details>

<!-- - <span class="highlighter-rouge">TCYB 2023</span>  [Exploring temporal community structure via network embedding](https://ieeexplore.ieee.org/abstract/document/9768181), Tianpeng Li, Wenjun Wang, Pengfei Jiao, Yinghui Wang, **Ruomeng Ding**, Huaming Wu, Lin Pan, Di Jin [[paper]](https://ieeexplore.ieee.org/abstract/document/9768181)  -->


<!-- 
# 📖 Educations
- *2022.08 - 2025.05 (Estimated)*, **M.S. in Computer Science**, **Georgia Institute of Technology**
  - GPA: 4.0/4.0, Both in Atlanta and Shenzhen Campus. 
  - pursuing a dual master’s degree at Tianjin University. Expected to graduate with separate M.S. degrees from both institutions in May 2025. 
- *2018.08 - 2022.05*, **Bachelor in Computer Science and Technology**, **Tianjin University** 
  - GPA: 3.75/4.0, Rank: 11/169 (6.5%).
 -->

# 💻 Internships
- *2026.05 - 2026.08*, Alibaba Token Foundry (Tongyi Lab), Hangzhou, China.
  <!-- - Advised by [Dr. Qianli Shen](https://shenqianli.github.io/) and [Daoyuan Chen](https://yxdyc.github.io/). -->
- *2024.05 - 2024.08*, Microsoft Research, Redmond, WA.
  <!-- - Advised by [Dr. Minghua Ma](https://www.microsoft.com/en-us/research/people/minghuama/) and [Dr. Ze Li](https://scholar.google.com/citations?user=hhGVDJwAAAAJ&hl=en). -->
- *2022.11 - 2023.08*, Microsoft Research Asia, Beijing, China.
  <!-- - Advised by [Dr. Lu Wang](https://scholar.google.com/citations?user=hqlU92YAAAAJ&hl=en) and [Dr. Chaoyun Zhang](https://www.microsoft.com/en-us/research/people/chaoyunzhang/). -->

# 🎖 Honors and Fellowships
- Doctoral Merit Fellowship, University of North Carolina at Chapel Hill, 2025–2026
- Merit Scholarship, Georgia Institute of Technology, 2022-2023

<!-- # 🛠️ Services
- Reviewer, KDD 2025, KDD 2024
- Reviewer, UDM-KDD 2023
   -->
<!-- - *2023*, Reviewer, Journal of Information Processing and Management -->

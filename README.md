# 📊 SaaS 数据分析项目案例：产品使用、销售漏斗与客户反馈洞察

本项目模拟一个 B2B SaaS 产品的真实运营场景，从数据生成到可视化分析，系统性地展示产品使用行为、销售转化路径、市场趋势与客户反馈，适合用作数据分析作品集展示或业务汇报模版。

---

## 📁 项目结构
product-insight-case/
│
├── product_usage.py # 数据生成 + 分析脚本
├── charts/ # 图表文件夹（截图保存为 .png）
│ ├── top5_feature_usage.png
│ ├── platform_usage.png
│ ├── sales_funnel_stage_distribution.png
│ ├── win_rate_by_source.png
│ ├── campaign_conversions.png
│ ├── campaign_cpl.png
│ ├── feedback_type_distribution.png
│ └── ...（其余图表）
└── README.md # 项目说明文档（即本文件）

---

## 🧠 项目背景与目标

我们设计了一个虚拟的 SaaS 企业场景，生成并分析以下类型的数据：

- 用户产品使用日志（功能点击、平台偏好、使用时长）
- 营销线索转化数据（典型销售漏斗模型）
- 客户反馈文本数据（模拟打分、情绪分析）
- 市场趋势指标（行业增长、竞争活跃度、均价波动）
- 多渠道营销活动成效数据（点击、转化、成本）

---

## 🔍 分析模块

### 1️⃣ 产品功能使用分析

- 最受欢迎的产品功能
- Web/iOS/Android 各平台的使用偏好
- 用户平均使用时长趋势

📊 图示：

![Top Features](charts/top5_feature_usage.png)  
![Platform Usage](charts/platform_usage.png)

---

### 2️⃣ 销售转化漏斗分析

- 销售线索在各阶段的数量分布
- 每个阶段的转化率计算
- 不同渠道带来的赢单率对比

📊 图示：

![Funnel Stage](charts/sales_funnel_stage_distribution.png)  
![Win Rate by Source](charts/win_rate_by_source.png)

---

### 3️⃣ 营销活动效果分析

- 按渠道/类型统计转化总量
- 平均转化成本（CPL）对比
- 点击率与成本效率评估

📊 图示：

![Campaign Conversion](charts/campaign_conversions.png)  
![CPL Comparison](charts/campaign_cpl.png)

---

### 4️⃣ 客户反馈分析

- 反馈类型分布（NPS、Review、社媒评论等）
- 各类反馈的情感倾向与打分分布
- 高频关键词和负面情绪词云分析（可拓展）

📊 图示：

![Feedback Type](charts/feedback_type_distribution.png)

---

## ⚙️ 技术栈与工具

- 语言与框架：**Python**（Pandas, Numpy, Random, datetime）
- 数据可视化：**Matplotlib, Seaborn, WordCloud**
- NLP 处理（可选扩展）：**TextBlob, Jieba**
- 开发环境：Jupyter Notebook
- 版本管理：Git + GitHub

---

## 🌟 项目亮点

✅ 全流程演示数据模拟 → 清洗处理 → 多维度分析 → 图形展示  
✅ 商业常用主题：功能使用、销售漏斗、反馈分析、营销效果  
✅ 图表样式清晰，适合汇报或展示使用  
✅ 可拓展性强，可替换真实业务数据进行复用

---

## 🔗 项目地址

👉 GitHub 仓库：[glowye/product-insight-case](https://github.com/glowye/product-insight-case)

---


#  SaaS 数据分析项目案例：产品使用、销售漏斗与客户反馈洞察

🎯 本项目模拟一个 B2B SaaS 产品的真实运营场景，系统性展示如何通过数据分析支持 产品优化、销售策略调整和市场决策制定。从数据生成到可视化呈现，涵盖产品使用行为、销售转化路径、客户反馈和营销渠道表现等多个维度。

🎯 本项目旨在展示我独立完成从数据构建、清洗、分析到可视化呈现的能力，尤其是在构建富有洞察力的分析报告方面，帮助业务理解用户行为、优化漏斗表现、评估渠道效率并挖掘潜在市场机会。

## 🟣 项目背景与目标

🎯 项目背景：
我构建了一个虚拟的 SaaS 企业数据环境，模拟并分析以下典型业务数据：

- 用户产品使用日志（功能点击、平台偏好、使用时长）
- 营销线索转化数据（典型销售漏斗模型）
- 客户反馈文本数据（模拟打分、情绪分析）
- 市场趋势指标（行业增长、竞争活跃度、均价波动）
- 多渠道营销活动成效数据（点击、转化、成本）

🎯 项目目标：通过数据分析还原真实业务逻辑，挖掘用户行为与业务指标间的关联，助力产品和市场决策。

## 🟣 分析模块

### 1. 产品功能使用分析

1.1 分析内容：

- 最受欢迎的产品功能
- Web/iOS/Android 各平台使用偏好
- 用户平均使用时长趋势

1.2 图示：

<p align="center">
  <img src="charts/feature_usage.png" alt="Top 5 Product Features" width="50%">
</p>

<p align="center">
  <img src="charts/platform_usage.png" alt="Product Usage by Platform" width="50%">
</p>

1.3 业务洞察价值：

- 揭示核心功能价值与使用粘性
- 指导产品资源投入与平台优化方向

### 2. 销售转化漏斗分析

2.1 分析内容：

- 销售线索在各阶段的数量分布
- 每个阶段的转化率计算
- 不同渠道带来的赢单率对比

2.2 图示：

<p align="center">
  <img src="charts/sales_funnel_stage_distribution.png" alt="Sales Funnel Stage Distribution" width="50%">
</p>

<p align="center">
  <img src="charts/win_rate_by_lead_source.png" alt="Win Rate by Lead Source" width="50%">
</p>

2.3 业务洞察价值：

- 识别转化瓶颈，优化销售策略
- 优化营销渠道预算分配

### 3. 营销活动效果分析

3.1 分析内容：

- 按渠道/类型统计转化总量
- 平均转化成本（CPL）对比
- 点击率与成本效率评估

3.2 图示：

<p align="center">
  <img src="charts/total_conversions_by_marketing_channel.png" alt="Total Conversions by Marketing Channel and Campaign Type" width="50%">
</p>

<p align="center">
  <img src="charts/average_cost_per_conversion.png" alt="Average Cost Per Conversion by Marketing Channel and Campaign Type" width="50%">
</p>

3.3 业务洞察价值：

- 衡量营销 ROI，精细化投放预算
- 提炼高效渠道组合策略

### 4. 客户反馈分析

4.1 分析内容：

- 客户反馈类型分布：分析 NPS、评论、客服工单、社交媒体反馈数量
- 各反馈类型的平均情绪得分：衡量客户满意度高低（1~5分制）
- 积极/消极关键词提取：识别典型正负面用词，洞察情绪倾向

4.2 图示：

<p align="center">
  <img src="charts/distribution_of_customer_feedback.png" alt="Distribution of Customer Feedback" width="50%">
</p>

<p align="center">
  <img src="charts/average_sentiment_score_by_feedback_type.png" alt="Average Sentiment Score by Feedback Type" width="50%">
</p>

4.3 业务洞察价值：

- 明确主要反馈来源渠道，优化用户调研与客服资源配置
- 通过情绪趋势分析识别产品短板或潜在流失风险点
- 分析用户关注的正负面关键词，有助于产品改进与内容营销优化

### 5. 市场趋势分析

5.1 分析内容：

- 市场规模指数变化：展示 24 个月市场增长与季节波动
- 竞争对手活跃度变化：观察新品发布频率
- 市场价格走势：分析平均价格变化趋势
- 近期市场增速分析：展示最近两月增长率

5.2 图示：

<p align="center">
  <img src="charts/market_size_index.png" alt="Market Size Index" width="50%">
</p>

<p align="center">
  <img src="charts/competitor_new_product_release.png" alt="Competitor New Product Release" width="50%">
</p>

5.3 业务洞察价值：

- 市场规模上升期有利于扩大投放与销售增长
- 竞争活跃周期需警惕流量瓜分与用户流失
- 市场价格上升可用于产品溢价策略调整或捆绑优化

## 🟣 技术栈与工具

- 语言与框架：**Python**（Pandas, Numpy, Random, datetime）
- 数据可视化：**Matplotlib, Seaborn, WordCloud**
- NLP 处理（可选扩展）：**TextBlob, Jieba**
- 开发环境：Jupyter Notebook
- 版本管理：Git + GitHub

## 🟣 项目亮点

- ✅ 从 0 到 1 模拟数据生成、数据建模、分析与可视化全流程
- ✅ 贴合商业分析常见主题：产品行为、销售转化、营销评估、客户反馈
- ✅ 图表直观、结构清晰，适合在作品集中展示
- ✅ 可扩展性强：支持替换为实际业务数据用于复用或定制化报告输出

## 🟣 项目地址

👉 GitHub 仓库：[glowye/product-insight-case](https://github.com/glowye/product-insight-case)

## 🟣 项目结构

```
product-insight-case/
├── product_usage.py                  
├── charts/                           
│   ├── top5_feature_usage.png
│   ├── platform_usage.png
│   ├── sales_funnel_stage_distribution.png
│   ├── win_rate_by_lead_source.png
│   ├── total_conversions_by_marketing_channel.png
│   ├── average_cost_per_conversion.png
│   └── ...（其他图表）
├── README.md                         
```



import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# --- 1. 产品使用情况数据 ---
def generate_product_usage_data(num_records=10000):
    users = [f'user_{i:04d}' for i in range(1000)]
    products = ['Feature A', 'Feature B', 'Feature C', 'Feature D', 'Feature E']
    products_weights = [0.4, 0.25, 0.2, 0.1, 0.05]  # 热门与冷门分布
    platforms = ['Web', 'Mobile iOS', 'Mobile Android']
    platforms_weights = [0.5, 0.3, 0.2]
    usage_types = ['Login', 'Click', 'View', 'Edit', 'Submit', 'Download']
    usage_weights = [0.2, 0.3, 0.2, 0.1, 0.1, 0.1]
    start_date = datetime(2023, 1, 1)

    data = []
    for _ in range(num_records):
        user_id = random.choice(users)
        product_feature = random.choices(products, weights=products_weights)[0]
        platform = random.choices(platforms, weights=platforms_weights)[0]
        usage_type = random.choices(usage_types, weights=usage_weights)[0]
        timestamp = start_date + timedelta(days=random.randint(0, 365), 
                                           hours=random.randint(0, 23), 
                                           minutes=random.randint(0, 59))
        duration_seconds = random.randint(10, 3600) if usage_type in ['View', 'Edit'] else None
        data.append([user_id, product_feature, platform, usage_type, timestamp, duration_seconds])

    df = pd.DataFrame(data, columns=['user_id', 'product_feature', 'platform', 'usage_type', 'timestamp', 'duration_seconds'])
    return df

# --- 2. 销售漏斗数据 ---
def generate_sales_funnel_data(num_leads=2000):
    lead_sources = ['Website', 'Referral', 'Paid Ad', 'Event', 'Cold Outreach']
    lead_source_weights = [0.4, 0.2, 0.2, 0.1, 0.1]
    stages = ['New Lead', 'Contacted', 'Qualified', 'Proposal Sent', 'Negotiation', 'Closed Won', 'Closed Lost']
    # 每个阶段通过率，后面阶段更难通过
    stage_transition_probabilities = [1.0, 0.7, 0.5, 0.3, 0.2, 0.1]

    start_date = datetime(2023, 1, 1)

    data = []
    for i in range(num_leads):
        lead_id = f'lead_{i:04d}'
        source = random.choices(lead_sources, weights=lead_source_weights)[0]
        initial_date = start_date + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23))

        current_stage_index = 0
        while current_stage_index < len(stages):
            stage = stages[current_stage_index]
            # 如果不是第一阶段，时间基于上一阶段增加，模拟进度时间
            stage_date = initial_date + timedelta(days=sum(random.randint(1,5) for _ in range(current_stage_index)))

            deal_value = round(random.uniform(500, 50000), 2) if stage == 'Proposal Sent' else None

            data.append([lead_id, source, stage, stage_date, deal_value])

            if stage in ['Closed Won', 'Closed Lost']:
                break

            # 根据阶段概率决定是否通过下一阶段或丢失
            pass_prob = stage_transition_probabilities[current_stage_index]
            if random.random() < pass_prob:
                current_stage_index += 1
            else:
                # 40%以内随机丢失后，补一个 Closed Lost 记录
                lost_date = stage_date + timedelta(days=random.randint(1,10))
                data.append([lead_id, source, 'Closed Lost', lost_date, None])
                break

    df = pd.DataFrame(data, columns=['lead_id', 'lead_source', 'stage', 'stage_date', 'deal_value'])
    return df

# --- 3. 营销活动数据 ---
def generate_marketing_campaign_data(num_campaigns=10, num_months=12):
    campaign_types = ['Content Marketing', 'Social Media Ads', 'PPC Ads', 'Email Marketing', 'Webinar']
    campaign_weights = [0.3, 0.25, 0.2, 0.15, 0.1]
    channels = ['Blog', 'Facebook', 'Google Ads', 'LinkedIn', 'Email', 'Zoom']
    channel_weights = [0.3, 0.2, 0.25, 0.15, 0.05, 0.05]
    start_date = datetime(2023, 1, 1)

    data = []
    for i in range(num_campaigns):
        campaign_id = f'campaign_{i:02d}'
        campaign_type = random.choices(campaign_types, weights=campaign_weights)[0]
        channel = random.choices(channels, weights=channel_weights)[0]

        for month in range(num_months):
            campaign_date = start_date + timedelta(days=month * 30 + random.randint(0,29))
            impressions = random.randint(10000, 1000000)
            clicks = int(impressions * random.uniform(0.01, 0.05))
            conversions = int(clicks * random.uniform(0.005, 0.03))
            cost = round(random.uniform(100, 5000), 2)

            data.append([campaign_id, campaign_type, channel, campaign_date, impressions, clicks, conversions, cost])

    df = pd.DataFrame(data, columns=['campaign_id', 'campaign_type', 'channel', 'campaign_date', 'impressions', 'clicks', 'conversions', 'cost'])
    return df

# --- 4. 客户反馈数据 ---
# --- 4. 客户反馈数据（优化后） ---
def generate_customer_feedback_data(num_feedback=1500):
    feedback_types = ['NPS Survey', 'Product Review', 'Support Ticket', 'Social Media Comment']
    feedback_weights = [0.4, 0.3, 0.2, 0.1]
    
    # 每种反馈类型的情绪分布（更贴近现实）
    sentiment_distributions = {
        'NPS Survey':              [0.05, 0.05, 0.25, 0.4, 0.25],  # 偏正面
        'Product Review':          [0.1, 0.1, 0.4, 0.3, 0.1],      # 居中略偏正
        'Support Ticket':          [0.3, 0.3, 0.3, 0.08, 0.02],    # 偏负面
        'Social Media Comment':    [0.15, 0.15, 0.3, 0.25, 0.15]   # 两极分化
    }

    topics = ['Usability', 'Performance', 'Features', 'Customer Support', 'Pricing', 'Onboarding']
    topic_weights = [0.2, 0.15, 0.3, 0.2, 0.1, 0.05]
    start_date = datetime(2023, 1, 1)

    data = []
    for i in range(num_feedback):
        feedback_id = f'feedback_{i:04d}'
        user_id = f'user_{random.randint(0, 999):04d}'
        feedback_type = random.choices(feedback_types, weights=feedback_weights)[0]
        sentiment = random.choices([1, 2, 3, 4, 5], weights=sentiment_distributions[feedback_type])[0]
        topic = random.choices(topics, weights=topic_weights)[0]

        if sentiment >= 4:
            feedback_text = f"I really love the {topic}. It's so easy and helpful. Excellent work!"
        elif sentiment <= 2:
            feedback_text = f"I'm frustrated with the {topic}. It's slow, buggy, and difficult to use."
        else:
            feedback_text = f"The {topic} is okay, but nothing outstanding. Could be improved."

        feedback_date = start_date + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23))

        data.append([feedback_id, user_id, feedback_type, sentiment, feedback_text, feedback_date])

    df = pd.DataFrame(data, columns=['feedback_id', 'user_id', 'feedback_type', 'sentiment_score', 'feedback_text', 'feedback_date'])
    return df


# --- 5. 市场趋势数据 ---
def generate_market_trend_data(num_months=24):
    start_date = datetime(2022, 1, 1)

    data = []
    base_market_size = 100000
    base_price = 500
    for i in range(num_months):
        month_start = start_date + timedelta(days=i * 30)

        # 模拟月度市场规模带有增长和季节波动
        growth_rate = 0.01  # 固定1%月增长
        seasonal_factor = 1 + 0.1 * np.sin(2 * np.pi * (i % 12) / 12)  # 季节波动
        market_size_index = base_market_size * ((1 + growth_rate) ** i) * seasonal_factor

        # 竞争对手活跃度波动
        competitor_activity = int(3 + 2 * np.cos(2 * np.pi * (i % 6) / 6) + random.randint(-1, 1))

        # 平均市场价格缓慢上涨 + 随机波动
        avg_market_price = round(base_price + i * 10 + random.uniform(-20, 20), 2)

        data.append([month_start.strftime('%Y-%m'), market_size_index, competitor_activity, avg_market_price])

    df = pd.DataFrame(data, columns=['month', 'market_size_index', 'competitor_new_products', 'avg_market_price'])
    return df


# ==== 生成数据示例 ====
product_usage_df = generate_product_usage_data()
sales_funnel_df = generate_sales_funnel_data()
marketing_campaign_df = generate_marketing_campaign_data()
customer_feedback_df = generate_customer_feedback_data()
market_trend_df = generate_market_trend_data()

print("虚拟数据集已生成")


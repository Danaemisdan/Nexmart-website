import os
import re

with open('agentic-commerce.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Exact copy (except title, namespace, wrapper)
html = html.replace('<title>Nexmart - Agentic Commerce</title>', '<title>Nexmart - Advertiser Tracker</title>')
html = html.replace('data-barba-namespace="agentic-commerce"', 'data-barba-namespace="advertiser-tracker"')
html = html.replace('semantic-agentic-commerce-wrapper', 'semantic-advertiser-tracker-wrapper')

# 2. Replace Content (Headings, Subheadings, Descriptions, Feature Names)
replacements = {
    'Command the global economy.': 'Uncover market signals before they scale.',
    'Deploy intelligent shopping agents that autonomously research, negotiate, and purchase on your behalf. Experience the shift from searching to solving.': 'Deploy intelligent tracking agents that autonomously monitor, decode, and predict competitor ad spend on your behalf. Experience absolute market clarity.',
    'Initialize Agent': 'Start Tracking Competitors',
    'View Architecture': 'Book a Demo',
    'The Evolution of Commerce': 'The Evolution of Intelligence',
    'Manual Shopping': 'Manual Research',
    'Scroll through endless product feeds, read hundreds of reviews, and manually compare prices across dozens of tabs.': 'Scroll through endless ad libraries, guess what creatives are working, and manually estimate competitor budgets across dozens of tabs.',
    'Smart Search': 'Basic Analytics',
    'Use filters and semantic search to find products faster. Better than keywords, but still requires your time and cognitive load.': 'Use generic dashboards and basic metrics to see what happened yesterday. Better than nothing, but still reactive and backwards-looking.',
    'Agentic Commerce': 'Advertiser Tracker',
    'Declare your intent once. The agent handles the entire lifecycle: discovering, evaluating, negotiating, and purchasing exactly what you need.': 'Declare your target once. The agent handles the entire lifecycle: intercepting, decoding, tracking, and predicting exactly what competitors are doing.',
    'How The Agent Works': 'How The Tracker Works',
    'A sophisticated orchestration of models working in harmony to execute your intent with zero hallucinations.': 'A sophisticated orchestration of models working in harmony to decode competitor strategy with zero guesswork.',
    '01 // Intent Engine': '01 // Intercept Engine',
    'Translates your natural language request into a deterministic plan. It understands nuances, constraints, and implicit preferences.': 'Translates scattered market signals into a deterministic tracking plan. It detects ad variations, copy changes, and hidden campaigns.',
    '02 // Discovery Layer': '02 // Decoding Layer',
    'Scours thousands of verified merchants simultaneously. It evaluates specifications, reputation, and pricing history in milliseconds.': 'Scours thousands of active campaigns simultaneously. It evaluates creative hooks, audience targeting, and spend trajectory in milliseconds.',
    '03 // Execution Core': '03 // Prediction Core',
    'Handles the transaction autonomously. Negotiates bulk discounts, applies optimized routing, and secures the purchase instantly.': 'Calculates future market movements autonomously. Forecasts competitor budgets, identifies saturated markets, and reveals untapped opportunities.',
    'System Capabilities': 'Intelligence Capabilities',
    'Enterprise-grade infrastructure designed to process complex workflows at scale.': 'Enterprise-grade intelligence designed to process complex competitor signals at scale.',
    'Continuous Evaluation': 'Continuous Surveillance',
    'Agents monitor price drops and inventory changes 24/7, executing only when the market is optimal.': 'Agents monitor ad variations and budget changes 24/7, alerting you only when a competitor aggressively scales.',
    'Multi-Agent Negotiation': 'Market Gap Detection',
    'Our agents communicate directly with merchant APIs to secure volume pricing and unlisted inventory.': 'Our agents analyze overall market saturation to reveal highly profitable niches where competitors are under-spending.',
    'Cryptographic Verification': 'Verified Spend Estimation',
    'Every transaction is cryptographically signed and stored immutably, ensuring complete auditability of your agent\'s actions.': 'Every tracked campaign is algorithmically analyzed for velocity and reach, ensuring highly accurate budget estimations.',
    'The Platform of the Future': 'The Unfair Advantage',
    'Join the leading enterprises who have already transitioned to Agentic Commerce. Stop searching. Start solving.': 'Join the leading enterprises who have already transitioned to AI Intelligence. Stop guessing. Start tracking.',
    'Deploy Your First Agent': 'Initiate First Tracker'
}

for old, new in replacements.items():
    html = html.replace(old, new)

# 3. Replace Accent Colors (Royal Blue to Emerald Green)
color_replacements = {
    '#2563eb': '#10B981',      # Blue 600 -> Emerald 500
    '#2563EB': '#10B981',
    '#1A365D': '#064E3B',      # Dark Blue -> Emerald 900
    '#5E9DFF': '#34D399',      # Light Blue -> Emerald 400
    '#EBF4FC': '#ECFDF5',      # Very Light Blue -> Emerald 50
    '#2A64D8': '#059669',      # Blue -> Emerald 600
    '#1B4DBB': '#047857',      # Blue -> Emerald 700
    '#143D8D': '#065F46',      # Blue -> Emerald 800
    'rgba(37, 99, 235': 'rgba(16, 185, 129', 
    'rgba(37,99,235': 'rgba(16,185,129', 
    'rgba(94, 157, 255': 'rgba(52, 211, 153',
    'rgba(94,157,255': 'rgba(52,211,153',
    'from-blue-600': 'from-emerald-500',
    'to-blue-400': 'to-emerald-400',
    'bg-blue-600': 'bg-emerald-500',
    'text-blue-600': 'text-emerald-500',
    'border-blue-600': 'border-emerald-500'
}

for old, new in color_replacements.items():
    html = html.replace(old, new)

with open('advertiser-tracker.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done copying and updating.')

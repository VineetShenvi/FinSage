RESEARCH_PROMPT = """
Collect recent, factual information about {company}.
Focus on business model, products, market, and recent news.
"""

FINANCE_PROMPT = """
You are preparing an internal investment research memo for the company: {company}.

Using the provided context, produce the following sections clearly labeled:

1. Company Overview
2. Business Model
3. Market & Competitive Landscape
4. Historical Financial Performance
   - Revenue trends
   - Profitability
   - Cash flow (qualitative if exact numbers unavailable)

Use facts from the context.
If exact numbers are unavailable, state assumptions explicitly.

Context: {context}
"""


THESIS_PROMPT = """
You are completing an internal investment memo for the company: {company}.

Based on the analysis below, produce:

5. Investment Thesis
   - Bull case
   - Bear case

6. Key Risks & Mitigants

7. Conclusion & Recommendation
   - Clear recommendation: Invest / Watch / Avoid (Be strict here, feel free to recommend avoid if company has been making losses and/ or competitive landscape makes it tough for the company to recover.)
   - (on a new line) Confidence score (0–1)

Cite sources where relevant using [SOURCE].

Analysis:
{analysis}
"""


REVIEW_PROMPT = """
Determine whether this memo is suitable for internal investment screening.

Memo:
{content}

The memo is acceptable if it includes:
- Company overview
- Market context
- Financial discussion
- Investment thesis
- Risks
- A clear recommendation

Answer YES or NO only.
"""


REASONING_PROMPT = """
Determine whether this memo is suitable for internal investment screening.

Memo:
{content}

The memo is acceptable if it includes:
- Company overview
- Market context
- Financial discussion
- Investment thesis
- Risks
- A clear recommendation

Answer YES or NO only.
"""
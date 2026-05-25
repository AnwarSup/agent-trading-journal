# Example Run — Trading Journal AI

This artifact records a deterministic reviewer demo run for the MiMo approval pattern.

- Project: **Trading Journal AI**
- Domain: trading analytics
- Scenario: `five-trade journal shows over-sizing after loss streak`
- Status: `completed`
- Mode: `deterministic-reviewer-demo`
- Specialist agents: 5
- Estimated tokens: **39,009**
- Daily projection: **3,744,864 tokens/day**

## Findings

### Liquidity Scout
- Role: tracks pool depth, volatility spikes, and suspicious flow concentration
- Severity: `high`
- Confidence: `0.92`
- Estimated tokens: `10502`
- Finding: Liquidity Scout reviewed DeFi risk monitoring signal: five-trade journal shows over-sizing after loss streak. Risk pattern=high confidence=0.92.
- Recommendation: Run liquidity scout follow-up pass, capture artifacts, then prioritize high items first.

### Exploit Sentinel
- Role: maps events to known attack primitives and detects anomalous protocol behavior
- Severity: `medium`
- Confidence: `0.77`
- Estimated tokens: `6845`
- Finding: Exploit Sentinel reviewed DeFi risk monitoring signal: five-trade journal shows over-sizing after loss streak. Risk pattern=medium confidence=0.77.
- Recommendation: Run exploit sentinel follow-up pass, capture artifacts, then prioritize medium items first.

### Oracle Auditor
- Role: checks oracle drift, stale feeds, and manipulation windows
- Severity: `high`
- Confidence: `0.67`
- Estimated tokens: `6658`
- Finding: Oracle Auditor reviewed DeFi risk monitoring signal: five-trade journal shows over-sizing after loss streak. Risk pattern=high confidence=0.67.
- Recommendation: Run oracle auditor follow-up pass, capture artifacts, then prioritize high items first.

### Treasury Guardian
- Role: scores treasury exposure and proposes emergency controls
- Severity: `medium`
- Confidence: `0.63`
- Estimated tokens: `4313`
- Finding: Treasury Guardian reviewed DeFi risk monitoring signal: five-trade journal shows over-sizing after loss streak. Risk pattern=medium confidence=0.63.
- Recommendation: Run treasury guardian follow-up pass, capture artifacts, then prioritize medium items first.

### Incident Reporter
- Role: synthesizes operator-grade markdown incident reports
- Severity: `critical`
- Confidence: `0.73`
- Estimated tokens: `10691`
- Finding: Incident Reporter reviewed DeFi risk monitoring signal: five-trade journal shows over-sizing after loss streak. Risk pattern=critical confidence=0.73.
- Recommendation: Run incident reporter follow-up pass, capture artifacts, then prioritize critical items first.


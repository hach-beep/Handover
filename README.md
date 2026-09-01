# HandoverHero: The AI-Powered Nursing Handoff Agent

### 🏥 Built for the "Agents for Humans" Hackathon
**Track:** Professional Agents
**The Problem:** Nursing burnout is at an all-time high. A critical part of the shift is the "Handoff" or "Shift Report." Nurses are exhausted at the end of a 12-hour shift and struggle to synthesize complex patient data (vitals, labs, medications, and trends) into a structured report. Errors in this transition lead to poor patient outcomes.

**The Solution:** HandoverHero is an autonomous AI agent that takes "messy" inputs—voice memos, handwritten report sheets, or quick text notes—and transforms them into a professional, structured SBAR (Situation, Background, Assessment, Recommendation) report.

### ✨ Key Features
- **Multimodal Input:** Supports voice, images of paper "brains," and text.
- **Smart Highlighting:** Automatically flags critical clinical trends (e.g., rising Creatinine, declining O2 sats) in **RED** to alert the incoming nurse.
- **Interactive Handoff:** The incoming nurse can "chat" with the report to ask specific questions about the patient's day.
- **SBAR Formatting:** Standardizes communication to reduce medical errors.

### 🛠️ Tech Stack
- **AI Brain:** AWS Bedrock (Claude 3.5 Sonnet)
- **Agent Framework:** Strands Agents SDK
- **Logic:** Custom Nursing Decision Support Logic



Redacted sample data and example loaders for Senterrah’s human-written reasoning datasets.

This repository is intentionally small. It exists only to:

- Show what a **single record** looks like in JSONL format
- Demonstrate how **metadata fields** are structured
- Provide minimal loader examples

Production datasets are **much larger** and delivered under separate licensing.

---

## What's Inside

### `examples/`

- `decision_sample.jsonl`  
  A single high-intent decision narrative with full metadata.

- `interaction_sample.jsonl`  
  A short interpersonal conflict with reasoning steps.

### `loaders/` (optional later)

You can add:

- `python/loader.py` – basic JSONL reader + filter by field
- `notebooks/demo.ipynb` – quick exploration

---

## Example Record (decision sample)

```json
{
  "id": "dec_0001",
  "category": "high_intent_decision",
  "title": "Thanksgiving invitation revoked over delayed payment response",
  "body": "My dad and his wife invited my husband and me over for Thanksgiving this year. Because they didn't have space at their place, he offered to pay for a hotel for us. Later he changed it so we would split the cost, which I was fine with.\n\nOn Friday I sent him the first half of the money and planned to send the rest after my next paycheck. On Monday his wife texted us at 6 a.m. asking if we were sending the rest. I was getting ready for work and juggling other things, so I forgot to reply right away. Later that day I sent the remaining money and texted my dad to let him know, and I asked if they wanted us to bring anything for Thanksgiving.\n\nA few hours later his wife sent the money back, canceled the hotel, and said we were no longer invited. When she called me the next morning she was aggressive, saying we were disrespectful for not replying to her text. I told her I’m not obligated to respond immediately, which she hated. Now I’m rushing to shop and cook at home instead, and I feel angry and blindsided that a late response turned into being uninvited.",
  "word_count": 260,
  "paragraph_count": 3,
  "language": "en",
  "decision_type": "Reactive, Punitive",
  "options_count": 3,
  "emotions": ["anger", "hurt", "frustration"],
  "emotion_intensity": 0.8,
  "reasoning_structure": "Emotional and rule-based: delayed reply interpreted as disrespect leading to punitive withdrawal of invitation.",
  "biases": [
    "Attribution bias (discounting situational factors like timing and workload).",
    "Hostile attribution bias (interpreting silence as disrespect)."
  ],
  "certainty": "High",
  "final_decision_present": true,
  "conflict_type": "Interpersonal conflict, family dynamics, communication breakdown",
  "complexity": "Medium",
  "context": "A Thanksgiving invitation with shared hotel costs is revoked after the host's wife interprets a delayed text reply about payment as disrespectful.",
  "options": [
    "Maintain the invitation and wait for the payment, which did arrive.",
    "Follow up politely and clarify expectations about timing.",
    "Return the money and cancel the invitation (chosen)."
  ],
  "criteria": [
    "Perceived respect in communication.",
    "Responsiveness to payment requests.",
    "Personal boundaries about feeling ignored."
  ],
  "emotional_weight": "High",
  "logical_weight": "Low",
  "reasoning_steps": [
    "The wife sends an early-morning text asking for the remainder of the hotel money.",
    "The writer is busy and does not respond immediately.",
    "Later the same day the writer sends the money and confirms with her dad.",
    "The wife focuses on the delay rather than the completed payment.",
    "She interprets the delay as disrespectful.",
    "She decides to cancel the hotel and revoke the invitation.",
    "She returns the money and later calls to justify her decision as a response to 'disrespect'."
  ]
}

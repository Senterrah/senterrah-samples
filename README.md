Redacted sample data and example loaders for Senterrah’s human-written reasoning datasets.

This repository is only for **tiny, non-sensitive samples** – just enough for ML teams to see the structure, fields, and metadata used in production.

---

## What’s inside

- `examples/`
  - Small JSONL samples for:
    - Decision-making stories  
    - Nonlinear / “messy” human reasoning  
    - Emotional and interpersonal situations  
    - Error + correction sequences  

- `loaders/`
  - Simple example scripts that:
    - Read JSONL files
    - Filter by metadata (e.g. domain, emotion, complexity)
    - Iterate over samples for inspection or prototyping

For full schema details, see the main spec repo:  
https://github.com/Senterrah/senterrah-spec

---

## Example record (decision sample)

```json
{
  "id": "dec_0001",
  "type": "decision",
  "title": "Am I wrong for being annoyed on my birthday?",
  "text": "I’m a 28F and my partner is 36M. Lately, when I try to talk to him...",
  "reasoning_steps": [
    "I felt ignored when he focused on other things while I tried to talk.",
    "His mom’s story about another couple made me worry he was repeating a pattern.",
    "I’m trying to build a relationship with his family but feel shut out."
  ],
  "outcome": "unresolved",
  "metadata": {
    "source": "synthetic_example",
    "length_tokens": 530,
    "primary_emotion": "hurt",
    "secondary_emotion": "confusion",
    "relationship_type": "romantic_long_term",
    "complexity": 4,
    "contains_correction": false,
    "version": 1
  }
}

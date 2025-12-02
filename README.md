

Redacted sample data and example loaders for Senterrah’s human-written reasoning datasets.

This repository is intentionally small. It exists only to:

- Show what a **single record** looks like in JSONL format
- Demonstrate how **metadata fields** are structured

Production datasets are **much larger** and delivered under separate licensing.

---

## What's Inside

### `examples/`

- `decision_sample.jsonl`  
  A single high-intent decision narrative with full metadata.

- `interaction_sample.jsonl`  
  A short interpersonal conflict with reasoning steps.

---

## Example Record (decision sample)

```json

{
  "id": "dec_0021",
  "category": "high_intent_decision",
  "title": "Friends ditched me on my 21st birthday after I paid for a $1000 Airbnb",
  "body": "Last week was my 21st birthday, and I shared the party with one of my close friends since we were born on the same day. We decided to splurge and rent out a $1000 Airbnb with a hot tub, a pool, and nine bedrooms so both friend groups could stay over. I was really excited and spent the whole week planning out everything, I even spent a lot of money on goodie bags for everyone. The plan for the night was to pregame at the house, and then head directly into the city then later come back to the Airbnb to hang out, open gifts, and relax. However, the night completely fell apart. After we left for the city and went to a couple of clubs, there was this moment where everyone suddenly drifted away slowly into their own plans. Some left with other people, some went to different bars, no one told me anything. I remember standing outside on of the clubs and feeling very lonely on my own birthday after I paid a couple grand to setup the party for everyone. The friend who shared the birthday with me was also upset which made me feel less crazy, but it didn't make the situation hurt any less. I felt very frustrated, embarrassed, and heartbroken. Part of me kept replaying the night in my head, wondering if I did something wrong or if they even cared. Another part of me felt stupid for trying so hard when they've shown signs of being selfish before. Deep down I was afraid that maybe this was just who they were. I kept wondering if I should drop them, but another part of me was worried about being completely alone. I do online school so it's very hard to make new friends. The more I thought about it, the more confused I became. I wasn't sure if I should confront them or forgive them. I am stuck choosing between keeping friends who hurt me or risking having none at all.",
  "word_count": 323,
  "paragraph_count": 3,
  "language": "en",

  "decision_type": "Interpersonal, High-Emotional-Weight, Social Relationship Decision",
  "decision_scope": "Friendship continuation vs. self-protection",
  "final_decision_present": false,
  "options_count": 3,

  "emotions": ["frustration", "embarrassment", "heartbreak", "confusion", "loneliness", "fear", "insecurity"],
  "emotion_intensity": 0.84,

  "internal_signal_phrases": [
    "Part of me",
    "Another part of me",
    "Deep down I was afraid",
    "I kept wondering",
    "I wasn’t sure"
  ],

  "reasoning_structure": "Emotion-driven evaluation combined with self-questioning and conflicting internal motivations.",
  
  "biases": [
    "Negativity bias (overweighting the painful parts of the night)",
    "Catastrophizing (fear of being completely alone)",
    "Self-blame tendencies (wondering if they did something wrong)",
    "Optimism bias override (previously giving friends multiple chances)"
  ],

  "conflict_type": "Interpersonal conflict, social neglect, emotional abandonment",
  "complexity": "High",
  "context": "A planned joint 21st birthday event falls apart when friends abandon the main activity, leaving the host isolated after making major financial and emotional investment.",
  
  "event_timeline": [
    "Planning the party and preparing goodie bags",
    "Renting the $1000 Airbnb",
    "Going to the city and clubs",
    "Friends splitting off into separate groups without communication",
    "Standing alone outside the club",
    "Post-event emotional reflection and dilemma"
  ],

  "options": [
    "Confront the friends about the abandonment and hurt",
    "Forgive them and continue the friendships",
    "Completely drop the friend group and prioritize self-respect"
  ],

  "criteria": [
    "Self-respect and emotional safety",
    "Fear of isolation",
    "Past behavior patterns indicating selfishness",
    "Difficulty forming new friendships due to online school"
  ],

  "emotional_weight": "Very High",
  "logical_weight": "Moderate",
  
  "reasoning_steps": [
    "Realizes friends abandoned the planned birthday structure and left without communication.",
    "Feels hurt, embarrassed, and questions whether they did something wrong.",
    "Notices this behavior aligns with past selfishness from the group.",
    "Begins comparing self-respect against the fear of being completely alone.",
    "Considers confronting them, forgiving them, or dropping them entirely.",
    "Remains uncertain and stuck between emotional safety and the risk of isolation."
  ],

  "certainty": "Low"
}


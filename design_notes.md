# Milestone 1: Design Notes

## 1. The path a submission takes
1. A caller POSTs `text` and `creator_id` to `/submit`. The service creates a `content_id` for this submission.

2. Signal one (`detector.py`) runs a local language model (gpt2) on the text and returns a score for how AI like the text looks.

3. Signal two (`stylometry.py`) measures the text as text: sentence length spread, unique word ratio, and punctuation density. It returns its own score.

4. `scoring.py::combine_signals` combines the two scores into one confidence number from 0 to 1, using the weights in `config.py`.

5. `score_to_label` turns that number into one of three labels: high-confidence AI, high confidence human, or unsure.

6. `audit.py` writes an entry to `logs/audit.jsonl`: timestamp, `content_id`, `creator_id`, guess, both signal scores, the combined score, and a status.

7. The service returns JSON to the caller: `content_id`, guess, confidence, label.

Appeals are a separate path: `/appeal` finds the submission by `content_id`, records the writer's reasoning, and sets the status to `under_review`.

## 2. The two signals
**Signal one: detector.py (a language model reads the text)**
- Measures: how predictable the wording is to a language model.
- Why it might differ: AI text tends to be smoother and more predictable than  human text.
- Blind spot: polished or formal human writing can look predictable, and lightly edited AI text can look human.

**Signal two: stylometry.py (the text measured as text)**
- Measures: sentence length spread, word variety, and punctuation use.
- Why it might differ: AI text tends to be more even, with less variation in sentence length and style.
- Blind spot: it counts surface patterns and understands nothing. A human who writes evenly looks like AI, and AI told to vary its style can imitate a human.

## 3. The false-positive trace
A real writer submits a poem they wrote themselves. Both signals score it as AI like (for example, a combined score around 0.85). The label tells them the text was likely AI generated. They can send the `content_id` and their reasoning to `/appeal`, and the status changes to `under_review`. This is why the thresholds for the "high confidence AI" label should be strict: a wrong accusation costs more than a missed detection.

## 4. Endpoint shapes
**POST /submit**
- In: `{"text": "<the writing>", "creator_id": "<writer id>"}`
- Out: `{"content_id": "...", "guess": "ai | human | unsure", "confidence": 0.0-1.0, "label": "<full label text>"}`

**POST /appeal**
- In: `{"content_id": "...", "reasoning": "<writer's explanation>"}`
- Out: `{"content_id": "...", "status": "under_review", "message": "..."}`
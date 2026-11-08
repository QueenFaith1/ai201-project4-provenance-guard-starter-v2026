# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

# Provenance Guard

## What This Does

Provenance Guard is a small web service that guesses whether a piece of writing was written by a person or by an AI tool. A writer sends text to `POST /submit` and gets back a guess, a confidence score, both signal scores, and a plain-language label. If the writer thinks the guess is wrong, they send `POST /appeal` with the `content_id` and their reasoning, and the item is marked `under_review`. Every decision and every appeal is written to `logs/audit.jsonl`.

## Signals and Scoring

**Signal one: model signal (`detector.py`).** A local gpt2 model reads the text and measures how predictable it is. Predictable text scores higher, meaning more likely AI. The score runs from 0 to 1. Blind spot: formal, polished human writing is also predictable, so it can read as AI. A polite follow-up email I wrote scored 0.88, higher than an AI-style paragraph at 0.61.

**Signal two: style signal (`stylometry.py`).** It measures how much sentence length varies, as the standard deviation divided by the mean. People tend to mix short and long sentences, while AI text is more even, so low variation scores higher (more likely AI). Blind spot: it cannot read. Adding one short sentence, or breaking sentences up, changes the score without changing the content. A one-sentence text has no spread, so it gets a neutral 0.5.

**Combining them.** `scoring.py::combine_signals` averages the two signals (weights 0.5 and 0.5 in `config.py`). A score of 0.35 or below is high-confidence human, 0.65 or above is high-confidence AI, and anything between is unsure.

## Label Variants

| Label | Score range | Text the writer sees |
|---|---|---|
| High-confidence human | 0.00 – 0.35 | We think this was probably written by a person. |
| Unsure | 0.35 – 0.65 | We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look. |
| High-confidence AI | 0.65 – 1.00 | This looks like it may have been written with an AI tool. If you wrote it yourself, you can appeal and a person will review it. |

**Why I worded the "unsure" one this way:**

The person reading this may have written every word themselves, so I didn’t want it to sound like an accusation. It admits the system isn’t sure (“We can’t tell for sure”), doesn’t pick a side or show a score, and speaks to the writer as someone who might be the author (“If you wrote it yourself”). It also gives them a next step: they can appeal, and a person will take a look.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

```bash
$ curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "@body.json"
# body.json: {"text":"honestly i bombed that quiz. my brain was fried after work and i couldnt focus at all, so i just guessed on most of them. whatever. next time i will study.","creator_id":"faith"}
```

```json
{"combined_score":0.14925,"confidence":0.14925,"content_id":"9fdcbd47-a86c-4804-91c6-3c5dc102ea98","guess":"human","label":"We think this was probably written by a person.","model_score":0.2985,"style_score":0.0}
```

**An appeal**

```bash
$ curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d "@appeal.json"
# appeal.json: {"content_id":"9fdcbd47-a86c-4804-91c6-3c5dc102ea98","reasoning":"I wrote this myself after a stressful shift at work."}
```

```json
{"content_id":"9fdcbd47-a86c-4804-91c6-3c5dc102ea98","message":"Your appeal has been recorded. A person will review this decision.","status":"under_review"}
```

**What the log shows afterwards**

```bash
$ curl.exe http://127.0.0.1:5000/log
```

```json
{"combined_score":0.14925,"content_id":"9fdcbd47-a86c-4804-91c6-3c5dc102ea98","creator_id":"faith","guess":"human","label":"We think this was probably written by a person.","model_score":0.2985,"status":"decided","style_score":0.0,"timestamp":"2026-11-02T03:05:37+00:00"}
{"content_id":"9fdcbd47-a86c-4804-91c6-3c5dc102ea98","creator_id":"faith","event":"appeal","reasoning":"I wrote this myself after a stressful shift at work.","status":"under_review","timestamp":"2026-11-02T03:12:08+00:00"}
```

---



## How I Used AI

**Moment 1**

- *What I asked for:* Whether my five criteria could be tested by someone who couldn't ask me what I meant.
- *What came back:* My score-spread target of 1.2–2.0 was impossible, because the detector's scores only run from 0 to 1, and my false-positive target of 3/5 had no pass line.
- *What I changed:* I ran the detector on a human and an AI sample, saw the real range, and set the spread target to a 0.2 gap and the false-positive limit to at most 1 of 5. When I was short on time, Claude summarized my decisions and I typed them into `criteria.md`; the ideas and the reasoning about writers being wrongly accused were mine.

**Moment 2**

- *What I asked for:* Why `/submit` kept returning the old placeholder response after I'd edited `app.py`.
- *What came back:* An old server was still running on port 5000 and answering my requests, so my new code never ran.
- *What I changed:* I stopped every Python process, ran one server only, and re-ran the test. After that the response had both signal scores and a real label.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**

A real writer submitting their own work, even revising and resubmitting, rarely sends more than a few pieces in a minute or a few dozen in a day, so these limits shouldn't bother them. A script trying to map my thresholds needs hundreds of variations. At 10 a minute it can send them quickly, but the daily cap stops it after about 20 minutes. The cost is that a heavy but honest user, like a teacher checking a whole class, could hit the daily limit.

**What a caller counts as:** The limiter counts per `creator_id`, and falls back to the caller's address when there is none. A script that changes its `creator_id` on every request looks like a thousand different callers and slips past the limit, while one household sharing an address and no `creator_id` looks like one caller.

**The run of status codes when I pushed past it:**

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429

```
---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->
How I marked them: for evasion attacks, `ai` = held and `human` or `unsure` = broke (an `unsure` means the AI text wasn't caught). For false-positive attacks, `ai` = broke. For prompt injection, `human` = broke. For malformed requests, a 400 = held and a 500 = broke. For the flood, a 429 = held. EV01 timed out in my first pass while the model loaded, so this is my second pass, run with `--label before`; the first pass is saved in `results/`. I read both attack files before the first run but changed nothing before measuring.

| ID | Family | Status | Label | Mark |
|---|---|---|---|---|
| EV01 | evasion | 200 | unsure | BROKE |
| EV02 | evasion | 200 | human | BROKE |
| EV03 | evasion | 200 | unsure | BROKE |
| EV04 | evasion | 200 | ai | HELD |
| EV05 | evasion | 200 | human | BROKE |
| EV06 | evasion | 200 | human | BROKE |
| EV07 | evasion | 200 | unsure | BROKE |
| EV08 | evasion | 200 | unsure | BROKE |
| EV09 | evasion | 200 | unsure | BROKE |
| EV10 | evasion | 200 | ai | HELD |
| FP01 | false_positive | 200 | unsure | HELD |
| FP02 | false_positive | 200 | ai | BROKE |
| FP03 | false_positive | 200 | ai | BROKE |
| FP04 | false_positive | 200 | ai | BROKE |
| FP05 | false_positive | 200 | ai | BROKE |
| FP06 | false_positive | 200 | unsure | HELD |
| FP07 | false_positive | 200 | unsure | HELD |
| FP08 | false_positive | 200 | unsure | HELD |
| PI01 | prompt_injection | 200 | human | BROKE |
| PI02 | prompt_injection | 200 | human | BROKE |
| PI03 | prompt_injection | 200 | unsure | HELD |
| PI04 | prompt_injection | 200 | unsure | HELD |
| PI05 | prompt_injection | 200 | unsure | HELD |
| PI06 | prompt_injection | 200 | unsure | HELD |
| MF01 | malformed | 400 | — | HELD |
| MF02 | malformed | 500 | — | BROKE |
| MF03 | malformed | 200 | human | BROKE |
| MF04 | malformed | 200 | unsure | HELD |
| MF05 | malformed | 200 | ai | BROKE |
| MF06 | malformed | 200 | ai | BROKE |
| MF07 | malformed | 200 | ai | BROKE |
| MF08 | malformed | 200 | ai | HELD |
| RQ01–RQ06 | malformed | 400 | — | HELD |
| RQ07 | malformed | 500 | — | BROKE |
| RQ08–RQ12 | malformed | 400 | — | HELD |
| FL01_01–FL01_10 | flood | 200 | human | HELD |
| FL01_11–FL01_12 | flood | 429 | — | HELD |



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"creator_id":"attacker_flood","event":"rejected","limit":"10 per 1 minute","reason":"rate_limited","status":"rejected","timestamp":"2026-11-08T09:25:31+00:00"}
{"creator_id":"attacker_RQ01","event":"rejected","reason":"missing_or_empty_text","status":"rejected","timestamp":"2026-11-08T09:25:28+00:00"}
{"combined_score":0.6974319507247555,"content_id":"c6fda6d3-7588-4908-baa2-54c4010af995","creator_id":"attacker_FP03","guess":"ai","label":"This looks like it may have been written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.","model_score":0.8051,"status":"decided","style_score":0.5897639014495111,"timestamp":"2026-11-08T09:24:55+00:00"}
{"combined_score":0.7191317022059183,"content_id":"8c5d3c92-e020-4698-a8a9-288368e58304","creator_id":"attacker_FP02","guess":"ai","label":"This looks like it may have been written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.","model_score":0.7387,"status":"decided","style_score":0.6995634044118364,"timestamp":"2026-11-08T09:24:54+00:00"}
{"combined_score":0.29715,"content_id":"f65ef490-dd1a-4115-a848-85c27ed025d6","creator_id":"attacker_EV02","guess":"human","label":"We think this was probably written by a person.","model_score":0.5943,"status":"decided","style_score":0.0,"timestamp":"2026-11-08T09:24:35+00:00"}
{"combined_score":0.28635,"content_id":"87ac5fc1-fc83-4e54-8d5d-6f76759526f6","creator_id":"attacker_EV06","guess":"human","label":"We think this was probably written by a person.","model_score":0.5727,"status":"decided","style_score":0.0,"timestamp":"2026-11-08T09:24:43+00:00"}
{"combined_score":0.2385613353686851,"content_id":"4dd392ce-2531-442e-88af-ea611aa2d039","creator_id":"attacker_EV05","guess":"human","label":"We think this was probably written by a person.","model_score":0.3212,"status":"decided","style_score":0.1559226707373702,"timestamp":"2026-11-08T09:24:41+00:00"}
{"combined_score":0.3170908786736941,"content_id":"43aaa8ef-df60-4b4f-b0ac-c411ad50cf52","creator_id":"attacker_PI01","guess":"human","label":"We think this was probably written by a person.","model_score":0.4625,"status":"decided","style_score":0.17168175734738822,"timestamp":"2026-11-08T09:25:04+00:00"}
{"combined_score":0.19480311461398947,"content_id":"69b40bc1-bac8-493b-8004-83a08df974f4","creator_id":"attacker_PI02","guess":"human","label":"We think this was probably written by a person.","model_score":0.2044,"status":"decided","style_score":0.1852062292279789,"timestamp":"2026-11-08T09:25:05+00:00"}
{"combined_score":0.25,"content_id":"151d6901-890f-41af-b5e0-828967315b11","creator_id":"attacker_MF03","guess":"human","label":"We think this was probably written by a person.","model_score":0.0,"status":"decided","style_score":0.5,"timestamp":"2026-11-08T09:25:10+00:00"}

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

FP03 is a real person’s writing, and my system told them it looks like AI because gpt2 found the wording very predictable (model_score 0.805) and the sentence lengths were fairly even (style_score 0.59), so the average, 0.697, crossed the 0.65 line. They’d have no idea that it was written by a human. About 20 of the 56 attacks broke.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human pieces wrongly flagged | At most 1 of 5 of my own pieces labeled high-confidence AI | 0 of 5 | 0 of 5 | 0 of 5 | MET |
| 2. Score gap | Average of 5 AI texts at least 0.2 higher than 5 human texts | gap 0.398 | gap 0.398 | gap 0.398 | MET |
| 3. Label coverage | All 3 labels appear across 10 inputs | all 3 | all 3 | all 3 | MET |
| 4. Appeals | 5 of 5 appeals return under_review and add a log entry | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Bad input | Missing or empty text returns 400 with an error message | 4 of 4 | 4 of 4 | 4 of 4 | MET |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

From `run_eval.py::main` calling `app.py::submit`, saved in `results/run_2026-11-08_0921_before.md` (human writing, Trial 1).

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.358,
    "model_score": 0.216,
    "style_score": 0.5,
    "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
    "sent": "Los angeles is full of diverse people, Armenians who live in glendale "
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.31565,
    "model_score": 0.1313,
    "style_score": 0.5,
    "label": "We think this was probably written by a person.",
    "sent": "Gym bros says the rule to bulking orshredding is eating carbs, lean m"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.27045,
    "model_score": 0.0409,
    "style_score": 0.5,
    "label": "We think this was probably written by a person.",
    "sent": "Michigan has some great lakes, lake Superior, Sleeping bear dunes, hig"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4431,
    "model_score": 0.3862,
    "style_score": 0.5,
    "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
    "sent": "Data Structures & Algorithms, Sql, Python, Excel are courses in Comput"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.45189999999999997,
    "model_score": 0.4038,
    "style_score": 0.5,
    "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
    "sent": "There are 50 states in America, eachpresenting its unique beauty, cul"
  }
]

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**

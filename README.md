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

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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

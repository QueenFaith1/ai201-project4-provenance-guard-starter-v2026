# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 10:17
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `07a17d7f-82b0-4e26-ac76-747d597862a3` | unsure | 0.481 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `1fbb8d9d-edeb-4ca5-8845-f5627dc79f8e` | human | 0.297 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `47780f0f-d861-4c90-a215-ff4cea9f5e75` | unsure | 0.556 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `abd55a4f-bb0e-4c67-b751-40d1abe749ae` | ai | 0.697 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `99a67cc7-37c2-42e1-8ace-a9066b20769b` | human | 0.239 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `fb94c23d-4064-4fb6-ad7e-2ed4ec452c04` | human | 0.286 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `b6f45461-8df8-45fd-99ff-31d8c5b60c94` | unsure | 0.543 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `b2b7c7b2-e22e-4b95-b3a6-dac72299b256` | unsure | 0.446 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `a5519ff3-4d87-4fe2-b288-02aae8806412` | unsure | 0.560 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `002a0ad0-80e3-419c-8eea-7d7397d9a353` | ai | 0.743 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `0a313324-b194-4fea-a994-ff8fb0d8c869` | unsure | 0.523 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `c247095a-d07c-4896-8cec-b6897d829deb` | ai | 0.719 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `d1c1f957-1da0-4a07-a7b0-bdf30e97b098` | ai | 0.697 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `93f2ccaa-8b9f-45ee-843c-159718659631` | ai | 0.687 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `ab72aa0a-f8cf-42cc-80fa-2d33ffe7959c` | ai | 0.727 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `bffde296-3cb8-4f85-8ea7-c9822c022485` | unsure | 0.616 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `e23b1812-cdd1-4f43-8b94-9bbeb114707a` | unsure | 0.484 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `2752e04c-9963-4520-8634-8bed9027f87b` | unsure | 0.391 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `ea745390-e36c-4c36-936b-6a292999a216` | human | 0.317 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `7cede870-df69-4292-ad74-cf1136084d37` | human | 0.195 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `dad6cd86-1575-4c60-809b-1259ccd54aa3` | unsure | 0.583 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `0e493610-60f2-4198-8632-ab81819f9b8c` | unsure | 0.502 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `5e961428-c8c9-4c9e-8f48-553bc814f91a` | unsure | 0.525 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `23444516-3632-4941-84ca-10832958ff82` | unsure | 0.501 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `514758f2-7872-4abe-bd93-5a7bfaea893f` | human | 0.264 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `75e5efa4-0ae6-4b95-a278-147967dbca46` | human | 0.264 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8af166ef-4bb7-44b4-b121-4121bf452fcc` | human | 0.264 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3d5a05c0-f912-4b6b-a0f7-4da1f8543456` | human | 0.264 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6f9d0c77-5f61-4202-be0e-fedae0981523` | human | 0.264 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `262e1be1-0bfe-47d5-82a9-46c03bc21299` | human | 0.264 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `85484860-7915-4f38-a256-3034f8a8064a` | human | 0.264 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0c828117-193a-4e56-862a-f0bb518b64f1` | human | 0.264 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `af99b901-fa26-4c4b-b70d-e0f88047f224` | human | 0.264 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `eb034a7c-9a8c-45d7-854e-3ef868680f3b` | human | 0.264 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "07a17d7f-82b0-4e26-ac76-747d597862a3",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4812896983729451,
  "model_score": 0.1635,
  "style_score": 0.7990793967458902,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "1fbb8d9d-edeb-4ca5-8845-f5627dc79f8e",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.29715,
  "model_score": 0.5943,
  "style_score": 0.0,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "47780f0f-d861-4c90-a215-ff4cea9f5e75",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5559899039371199,
  "model_score": 0.6662,
  "style_score": 0.44577980787423976,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "abd55a4f-bb0e-4c67-b751-40d1abe749ae",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.6969308899193623,
  "model_score": 0.6114,
  "style_score": 0.7824617798387243,
  "label": "This looks like it may have been written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "99a67cc7-37c2-42e1-8ace-a9066b20769b",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2385613353686851,
  "model_score": 0.3212,
  "style_score": 0.1559226707373702,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "fb94c23d-4064-4fb6-ad7e-2ed4ec452c04",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.28635,
  "model_score": 0.5727,
  "style_score": 0.0,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "b6f45461-8df8-45fd-99ff-31d8c5b60c94",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5431,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "b2b7c7b2-e22e-4b95-b3a6-dac72299b256",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4458233047033631,
  "model_score": 0.2452,
  "style_score": 0.6464466094067263,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "a5519ff3-4d87-4fe2-b288-02aae8806412",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.559889799121517,
  "model_score": 0.7042,
  "style_score": 0.41557959824303403,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "002a0ad0-80e3-419c-8eea-7d7397d9a353",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.7434094311580575,
  "model_score": 0.9792,
  "style_score": 0.5076188623161149,
  "label": "This looks like it may have been written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "0a313324-b194-4fea-a994-ff8fb0d8c869",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5228098330376612,
  "model_score": 0.6175,
  "style_score": 0.42811966607532237,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "c247095a-d07c-4896-8cec-b6897d829deb",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7191317022059183,
  "model_score": 0.7387,
  "style_score": 0.6995634044118364,
  "label": "This looks like it may have been written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "d1c1f957-1da0-4a07-a7b0-bdf30e97b098",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6974319507247555,
  "model_score": 0.8051,
  "style_score": 0.5897639014495111,
  "label": "This looks like it may have been written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "93f2ccaa-8b9f-45ee-843c-159718659631",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6872753757429472,
  "model_score": 0.8329,
  "style_score": 0.5416507514858944,
  "label": "This looks like it may have been written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "ab72aa0a-f8cf-42cc-80fa-2d33ffe7959c",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7271953361892067,
  "model_score": 0.8005,
  "style_score": 0.6538906723784136,
  "label": "This looks like it may have been written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "bffde296-3cb8-4f85-8ea7-c9822c022485",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6162225053547626,
  "model_score": 0.8814,
  "style_score": 0.3510450107095253,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "e23b1812-cdd1-4f43-8b94-9bbeb114707a",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.4839795271001922,
  "model_score": 0.8816,
  "style_score": 0.08635905420038437,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "2752e04c-9963-4520-8634-8bed9027f87b",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.39051706131736297,
  "model_score": 0.3223,
  "style_score": 0.4587341226347259,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "ea745390-e36c-4c36-936b-6a292999a216",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3170908786736941,
  "model_score": 0.4625,
  "style_score": 0.17168175734738822,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "7cede870-df69-4292-ad74-cf1136084d37",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.19480311461398947,
  "model_score": 0.2044,
  "style_score": 0.1852062292279789,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "dad6cd86-1575-4c60-809b-1259ccd54aa3",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5827413379078045,
  "model_score": 0.5943,
  "style_score": 0.5711826758156089,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "0e493610-60f2-4198-8632-ab81819f9b8c",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5019589721324589,
  "model_score": 0.4998,
  "style_score": 0.5041179442649177,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "5e961428-c8c9-4c9e-8f48-553bc814f91a",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5254221745056052,
  "model_score": 0.6401,
  "style_score": 0.4107443490112105,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "23444516-3632-4941-84ca-10832958ff82",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5007546172196485,
  "model_score": 0.5583,
  "style_score": 0.44320923443929705,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "514758f2-7872-4abe-bd93-5a7bfaea893f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "75e5efa4-0ae6-4b95-a278-147967dbca46",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "8af166ef-4bb7-44b4-b121-4121bf452fcc",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "3d5a05c0-f912-4b6b-a0f7-4da1f8543456",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "6f9d0c77-5f61-4202-be0e-fedae0981523",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "262e1be1-0bfe-47d5-82a9-46c03bc21299",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "85484860-7915-4f38-a256-3034f8a8064a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "0c828117-193a-4e56-862a-f0bb518b64f1",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "af99b901-fa26-4c4b-b70d-e0f88047f224",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "eb034a7c-9a8c-45d7-854e-3ef868680f3b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.26435,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

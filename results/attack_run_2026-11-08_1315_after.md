# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 13:15
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `5ceaa7cd-9790-47b1-91ed-b2cb2bb1f320` | unsure | 0.481 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `ec0b89c7-eaa1-49c5-9c67-8642fb5ae8ef` | human | 0.297 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `1fe2ad7f-936b-4829-80ab-73f87ada746b` | unsure | 0.556 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `d616b61b-37b2-4ae6-bc52-031c45ce131e` | ai | 0.697 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `98efab99-98bd-49af-b6b6-e7e8e87a1b02` | human | 0.239 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `2e3e6890-e74a-4761-ba46-646042c75ecc` | human | 0.286 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `a78f793e-7237-48d2-b4f5-5308af27de9c` | unsure | 0.543 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `ad5a352f-da82-46b1-ba1d-db25e17bf1fc` | unsure | 0.446 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `4cb33e0c-dab6-474e-8e9f-57af0fbf836b` | unsure | 0.560 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `e469ff28-9b43-4905-9d95-4a77592553cc` | ai | 0.743 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `2562c1c9-852e-4e67-822f-f53b90cce2e6` | unsure | 0.523 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `d5638e1e-dd5b-4365-a1ac-3550c9c02a08` | ai | 0.719 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `12bd833f-e736-4c45-a6fd-dc7d407297b0` | ai | 0.697 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `4060b392-cfe0-42a2-85f9-3def535251c2` | ai | 0.687 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `f832769e-8e30-4cd3-9cc5-6815010928ab` | ai | 0.727 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `ebc253f6-0698-49ac-b416-0d21db4f71a2` | unsure | 0.616 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `a79ed800-e915-4158-a0b2-ebac1524ae20` | unsure | 0.484 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `2b00617e-018f-430e-8b32-83f8c611cb36` | unsure | 0.391 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `7f0f8874-2cfc-4ed9-8977-8a5da2be651e` | human | 0.317 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `affd7463-ca9c-47a4-af13-057beecf8367` | human | 0.195 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `4379b8a3-d6c6-424b-beab-bf50ddc1f9db` | unsure | 0.583 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `de262723-835c-4685-978c-2964338f7c49` | unsure | 0.502 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `5fe47746-2603-4b20-8510-89b72c111352` | unsure | 0.525 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c6426b7e-32cf-4644-a5b6-01b9689c5447` | unsure | 0.501 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8188c27d-ee05-40d3-a590-e82692efd7ca` | human | 0.264 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bb731d89-de52-4659-ab72-ed4a0fe95721` | human | 0.264 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `64a07273-c068-4cbf-a3b9-42ceac54e95e` | human | 0.264 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `051a3d0c-8025-4e5d-a9aa-166fa1a665c9` | human | 0.264 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ef792141-4dad-4f6f-bc41-8545a5d5bc91` | human | 0.264 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `598fd30f-8d5c-4cf8-9027-21481f7923d0` | human | 0.264 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `61db2cfb-dfd0-4567-9df9-3ca5711ea606` | human | 0.264 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cabafbd0-5c93-4337-ba63-4a1ba67d26e9` | human | 0.264 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ffbd1eb8-f112-4939-b640-86327293fb18` | human | 0.264 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7e123bf1-a1aa-4d52-ab82-07cb924158bb` | human | 0.264 |  |
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
  "content_id": "5ceaa7cd-9790-47b1-91ed-b2cb2bb1f320",
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
  "content_id": "ec0b89c7-eaa1-49c5-9c67-8642fb5ae8ef",
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
  "content_id": "1fe2ad7f-936b-4829-80ab-73f87ada746b",
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
  "content_id": "d616b61b-37b2-4ae6-bc52-031c45ce131e",
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
  "content_id": "98efab99-98bd-49af-b6b6-e7e8e87a1b02",
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
  "content_id": "2e3e6890-e74a-4761-ba46-646042c75ecc",
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
  "content_id": "a78f793e-7237-48d2-b4f5-5308af27de9c",
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
  "content_id": "ad5a352f-da82-46b1-ba1d-db25e17bf1fc",
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
  "content_id": "4cb33e0c-dab6-474e-8e9f-57af0fbf836b",
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
  "content_id": "e469ff28-9b43-4905-9d95-4a77592553cc",
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
  "content_id": "2562c1c9-852e-4e67-822f-f53b90cce2e6",
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
  "content_id": "d5638e1e-dd5b-4365-a1ac-3550c9c02a08",
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
  "content_id": "12bd833f-e736-4c45-a6fd-dc7d407297b0",
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
  "content_id": "4060b392-cfe0-42a2-85f9-3def535251c2",
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
  "content_id": "f832769e-8e30-4cd3-9cc5-6815010928ab",
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
  "content_id": "ebc253f6-0698-49ac-b416-0d21db4f71a2",
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
  "content_id": "a79ed800-e915-4158-a0b2-ebac1524ae20",
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
  "content_id": "2b00617e-018f-430e-8b32-83f8c611cb36",
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
  "content_id": "7f0f8874-2cfc-4ed9-8977-8a5da2be651e",
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
  "content_id": "affd7463-ca9c-47a4-af13-057beecf8367",
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
  "content_id": "4379b8a3-d6c6-424b-beab-bf50ddc1f9db",
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
  "content_id": "de262723-835c-4685-978c-2964338f7c49",
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
  "content_id": "5fe47746-2603-4b20-8510-89b72c111352",
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
  "content_id": "c6426b7e-32cf-4644-a5b6-01b9689c5447",
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
  "content_id": "8188c27d-ee05-40d3-a590-e82692efd7ca",
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
  "content_id": "bb731d89-de52-4659-ab72-ed4a0fe95721",
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
  "content_id": "64a07273-c068-4cbf-a3b9-42ceac54e95e",
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
  "content_id": "051a3d0c-8025-4e5d-a9aa-166fa1a665c9",
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
  "content_id": "ef792141-4dad-4f6f-bc41-8545a5d5bc91",
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
  "content_id": "598fd30f-8d5c-4cf8-9027-21481f7923d0",
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
  "content_id": "61db2cfb-dfd0-4567-9df9-3ca5711ea606",
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
  "content_id": "cabafbd0-5c93-4337-ba63-4a1ba67d26e9",
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
  "content_id": "ffbd1eb8-f112-4939-b640-86327293fb18",
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
  "content_id": "7e123bf1-a1aa-4d52-ab82-07cb924158bb",
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

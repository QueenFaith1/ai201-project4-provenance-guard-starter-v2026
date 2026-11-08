# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 04:25
- Auto-marked BROKE (5xx, crash, no response): **2**
- Left for you to judge: **54**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `5573e210-8de2-480d-b219-49aa3b799ad4` | unsure | 0.481 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `f65ef490-dd1a-4115-a848-85c27ed025d6` | human | 0.297 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `eca0fd29-9900-4062-9122-96993968b529` | unsure | 0.556 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `ff0f8e2c-3e6c-4e97-904d-676cd42bf474` | ai | 0.697 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `4dd392ce-2531-442e-88af-ea611aa2d039` | human | 0.239 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `87ac5fc1-fc83-4e54-8d5d-6f76759526f6` | human | 0.286 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `be7ad117-3878-4273-80ce-ddb708d68891` | unsure | 0.543 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `34a5f528-483d-498f-a14a-f96fae211b93` | unsure | 0.446 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `481e7297-5aa0-43f9-b0fc-5c1848340760` | unsure | 0.560 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `daadca01-885a-4e41-a37f-95d00f574328` | ai | 0.743 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `9cd2303e-8d19-4ba7-8c7d-39555a1fc0a9` | unsure | 0.523 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `8c5d3c92-e020-4698-a8a9-288368e58304` | ai | 0.719 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c6fda6d3-7588-4908-baa2-54c4010af995` | ai | 0.697 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `375b87ec-d207-45a9-ad27-a052668bdc5e` | ai | 0.687 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `5e9f8ae0-572f-472b-a649-286db610fc07` | ai | 0.727 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `ae40b302-3525-4a1a-ad0e-50efbf4c70f9` | unsure | 0.616 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `8b9f35f1-16a2-43c4-a933-8029b5eb5576` | unsure | 0.484 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `4120355f-ea2d-4024-bfb5-8ccb0b0f6ce7` | unsure | 0.391 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `43aaa8ef-df60-4b4f-b0ac-c411ad50cf52` | human | 0.317 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `69b40bc1-bac8-493b-8004-83a08df974f4` | human | 0.195 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `46963341-919c-4005-8fb7-ca12a1c7806e` | unsure | 0.583 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `281204da-094c-44b4-a83f-a560a7f05473` | unsure | 0.502 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `44befd4a-87f9-4a58-bb99-389aeab80d6a` | unsure | 0.525 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `25b0409e-fb54-4e43-8a2b-95dad789514e` | unsure | 0.501 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `151d6901-890f-41af-b5e0-828967315b11` | human | 0.250 |  |
| MF04 | malformed | text is only punctuation | 200 | `3b640a9e-0ba7-4989-a67f-6670aac45e6e` | unsure | 0.506 |  |
| MF05 | malformed | text is a very long single word | 200 | `ecb0a09d-1323-43be-a0bd-06a8d3f0fe4e` | ai | 0.749 |  |
| MF06 | malformed | text is emoji only | 200 | `c9a3af40-b70e-48fb-8653-0ecc1184ae70` | ai | 0.748 |  |
| MF07 | malformed | text is right-to-left script | 200 | `8dabf650-f5dd-4a3a-830d-3f6cf3db507e` | ai | 0.703 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `07937cb0-b976-4db6-8899-a302c93f0b3b` | ai | 0.726 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b1cb4270-335f-4793-9ebc-5e48793c89fc` | human | 0.264 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `663856e6-8404-4175-8ba6-77bebee8607f` | human | 0.264 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cccdb02c-cd79-4ef7-b939-e99fe8bf0110` | human | 0.264 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9682a063-d53c-46df-b877-5c3c58169b1a` | human | 0.264 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c2e40384-45fa-4b29-a747-9afa697b0e04` | human | 0.264 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b0e44c6e-de24-4ea0-abcd-cad5ab265293` | human | 0.264 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `38eb271c-4289-48ba-a284-a02b6eefb483` | human | 0.264 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0b043cfb-53c0-4632-aac6-8ade2f20f114` | human | 0.264 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f414006f-b744-4340-8e6a-6404f0e169e0` | human | 0.264 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ed1dc895-378e-4fda-9301-61e3a03a69ca` | human | 0.264 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 2 | 18 |
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
  "content_id": "5573e210-8de2-480d-b219-49aa3b799ad4",
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
  "content_id": "f65ef490-dd1a-4115-a848-85c27ed025d6",
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
  "content_id": "eca0fd29-9900-4062-9122-96993968b529",
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
  "content_id": "ff0f8e2c-3e6c-4e97-904d-676cd42bf474",
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
  "content_id": "4dd392ce-2531-442e-88af-ea611aa2d039",
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
  "content_id": "87ac5fc1-fc83-4e54-8d5d-6f76759526f6",
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
  "content_id": "be7ad117-3878-4273-80ce-ddb708d68891",
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
  "content_id": "34a5f528-483d-498f-a14a-f96fae211b93",
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
  "content_id": "481e7297-5aa0-43f9-b0fc-5c1848340760",
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
  "content_id": "daadca01-885a-4e41-a37f-95d00f574328",
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
  "content_id": "9cd2303e-8d19-4ba7-8c7d-39555a1fc0a9",
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
  "content_id": "8c5d3c92-e020-4698-a8a9-288368e58304",
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
  "content_id": "c6fda6d3-7588-4908-baa2-54c4010af995",
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
  "content_id": "375b87ec-d207-45a9-ad27-a052668bdc5e",
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
  "content_id": "5e9f8ae0-572f-472b-a649-286db610fc07",
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
  "content_id": "ae40b302-3525-4a1a-ad0e-50efbf4c70f9",
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
  "content_id": "8b9f35f1-16a2-43c4-a933-8029b5eb5576",
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
  "content_id": "4120355f-ea2d-4024-bfb5-8ccb0b0f6ce7",
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
  "content_id": "43aaa8ef-df60-4b4f-b0ac-c411ad50cf52",
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
  "content_id": "69b40bc1-bac8-493b-8004-83a08df974f4",
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
  "content_id": "46963341-919c-4005-8fb7-ca12a1c7806e",
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
  "content_id": "281204da-094c-44b4-a83f-a560a7f05473",
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
  "content_id": "44befd4a-87f9-4a58-bb99-389aeab80d6a",
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
  "content_id": "25b0409e-fb54-4e43-8a2b-95dad789514e",
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
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the s",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "151d6901-890f-41af-b5e0-828967315b11",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.25,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "3b640a9e-0ba7-4989-a67f-6670aac45e6e",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5056,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't tell for sure whether a person or an AI wrote this. If you wrote it yourself, you can appeal and a person will take a look.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "ecb0a09d-1323-43be-a0bd-06a8d3f0fe4e",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7488,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "This looks like it may have been written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "c9a3af40-b70e-48fb-8653-0ecc1184ae70",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7484500000000001,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "This looks like it may have been written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "8dabf650-f5dd-4a3a-830d-3f6cf3db507e",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7032,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "This looks like it may have been written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "07937cb0-b976-4db6-8899-a302c93f0b3b",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.7261753628513019,
  "model_score": 0.9876,
  "style_score": 0.4647507257026039,
  "label": "This looks like it may have been written with an AI tool. If you wrote it yourself, you can appeal and a person will review it.",
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
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n<title>500 Internal Server Error</title>\n<h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the s",
  "verdict": "BROKE"
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
  "content_id": "b1cb4270-335f-4793-9ebc-5e48793c89fc",
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
  "content_id": "663856e6-8404-4175-8ba6-77bebee8607f",
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
  "content_id": "cccdb02c-cd79-4ef7-b939-e99fe8bf0110",
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
  "content_id": "9682a063-d53c-46df-b877-5c3c58169b1a",
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
  "content_id": "c2e40384-45fa-4b29-a747-9afa697b0e04",
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
  "content_id": "b0e44c6e-de24-4ea0-abcd-cad5ab265293",
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
  "content_id": "38eb271c-4289-48ba-a284-a02b6eefb483",
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
  "content_id": "0b043cfb-53c0-4632-aac6-8ade2f20f114",
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
  "content_id": "f414006f-b744-4340-8e6a-6404f0e169e0",
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
  "content_id": "ed1dc895-378e-4fda-9301-61e3a03a69ca",
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

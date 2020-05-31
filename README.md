Flair sentiment model:
```python
 Model config DistilBertConfig {
  "activation": "gelu",
  "architectures": [
    "DistilBertForMaskedLM"
  ],
  "attention_dropout": 0.1,
  "dim": 768,
  "dropout": 0.1,
  "hidden_dim": 3072,
  "initializer_range": 0.02,
  "max_position_embeddings": 512,
  "model_type": "distilbert",
  "n_heads": 12,
  "n_layers": 6,
  "pad_token_id": 0,
  "qa_dropout": 0.1,
  "seq_classif_dropout": 0.2,
  "sinusoidal_pos_embds": false,
  "tie_weights_": true,
  "vocab_size": 30522
}
```
__in terminal__:


twitterscraper "cuomo -chris" -bd 2020-02-15 -ed 2020-3-01 -o cuomofeb_part1.json

twitterscraper "cuomo -chris" -bd 2020-3-01 -ed 2020-3-15 -o cuomo_march_part1.json

twitterscraper "cuomo -chris" -bd 2020-3-15 -ed 2020-3-31 -o cuomo_march_part2.json



#doing with fixed one.

twitterscraper "cuomo -chris" -bd 2020-3-31 -ed 2020-4-15 -o cuomo_april_part2.json


#info about virus
On January 19, 2020, a 35-year-old man presented to an urgent care clinic in Snohomish County, Washington, with a 4-day history of cough and subjective fever.


jan15-31:
Found: 40188 tweets
Wrote: 4477 tweets

jan31-feb15:
Found: 49487 tweets
Wrote: 4943 tweets

feb-16-29
Found: 27079 tweets
Wrote: 3369 tweets

march-01-15
Found: 139582 tweets
Wrote: 9586 tweets

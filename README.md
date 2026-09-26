# Lightweight Entity Extractor

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)

Lightweight Entity Extractor pulls lightweight entities from text (emails, URLs, dates, and named lists).

## Quick start

```bash
python -m lightweight_entity_extractor.server --port 5173
```

Open http://localhost:5173

## API

- POST `/api/extract` `{ "text": "" }`


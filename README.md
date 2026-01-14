# EntityWeaver

EntityWeaver pulls lightweight entities from text (emails, URLs, dates, and named lists).

## Quick start

```bash
python -m app.server --port 5173
```

Open http://localhost:5173

## API

- POST `/api/extract` `{ "text": "" }`


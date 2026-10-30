# Magma Manager v1.0.1 Gemini Hotfix

This hotfix fixes `GenerateContentRequest.model: unexpected model name format`.

After installation, set:

```env
AI_PROVIDER=gemini
AI_MODEL=gemini-3.6-flash
AI_BASE_URL=
```

Then run in Discord:

1. `/ai reset-model`
2. `/ai model` with `gemini-3.6-flash`
3. `/ai test`

The bot accepts plain IDs, `models/...`, quoted values, and copied full Gemini REST endpoint URLs, and normalizes them to the model ID required by the native API.

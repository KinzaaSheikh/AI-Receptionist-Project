**Decision principle:** Prefer managed services and provider abstractions during MVP development. Avoid implementing infrastructure that does not contribute directly to validating the receptionist product.

Caller

  │

  │ Phone call

  ▼

Retell AI (Can be abstracted to different voice providers later)

  │

  │ Voice interaction

  ▼

AI Receptionist

  │

  ├── STT

  ├── LLM 

  └── TTS

  │

  ▼

FastAPI Backend

  │

  ├── Call Sessions

  ├── Agent Configuration

  ├── Business Configuration

  └── Scheduling

  │

  ▼

Supabase / PostgreSQL

| Component   | Initial choice              | Reason                                   |
| ----------- | --------------------------- | ---------------------------------------- |
| Language    | Python                      | Existing strength + AI ecosystem         |
| API         | FastAPI                     | Async + lightweight + familiar           |
| Database    | PostgreSQL                  | Strong relational model for scheduling   |
| DB platform | Supabase                    | Managed PostgreSQL + auth/storage/etc.   |
| Telephony   | Retell AI                   | Avoid telephony complexity initially     |
| STT         | Retell/provider abstraction | Avoid premature infrastructure           |
| TTS         | Retell/provider abstraction | Same                                     |
| LLM         | Gemini / cheap model        | Cost-efficient experimentation           |
| Cache       | None initially              | No demonstrated requirement              |
| Redis       | Deferred                    | Introduce only when workload requires it |
| Deployment  | TBD                         | Decide before integration deployment     |
| Logging     | Python structured logging   | Debug latency and call failures          |



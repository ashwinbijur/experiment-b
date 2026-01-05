Architecture Draft (v1)<br />
Components<br />
Frontend: Streamlit chat UI<br />
Backend: FastAPI<br />
Vector DB: Qdrant (local)<br />
LLM: OpenAI GPT‑4.1 or GPT‑4.1‑mini<br />
Embeddings: text-embedding-3-large<br />

Data: PSD2, SEPA SCT, EBA Guidelines<br />

Flow<br />
User enters question in Streamlit<br />
Streamlit sends request to FastAPI /ask<br />
FastAPI retrieves relevant chunks from Qdrant<br />
FastAPI constructs RAG prompt<br />
FastAPI calls OpenAI<br />
Response returned to Streamlit with citations<br />

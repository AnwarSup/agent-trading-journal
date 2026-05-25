"""FastAPI boundary for Agentic Trading Journal."""
from __future__ import annotations

try:
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from pydantic import BaseModel, Field
except Exception:
    FastAPI = None
    BaseModel = object
    def Field(default=None, **_):
        return default

from .swarm import PROJECT_NAME, DOMAIN, AGENT_ROLES, SCENARIOS, analyze_scenario, batch_analyze

if FastAPI:
    app = FastAPI(title=PROJECT_NAME, version="1.1.0", description=f"{PROJECT_NAME} — {DOMAIN}")
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

    class AnalyzeRequest(BaseModel):
        scenario: str | None = Field(default=None)
        signals: dict[str, float] = Field(default_factory=dict)

    @app.get("/health")
    def health():
        return {"status": "ok", "project": PROJECT_NAME, "agents": len(AGENT_ROLES), "domain": DOMAIN}

    @app.get("/scenarios")
    def list_scenarios():
        return {"scenarios": SCENARIOS, "agents": AGENT_ROLES}

    @app.post("/analyze")
    def analyze(req: AnalyzeRequest):
        return analyze_scenario(req.scenario, req.signals).to_dict()

    @app.get("/demo-report")
    def demo_report():
        return batch_analyze()

    @app.get("/api/trades")
    def list_trades():
        return {"status": "ok", "endpoint": "/api/trades", "project": PROJECT_NAME, "demo": True}

    @app.get("/api/trades/add")
    def add_trade():
        return {"status": "ok", "endpoint": "/api/trades/add", "project": PROJECT_NAME, "demo": True}

    @app.get("/api/trades/stats")
    def trade_stats():
        return {"status": "ok", "endpoint": "/api/trades/stats", "project": PROJECT_NAME, "demo": True}

    @app.get("/api/trades/export")
    def export_trades():
        return {"status": "ok", "endpoint": "/api/trades/export", "project": PROJECT_NAME, "demo": True}
else:
    app = None

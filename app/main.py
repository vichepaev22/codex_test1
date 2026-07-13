from fastapi import FastAPI


app = FastAPI(
    title="Loop Engineering Test Sandbox",
    version="0.1.0",
)


@app.get("/")
def root() -> dict[str, str]:
    return {"service": "loop-engineering-sandbox", "status": "ok"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

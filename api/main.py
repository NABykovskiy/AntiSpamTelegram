from fastapi import  FastAPI
from models import RootResponse
from routers import router

app = FastAPI()


@app.get("/", response_model=RootResponse)
async def read_root():
    return RootResponse(message="Murik Bot API is up and running")


app.include_router(router)


if __name__ == "__main__":  # для отладки
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8082)
from fastapi import Request, Response;
from time import time;


async def add_process_time_header(request: Request, call_next):
    start_time = time();
    response: Response = await call_next(request);
    elapsed_total_seconds: int = time() - start_time;
    print(f"Elapsed time: {elapsed_total_seconds} seconds.");
    response.headers["X-Process-Time"] = str(elapsed_total_seconds);
    return response;


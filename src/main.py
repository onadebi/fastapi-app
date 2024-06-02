from fastapi import FastAPI
from .middleware.process_time import add_process_time_header;
app = FastAPI()

app.middleware("http")(add_process_time_header);


if __name__ == "__main__":
    print(f"Running {__file__}...")
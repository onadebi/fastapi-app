from .controllers.home_controller import HomeController;
from .main import app;

homeRoutes = HomeController();

app.include_router(homeRoutes.router, prefix="/api", tags=["home"]);

if __name__ == "__main__":
    print(f"Running {__file__}...")
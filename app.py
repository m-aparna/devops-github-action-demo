from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Initialize the FastAPI app
app = FastAPI()
# Link the 'templates' folder for HTML rendering
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # Renders index.html and passes dynamic data (Context)
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "status": "Online", 
        "version": "2.0.0 (FastAPI)"
    })

@app.get("/health")
async def health_check():
    # Simple JSON endpoint for monitoring tools to check if app is alive
    return {"status": "healthy"}
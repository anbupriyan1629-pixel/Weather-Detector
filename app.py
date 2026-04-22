import os
import runpy

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    backend_app = os.path.join(current_dir, "backend", "app.py")
    runpy.run_path(backend_app, run_name="__main__")

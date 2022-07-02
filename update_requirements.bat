CALL .\venv\Scripts\activate.bat
pip list --format=freeze > requirements.txt
CALL .\venv\Scripts\deactivate.bat
PAUSE
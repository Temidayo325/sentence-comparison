FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/requirements.txt
# Fixed the path of the requirements.txt file

RUN pip install --no-cache-dir --upgrade -r requirements.txt
# Updated the path of the requirements.txt file

COPY comparisonApi /code/comparisonApi
# Removed the dot (.) from the source path

WORKDIR /code/comparisonApi/router
# Changed the working directory to /code/comparisonApi/router

CMD ["python", "main.py"]
# Using the correct Python file to run

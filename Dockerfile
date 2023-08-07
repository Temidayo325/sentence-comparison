FROM python:3.9
# 
WORKDIR /code
# 
COPY ./requirements.txt /code/requirements.txt
# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# 
COPY ./comparisonApi /code/comparisonApi
# 
CMD ["cd", "router"]
CMD ["python", "main.py"]
# CMD ["python", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
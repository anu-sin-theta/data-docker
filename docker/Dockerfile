FROM python:3.11
WORKDIR /docker
COPY tasty.py .
RUN pip install pyarrow
RUN pip install pandas
RUN pip install numpy
CMD ["python", "tasty.py"]


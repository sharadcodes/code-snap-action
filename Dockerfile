FROM python
COPY gen.py /gen.py
RUN chmod +x /gen.py
RUN  apt-get update \
  && apt-get install -y wkhtmltopdf \
  && pip install Pygments \
  && pip install imgkit
ENTRYPOINT ["python", "/gen.py"]

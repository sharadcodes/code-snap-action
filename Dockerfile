FROM python
COPY gen.sh /gen.py
RUN chmod +x /gen.py
RUN  apt-get update \
  && apt-get install -y wkhtmltopdf \
  && pip install Pygments
ENTRYPOINT ["python", "/gen.py"]

FROM python
RUN  apt-get update \
  && apt-get install -y wkhtmltopdf \
  && pip install Pygments
RUN chmod +x gen.py
ENTRYPOINT ["python", "gen.py"]

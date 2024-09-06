FROM python:3.10-slim-bookworm
ENV PYTHONUNBUFFERED=1
ENV PYTHONPYCACHEPREFIX=/cache/cpython/

WORKDIR /app
COPY . /app/
RUN --mount=type=cache,mode=0755,target=/root/.cache pip install -r requirements.txt
RUN chmod +x ./entrypoint.sh
EXPOSE 5000
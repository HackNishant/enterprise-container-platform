# Stage 1: Build dependencies & patch system libraries
FROM python:3.11-slim AS builder
WORKDIR /app

# Upgrade system packages to pull down the CVE patches (like libssl3 and python3.11-minimal fixes)
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Secure Runtime
# Using the specific latest tag to catch recent Debian 12 patches automatically
FROM gcr.io/distroless/python3-debian12:latest
WORKDIR /app

# Copy system libraries patched in Stage 1 if necessary, or let distroless:latest handle it
COPY --from=builder /root/.local /root/.local
COPY app.py .

ENV PATH=/root/.local/bin:$PATH
EXPOSE 8080

CMD ["app.py"]
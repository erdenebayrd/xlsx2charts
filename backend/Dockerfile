FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create static directory
RUN mkdir static

# Copy backend code
COPY . .

# Copy frontend build files
COPY --from=frontend-build /app/build /app/static

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 
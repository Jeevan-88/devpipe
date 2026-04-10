# DevPipe — Cloud-Native DevSecOps Pipeline

A production-grade DevSecOps pipeline built with Docker, AWS and GitHub Actions.

## Tech Stack
- Python Flask (Backend API)
- Docker (Containerization)
- AWS EC2 (Deployment)
- GitHub Actions (CI/CD)

## Run Locally
```bash
docker pull jeevan4488/devpipe-backend:v1
docker run -p 5000:5000 jeevan4488/devpipe-backend:v1
```

## API Endpoints
- `GET /` - API status
- `GET /health` - Health check

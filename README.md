# Django REST Enterprise

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![Docker](https://img.shields.io/badge/Docker-enabled-lightgrey)

**Django REST Enterprise** is a ready-to-use, modular template for Django REST Framework projects with a clean architecture. It is designed for scalable, maintainable, and production-ready applications.

---

## 🔹 Key Features

- **Clean / Layered Architecture**: domain, application, infrastructure, presentation
- **Modular Design**: independent modules (`users`, `authentication`) that are easily extendable
- **Multi-database Support**: primary and analytics databases
- **Multi-client**: multi client & feature flag system via a single `features.yaml` file
- **Docker-ready**: PostgreSQL, Redis, and other services are containerized
- **DRF + Modular APIs**: each module provides its own API endpoints
- **Testing Included**: Unit and API tests for each module
- **Production-ready**: environment variables, Docker, migrations, and seeds ready to use

---
## Game-Changing Feature: Multi-Client & Feature Flags

**Build once. Deliver to 100 clients with different requirements – without changing a single line of code.**

Just create one `features.yaml` file per client and mount it as a Docker volume.

### Example: `config/features-client-xyz.yaml`

```yaml
enabled_modules:
  - modules.users
  - modules.authentication
  - modules.products
  - modules.cart
  - modules.orders
  # - modules.payment          # disabled for this client
  - modules.shipping
  - modules.notifications

enabled_features:
  - celery
  - redis_cache
  - drf_spectacular
  # - sentry
  # - debug_toolbar
```

## 🔹 Getting Started (How to Get It)

1. **Clone the repository:**

```bash
git clone https://github.com/vahiddev7/django-rest-enterprise.git
cd django-rest-enterprise
pip install cookiecutter
cookiecutter path/to/django-rest-enterprise
```

or

2. **Use directly:**

```bash
pip install cookiecutter
cookiecutter https://github.com/vahiddev7/django-rest-enterprise.git
```

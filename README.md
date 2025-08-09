# Dynamic Orchestrator

A minimal, contract-driven orchestrator service built with Django REST Framework that dynamically validates incoming requests against JSON schemas representing microservice contracts.

---

## Overview

This project demonstrates a **fully dynamic orchestration** approach where:

- Input contracts (schemas) for microservices are stored as JSON files (or can be fetched remotely).
- DRF serializers are generated dynamically at runtime from these JSON schemas.
- Orchestrator validates requests against the relevant schema without any hardcoded serializers.
- Designed for saga-based orchestration across microservices with loose coupling and flexibility.

---

## Features

- Dynamic serializer generation from JSON schema definitions
- Flexible contract loading (local files or remote HTTP endpoint)
- Simple API endpoint to validate and forward requests dynamically per microservice
- Lightweight and extensible foundation to build complex orchestration logic

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository

```bash
git clone https://github.com/farzinsh7/dynamic-orchestrator.git
cd dynamic-orchestrator

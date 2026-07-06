# OODO Platform

<p align="center">

<img src="docs/assets/logo.png" width="180"/>

</p>

> **An AI-first modular ERP platform built on Odoo 18.**

OODO is a personal learning and development project focused on understanding the internals of **Odoo 18**, modern ERP architecture, Docker deployment, AI integration, and enterprise software engineering.

The long-term vision is to build a fully modular ERP platform that combines traditional business management with AI-powered automation.

---

# Project Goals

- Learn Odoo 18 development from the ground up
- Build production-quality custom modules
- Design a scalable ERP architecture
- Integrate AI into everyday business workflows
- Learn Git, GitHub, Docker and DevOps best practices
- Maintain clean, modular and reusable code

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Odoo 18 | ERP Framework |
| PostgreSQL 16 | Database |
| Docker & Docker Compose | Containerization |
| Python | Backend Development |
| XML | Views & UI |
| Git & GitHub | Version Control |
| VS Code | Development Environment |
| Windows 11 + Docker Desktop | Host Environment |

---

# Current Architecture

```
OODO Platform
│
├── oodo_base
│   ├── Platform foundation
│   ├── Root menu
│   ├── Shared UI
│   ├── Security
│   └── Common assets
│
├── oodo_core
│   ├── Shared Python logic
│   ├── Utilities
│   ├── Mixins
│   ├── Common services
│   └── Future AI integrations
│
├── oodo_hr
│
├── oodo_inventory
│
├── oodo_ai
│
└── oodo_whatsapp
```

---

# Repository Structure

```
oodo_platform/
│
├── addons/
│   ├── custom/
│   │   ├── oodo_base/
│   │   ├── oodo_core/
│   │   ├── oodo_hr/
│   │   ├── oodo_inventory/
│   │   ├── oodo_ai/
│   │   └── oodo_whatsapp/
│   │
│   └── third_party/
│
├── backups/
├── config/
├── logs/
├── postgres-data/
├── odoo-data/
│
├── compose.yaml
├── .env
└── .gitignore
```

---

# Current Features

## Platform

- Dockerized deployment
- PostgreSQL database
- Odoo 18
- Custom addon support
- Modular architecture

---

## HR Module

- Custom OODO HR application
- Employee Directory
- Reuses Odoo's built-in HR models
- Modular menu integration

---

## Planned Modules

- HR
- Inventory
- CRM
- AI Assistant
- WhatsApp Integration
- Knowledge Base
- Document Management
- Workflow Automation
- Dashboard
- Reporting
- Notifications

---

# Development Workflow

```
Create Feature
        ↓
Create Git Branch
        ↓
Develop
        ↓
Test
        ↓
Commit
        ↓
Push
        ↓
Merge into main
```

---

# Branch Strategy

```
main
│
├── feature/hr
├── feature/inventory
├── feature/ai
├── feature/whatsapp
├── feature/dashboard
└── feature/core
```

---

# Running the Project

## Clone

```bash
git clone https://github.com/Shreyas1860/oodo_platform.git
cd oodo_platform
```

## Configure

Create a local environment file:

```bash
cp .env.example .env
```

Update the database credentials and other environment variables as needed.

## Start

```bash
docker compose up -d
```

## Stop

```bash
docker compose down
```

---

# Development

Whenever a module changes:

```bash
docker exec -it odoo18 odoo \
-u <module_name> \
-d odoo18_dev \
--stop-after-init
```

Restart:

```bash
docker compose restart
```

---

# Project Roadmap

## Phase 1

- [x] Docker Environment
- [x] PostgreSQL
- [x] Odoo 18
- [x] GitHub Repository
- [x] Modular Architecture

---

## Phase 2

- [x] OODO Base Module
- [x] HR Module
- [x] Employee Directory

---

## Phase 3

- [ ] Employee Management
- [ ] Attendance
- [ ] Leave Management
- [ ] Payroll Extensions
- [ ] Recruitment

---

## Phase 4

- [ ] AI Assistant
- [ ] Ollama Integration
- [ ] Knowledge Base
- [ ] AI Chat
- [ ] Smart Workflows

---

## Phase 5

- [ ] Inventory
- [ ] CRM
- [ ] Finance
- [ ] Reporting
- [ ] Analytics

---

# Design Principles

- Modular architecture
- Reusable components
- Clean code
- AI-first design
- Docker-native deployment
- Enterprise-ready structure
- Scalable development
- Version controlled from day one

---

# Learning Objectives

This repository documents my journey of learning:

- Odoo 18 Development
- ERP Architecture
- Python Backend Development
- XML View Development
- PostgreSQL
- Docker
- Git & GitHub
- Enterprise Software Engineering
- AI Integration

---

# License

This project is released under the **LGPL-3 License**.

---

# Author

**Shreyas B S**

GitHub:
https://github.com/Shreyas1860

---

> **OODO isn't just another ERP customization project.**
>
> It is an attempt to build a modern, AI-powered, modular ERP platform while documenting the complete engineering journey from first principles.

## Overview

This component provides the Continuous Integration (CI) layer of the QA Intelligence Lab platform.
It enables automated execution of resilience tests using Jenkins running inside Docker, orchestrating the execution of the Cypress-based testing framework.
The CI pipeline allows the project to simulate a real-world DevOps environment, where automated tests validate system behavior under controlled failure conditions.

## Architecture

The CI system is built using the following technologies:

- Jenkins (LTS) — CI orchestration
- Docker — containerized Jenkins environment
- Node.js — runtime for test execution
- Cypress — automated resilience testing framework

Jenkins runs inside a Docker container and executes Cypress tests against the Resilience Testing Microservice.

## Dockerized Jenkins Setup

Jenkins is deployed using a custom Docker image that includes the dependencies required to execute Cypress tests.

The image is built using the following Dockerfile:

docker/Dockerfile.jenkins

## Jenkins Dockerfile

This Dockerfile extends the official Jenkins image and installs the required dependencies to run Node.js and Cypress tests.

FROM jenkins/jenkins:lts

USER root

# Install Node.js
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean

# Install dependencies required by Cypress
RUN apt-get install -y \
    libgtk2.0-0 \
    libgtk-3-0 \
    libgbm-dev \
    libnotify-dev \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    libasound2 \
    libxtst6 \
    xauth \
    xvfb

USER jenkins

These libraries are required because Cypress relies on several system-level graphical dependencies, even when running in headless mode.

## Building the Jenkins Image

To build the custom Jenkins image:
    docker build -t jenkins-docker -f docker/Dockerfile.jenkins

## Running the Jenkins Container

The Jenkins container can be started with the following command:

docker run -d \
  --name jenkins \
  -u root \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /Users/cristiannadj/Desktop/crisArch/ProgrammingStuff/Thesis/QAIntelligenceLab:/workspace \
  jenkins-docker

## Accessing Jenkins

Once the container is running, Jenkins can be accessed at:

    http://localhost:8080

During the first startup Jenkins will request the initial administrator password, which can be retrieved from the container logs:

    docker logs jenkins
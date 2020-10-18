---
layout: post
title:  Github Actions
comments: true
categories: [Devops, Github, Docker]
permalink: /github-actions/
excerpt: Github Actions enables you to create custom software development lifecycle workflows directly in your Github repository. These workflows are made out of different tasks so-called actions that can be run automatically on certain events.
---

- What is Github Actions?
- Developer workflow **Use cases**
- Github **Events** & **Actions**
- CI/CD Pipeline with Github Actions
    - Benifits of Github Actions CI/CD
    - Syntax

Github Actions enables you to create custom software development lifecycle workflows directly in your Github repository. These workflows are made out of different tasks so-called actions that can be run automatically on certain events.

This enables you to include Continues Integration (CI) and continuous deployment (CD) capabilities and many other features directly in your repository.

**Build into Github**

Github Actions is fully integrated into Github and therefore doesn't require and external site. This means that it can be managed in the same place as all your other repository related features like pull requests and issues

**Multi-container testing**

Actions allow you to test multi-container setups by adding support for Docker and docker-compose files to your workflow

**Multiple CI Templates**

Github provides multiple templates for all kinds of CI (Continous Integration) configurations which make it extremely easy to get started. You can also create your own templates which you can then publish as an Action on the Github Marketplace.

## Core Concepts

**Actions**

Actions are the smallest portable building block of a workflow and can be combined as steps to create a job. You can create your own Actions or use publicly shared Actions from the Marketplace.

**Events**

Events are specific activities that trigger a workflow run. For example, a workflow is triggered when somebody pushes to the repository or when a pull request is created. Events can also be configured to listen to external events using Webhooks.

**Runner**

A runner is a machine with the Github Actions runner application installed. Then runner waits for available jobs it can then execute. After picking up a job they run the job's actions and report the progress and results back to Github. Runners can be hosted on Github or self-hosted on your own machines/servers.

**Job**

A job is made up of multiple steps and runs in an instance of the virtual environment. Jobs can run independently of each other or sequential if the current job depends on the previous job to be successful.

**Step**

A step is a set of tasks that can be executed by a job. Steps can run commands or actions.

**Workflow**

A Workflow is an automated process that is made up of one or multiple jobs and can be triggered by an event. Workflows are defined using a YAML file in the .github/workflows directory.

### K8stest project

<script src="https://gist-it.appspot.com/https://github.com/prakashdale/k8stest/raw/master/.github/workflows/dotnet-core.yml?footer=0"></script>


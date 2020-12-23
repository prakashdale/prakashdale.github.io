---
layout: post
title: Kubernetes
comments: true
categories: [devops, kubernetes, docker, container]
permalink: /kubernetes/
excerpt: Kubernetes, the open source containerization platform
---

## What is Kubernetes?

Kubernetes is a portable, extensible, open-source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation.

### Container deployment era

Containers are similar to VMs, but they have relaxed isolation properties to shre the Operating System (OS) among the applications. Therefore, containers are considered lightweight. Similar to VM, a container has its own filesystem, share of CPU, memory, process space, and more. As they are decoupled from the underlying infrastructure, they are portable across clouds and OS distributions.

### Container benefits

- Agile application creation and deployment: increased ease and efficiency of container image creation compared to VM image use.
- Contineous development, integration, and deployment: provides for reliable and frequent container image build and deployment with quick and easy rollbacks (due to image immutability).
- Dev andOps separation of concerns: create application contain images at build/release time rather than deployment time, thereby decoupling applications from infrastructure.
Observability not only surfaces OS-level information and metrics, but application health and other signals.
- Environmental consistency across development, testing, and production: Runs the same on a laptop as it does in the cloud.
- Cloud and OS distibution portability: Runs on Ubuntu, RHEL, CoreOS, on-premise, on major public clouds, and anywhere else.
- Application-centric management: Raises the level of abstraction from running an OS on virtual hardware to running an application on an OS using logical reources.
- Loosely coupled, distributed, elastic, liberated micro-services: applications are broken into smaller, independent pieces and can be deployed and managed dynamically - not a monolithic stack running on one big single-purpose machine.
- Resource isolation: predictable application performance.
- Resource utilization: high efficiency and density.

### Kubernetes benefits

- **Service discovery and load balancing** Kubernetes can expose a container using the DNS name or using their own IP address. If traffic to a container is high, Kubernetes is able to load balance and distribute the network traffic so that the deployment is stable.
- **Storage orchastration** Kubernetes allows you to automatically mount a storage system of your choice such as local storage, public cloud providers, and more.
- **Automated rollouts and rollbacks** you can desribe the desired state for your deployed containers using Kubernetes, and it can change the actual state to the desired state at a controlled rate. For exampled, you can automate Kubernetes to create new containers for your deployment, remove existing containers and adopt all their resources to the new container.
- **Automatic bin packing** You provide Kubernetes with a cluster of nodes that it can use to run containerized tasks. You tell Kubernetes how much CPU and memory (RAM) each container needs. Kubernetes can fit containers onto your nodes to make the best use of your resources.
- **Self-healing** Kubernetes restarts containers that fail, replaces containers, kills containers that don't respond to your user-defined health check, and doesn't advertise them to the clients until they are ready to serve.
- **Secret and configuration management** Kubernetes lets you store and manage sensitive information, such as passwords, OAuth tokens, and SSH keys. You can deploy and update secrets and application configuration without rebuilding the container images, and without exposing secrets in your stack configuration.

### What Kubernetes is not

Kubernetes:
- Does not limit the types of applications supported. Kubernetes aims to support an extemely diverse variety of workloads, including stateless, stateful, and data-processing workloads, If an application run in a container, it should run great on Kubernetes.
- Does not deploy source code and does not build your application. Contineous integration, Delivery, and Deployment (CI/CD) workflows are determined by organization culture and preferences as well as technical requirements.
- Does not provide application-level services, such as middleware (for example, message buses), data processing frameworks (for example, Spark), databases (for example, MySQL), caches, nor cluster storage systems (for example, Ceph) as build-in services. Such components can run on Kubernetes, and/or can be accessed by applications running on Kubernetes through portable mechanisms, such as the *Open Service Broker*.
- Does not dictate logging, monitoring, or alerting solutions. It provides integrations as proof of concept, and mechanisms to collect and export metrics.
- Does not provide nor mandate a configuration language/system.
- Does not provide nor adopt any comprehensive machine configuration, maintenance, management, or self-healing systems.
- Additionally, Kubernetes is not a mere orchastration system, In fact, it eliminates the need for orchestration. The technical definition of orchestration is execution of a defined workflow: first do A, then B, then C. In contrast, Kubernetes comprises a set of independent, composable control processes that contineously drive the current state towards the provided desired state, It shouldn't matter hou you get from A to C. Centralized control is also not requirement. This results in a system that is easier to use and more powerful, robust, resilient, and extensible.

## Kubernetes Components

When you deploy Kubernetes, you get a cluster.

A Kubernetes cluster consists of a set of worker machines, called *nodes*, that run containerized applications. Every cluster has at least one worker node.

The worker node(s) host the *Pods* that are the components of the application workload. The *control plane* manages the worker nodes and the Pods in the cluster. In production environments, the control plane usually runs across multiple computers and a cluster usually runs multiple nodes, providing fault-tolerance and high availability.

- Pod
- Service
- Ingress
- ConfigMap
- Secretes
- Volumes
- Deployment
- StatefulSet

## Setup

Kubernetes UI token:
eyJhbGciOiJSUzI1NiIsImtpZCI6IjA4RjU3VHhzLUp1S19SMHRaWnNzRzZjZDlHUXZNRm41bXlhci1MVVd5MG8ifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXRva2VuLXI0cWI2Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIxMmZlMjkzYS1iNzM0LTRiOWMtOWFiYy02YzBkM2U1ZDQ4ODciLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZXJuZXRlcy1kYXNoYm9hcmQ6YWRtaW4tdXNlciJ9.BT4-IetrzFKAsNDIc3EQFaL5BLbQkLLwEQ66oPBxQpUj4aQTnggaGGIHDnAeoGgXGfbMMJZcJNYn36PKkYQarjU_QXfI3s-IOjQ6YEAQpfLflPFJn--DAmKfQISU97YqOar4AAoPAwUo5EiHFPYAP8-tiAxshyD4T-F4hhOhJ0iu72YaUnbIP-cqXExqdW_edhTtcgJm-ZSvUzKYv87mSlWzMdX2QRZF7YjhbIRjRqaDY5F7EDWXM6piXd0OFKuP1J1Opdx9ezQUhUwCWI2pixiou5F-ua_lKwc8xnTQSUetcBr57jRKBOw5CoxSMBDDVkYyoH56lXMUNHhmfrdr_A

`kubectl create deployment nginx-deployment --image=nginx`

`kubectl get deployment`

`kubectl get pod`

`kubectl get replicaset`

`kubectl edit deployment nginx-deployment`

`kubectl create deployment mongo-deployment --image=mongo`

`kubectl delete deployment mongo-deployment`

`kubectl delete deployment nginx-deployment`

<script src="https://gist-it.appspot.com/https://github.com/prakashdale/prakashdale.github.io/raw/master/src/kubernetes/nginx-deployment.yaml?footer=0"></script>




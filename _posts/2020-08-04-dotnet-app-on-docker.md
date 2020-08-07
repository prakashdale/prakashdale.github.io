---
layout: post
title:  Run ASP.NET Core 3.1 Apps in Docker with HTTPS.
comments: true
categories: [Dotnet]
excerpt: Package your ASP.NET Core app as a Docker Image and then run your image as a Docker container with HTTPS Enabled. This includes creating a dedicated self-signed development certificate, configuring user secrets and passing in the necessary environment variables to the container to enable HTTPS. We further configure this with Docker Compose for ease of use and reuse going forward.

---

## What is Docker?
Docker is a **containerization** platform, meaning that it enables you to **package, (build)**, your applications into **images**, and run them as **containers** on any platform that can run *Docker*.

## DotNet web api
Get the sample webapi project from the [Github repository](https://github.com/prakashdale/k8stest)

`dotnet run` to run the project.

If you run into any certificate issue then run following:

`dotnet dev-certs https --trust`

![Manage User Certificates](/assets/misc/manage-user-certificates.png "Manage user certificates")

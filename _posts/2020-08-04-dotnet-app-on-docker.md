---
layout: post
title:  Run ASP.NET Core 3.1 Apps in Docker with HTTPS.
comments: true
categories: [Dotnet, Docker]
excerpt: Package your ASP.NET Core app as a Docker Image and then run your image as a Docker container with HTTPS Enabled. This includes creating a dedicated self-signed development certificate, configuring user secrets and passing in the necessary environment variables to the container to enable HTTPS. We further configure this with Docker Compose for ease of use and reuse going forward.

---

## What is Docker?
Docker is a **containerization** platform, meaning that it enables you to **package, (build)**, your applications into **images**, and run them as **containers** on any platform that can run *Docker*.

## DotNet web api
Get the sample webapi project from the [Github repository](https://github.com/prakashdale/prakashdale.github.io/tree/master/src/dotnet-app-on-docker)

`dotnet run` to run the project.

If you run into any certificate issue then run following:

`dotnet dev-certs https --trust`

![Manage User Certificates](/assets/misc/manage-user-certificates.png "Manage user certificates")

**Run command on powershell to generate dev certificate**

`dotnet dev-certs https -ep $env:USERPROFILE\.aspnet\https\weatherapp.pfx -p pa55w0rd!`

**Add UserSecretsId in .csproj file**

Update .csproj file with `<UserSecretsId>2cc80554-4f6f-47c9-812c-9288aa2f1bdf</UserSecretsId>` so that it looks like below:

```
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>netcoreapp3.1</TargetFramework>
    <UserSecretsId>2cc80554-4f6f-47c9-812c-9288aa2f1bdf</UserSecretsId>
  </PropertyGroup>


</Project>

```

**Create UserSecrets file**

Run command `dotnet user-secrets set "Kestrel:Certificates:Development:Password" "pa55w0rd!"` from project folder.

**Build docker image**

Build Image using command `docker build -t prakashdale/weatherapp .`

**Run docker container**

`docker run -p 8080:80 -p 8081:443 -e ASPNETCORE_URLS="https://+;http://+" -e ASPNETCORE_HTTPS_PORT=8081 -e ASPNETCORE_ENVIRONMENT=Development -v C:\Users\admin\AppData\Roaming\Microsoft\UserSecrets:/root/.microsoft/usersecrets -v $env:USERPROFILE\.aspnet\https:/root/.aspnet/https/ prakashdale/weatherapp`

Browse to [http://localhost:8080](http://localhost:8080)

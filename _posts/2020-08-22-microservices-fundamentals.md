---
layout: post
title:  Microservices.Net Fundamentals
comments: true
categories: [Dotnet, C#, Microservices]
excerpt: A comprehensive introduction into the modern microservices architecture based on the most popular technologies such as .NET Core, Docker, Kubernetes, Istio Service Mesh and many more.
---
## What is Microservice?

Microservices - also known as the microservice architecture - is an architectural style that structures an application as a collection of services that are 
- Hightly maintainable and testable
- Loosely coupled
- Independently deployable
- Organized around business capabilities
- Owned by a small team

![Monolith vs Microservices Architecture](/assets/microservices/monolithvsmicroservices.jpg "Monolith vs Microservices Architecture")

![Monolith vs Microservices Architecture](/assets/microservices/monolithvsmicroservices2.jpg "Monolith vs Microservices Architecture")

What’s the difference between monolith and microservices? 

What are the most demanding challenges of distributed systems? 

How to avoid the distributed monolith?

## Modular Monolith

What’s the modular monolith all about? 

What are modules and how can they communicate with each other? Will the modular monolith help avoiding the distributed monolith trap?


Clone Convey repository

```
mkdir snatch-dev
cd snatch-dev
git clone https://github.com/snatch-dev/Convey.git
cd Convey/
dotnet restore
```

Go back to git folder

```
cd ..
cd ..
```
Clone Pacco repository

```
mkdir devmentors
cd devmentors
git clone https://github.com/devmentors/Pacco.git
cp ./Pacco/scripts/git-clone.sh ./git-clone.sh
./git-clone.sh
```

Confirm that projects build

```
cd pacco
dotnet restore
dotnet build
```

Run infrastructure components

```
cd compose
docker-compose -f infrastructure.yml up -d
```

Create Project

```
mkdir sanstha
cd sanstha
dotnet new sln -n Sanstha -o ./src
cd ./src
dotnet new webapi -n Sanstha.Api -o ./Sanstha.Api -f netcoreapp3.1
dotnet sln add ./Sanstha.Api/Sanstha.Api.csproj
```

Add *Convey* references

```
dotnet add ./Sanstha.Api/Sanstha.Api.csproj reference ../../../snatch-dev/Convey/src/Convey/src/Convey/Convey.csproj
dotnet add ./Sanstha.Api/sanstha.Api.csproj reference ../../../snatch-dev/Convey/src/Convey.Logging/src/Convey.Logging/Convey.Logging.csproj
dotnet add ./Sanstha.Api/sanstha.Api.csproj reference ../../../snatch-dev/Convey/src/Convey.WebApi/src/Convey.WebApi/Convey.WebApi.csproj
dotnet add ./Sanstha.Api/sanstha.Api.csproj reference ../../../snatch-dev/Convey/src/Convey.WebApi.CQRS/src/Convey.WebApi.CQRS/Convey.WebApi.CQRS.csproj

```

Create *Core* project

```
dotnet new classlib -n Sanstha.Core -o ./Sanstha.Core -f netcoreapp3.1
dotnet sln add ./Sanstha.Core/Sanstha.Core.csproj
dotnet add ./Sanstha.Core/Sanstha.Core.csproj reference ../../MS.Common/src/MS.Common.Core/MS.Common.Core.csproj
cd Sanstha.Core
rm Class1.cs
mkdir Entities

cd ..

```

Create *Application* project

```
dotnet new classlib -n Sanstha.Application -o ./Sanstha.Application  -f netcoreapp3.1
dotnet sln add ./Sanstha.Application/Sanstha.Application.csproj
dotnet add ./Sanstha.Application/Sanstha.Application.csproj reference ./Sanstha.Core/Sanstha.Core.csproj
dotnet add ./Sanstha.Application/Sanstha.Application.csproj package Microsoft.Extensions.Logging -v 3.1.3
```

Add *Convey* reference to *Application* project

```
dotnet add ./Sanstha.Application/Sanstha.Application.csproj reference ../../../snatch-dev/Convey/src/Convey/src/Convey/Convey.csproj
dotnet add ./Sanstha.Application/Sanstha.Application.csproj reference ../../../snatch-dev/Convey/src/Convey.CQRS.Commands/src/Convey.CQRS.Commands/Convey.CQRS.Commands.csproj
dotnet add ./Sanstha.Application/Sanstha.Application.csproj reference ../../../snatch-dev/Convey/src/Convey.CQRS.Events/src/Convey.CQRS.Events/Convey.CQRS.Events.csproj
dotnet add ./Sanstha.Application/Sanstha.Application.csproj reference ../../../snatch-dev/Convey/src/Convey.CQRS.Queries/src/Convey.CQRS.Queries/Convey.CQRS.Queries.csproj
dotnet add ./Sanstha.Application/Sanstha.Application.csproj reference ../../../snatch-dev/Convey/src/Convey.MessageBrokers/src/Convey.MessageBrokers/Convey.MessageBrokers.csproj

```

Create *Infrastructure* project

```
dotnet new classlib -n Sanstha.Infrastructure -o ./Sanstha.Infrastructure  -f netcoreapp3.1
dotnet sln add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ./Sanstha.Core/Sanstha.Core.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ./Sanstha.Application/Sanstha.Application.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj package Microsoft.Extensions.Logging -v 3.1.3

dotnet add ./Sanstha.Api/Sanstha.Api.csproj reference ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj
```

Add *Convey* reference to *Application* project

```
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey/src/Convey/Convey.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.Secrets.Vault/src/Convey.Secrets.Vault/Convey.Secrets.Vault.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.CQRS.Queries/src/Convey.CQRS.Queries/Convey.CQRS.Queries.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.Discovery.Consul/src/Convey.Discovery.Consul/Convey.Discovery.Consul.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.LoadBalancing.Fabio/src/Convey.LoadBalancing.Fabio/Convey.LoadBalancing.Fabio.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.HTTP/src/Convey.HTTP/Convey.HTTP.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.Logging/src/Convey.Logging/Convey.Logging.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.Logging.CQRS/src/Convey.Logging.CQRS/Convey.Logging.CQRS.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.MessageBrokers/src/Convey.MessageBrokers/Convey.MessageBrokers.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.MessageBrokers.CQRS/src/Convey.MessageBrokers.CQRS/Convey.MessageBrokers.CQRS.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.MessageBrokers.Outbox/src/Convey.MessageBrokers.Outbox/Convey.MessageBrokers.Outbox.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.MessageBrokers.Outbox.Mongo/src/Convey.MessageBrokers.Outbox.Mongo/Convey.MessageBrokers.Outbox.Mongo.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.MessageBrokers.RabbitMQ/src/Convey.MessageBrokers.RabbitMQ/Convey.MessageBrokers.RabbitMQ.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.Metrics.AppMetrics/src/Convey.Metrics.AppMetrics/Convey.Metrics.AppMetrics.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.Persistence.MongoDB/src/Convey.Persistence.MongoDB/Convey.Persistence.MongoDB.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.Persistence.Redis/src/Convey.Persistence.Redis/Convey.Persistence.Redis.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.Security/src/Convey.Security/Convey.Security.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.Tracing.Jaeger/src/Convey.Tracing.Jaeger/Convey.Tracing.Jaeger.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.Tracing.Jaeger.RabbitMQ/src/Convey.Tracing.Jaeger.RabbitMQ/Convey.Tracing.Jaeger.RabbitMQ.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.WebApi.CQRS/src/Convey.WebApi.CQRS/Convey.WebApi.CQRS.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.WebApi.Security/src/Convey.WebApi.Security/Convey.WebApi.Security.csproj
dotnet add ./Sanstha.Infrastructure/Sanstha.Infrastructure.csproj reference ../../../snatch-dev/Convey/src/Convey.WebApi.Swagger/src/Convey.WebApi.Swagger/Convey.WebApi.Swagger.csproj

```




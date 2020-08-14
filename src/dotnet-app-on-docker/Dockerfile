FROM mcr.microsoft.com/dotnet/core/aspnet:3.1 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["weatherapp.csproj", "./"]
RUN dotnet restore "./weatherapp.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "weatherapp.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "weatherapp.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "weatherapp.dll"]

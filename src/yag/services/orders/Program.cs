using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace orders
{
    public class Program
    {
        public static Task Main(string[] args)
        => CreateHostBuilder(args).Build().RunAsync();

    public static IHostBuilder CreateHostBuilder(string[] args) =>
        Host.CreateDefaultBuilder(args)
            .ConfigureWebHostDefaults(webBuilder => webBuilder.Configure(app =>
            {
                app.UseRouting();
                app.UseEndpoints(endpoints =>
                {
                    endpoints.MapGet("", ctx => ctx.Response.WriteAsync("orders service"));
                    endpoints.MapGet("orders", ctx => ctx.Response.WriteAsync("orders list"));
                    endpoints.MapGet("orders/{id}", ctx => ctx.Response.WriteAsync("orders details"));
                });
            }));
    }
}

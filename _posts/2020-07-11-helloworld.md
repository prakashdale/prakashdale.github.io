---
layout: post
title:  Hello World
categories: [General]
excerpt: Hello world. First blog after created this site.
---

I was looking for a solution to host a personal site to tell something about my self, what I do, my interests, hobbies, job, what I learnt today, or anything that comes to mind. And then came across [github-pages](https://pages.github.com/). This fits perfectly with my requirement and more over it will not cost anything for hosting and maintaining the site.

## Jekyll

You can add more power to your github-pages with Jekyll. It is the engine behind Github Pages, a feature that allows users to host websites based on their github repositories for no additional cost.

[Jekyll](https://en.wikipedia.org/wiki/Jekyll_(software)) is a simple, blog-aware, static site generator for personal, project or organization sites. Written in Ruby by Tom Preston-Werner, Github's co-founder, it is distributed under open source MIT license.

Some of the features mentioned on [Jekyll site](https://jekyllrb.com/)
- Simple: No more database, comment moderation or persky updates to install-just your content.
- Static: Markdown, Liquid, HTML & CSS go in. Static sites come out ready for deployment.
- Blog aware: Permalink, catogories, pages, posts and custom layouts are all first class citizens here.



## Docker
Updating website is quite simple. Make changes to the pages in the github repository. Site is updated in less than a minute after you commit changes.

For local development and testing the site before uploading to github, you need to install 'Ruby Development Environment' which I didn't want to install on my windows development machine. 

Docker (docker-compose) came to rescue as a work around for local developement environment. The steps to setup environment are as follows:

- To start a new project, google 'Jekyll Theme' and download a Jekyll theme which suites your taste.
- Add 'docker-compose.yml' to your project and copy below mentioned code.
```
version: '3'
services: 
  jekyll-serve:
    image: jekyll/jekyll:4.0
    volumes: 
      - '.:/srv/jekyll'
    ports: 
      - 4000:4000
    command: 'jekyll serve'
```
- Run 'docker-compose up'.
- Site will be hosted on localhost. Open browser and go to 'http://localhost:4000'

Todo: I could not make 'jekyll serve --livereload' work with docker. Becuase of this, I have stop and restart docker-compose every time to see the changes made to the site. I'll look into this issue later.

Once you are satisfied with changes, just upload the files to github repository and site will update automatically in few seconds.
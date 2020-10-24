---
layout: post
title:  Email Server
comments: true
categories: [Postfix, SMTP, Raspberry Pi]
permalink: /email-server/
excerpt: Host email server locally.
---

`sudo apt-get update`

`sudo apt-get install postfix`

From menu select *Internet Site* and then enter domain as *morayaa.com*

`cd /etc/postfix`

To check status of postfix service

`service postfix status`

Edit *main.cf* file.

`sudo nano main.cf`

Go to bottom of the file and enter following two lines 

```
home_mailbox = Maildir/
mailbox_command = 
```

Save file and exit nano

Install *devecot* using below command

`sudo apt-get install dovecot-common dovecot-imapd`

Create skaleton structure.


```
sudo maildirmake.dovecot /etc/skel/Maildir
sudo maildirmake.dovecot /etc/skel/Maildir/.Draft
sudo maildirmake.dovecot /etc/skel/Maildir/.Sent
sudo maildirmake.dovecot /etc/skel/Maildir/.Spam
sudo maildirmake.dovecot /etc/skel/Maildir/.Trash
sudo maildirmake.dovecot /etc/skel/Maildir/.Templates
```

Copy folder strutction to 'pi' user home

`sudo cp -r /etc/skel/Maildir/ /home/pi/`

Go to *pi* home directory 

`cd ~/`

Add permission

`sudo chown -R pi:pi ./Maildir`

`sudo chmod -R 700 ./Maildir/`

Restart *postfix* service

`sudo service postfix restart`

## Send first email using telnet

To install telnet,

`sudo apt-get install telnet`

Run telnet

`telnet localhost 25`

`ehlo morayaa.com`

`mail from: pi`

`rcpt to: prakashdale@gmail.com`

`data`

```
Subject: Email from my raspberry pi
This is the body of the email from raspberry pi
.
```

`quit`


## SASL

Edit main.cf file and add following lines at end of the file


```
smtpd_recipient_restrictions = 
    permit_sasl_authenticated,
    permit_mynetworks,
    reject_unauth_destination
```

```
smtpd_helo_required = yes
smtpd_helo_restrictions = 
    permit_mynetworks,
    permit_sasl_authenticated,
    reject_invalid_helo_hostname,
    reject_non_fqdn_helo_hostname,
    reject_unknown_helo_hostname,
    check_helo_access hash:/etc/postfix/helo_access
```


`sudo apt install certbot`

`sudo certbot certonly --standalone -d mail.morayaa.com`
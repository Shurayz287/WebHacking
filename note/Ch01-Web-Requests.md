# 1. Web Requests

## HTTP

- Default port is `80`
- We use `Fully Qualified Domain Name` (`FQDN`) as a `Uniform Resource Locator` (`URL`).

## URL

`http://username:password@host:port/path?query=value#fragment`

- `http`: protocol or scheme, end with a colon and a double slash `://`
- `username:password`: option, depending on the protocol, end with an at sign `@`
- `host:port`: requeried, default port depends on the protocol (HTTP-80, HTTPS-443)
- `/path`: this point to the resource, default is depended on server.
- `?query=value`: start with `?`, consists of a paramenter and value. Multipe parameters can be separated by an ampersand
- `#fragment`: Processed by the browsers on the client-side

## HTTP Flow

Flow:
- Client requests by URL on the browser
- DNS translate URL to IP Address
- Browser requests to IP Address
- Server responses to client

Browsers usually first look up records in the local `/etc/hosts` file. If the requested domain does not exist within it, they would contact other DNS servers. 

## cURL

`-O` for downloading  
`curl -O example.com/example.html`  >> html file from example.com > example.html

`curl -s` silent mode!  

**Fun fact:** `You can use`**`nc`**`to make requests using any protocol`

```bash
$ printf "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n" | nc 127.0.0.1 80
```

## HTTPS 

Main in the Middle attack prevent

- TCP three way handshake
- TLS handshake 
- HTTP encrypted transfer

DNS server stills visited URL if it contacted a clear-text. Recommended to utilize `encrypted DNS server`, `8.8.8.8` and `1.1.1.1`

## HTTP Flow

- `TCP` Three ways handshake
    + Client -----> SYN -----> Server
    + Client <-- SYN + ACK <-- Server
    + Client -----> ACK -----> Server
- `TLS` TLS handshake
    + Client --> CryInfo --> Server
    + Client <-- Certifi <-- Server
    + Client --> VerCert --> Server
    + Client <-> KeyExch <-> Server
    + Client <-> EncSess <-> Server

## HTTP Requests

## HTTP Responses

## Curl with -v, -I

## Security Headers

- `Content-Security-Policy: script-src 'self'` Only self domain 
- `Strict-Transport-Security: max-age=31536000` HTTPS, no-HTTP
- `Referrer-Policy: origin` 

## HTTP Request Methods

`GET`, `POST`, `PUT`, `PATCH`, `DELETE`  
`HEAD`, `OPTIONS`, `CONNECT`, `TRACE`

## HTTP Response Codes

`1xx`, `2xx`, `3xx`, `4xx`, `5xx`

## Authorization Header

`Authorization: <scheme> <token>`

`Authorization: Basic YWRtaW46YWRtaW4=`

`Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30`

Or custom from bushjt admin?

## Parameters

# 2. Web App

## Web Applications

client-server architecture

## Web Applications (Web 2.0) vs. Websites (Web 1.0)

Website:
- Static Pages
- Same for everyone

Web App:
- Dynamic Pages
- Interactive
- Different view
- Functional

## Attacking WebApp

- SQLi
- File Inclusion
- Unrestricted File Upload
- Insecure Direct Object Referencing (IDOR)
- Broken Access Control

## WebApp Layout

### Infrastructure

`models`
- `Client-Server`
- `Many Servers - One Database`

### Components

1. Client
2. Server:
    - Web App Logic
    - Database
3. Services
4. Functions 

### Architecture

## Front End and Back End

Front End:
- HTML
- CSS
- JavaScript

Back End:
- Back end Servers: Hardware and OS or `Containers`
- Web Servers: Handling HTTP requests
- Databases:
- Development Frameworks

## URL Encoding

## Sensitive Data Exposure

**Client-side has a sensitive data or error message**

**HTML Injection**

**Cross-Site Scripting (XSS)**

**Cross-Site Request Forgery (CSRF)**

*Prevention*:
- Sanitization
- Validation

For more *Web Application Firewall* (WAF)

Back End Servers: 
- Web Server
- Database
- Web Application
- WAFs (Option)

Web server run on the backend, handles all of the HTTP traffic from the client. Default TCP ports are 80 and 443 for HTTP and HTTPS

**`Web Servers`**
- Apache (httpd) usually used with PHP, but it supports more than PHP, python, .Net, Perl, Bash: Apple, Adobe and Baidu
- NGINX, many concurrent web request with low memory and CPU load: Google, Facebook, Twitter, Cisco, Intel, ...
- IIS (Internet Information Services) (Microsoft)
- NodeJS

**`Databases`**
- SQL (Structured Query Language)
    + MySQL
    + MSSQL
    + Oracle
    + PostgreSQL
- NoSQL 
    + Key-Value: XML or JSON
    + Graph
    + Document-Based: MongoDB
    + Redis, CouchDB

**`DevFrame`**
- Laravel (PHP)
- Express (NodeJS)
- Django (Python)
- Rails (Ruby)

**`Web APIs`**
- SOAP: Simple Objects Access: XML
- REST: Representational State Transfer: JSON, share data through URL path: GET, POST, PUT, DELETE

**`Common Web Vulns`**
- Broken Authentication/ Broken Access Control (Logical)
- Malicious File Upload (Injection)
- Command Injection (Injection)
- SQLi (Injection)

CVE: Common Vulnerabilities and Exposures


# 3. Information gathering and Fuzzing

**Web Reconnaissance**

*Goal*
- Identifying Assets
- Discovering Hidden Information
- Analysing the Attack Surface
- Gathering Intelligence

*Type* 
- Active Reconnaissance
    + Port Scanning (nmap): Trigger IDS and FireWalls
    + Vulnerability Scanning (Nessus): Security solution can detect
    + Network Mapping (traceroute, nmap): Excessive or unusual network traffic
    + Banner Grabbing (nc, curl): minimal interaction but can still be logged
    + OS Fingerprinting (nmap): usually passive, but some advanced techniques can be detected
    + Service Enumeration (nmap): 
    + Web spidering (Burp Suite Spider): Crawler can be detected
- Passive Reconnaissance
    + 

# 4. Source code Analyst

# Vulnerabilities

## `XSS`

front-end works with HTML and JS code, User input can broke structure, make a malicious behaviour.

Low impact + High probability = Medium risk

Wide range of Attacks via XSS, XSS attacks execute JS code within the browser, browser'JS engine. *curl to view the web page don't make XSS*. More than XSS, hackers can exploit browser with binary exploitaion, which breaks out of the browser' sandbox and execute code on the user's machine.

Types of XSS:
- Stored XSS: most critical type of XSS, store user input in back-end databases and displayed upon retrieval (in backend server)
- Reflected XSS: display after being processed by backend without stored (in frontend server display, in backend server process, only hackers impacted)
- DOM-based XSS: display directerly after frontend process (only frontend, only hacker impacted)

### *Stored XSS* or *Persitent XSS*

Testing payloads: `<script>alert(0)</script>`

Comfirm by **view page source**

### *Reflected XSS* and *DOM-based XSS*

Reflected XSS: User's input $\rightarrow$ Backend $\rightarrow$ User

DOM-based XSS: User's input $\rightarrow$ Frontend $\rightarrow$ User

How to attack? `index.php?msg=<script>alert(1)</script>`, this link is the weapon

DOM-based XSS: Document Object Model, which the model can be changed in the frontend with JS code

DOM-based XSS objects displayed on the page
- Source: JS object that takes the user input
- Sink: is the function that writes the user input to a DOM object on the page
    + document.write()
    + DOM.innerHTML
    + DOM.outerHTML

Furthermore, some jQuery lib: add() after() or append(), if Sink writes exact input without any sanitization this is vulnerable to XSS

DOM Attacks. Script tag can't execute, because the innerHTML function does not allow use of the script tag within it as a security feature. So other XSS payload: `<img src="" onerror=alert(window.origin)>`

### *Impact*

- Defacing:
    + Background Color: `document.body.style.background`
    + Background: `document.body.background`
    + Page Title: `document.title`
    + Page Text: `DOM.innerHTML`
- Phishing by XSS url

**XSS Discovery**, the way to become a real hacker is writing your tool

Login Form injection: Kha ngu

Credential Stealing

Session Hijacking aka Cookie Stealing

Blind XSS, Vulnerability in the page we can't access. But how to detect?
- Loading a Remote Script
- Session Hijacking 

PortSwigger Lab


## SQLi 

## Command Injection

## File Upload

## SSA

### SSRF
### SSTI
### SSII




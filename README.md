<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![oc][oc-project-shield]][oc-project-url]
[![rest-api][rest-api-shield]][rest-api-url]
[![django-rest-framework][django-rest-framework-shield]][django-rest-framework-url]
[![endpoints][endpoints-shield]][endpoints-url]
[![permissions][permissions-shield]][permissions-url]
[![postman][postman-shield]][postman-url]
[![swagger][swagger-shield]][swagger-url]
[![json-web-token][json-web-token-shield]][json-web-token-url]
[![cors][cors-shield]][cors-url]
[![owasp][owasp-shield]][owasp-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">

<h1 align="center">OC - PROJECT N°10 - RESTful API Using Django Rest Framework</h1>

  <p align="center">
   SoftDesk is an API for reporting and tracking technical issues. 
    <br /></p>
</div>
<img src="https://images.unsplash.com/photo-1623282033815-40b05d96c903?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80">
<a href="https://images.unsplash.com/photo-1623282033815-40b05d96c903?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"><small>By Douglas Lopes</small></a>




<!-- ABOUT THE PROJECT -->
## Project Overview
![Overview](static/assets/oc_project_10_drf.gif)

## Endpoints Summary
![Authentication](static/assets/oc_10_endpoints.jpg)

## Access Specification
![Access](static/assets/oc_project_10_access.jpg)
#### Example
PUT : /projects/1/
- Author of the project 1 can update it
- Contributor of the project 1 can read only detail
- Other user of the API (not author or contributor) of project 1 can't access detail information of project 1




<p align="right">(<a href="#top">back to top</a>)</p>



## Built With

* Python 
* Django Rest Framework
* JSON Web Token

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Installation & Running the script

1. Clone the repo
   ```sh
   git clone https://github.com/Jliezed/oc_project_10_softdesk.git
   ```

### Create and activate a virtual environment
2. Go to your project directory
   ```sh
   cd oc_project_10_litreview
   ```
3. Install venv library (if not yet in your computer)
   ```sh
   pip install venv
   ```
4. Create a virtual environment
   ```sh
   python -m venv env
   ```
5. Activate the virtual environment
   ```sh
   source env/bin/activate
   ```
#### Install packages
6. Install the packages using requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
#### Set environment variables
7. Create a copy of the file ".env.default" and rename it ".env"
8. Set value to the .env file:
   1. Define a secret key
   2. Debug to True for local development or False for production
   3. Allowed host equal to 127.0.0.1 for local environment

      ```sh
      SECRET_KEY='YOUR SECRET KEY'
      DEBUG=True
      ALLOWED_HOSTS=['127.0.0.1']
      ```

#### Run the server
   ```sh
   python manage.py runserver
   ```
9. Log to the API: http://127.0.0.1:8000/api/auth/login/
   ```sh
   User: toto
   Password: secret
   ```
10. Or create a superuser
   ```sh
   python manage.py createsuperuser
   ```

### Access the different endpoints
- http://127.0.0.1:8000/api/projects/
- http://127.0.0.1:8000/api/projects/1
- http://127.0.0.1:8000/api/projects/1/users/
- http://127.0.0.1:8000/api/projects/1/issues/
- http://127.0.0.1:8000/api/projects/1/issues/1
- http://127.0.0.1:8000/api/projects/1/issues/1/comments/
- http://127.0.0.1:8000/api/projects/1/issues/1/comments/1
---


<p align="right">(<a href="#top">back to top</a>)</p>


## API Documentation
- Postman: https://documenter.getpostman.com/view/21205949/2s8YCboFSd
- Swagger: http://127.0.0.1:8000/api/docs/#/
![Swagger](static/assets/oc_project_10_swagger.gif)



<p align="right">(<a href="#top">back to top</a>)</p>






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[oc-project-shield]: https://img.shields.io/badge/OPENCLASSROOMS-PROJECT-blueviolet?style=for-the-badge
[oc-project-url]: https://openclassrooms.com/fr/paths/518-developpeur-dapplication-python

[rest-api-shield]: https://img.shields.io/badge/-REST%20API-blue?style=for-the-badge
[rest-api-url]: https://en.wikipedia.org/wiki/Representational_state_transfer

[django-rest-framework-shield]: https://img.shields.io/badge/-Django%20Rest%20Framework-blue?style=for-the-badge
[django-rest-framework-url]: https://www.django-rest-framework.org/

[endpoints-shield]: https://img.shields.io/badge/-ENDPOINTS-blue?style=for-the-badge
[endpoints-url]: https://kinsta.com/knowledgebase/api-endpoint/

[postman-shield]: https://img.shields.io/badge/-POSTMAN-blue?style=for-the-badge
[postman-url]: https://www.postman.com/

[swagger-shield]: https://img.shields.io/badge/-SWAGGER-blue?style=for-the-badge
[swagger-url]: https://swagger.io/

[json-web-token-shield]: https://img.shields.io/badge/-JSON%20WEB%20TOKEN-blue?style=for-the-badge
[json-web-token-url]: https://jwt.io/

[cors-shield]: https://img.shields.io/badge/-CORS-blue?style=for-the-badge
[cors-url]: https://developer.mozilla.org/fr/docs/Web/HTTP/CORS

[owasp-shield]: https://img.shields.io/badge/-OWASP-blue?style=for-the-badge
[owasp-url]: https://owasp.org/www-project-top-ten/

[permissions-shield]: https://img.shields.io/badge/-PERMISSIONS-blue?style=for-the-badge
[permissions-url]: https://www.django-rest-framework.org/api-guide/permissions/
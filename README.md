# backend

<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About
This is the source code for the API service used by the Learning Journey Planning System by All-in-One.

### Documentation

[![Swagger Documentation][product-screenshot-1]](http://127.0.0.1:8000/docs)

Documentation for the API Service can be viewed on swagger docs with the following URL: http://127.0.0.1:8000/docs

### Alternative Documentation
[![Redoc Documentation][product-screenshot-2]](http://127.0.0.1:8000/redoc)
Alternative documentation on redoc is available as well: http://127.0.0.1:8000/redoc

### Built With

<a href="https://fastapi.tiangolo.com/"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="100"/></a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started
1. Clone repository on local.
2. Ensure [MAMP](https://www.mamp.info/en/downloads/)/[WAMP](https://www.wampserver.com/en/download-wampserver-64bits/) is on.
3. Rename `.env.example` to `.env`. Configure the connection string in that file. (see [DB Connection String Examples](#conn-str-ex))
4. Ensure you have [pipenv](https://pipenv.pypa.io/en/latest/) installed.
5. Enter the `backend` directory and run `pipenv shell`.
6. Then run `./start_backend.sh`
7. Once you have finished using the API service, refer [here](#end-service) to end the service.
  
<h3 id="#conn-str-ex">DB Connection String Examples</h3>
<table border=1>
  <tr>
    <td>General Format</td>
    <td>mysql+mysqlconnector://&lt;username&gt;:&lt;password&gt;@localhost:&lt;port_no&gt;/&lt;database_name&gt;</td>
  </tr>
  <tr>
    <td>MacOS</td>
    <td>mysql+mysqlconnector://root:root@localhost:3306/G10T3_LJPS_DB</td>
  </tr>
  <tr>
    <td>Windows</td>
    <td>mysql+mysqlconnector://root@localhost:3306/G10T3_LJPS_DB</td>
  </tr>
</table>

<h3 id="#end-service">End Service</h3>

1. Stop backend service: `ctrl` + `C`
2. Exit pipenv shell: `ctrl` + `D`

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- DEVELOPMENT -->
## Feature Development Workflow
1. Create a new branch (`git checkout -b feature/<jira-ticket-number>-<short description>`)
2. Develop feature
3. Write unit tests (if needed)
2. Commit your Changes (`git commit -m 'Adds <feature-description>'`)
3. Push to the Branch (`git push origin feature/<jira-ticket-number>-<short description>`)
4. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [tiangolo of FastAPI](https://fastapi.tiangolo.com/)
* [mihi on stackoverflow](https://stackoverflow.com/questions/67255653/how-to-set-up-and-tear-down-a-database-between-tests-in-fastapi)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/learning-journey-planning-system/backend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/learning-journey-planning-system/backend/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/learning-journey-planning-system/backend/stargazers
[product-screenshot-1]: img/swagger-ui.png
[product-screenshot-2]: img/redoc.png
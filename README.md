# PyDIDS

<!-- Improved compatibility of back to top link: See: https://github.com/ralucanegre/pydids/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out PyDIDS. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ralucanegre/pydids">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">PyDIDS</h3>

  <p align="center">
    Python blockchain-based Decentralized Identity Management (DID) system
    <br />
    <a href="https://github.com/ralucanegre/pydids"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ralucanegre/pydids">View Demo</a>
    &middot;
    <a href="https://github.com/ralucanegre/pydids/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/ralucanegre/pydids/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



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
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

A Blockchain-based Decentralized Identity Management (DID) system enables individuals to own and control their identities without relying on a central authority.

To build a simple implementation of a basic DID system, we can use blockchain technology to store identity-related information, ensuring transparency, security, and privacy.

We'll use hashlib for cryptographic hashing and json for storing identity data
and ed25519 elliptic curve signature cryptographic algorithm, which is known for its security, efficiency, and faster operations.


Key Components:
* Blockchain: A basic blockchain structure that stores identity information in blocks.
* Identity Management: An identity will be associated with a DID and stored in the blockchain.
* Public/Private Key: The DID will use asymmetric encryption (public/private key pairs) for managing identity-related actions securely.

Notes:

Security Considerations: This is a simplified implementation for demonstration purposes. In a real-world system, additional features like secure key storage, encryption, and more robust identity verification mechanisms would be required.

Scalability: This example uses a simple blockchain. For production systems, you would want to use a more advanced and scalable solution, such as Ethereum or Hyperledger Indy, which provide specialized DID frameworks.

Signature Generation: The signature verification here is a placeholder, as generating and verifying RSA signatures requires using the private key to sign messages and the public key to verify them.

This implementation provides a foundation for understanding how a decentralized identity management system works using blockchain, but it would need further expansion for use in a real-world scenario.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With Python 3.13

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This example requires Python 3.10 or higher version.

Install the ed25519 library using pip3 tool.

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```
3. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/ralucanegre/pydids/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the Unlicense License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [Ed25519 Implementation Vulnerability in Python (Recovering Private Key)](https://asecuritysite.com/eddsa/ed03)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-shield]: https://img.shields.io/github/issues/ralucanegre/pydids.svg?style=for-the-badge
[issues-url]: https://github.com/ralucanegre/pydids/issues
[license-shield]: https://img.shields.io/github/license/ralucanegre/pydids.svg?style=for-the-badge
[license-url]: https://github.com/ralucanegre/pydids/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/raluca-n-81627773
[product-screenshot]: images/screenshot.png

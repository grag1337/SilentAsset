<p align="center">
   <img src="https://i.ibb.co/dJdVc5M/Screenshot-2021-09-16-11-41-08.png" width="412.6" height="476"></img>
</p>
   <p align="center"><b>Please star this project!</b></p>
  <p align="center">
    Written in Python
    <br/>
    <br/>
    <a href="https://github.com/Grag1337/SilentAsset/issues">Report Bug</a>
    .
    <a href="https://github.com/Grag1337/SilentAsset/issues">Request Feature</a>
  </p>
</p>

<p align="center">
<img src="https://img.shields.io/github/downloads/Grag1337/SilentAsset/total?style=for-the-badge"></img>
<img src="https://img.shields.io/github/contributors/Grag1337/SilentAsset?color=dark-green&style=for-the-badge"></img>
<img src="https://img.shields.io/github/issues/grag1337/SilentAsset?style=for-the-badge"></img>
<img src="https://img.shields.io/github/license/grag1337/SilentAsset?style=for-the-badge"></img>
</p>
<h1>Unbelieveably broken after not being maintained for a year</h1>
<h1>Probably doesn't work anymore, moving on to other things</h1>

## DISCLAIMER ##

This project is in its early days, everything you see here is almost a POC. I will constantly be changing this project and adding / removing features. As said below, suggestions are greatly appreciated and assist me in prioritising feature addition. 

<b>PS</b>: Don't run this as root, unless you are prepared to debug for hours. I have no idea why it fails when running as root.<br>
<b>PSPS</b>: Make sure you have chromium and chromium-webdriver installed before lodging issues, just incase that's the problem.

## About The Project

After trying to make-do with a handful of asset discovery tools, I decided that it was time to just create something that does what I want, how I want it. This is an ongoing project and features are prone to change / deletion. I'm taking any/all suggestions and code additions that assist in creating a tool that can compete with it's predecessors. 

It's mainly written in python, but I'm planning on adding a website / report function, which will use markup languages. So contact me if you're confident with HTML / JS, etc..

## Built With

Python3

## Getting Started

Disclaimer: Afaik, one of the libraries I use downloads a 100mb chromium package during use somewhere. It only does it once, but just ensure that you have the space for that prior to running this.

This is how you currently install and run this program:

### Prerequisites

* Python3

```sh
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.8
```

* Go<br>
You need this to run and install gobuster, if you don't have go installed the intial setup will fail.

```sh
https://golang.org/doc/install
```

p7zip
```sh
sudo apt install p7zip
```
### Installation

1. Clone the repo

```sh
git clone https://github.com/grag1337/SilentAsset.git
```

2. Install Requirements

```sh
pip3 install -r requirements.txt
```
or
```sh
sudo pip3 install -r requirements.txt
```

3. Run the program, it will do an initial installation.

```sh
chmod +x run.py
./run.py
```

## Usage

Type ```help``` in the main menu to get a list of commands.

## Latest Updates

As of 15/10/2021 I can confidently say that this tool can do a basic subdomain audit. The screenshot function is working as intended, even if the HTML report looks like it's still in its infancy.

More features to come! Help with the HTML report side is appreciated, feature requests are also greatly appreciated! 

## Roadmap

See the [open issues](https://github.com/Grag1337/SilentAsset/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/Grag1337/SilentAsset/issues/new) to discuss it, or directly create a pull request.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/Grag1337/SilentAsset/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/Grag1337/SilentAsset/blob/main/LICENSE) for more information.

## Authors

* **Grag1337** - *Cyber Security Student* - [Grag1337](https://github.com/grag1337/) 

## Acknowledgements

* [ShaanCoding](https://github.com/ShaanCoding/)
* [Othneil Drew](https://github.com/othneildrew/Best-README-Template)
* [ImgShields](https://shields.io/)
* [Turbolist3r](https://github.com/fleetcaptain/Turbolist3r)
* [FindDomain](https://github.com/Findomain/Findomain)

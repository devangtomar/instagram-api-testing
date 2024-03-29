<h1 align="center">
  📷 InstaPy Testing Repo 📷
</h1>

<p align="center">
  <img src="https://img.shields.io/github/license/devangtomar/instagram-api-testing" alt="License">
  <img src="https://img.shields.io/github/issues/devangtomar/instagram-api-testing" alt="Issues">
  <img src="https://img.shields.io/github/stars/devangtomar/instagram-api-testing" alt="Stars">
  <img src="https://img.shields.io/github/forks/devangtomar/instagram-api-testing" alt="Forks">
</p>

<p align="center">
  This repository was created to test and experiment with the InstaPy Python package for automating Instagram interactions.
</p>

## 🚀 Getting Started

To get started with this repository, you'll need to have Python 3 installed on your machine. You can download Python from the [official website](https://www.python.org/downloads/).

After installing Python, you can clone this repository using the following command:

```
git clone https://github.com/devangtomar/instagram-api-testing.git
```

Then, navigate to the project directory and install the required dependencies:


```bash
cd instagram-api-testing
pip install instapy
```

## 📄 Usage

This repository contains a few sample scripts for using InstaPy. You can run each script by executing the corresponding Python file:

- `like_by_tag.py`: likes posts with a specified hashtag
- `like_by_location.py`: likes posts from a specified location
- `follow_by_tag.py`: follows users who have posted with a specified hashtag
- `unfollow_nonfollowers.py`: unfollows users who do not follow you back

Before running any of these scripts, you'll need to edit the `config.py` file and enter your Instagram username and password. You can also configure other settings such as the number of likes or follows to perform per hour.

Note that automating interactions on Instagram may violate the platform's terms of service, so use InstaPy at your own risk.

## 📝 Contributing

If you'd like to contribute to this repository, please open an issue or submit a pull request. We welcome contributions of all kinds, from bug fixes to new features.

Before contributing, please make sure to read our [code of conduct](CODE_OF_CONDUCT.md) and [contribution guidelines](CONTRIBUTING.md).

## 📖 License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

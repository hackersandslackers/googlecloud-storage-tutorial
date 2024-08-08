# Google Cloud Storage Python SDK Tutorial

![Python](https://img.shields.io/badge/Python-v3.10-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Google Cloud Storage](https://img.shields.io/badge/Google--Cloud--Storage-v2.18.0-blue.svg?logo=Google&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/toddbirchard/tableau-extraction.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/hackersandslackers/googlecloud-storage-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/toddbirchard/tableau-extraction.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a)](https://github.com/hackersandslackers/googlecloud-storage-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/toddbirchard/tableau-extraction.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/hackersandslackers/googlecloud-storage-tutorial/network)

![Google Cloud Storage Python SDK Tutorial](./.github/gcpcloudstorage@2x.jpg)

Source for the accompanying tutorial here: [https://hackersandslackers.com/google-cloud-storage-with-python/](https://hackersandslackers.com/google-cloud-storage-with-python/)

## Getting Started

Get set up locally in two steps:

### Environment Variables

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `GCP_BUCKET_URL`: URL of your Google Cloud Storage bucket.
* `GCP_BUCKET_NAME`: Name of your Google Cloud Storage bucket.
* `GCP_BUCKET_FOLDER_NAME`: Directory within your bucket to store and modify files.
* `GOOGLE_APPLICATION_CREDENTIALS`: Path to your Google Cloud Platform service account key file.

### Installation

Get up and running with `make run`:

```shell
git clone https://github.com/hackersandslackers/googlecloud-storage-tutorial.git
cd googlecloud-storage-tutorial
make run
```

-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.

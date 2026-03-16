# High-Accuracy Fish Species Identification Using Transfer Learning on Vision Foundation Models

## *MEDFISH101*

<div align="center">
  
[![Dataset](https://img.shields.io/badge/Dataset-MEDFISH101-1f6feb)](#)
[![Images](https://img.shields.io/badge/Images-69,152-success)](#)
[![Classes](https://img.shields.io/badge/Classes-101-orange)](#)
[![Region](https://img.shields.io/badge/Region-Mediterranean-blue)](#)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-compatible-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-supported-11557c)](https://matplotlib.org/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-supported-f7931e?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)

</div>


*MEDFISH101* is a curated image dataset for Mediterranean fish species classification.  
It contains **69,152 validated images** spanning **101 fish species** found in the Mediterranean Sea.

The dataset was created to support:
- marine biodiversity monitoring
- citizen-science assisted species identification
- benchmarking computer vision models on Mediterranean fish imagery
- transfer learning and foundation-model research for ecological applications

### Dataset Summary

- **Number of classes:** 101
- **Number of images:** 69,152
- **Domain:** Marine biodiversity imagery
- **Geographic focus:** Mediterranean Sea
- **Image source:** Primarily iNaturalist research-grade observations
- **Validation:** Additional review by marine science experts

This dataset was introduced in the paper:

### Motivation

The Mediterranean Sea is one of the most biodiverse yet heavily impacted marine ecosystems.  
Reliable automated fish identification can help improve large-scale biodiversity monitoring, especially in citizen-science settings where observations are often contributed by non-experts.

*MEDFISH101* was designed to provide an open and curated benchmark for Mediterranean fish recognition and to support the development of AI tools for ecological monitoring.

### Data Collection and Curation

Images were primarily sourced from **iNaturalist** using **research-grade** observations.  
Only entries meeting iNaturalist’s research-grade standard were considered, and the collected images were further reviewed by a panel of marine science experts to improve annotation reliability.

The dataset was curated to include **101 Mediterranean fish species** and to provide broad geographic coverage across the Mediterranean region.

### Class Distribution

The dataset is mildly imbalanced by design, reflecting ecological observation frequency rather than enforcing artificial uniformity.

Each class contains between roughly **100 and 1000 images**, depending on species availability and validation outcomes.

### Dataset Structure

Each example contains:
- `image`: the fish image
- `label`: integer class label
- `class_name`: scientific species name

If you provide the dataset in folder-per-class format, the structure may look like:

```text
MEDFISH101/
├── Aidablennius sphynx/
├── Apogon imberbis/
├── Arnoglossus laterna/
├── ...
└── Xyrichtys novacula/

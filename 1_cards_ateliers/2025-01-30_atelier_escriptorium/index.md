---
uuid: 14f105ec-6f66-4f9b-98ae-885ba6a1d82c

title: Atelier eScriptorium
author: ceres
abstract: "Atelier sur l'utilisation d'eScriptorium"
event: true
tags:
    - atelier
    - ocr
    - htr
    - atr
    - escriptorium
    - corpus
    - manuscrits
    - transcription
    - édition
    - numérisation
---

![](atelier_escriptorium.png)

**eScriptorium** est une plateforme en ligne de transcription
automatique et de correction d'ATR.

L'Optical Character Recognition (OCR) et l'Handwritten Text Recognition (HTR) sont deux technologies permettant d'effectuer de la reconnaissance automatique de texte imprimé et de texte manuscrit. L'Automatic Text Recognition (ATR) est un terme générique qui englobe ces deux technologies.

Elles s’inscrivent dans un domaine vaste et parfois complexe, où il peut être difficile de se repérer, de savoir par où commencer et comment procéder. 
Toutefois, l'OCR et l'HTR sont suffisamment avancés pour proposer des outils à la disposition de tous, même sans connaissances en Deep Learning.

L'objectif de cet atelier est de présenter les différentes étapes dans la reconnaissance de texte imprimé ou manuscrit, de la préparation du corpus à la pratique avec eScriptorium.

[Lien vers la présentation](atelier_escriptorium.pdf)
<iframe src="https://ceres.sorbonne-universite.fr/22daca7c9ce30b59860f1120258dac3e/atelier_escriptorium.pdf" type="application/pdf" width="100%" height="500px">
    <p>Vous pouvez <a href="atelier_escriptorium.pdf">télécharger le PDF</a>.</p>
</iframe>

Les données utilisées pour cet atelier sont disponibles sur à partir du lien Google Drive suivant [https://drive.google.com/drive/folders/1FhG-B3Qxg6FesSuYkkvS_ryR4Iesd8Rg](https://drive.google.com/drive/folders/1FhG-B3Qxg6FesSuYkkvS_ryR4Iesd8Rg).

Pour une installation locale :
- Téléchargez l'archive contenant le code à partir du lien suivant [https://www.swisstransfer.com/d/43cde0d9-cffb-4bda-b6db-a05a47515ab5](https://www.swisstransfer.com/d/43cde0d9-cffb-4bda-b6db-a05a47515ab5)
- Décompressez l'archive
- Installez Docker sur votre machine (aide à l'installation au lien suivant [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/))
- Ouvrez un terminal et placez-vous dans le dossier décompressé
- Exécutez la commande `docker-compose up`
- Ouvrez un navigateur et rendez-vous à l'adresse [http://localhost:5813](http://localhost:5813)
- Vous pouvez maintenant utiliser eScriptorium en local

Après l'installation et pour chaque utilisation, vous pouvez lancer eScriptorium en exécutant la commande `docker-compose up` dans le dossier décompressé.

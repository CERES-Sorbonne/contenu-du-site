---
title: 'Outil CERES : Panoptic'
author: ceres
tags:
    - images
    - outils CERES
---

![big](panoptic_screenshot.png)

## En bref

Développé par le CERES, *Panoptic* est un outil de visualisation, d’exploration et d'annotation de grands corpus d’images. Cet outil intègre notamment des algorithmes de groupage d'images par similarité (MobileNet, average hash, sha1), ce qui permet d'aider l'usager·e dans le tri et l'exploration. L’outil propose par ailleurs diverses options de filtrage, de recherche et d'annotation, permettant la création, l'analyse et l’exportation de sous-corpus.

[Le code est en libre accès](https://github.com/CERES-Sorbonne/Panoptic) sous la [Mozilla public license 2.0](https://github.com/CERES-Sorbonne/Panoptic/blob/main/LICENSE).

## Quelques fonctions

### Créer de propriétés 

![big](create_prop.gif)

### Filtrer et grouper 

![big](group_filter.gif)

### Créer des groupements automatiques

![big](tag_group.gif)

### Trouver des images similaires à une image

![big](images_similaires.gif)

### Trouver des images similaires à un groupe

![big](reco.gif)

### Cas d'usage : mettre une image hors corpus

![big](hors_corpus.gif)

## Installation

<aside>

À terme, nous aimerions qu'il soit aussi facile d'installer Panoptic que n'importe quel autre logiciel. Mais nous n'avons pas encore pris le temps de construire un installeur, donc il vous faudra suivre les étapes suivantes.

**Attention :** le logiciel auquel vous avez accès est toujours un prototype en développement. Certaines fonctions ne sont pas encore disponibles et il est probable que vous rencontriez des bugs. Nous vous recommandons donc pour le moment de ne pas vous reposer dessus pour votre travail de recherche, et de ne l'utiliser que pour faie des tests.

</aside>

1. Panoptic s'appuie sur un langage de programmation appelé Python, qu'il faut avoir déjà téléchargé pour pouvoir l'utiliser. Si vous n'avez jamais téléchargé Python, vous pouvez [obtenir la dernière version sur le site officiel](https://www.python.org/downloads/).
2. Ouvrez une fenêtre de terminal. C'est une application présente sur tous les ordinateurs, que vous trouverez probablement dans votre dossier d'applications. Elle s'appelle souvent "Terminal".
3. Tapez ou copiez-collez `pip install panoptic` puis appuyez sur la touche `Entrée`. Panoptic devrait s'installer.
4. Tapez `panoptic` puis appuyez sur la touche `Entrée` pour lancer le logiciel. À l'avenir, vous pourrez relancer Panoptic de cette manière.
5. Pour mettre à jour votre version de Panoptic, vous pouvez lancer la commande `pip install --upgrade panoptic`.
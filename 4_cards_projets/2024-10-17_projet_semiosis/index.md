---
uuid: 315d68b6-72b2-4017-b6d0-acf434cef96c

prettyName: Semiosis
title: "Projet SEMIOSIS (Sens, Expérimentation Méthodologique, Interprétation : Outils Scientifiques et Informatiques pour les SHS)"
author:
    - fred
abstract: "Le projet SEMIOSIS (Sens, Expérimentation Méthodologique, Interprétation : Outils Scientifiques et Informatiques pour les SHS), soumis par Sorbonne Université pour l’UMS CERES, a fait l'objet d'un financement dans le cadre du Dialogue stratégique et de gestion 2020-2021."
tags:
- semiosis
- panoptic
- collaboration
- images
- communautés
- controverses
---

![cartographie circulaire des usages des méthodes numériques à la Faculté des Lettres](semiosis.png)

Le projet SEMIOSIS (Sens, Expérimentation Méthodologique, Interprétation : Outils Scientifiques et Informatiques pour les SHS), soumis par Sorbonne Université pour l’UMS CERES, a fait l'objet d'un financement dans le cadre du Dialogue stratégique et de gestion 2020-2021. 
Coordination : Virginie Julliard
Équipe : Félix Alié, Édouard Bouté, Thomas Bottini, Victor Écrement, David Gödicke, Gaël Lejeune, fred Pailler, Émile Rebours, Antoine Lebrun, Rebecca Bristow, Alexandre Bartz

Grâce à l'emploi de 7 ingénieur·es, pour des durées variables réparties sur 3 années, SEMIOSIS a permis de développer quatre axes principaux concernant les méthodes numériques dédiées à la recherche en humanités et en sciences sociales.

#### Identifier les gestes communs aux disciplines convoquant l’interprétation pour analyser des corpus (analyse musicale, sémiotique, linguistique, sociologie, info-com…)
Le premier objectif a consisté en une enquête auprès des chercheur·ses mobilisant des méthodes numériques à la Faculté des Lettres. Après l'établissement d'une cartographie de ces recherches, une seconde phase de description des méthodes et des manières très concrètes de procéder a pu être engagée, principalement grâce à une série d'entretiens avec les chercheur·ses et au suivi ethnographique dans la durée de certains des projets. Enfin, des ateliers de co-conception ont été organisés avec les chercheur·se·s de la Faculté des Lettres afin de préfigurer et discuter le développement d'outils d’annotation et de visualisation adéquats.

#### Offrir aux SHS des outils d’annotation & de visualisation de corpus numériques multimédias
Afin de développer plusieurs de ces outils, il s'est agit de nourrir le dialogue SHS/informatique (ML, TAL, IHM, Web sémantique), et produire un lexique et des objectifs communs à des disciplines, des approches du logiciel, et des pratiques de l'étude/enquête relativement distinctes. 3 outils principaux ont pu émerger ou évoluer grâce au financement de SEMIOSIS : 
1. Le design d'une interface graphique pour l'application [Restweet](https://ceres.sorbonne-universite.fr/Restweet/) (développé sur le budget du CERES) : celle-ci permettait la collecte massive, et sur une longue durée, de données issues de la plateforme Twitter. L'interface graphique rend possible l'exploration des données qui ont été collectées, à l'aide de graphiques, d'un grand nombre de filtres, et de la possibilité de réaliser des requêtes supplémentaires.
2. Le prolongement du développement de [Sherlock](https://shs.hal.science/halshs-03950395/document), une plateforme d’annotation sémantique collaborative en ligne reposant intégralement sur des données ouvertes en RDF/CIDOC-CRM. Ce service, qui repose sur une API authentifié par comptes ORCID, a été éprouvé dans le cadre d’un outil d’annotation de partitions pour la musicologie développé à l’IReMus.
3. le développement de [Panoptic](https://ceres.sorbonne-universite.fr/Panoptic/), un outil de visualisation, d’exploration et d’annotation de grands ensembles d’images (co-financé entre SEMIOSIS et des fonds propres du CERES): Panoptic permet la navigation dans des corpus de dizaines/centaines de milliers d'images, en intégrant des briques de machine learning. Ces dernières permettant la découverte d’images similaires, la création de groupes sémantiques. L’outil propose diverses options de filtrage, de recherche et de labellisation, qui permettent aux chercheur·se·s de constituer et d'exporter des sous-corpus. Panoptic a fait l’objet de différents types de valorisation auprès de la communauté scientifique (2023-2024). Le prototype du logiciel est accessible sur [Github](https://github.com/CERES-Sorbonne/Panoptic). Il a permis l’accompagnement de plusieurs projets (Appel Emergence SU, ANR) et il a été présenté dans plusieurs articles, séminaires et conférences.
4. Par ailleurs, la dotation a permis de contribuer fortement à la mise en ligne de 4.000 documents numérisés de la Fronde au 17ème siècle (corpus dit des Mazarinades) avec un moteur de recherche et des fonctionnalités d’extraction associées, dans le cadre du projet [Antonomaz](https://ceres.sorbonne-universite.fr/Antonomaz/). La solution technique finalement utilisée est TEI publisher2 qui permet d’exploiter des annotations riches en XML-TEI. Ceci correspond à une demande importante des collègues de la faculté des Lettres. Nous accompagnons déjà deux projets, un en histoire et l’autre en langue française, dont les corpus seront diffusés via la même technologie.

#### Confronter annotations machiniques & humaines pour mieux cerner ce qui est irréductible à l’interprétation humaine
Un point d'innovation dans les SHS consiste à saisir non pas comment des outils numériques viendraient remplacer des techniques "manuelles", mais plutôt à saisir comment ces outils déplacent les modalités et les limites de l'interprétation humaine face à un corpus donné. Ce type de déplacements se produit à de multiples niveaux, par exemple en offrant à l'interprétation un corpus exhaustif là où elle aurait du se contenter de portions minuscules de textes ou d'images quelques années plus tôt (à ce propos, le chercheur É. Ollion explique très bien l'importance de cette transformation au micro de X. De La Porte [écouter le podcast](https://www.radiofrance.fr/franceinter/podcasts/le-code-a-change/le-code-a-change-4-10-9709507)). Un autre de ces déplacements, particulièrement travaillé dans le cadre de Semiosis, consiste à donner une plus grande mobilité au moment de l'interprétation, voire à démultiplier ce moment. Panoptic offre par exemple les moyens d'assembler des groupes images issues d'un corpus de différentes manières : soit directement à partir de ce que l'on peut en interpréter grâce à la connaissance de leur contexte de production, soit à partir de propriétés strictement formelles des images. La méthode engagée dans le second cas repousse le travail d'interprétation après les opérations de tri à proprement parler, ou dans d'autres cas permet de les relancer avec de nouvelles questions. La nature médiatique des corpus numériques/numérisés, leurs transformations, leurs remix, leur circulation, prend place dès lors au cœur de l'interprétation. 

#### Rendre compte de faits sociaux, culturels et politiques contemporains
Les recherches que nous avons menées grâce à ces outils ont permis d’atteindre le 4e objectif. Les outils développés grâce à la dotation SCSP ont permis à CERES d’accompagner des recherches sur la « haine en ligne », telle que la recherche doctorale sur le fonctionnement des algorithmes de modération de Twitter de T. Grison (soutenance prévue en décembre 2024). L'étude portant sur la montée de la droite réactionnaire de V. Julliard & f. Pailler (cf. ["The Womb, the Banknote and the Trolley. Elements of French Anti-Gender Visual Culture"](https://ceres.sorbonne-universite.fr/AntiGenderVisualCulture)), ainsi que celle portant sur les violences policières de É. Bouté (cf. ["Militantisme transplateforme : la répression policière des Gilets jaunes entre Facebook et Twitter"](https://edouardboute.github.io/files/Boute_SFSIC2023.pdf)) ont aussi fait l'objet de publications reposant en partie sur les méthodes et les outils développés dans le cadre de Semiosis.


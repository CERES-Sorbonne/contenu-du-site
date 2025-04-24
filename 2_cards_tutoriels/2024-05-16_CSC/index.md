---
uuid: 6dfca34b-bf71-4dad-8480-7ba0d129e593

title: "Cheat Sheet CQL - Feuille d'aide à la requête CQL pour TXM"
author: marceau
tags:
    - tutoriel
    - CQL
    - CQP
    - TXM
    - corpus
    - textométrie
    - cheat sheet
    - requêtes
    - recherche
    - feuille d'aide
    - corpus query language
    - traitement de corpus
    - text mining
    - text analysis
prettyName: RequetesCQL
---

TXM est un logiciel de traitement de corpus qui permet d'interroger des corpus textuels à l'aide de requêtes CQL (Corpus Query Language).
Cet article propose une liste de requêtes CQL pour vous aider à comooser vos propres requêtes sur vos corpus.

NB : Une partie de ces requêtes reposent sur des structures spécifiques présentes dans les fichiers XML importés dans TXM, vérifiez ce qui est disponible pour votre corpus au préalable.

Pour approfondir les usages de TXM, vous pouvez consulter notre [tutoriel avancé sur les usages de TXM](https://ceres.sorbonne-universite.fr/7e795cbe-ee56-471c-8dfb-9978dbeb7301/).
Ou encore consulter la [documentation officielle de TXM](https://txm.gitpages.huma-num.fr/textometrie/files/documentation/manual/0.7.9/fr/manual94.xhtml).


# Recherche simple
- `patate` : recherche le mot patate
- `patate patate` : recherche les deux mots patate et patate
- `patate [ ] patate` : recherche les deux mots patate et patate avec un mot entre eux

# Expressions régulières
CQL permet d'utiliser des expressions régulières pour affiner les recherches, en voici quelques exemples
- `patate.*` : recherche les mots commençant par patate
- `.*patate` : recherche les mots finissant par patate
- `.*patate.*` : recherche les mots contenant patate
- `patate|tomate` : recherche les mots patate ou tomate
- `patate.+` : recherche les mots patate suivis d'un ou plusieurs caractères
- `patate.{2,5}` : recherche les mots patate suivis de 2 à 5 caractères
- `patate[0-9]` : recherche les mots patate suivis d'un chiffre
- `patate[^0-9]` : recherche les mots patate suivis d'un caractère qui n'est pas un chiffre



# Changement de casse et accents
Par défaut, les requêtes CQL sont sensibles à la casse et aux accents (dialectriques), voici comment les ignorer
- `patate` : recherche les mots patate
- `"patate"%c` : recherche les mots patate sans tenir compte de la casse
- `"patate"%d` : recherche les mots patate sans tenir compte des accents et autres diacritiques
- `"patate"%cd` : recherche les mots patate sans tenir compte de la casse ni des accents et autres diacritiques

# Recherche sur les propriétés
Les propriétés différentes de `word` sont ici issues de TreeTagger, vérifiez ce qui est disponible pour votre corpus au préalable
- `[word="patate"]` : recherche les mots patate
- `[frlemma="patate"]` : recherche les lemmes patate
- `[frpos="NOM"]` : recherche les noms
- `[frpos="ADJ"]` : recherche les adjectifs

# Critères multiples 
On peut combiner plusieurs critères pour affiner la recherche sur un même terme
- `[word="avions" & frpos="VER.*"]` : recherche les verbes dont la graphie est avions
- `[word="avions" & frpos="NOM"]` : recherche les noms dont la graphie est avions

# Recherche sur les structures
Interrogation sur les attributs présents dans les fichiers XML déja présents avant importation
- `[_.text_annee="2023"]` : recherche les textes de l'année 2023
- `[_.text_annee="202[0-9]{1}"]` : recherche les textes des années 2020 à 2029
- `[_.text_annee="202[0-9]{1}" & word="patate"]` : recherche les mots patate dans les textes des années 2020 à 2029

# Distance
La distance permet de rechercher des mots séparés par un certain nombre de mots
- `[word="patate"] []{0,50} [word="patate"]` : recherche deux mots patate séparés de 0 à 50 mots
- `[word="patate"] []* [word="patate"] within 10` : recherche deux mots patate séparés de 0 à 50 mots

# Expansion
L'expansion permet d'élargir la recherche à des contextes plus larges, basés sur les structures présentes dans les fichiers XML, ici on part du principe que des balises `<s>` encadrent les phrases
- `[word="patate"] expand to s` : recherche les phrases contenant le mot patate (le motif reconnu par l'expression)

# Reprise de propriétés
La reprise de propriétés permet de réutiliser des propriétés de termes déjà trouvés dans la requête
- `m:[frpos="NOM|VER.*" & word="avions"] [frpos != m.frpos]` : recherche le mot avions (verbe ou nom) suivi d'un mot étiqueté avec une autre partie du discours

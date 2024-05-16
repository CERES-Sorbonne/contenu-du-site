---
title: "CSC : Cheat Sheet CQL"
author: marceau
tags:
    - tutoriel
    - CQL
    - CQP
    - TXM
    - corpus
---

# Recherche simple
- `patate` : recherche le mot patate
- `patate patate` : recherche les deux mots patate et patate
- `patate [ ] patate` : recherche les deux mots patate et patate avec un mot entre eux

# Expressions régulières
- `patate.*` : recherche les mots commençant par patate
- `.*patate` : recherche les mots finissant par patate
- `.*patate.*` : recherche les mots contenant patate
- `patate|tomate` : recherche les mots patate ou tomate
- `patate.+` : recherche les mots patate suivis d'un ou plusieurs caractères
- `patate.{2,5}` : recherche les mots patate suivis de 2 à 5 caractères
- `patate[0-9]` : recherche les mots patate suivis d'un chiffre
- `patate[^0-9]` : recherche les mots patate suivis d'un caractère qui n'est pas un chiffre


# Changement de casse et accents
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
- `[word="avions" & frpos="VER.*"]` : recherche les verbes dont la graphie est avions
- `[word="avions" & frpos="NOM"]` : recherche les noms dont la graphie est avions

# Recherche sur les structures
Interrogation sur les attributs présents dans les fichiers XML déja présents avant importation
- `[_.text_annee="2023"]` : recherche les textes de l'année 2023
- `[_.text_annee="202[0-9]{1}"]` : recherche les textes des années 2020 à 2029
- `[_.text_annee="202[0-9]{1}" & word="patate"]` : recherche les mots patate dans les textes des années 2020 à 2029

# Distance
- `[word="patate"] []{0,50} [word="patate"]` : recherche deux mots patate séparés de 0 à 50 mots
- `[word="patate"] []* [word="patate"] within 10` : recherche deux mots patate séparés de 0 à 50 mots

# Expansion
- `[word="patate"] expand to s` : recherche les phrases contenant le mot patate (le motif reconnu par l'expression)

# Reprise de propriétés
- `m:[frpos="NOM|VER.*" & word="avions"] [frpos != m.frpos]` : recherche le mot avions (verbe ou nom) suivi d'un mot étiqueté avec une autre partie du discours

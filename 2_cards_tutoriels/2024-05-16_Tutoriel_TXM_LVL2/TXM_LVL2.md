# Plan

Progression

- CQL (dans concordancier + exemple dans progresions)
- AFC
- Sous-corpus
- Partitions
- Spécificités
- AFC

# TXM - Niveau 2

## Progression

Nous pouvons utiliser TXM pour étudier la progression de l'utilisation d'un mot au cours du temps. Dans le corpus [Europresse-Meurice]{.smallcaps}, nous allons évaluer l'évolution de certains usages au fil du temps et des présidents grâce à la fonction **progression**.

1. Dans un premier temps, comparez l'évolution de l'usage des mots X et Y. Il est possible d'ajouter les mots un par un en les recherchant successivement. Notez-vous quelque chose d'intéressant ?

2. Affichez les paramètres de votre onglet progression (roue dentée)

3. Dans la partie "Unité structurelle et propriété", configurez TXM afin que les séparations (barres verticales) affichent la source et l'année. Choisissez dans le premier menu déroulant l'option X et dans le second l'option Y.

4. En quel année l'usage de X a-t-il connu la plus grande augmentation ? Dans quelle source la tendance entre l'usage de Y et de Z a changé ?

5. Comparez à présent les verbes au présent et ceux au conditionnel grâce à l'assistant de requêtes (propriété frpos) et un utilisant le jeu d'étiquettes figurant ici : https://txm.gitpages.huma-num.fr/textometrie/files/documentation/manual/0.7.9/fr/manual81.xhtml#toc431

## Requêtes complexes CQL &#40;dans concordancier + exemple dans progresions

1. Retournons dans le concordancier pour regarder les occurrences de motifs syntaxiques. Cliquez sur la baguette magique pour aller chercher un mot (word) dont l'étiquette (POS) est adjectif. Après avoir validé la fenêtre vous pouvez cliquer sur le bouton calculer (sur la droite de la barre de recherche avant la roue dentée).

2. Notez la syntaxe de la requête `[frpos = "ADJ"]`, on a fait une recherche sur l'attribut POS en demandant la valeur ADJ. Dans la barre de recherche, remplacez ADJ par NOM et observez le résultat.
3. "A la main" ou avec l'assistant (avec la fonction ajouter un mot), cherchez maintenant les séquences ADJ puis NOM.
4. Voilà, c'est ça le CQL, vous pouvez mélanger les différents attributs. Par exemple pour chercher le mot (word) écrivain suivi de l'étiquette (POS) adjectif.

### Se méfier de la progression

L'outil progression est très utile pour comparer l'évolution de l'usage des mots dans le temps... Cependant, TXM n'est seulement capable de genérer la progression en suivant l'ordre de votre corpus. Si vous avez un corpus qui n'est pas ordonné chronologiquement, il faudra d'abord le trier avant de lancer la progression.

## Sous-corpus

La fonction sous-corpus permet de créer ... un sous-corpus pour restreindre les résultats à un sous ensemble des textes

1. Choisissez la Structure Article. Ceci permet de faire apparaître la propriété "Année".
2. Choisissez l'année 2021, donnez un nom à ce sous-corpus et validez.
3. Refaites la même requête que précédémment (écrivain + ADJ)
4. Observez que le nombre de résultats est inférieur

## Partitions

La partition est un peu différente du sous-corpus en ce sens qu'elle sera surtout utile pour comparer différentes
parties du corpus de travail.

1. Choisissez la fonction "Partition"
2. Dans la structure Article choisissez Année, donnez un nom et validez
3. Vous verrez un nouvel élément est disponible dans la partie droite (avec P pour partition)
4. Ceci permet d'accéder à de nouvelles fonctionnalités de comapraison de corpus:

- Les spécificités qui permette de voir les mots les plus représentatifs de chaque partition
- L'analyse des correspondances qui va représenter graphiquement les mots proches et éloignés dans les différentes partitions
- Classification, qui va regrouper 2 à 2 les partitions

## Analyse Factorielle des Correspondances (AFC)

L'analyse factorielle des correspondances est une méthode statistique qui permet de mettre en évidence des relations entre des variables qualitatives. Dans le cas de TXM, les variables qualitatives sont les mots et les textes (sous-corpus). L'AFC permet de visualiser les relations entre les mots et ces textes dans un espace à deux dimensions.

1. Pour réaliser une AFC, il faut d'abord créer un ensemble de sous corpus, par exemple en utilisant la fonction "
   Partition" pour séparer les textes en deux groupes.
2. Ensuite, il faut lancer l'AFC en cliquant sur l'icône correspondante dans la barre d'outils.

# Glossaire

- [CQL ](https://txm.gitpages.huma-num.fr/textometrie/files/documentation/manual/0.7.9/fr/manual60.xhtml): Corpus
  Query Language, langage de requête pour les corpus textuels
- [AFC ](https://txm.gitpages.huma-num.fr/textometrie/files/documentation/manual/0.7.9/fr/manual44.xhtml#toc262): Analyse Factorielle des Correspondances,
  méthode statistique pour mettre en évidence des relations entre des variables qualitatives
- [POS ](https://txm.gitpages.huma-num.fr/textometrie/files/documentation/manual/0.7.9/fr/manual81.xhtml#toc431): Part of Speech, étiquette grammaticale
- [ADJ ](https://txm.gitpages.huma-num.fr/textometrie/files/documentation/manual/0.7.9/fr/manual81.xhtml#toc431): Adjectif
- [NOM ](https://txm.gitpages.huma-num.fr/textometrie/files/documentation/manual/0.7.9/fr/manual81.xhtml#toc431): Nom
- [frpos ](https://txm.gitpages.huma-num.fr/textometrie/files/documentation/manual/0.7.9/fr/manual81.xhtml#toc431):
  Propriété de TXM pour les étiquettes grammaticales
- Structure Article :
  Structure de texte dans TXM
- [Partition ](https://txm.gitpages.huma-num.fr/textometrie/files/documentation/manual/0.7.9/fr/manual41.xhtml#toc245):
  Fonctionnalité de TXM pour diviser un corpus en sous-ensembles
- [Progression ](https://txm.gitpages.huma-num.fr/textometrie/files/documentation/manual/0.7.9/fr/manual38.xhtml#toc239):
  Fonctionnalité de TXM pour étudier l'évolution de l'usage des mots dans le temps
- [Sous-corpus ](https://txm.gitpages.huma-num.fr/textometrie/files/documentation/manual/0.7.9/fr/manual40.xhtml#toc241):
  Sous-ensemble de textes d'un corpus
- [Spécificités ](https://txm.gitpages.huma-num.fr/textometrie/files/documentation/manual/0.7.9/fr/manual43.xhtml#toc253):
  Fonctionnalité de TXM pour identifier les mots les plus représentatifs d'un sous-corpus
- Analyse des Correspondances : Méthode statistique pour
  visualiser les relations entre les mots et les textes dans un espace à deux dimensions

# TODO

Cheat sheet cql


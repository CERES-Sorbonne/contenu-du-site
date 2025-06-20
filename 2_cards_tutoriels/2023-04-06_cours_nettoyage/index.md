---
uuid: 746b7a86-09af-480e-9140-57128c6fb933

title: Nettoyer, trier, indexer, explorer un corpus avec Notion
abstract: "Cet article offre une introduction sous forme de tutoriel au nettoyage, à l'indexation, au tri et à l'exploration de corpus textuels. Il est issu du cours de méthodes numériques proposé par Virginie Julliard, Félix Alié, Édouard Bouté et Victor Ecrement aux étudiant·es du master recherche du CELSA. Il est disponible en CC BY-SA 4.0, vous pouvez donc l'adapter en nous citant."
author:
    - victor
tags:
    - cours
    - notion
    - annotation
    - exploration
    - nettoyage
---

![big](Dither_it_Screenshot_2022-03-13_at_19.54.22.png)

<aside>

**Légende :**

- Les instructions sont en texte normal
- `Les éléments d’interface sont en code`

```
Les formules sont en bloc code
```

</aside>

## Qu'est-ce que Notion ?

[Notion](https://www.notion.so/) est un outil de gestion de projet en ligne

Il a des options de manipulation de bases de données et peut servir pour la recherche en sciences sociales

Les fonctions de base de données de Notion sont surtout utiles pour :

- Annoter des fragments textuels ou des images
- Stabiliser progressivement des catégories
- Explorer une base de données en triant, groupant, filtrant

Mais aussi pour d’autres usages, pas abordés aujourd’hui :

- Gérer des bases d’écrits de recherche
- Planifier et suivre des enquêtes avec beaucoup d’interlocuteur·rices
- Créer des espaces de travail en ligne pour des projets de recherche collectifs
- Mettre à disposition des bases de données interactives ou de petits sites internets sur le web.

Notion ne sert pas à grand chose pour :

- Réaliser des métriques ou des calculs à partir de données quantitatives
- Créer des visualisations
- Analyser automatiquement du texte ou des images

## Créer un compte et s’approprier l’outil

Notion a des “education plans”, ce qui donne la possibilité d’accéder à toutes les fonctions de l’outil sans rien payer tant qu’on est étudiant·e ou enseignant·e.

Les comptes gratuits sont également fonctionnels, mais limités dans la quantité de données qu’on peut importer et de documents qu’on peut créer.

Créer un compte enseignant·e ou étudiant·e sur Notion : [https://www.notion.so/fr-fr/product/notion-for-education](https://www.notion.so/fr-fr/product/notion-for-education)

Notion propose beaucoup de templates pour faire différentes choses, mais si vous ne construisez pas ces pages vous-mêmes, vous ne saurez pas comment les reproduire et vous prendrez plus de temps à vous approprier l’outil. Mieux vaut les supprimer.

Supprimer les fichiers de tutoriels

Créer un nouveau document avec le bouton `+ Ajouter une page` dans le panneau à gauche.

Notion est un très bon outil d’écriture, mais on va se concentrer sur les bases de données pour cette fois.

Écrire un peu

Créer une sous-page

## Importer des données

Pour cet exercice, on imagine qu’on fait une étude sur les stratégies professionnelles des acteur·rices de différents champs de la recherche sur le cancer : comment ils cherchent à gagner de la visibilité, se positionner publiquement, se mettre en lien, etc.

On va donc essayer d’analyser des tweets de la communauté anglophone de la recherche sur le cancer.

Télécharger puis importer dans Notion le fichier CSV des tweets sur la médecine :

[Tweets médecine small.csv](Tweets_medecine_small.csv)

Notion a du mal à importer des jeux de données de grande taille et affiche souvent `Import failed`. Parfois, changer de mode d’importation fonctionne, sinon, on peut faire des copier-coller depuis un logiciel de tableur comme Excel ou Numbers. En tout cas, ce logiciel n’est pas adapté pour importer des jeux de centaines de milliers de lignes.

Ce jeu de données comprend plusieurs types de champ : le nom du compte, le tweet, la date de création et des métriques. Les bases de données Notion ont plusieurs types de champs, parfois, le logiciel reconnaît de lui-même le type de champ, parfois il faut lui dire.

Vérifier que :

- les champs `comment_number`, `like_number`, `quote_tweet_number` et `retweet_number` sont au format `nombre`
- le champ `created_at` est au format `date`

## Parcourir et nettoyer ses données

Ces données ont été produites artificiellement, donc la notion de défaut n’a pas tellement de sens ici. Mais on va imaginer que les tweets ont été collectés à partir d’un ensemble de mots-clés sur Twitter, et donc qu’il y a potentiellement des tweets qui ne nous intéressent pas.

On va faire des tris et des requêtes dans notre base de données pour voir si des éléments indésirables s’y trouvent. Pour estimer la part de notre corpus qu’ils représentent, on peut activer un compte

En cliquant sur la barre en bas sous la colonne `Tweet`, activer l’option `Compter tout`

En parcourant les tweets, on peut voir qu’une organisation appelée “EORTC” est souvent mentionnée. C’est l’organisation européenne pour le traitement du cancer, qu’on a déjà étudiée dans d’autres démarches du mémoire.

Dans le champ `Tweet`, sélectionner `Filtrer` et écrire “eortc” dedans.

On voit qu’il y a 261 tweets sur 500 qui mentionnent l’eortc. C’est plus de la moitié, ça représente donc beaucoup de travail d’analyse pour des choses que l’on sait probablement déjà. Mieux vaut les masquer pour éventuellement les analyser plus tard.

Changer la mention `contient` dans le filtre, pour `ne contient pas`.

On peut remarquer aussi qu’il y a un tweet qui a beaucoup de citations, mais qui n’a ni like, ni retweet, ni commentaires. C’est une situation peu commune sur twitter, on peut donc se demander si notre collecte n’a pas eu un problème. On peut tester cette hypothèse en regardant si c’est le cas pour d’autres.

Dans le champ `quote_tweet_number`, sélectionner `Tri descendant`

On voit que parmi les tweets qui ont le plus de quote tweets, beaucoup ont 0 aux autres métriques. C’est totalement anormal sur twitter, donc la collecte a eu un problème. Il faudra revoir notre méthode et réimporter un autre jeu de données. Pour l’exercice, on va simplement écarter ces tweets anormaux de l’analyse.

Supprimer manuellement les tweets anormaux

## Créer un espace d’annotation

Maintenant que notre base de tweets est à peu près propre, on peut commencer l’analyse.

On cherche à distinguer les stratégies professionnelles pour différents champs de la cancérologie. On va donc devoir ajouter 2 propriétés pour décrire les tweets.

Sur notion, on peut créer des tags qu’on va pouvoir réutiliser et modifier sur toute une colonne. C’est très utile pour rendre comparable des éléments disparates.

Ajouter un champ `Sélection multiple` qu’on appellera `Sujet médecine` : les disciplines de médecine et les sujets de recherche mentionnés : oncologie, chirurgie, immunologie, oligométastases, etc.

Ajouter un champ `Sélection multiple` qu’on appellera `Visée` : diffuser une étude, proposer un poste, promouvoir un webinaire, interpeller les autorités, réagir à une nouvelle, etc.

On peut également rajouter une case pour signaler que le tweet est analysé.

Créer un champ `case à cocher` : “Analysé”

On peut avoir envie de prioriser les tweets qu’on veut voir en premier. Par exemple, ce serait intéressant d’extraire des mots-clés. Notion permet d’écrire des formules, comme dans Excel ou des programmes informatiques. On ne va pas apprendre la syntaxe de ces formules aujourd’hui, mais on peut faire beaucoup de choses avec !

Dans une nouvelle propriété `Formule`, copier-coller la formule suivante :

```
concat(if(contains(prop("Tweet"), "cancer"), "[cancer]  ", ""), if(contains(prop("Tweet"), "cell"), "[cell]  ", ""), if(contains(prop("Tweet"), "seminar"), "[seminar]  ", ""), if(contains(prop("Tweet"), "paper"), "[paper]  ", ""), if(contains(prop("Tweet"), "research"), "[research]  ", ""), if(contains(prop("Tweet"), "immunolog"), "[immunology]  ", ""), if(contains(prop("Tweet"), "radiation"), "[radiation]  ", ""), if(contains(prop("Tweet"), "biomark"), "[biomarker]  ", ""), if(contains(prop("Tweet"), "molecul"), "[molecule]  ", ""), if(contains(prop("Tweet"), "breast"), "[breast]  ", ""))
```

Les formules Notion ne tolèrent pas les retours à la ligne, les tabulations et les espaces multiples donc elle n’est pas très lisible. Voici à quoi elle ressemble avec quelques retours à la ligne.

```
concat(
    if(contains(prop("Tweet"), "cancer"), "[cancer]  ", ""), 
    if(contains(prop("Tweet"), "cell"), "[cell]  ", ""), 
    if(contains(prop("Tweet"), "seminar"), "[seminar]  ", ""), 
    if(contains(prop("Tweet"), "paper"), "[paper]  ", ""), 
    if(contains(prop("Tweet"), "research"), "[research]  ", ""), 
    if(contains(prop("Tweet"), "immunolog"), "[immunology]  ", ""), 
    if(contains(prop("Tweet"), "radiation"), "[radiation]  ", ""), 
    if(contains(prop("Tweet"), "biomark"), "[biomarker]  ", ""), 
    if(contains(prop("Tweet"), "molecul"), "[molecule]  ", ""), 
    if(contains(prop("Tweet"), "breast"), "[breast]  ", "")
  )
```

Cela va nous permettre de trier automatiquement nos tweets en fonction de cette colonne. On sait à peu près que s’ils contiennent des mots-clés similaires, ils traiteront des mêmes sujets et ce sera plus facile de leur attribuer des catégories.

Dans la colonne `Mots-clés`, faire un `Tri ascendant`.

Si on voulait commencer par les tweets qui ont le plus de visibilité, qui sont dans un sens les plus représentatifs de notre corpus, on pourrait également trier par le nombre de retweets. On peut également combiner les 2 tris.

Dans le tri en haut à gauche, `Ajouter un tri` pour `retweet_number` et le rendre `Descendant`. Ajuster l’ordre des tris en fonction de ce qui est considéré comme prioritaire.

## Annoter, trier

Annoter dans les champs `Sujet médecine` et `Visée`, cocher les cases une fois le tweet annoté.

Parfois, on créée beaucoup de tags et il devient difficile de s’y retrouver. Vous pouvez changer leur couleur et leur ordre pour créer implicitement des catégories de tags.

Modifier, colorer et trier les tags

Une fois qu’on a analysé beaucoup de tweets, il peut devenir intéressant de les cacher pour se concentrer sur le reste, et d’avoir une autre vue pour les modifier.

Dans les filtres `Ajouter un filtre`pour n'afficher que les lignes où `Analysé` n’est pas coché.

Dans l’onglet en haut à gauche du tableau, `Dupliquer` la vue et modifier le filtre pour n'afficher que les lignes où `Analysé` est coché.

## Explorer, analyser

Dans l’onglet en haut à gauche du tableau, `Dupliquer` la vue et l’appeler `Analyse`.

Si l’on a identifié les dates de certains évènements qui devraient avoir un impact sur l’expression en ligne de la communauté de recherche autour du cancer, on peut avoir besoin de les ordonner par jour. Comme on a beaucoup de tweets, il est impossible de jongler rapidement entre les jours. On va donc utiliser des groupes.

Dans le menu `•••` en haut à droite, sélectionner `Grouper par` `created_at`

Dans le même menu, sélectionner `Date par` `jour`

`Cacher les groupes vides`

On peut désormais se faire une idée de la quantité de tweets de notre corpus par jour, et lire ceux qui ont le plus de retweets pour se faire une idée de leur contenu. On peut également faire la même chose pour les tags qu’on a créés.

Dans le menu `•••` en haut à droite, sélectionner `Grouper par` `Sujet médecine`

Trier les groupes manuellement

Si l’on veut distinguer les stratégies professionnelles par champ de la médecine, on peut trier par visée à l’intérieur des groupes.

Supprimer les deux tris et les remplacer par un tri sur le champ `Visée`.

Si l’on repère un compte particulièrement actif, ou une formule que l’on retrouve souvent, on peut rapidement tester des hypothèses en les tapant dans la barre de recherche en haut à droite.

Chercher le nom d’un compte dans la barre de recherche en haut à droite.

Toutes ces options — trier, grouper, filtrer, rechercher — peuvent être utilisées pour tester des hypothèses. N’hésitez pas à créer de nombreuses vues pour regarder votre jeu de données de différentes manières.

<aside>

Si vous souhaitez aller plus loin, n'hésitez pas à lire notre [guide complet sur Notion pour la recherche en sciences sociales](https://ceres.sorbonne-universite.fr/e1700c76-c8eb-4cb1-841f-fcc2e9c57665/).

</aside>

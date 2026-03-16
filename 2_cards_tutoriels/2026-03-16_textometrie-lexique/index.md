
---
uuid: aa11afba-1614-49c3-aba6-57a1b7ec0005


prettyName: TextometrieLexique
title: "Lexique pour l'utilisation de logiciels de textométrie"
author:
    - rimane
    - marceau
tags:
    - tutoriel
    - corpus
    - textometrie
    - txm
    - antconc
    - lexique
    - terminologie
    - linguistique
---

# Lexique pour l'utilisation de logiciels de textométrie


## Terminologie grammaticale

- <span style=”color:blue”>**lemme**</span> : forme canonique d’un mot, la “version” du mot que l’on retrouverait dans le dictionnaire. Exemple : l’infinitif pour les verbes (dans un dictionnaire, pour trouver “voterions”, on chercherait le verbe à l’infinitif “voter”). La requête en <span style=”color:blue”>**CQL**</span> `[frlemma="voter"]` permet de retrouver toutes les flexions du verbe voter (voterais, voté, votera, votions, votent, …).
    
- <span style=”color:blue”>**radical / racine**</span> : plus petite partie lexicale permettant la production des mots d’une même famille (lumi ⇒ lumineux / lumière / illuminé / luminaire / … )
    
- <span style=”color:blue”>**casse**</span> (bas-de-casse / haut-de-casse) : de l’italien “cassa”, désignant à l’époque de l’imprimerie des caisses en bois compartimentées dans lesquelles étaient rangées les lettres en plomb. Les bas-de-casse regroupaient les lettres minuscules, les haut-de-casse les lettres capitales.  
    L’expression “respecter (strictement) la casse” signifie respecter les majuscules et minuscules du mot ou de l’expression.
    
    TXM permet d’ignorer la casse avec l’option `%c` après une requête (exemple `”Enquête”%c` trouvera `enquête` et `Enquête`)
    
- <span style=”color:blue”>**diacritique**</span> : signe accompagnant une lettre et qui peut en modifier la prononciation (accents, cédilles, tréma, tilde, …).
    
    TXM permet d’ignorer la présence de diacritiques avec l’option `%d` après une requête (exemple `”hôtel”%d` trouvera `hôtel` et `hotel`)
    
- <span style=”color:blue”>**pos / part of speech / partie du discours**</span> : catégorie grammaticale à laquelle appartient le mot, c’est-à-dire sa nature (nom, verbe, adjectif, nom propre, préposition…).
    
- <span style=”color:blue”>**hapax**</span> : mot qui n’apparaît qu’une seule fois dans le corpus d’étude.
    
- <span style=”color:blue”>**élision**</span> : chute de la voyelle finale d’un mot lorsqu’elle se trouve confrontée à la voyelle initiale du mot suivant (ou un h muet). Exemple : je + ai = j’ai ; de + aujourd’hui = d’aujourd’hui ; le + habit = l’habit, etc.
    
- <span style=”color:blue”>**mots-outils**</span> : les mots les plus fréquents d’un corpus (des déterminants, des prépositions, des articles…). Souvent courts / monosyllabiques, ils permettent néanmoins d’étudier la structure d’un texte, ou encore le style des auteur⋅ice⋅s.
    
- <span style=”color:blue”>**pronom personnel sujet**</span> : remplace un nom ou un groupe nominal : _je, tu, il, elle, on, nous, vous, ils, elles_. Attention _:_ à ne pas confondre avec : _mon, mes, ton, ta, vos, leur_ (etc.) qui sont des déterminants possessifs.  
    

## Terminologie propre aux logiciels de textométrie

- <span style=”color:blue”>**Bordures de mot**</span> : Limites de début et fin d'un mot. En RegEx, le métacaractère `\b` représente cette classe. On y retrouve : les débuts de texte (`^`), les fin de texte (`$`), les espaces (`\s`) (espace normal (` `), tabulation (`\t`), retour à la ligne (`\n`), ...) et les ponctuations (`[,?;.:!]`).  

- <span style=”color:blue”>**Token**</span> : Unité minimale considérée par l'outil, pour TXM, toute suite de caractères entre deux <span style=”color:blue”>**bordures de mots**</span>.

- <span style=”color:blue”>**CQL**</span> : Corpus Query Language - Le langage de requêtage utilisé par TXM, permet de requêter sur des formes (mots), mais aussi sur les étiquettes présentes (lemme, locuteur, pos, année, …)
    
- <span style=”color:blue”>**CQP**</span> : Corpus Query Processor - L’outil qui interprète une requête <span style=”color:blue”>CQL</span> et cherche les résultats correspondants.
    
- <span style=”color:blue”>**expression régulière**</span> : syntaxe à caractères spéciaux qui permet de combiner un ensemble de requêtes en une seule saisie. Elle ne concerne pas que les outils de textométrie : elle peut s’utiliser sur des logiciels très variés et même en programmation.
    
- <span style=”color:blue”>**concordance**</span> : fonctionnalité de recherche qui affiche le mot pivot* ou l’expression recherchée dans son contexte* gauche et droit. On parle aussi de concordancier pour désigner l’outil ou le logiciel qui permet ce type de recherche.
    
- <span style=”color:blue”>**pivot**</span> : mot ou expression que l’on cherche à requêter.
    
- <span style=”color:blue”>**contexte**</span> (gauche et droit) : l’ensemble des mots qui précèdent (contexte gauche) et suivent (contexte droit) le mot ou l’expression pivot. Il est possible de régler le contexte en ajustant le nombre de mots qui s’affichent à gauche et à droite du mot pivot. Pour avoir un contexte complet, c’est-à-dire un retour au texte, il suffit de double-cliquer sur l’occurrence qui vous intéresse.
    
- <span style=”color:blue”>**co-occurrence**</span> : fonctionnalité de recherche qui permet d’afficher les mots qui apparaissent le plus fréquemment dans le voisinage du mot pivot* saisi (soit juste à côté, soit avant / plus loin dans la phrase).
    
- <span style=”color:blue”>**balise**</span> : dans les langages de balisages (HTML, XML et autres), les balises permettent de structurer les données et d’y apposer des <span style=”color:blue”>métadonnées</span>. Par exemple `<div type=”Acte” n="2">…</div>` permet de signaler que le contenu de la balise appartient à l’acte 2 d’une pièce. Second exemple, la balise `<w pos=”pronom” lemme=”je”>j'</w>` permet de signaler des informations sur le mot `j’` .
    
- <span style=”color:blue”>**étiquette**</span> : dans TXM, une étiquette est une <span style=”color:blue”>métadonnée</span> apposée à un mot, notamment par le biais des <span style=”color:blue”>balises</span> `<w>` . On parle le plus souvent d’étiquettes morphosyntaxiques qui qualifient quant à elles les informations morphologiques et syntaxiques apposées à un mot (pos, lemme, genre, nombre, …).
    
- <span style=”color:blue”>**métadonnées**</span> : les données sur les données = toutes les informations autour des données qui apportent des précisions supplémentaires sur celles-ci ; en d’autres termes, tout ce qui concerne vos données sauf le contenu même de vos données. Exemple : l’information “locuteur” dans le corpus VOEUX est inscrite dans les métadonnées. (C’est l’équivalent du paratexte = tout ce qui concerne le texte mais qui n’est pas le texte lui-même.)
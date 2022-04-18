# N-body-problem

# Table des matières
1. [Le problème à n corps](#problème) <br>
  a. Qu’est-ce que le problème à n corps ? <br>
  b. Pourquoi le problème à n corps est intéressant et quelques exemples d’applications <br>
  c. Problème à n corps et théorie du chaos <br>
  d. L’avantage des simulations informatiques <br>
3. [Simulation du problème à n corps](#simulation) <br>
  a. Approche conceptuelle du problème <br>
		i. L’approche Particule-Particule <br>
		ii. Restriction au cas à 2 corps <br>
		iii. Généralisation de l’approche à plusieurs corps <br>
  b. Mise en lien entre l’approche conceptuelle et l’implémentation python <br>
		i. Avant le code, qu’est-ce qu’un intégrateur numérique ? <br>
		ii. Implémentation python <br>
5. [Sources bibliographiques](#bib)
6. [Remerciements](#merci)


## Le problème à n corps <a name="problème"></a>
### Qu'est-ce que le problème à n corps ?
Le problème à n corps consiste à prédire le mouvement des astres dans l’espace en fonction de 
certaines conditions initiales [5]. En effet, c’est grâce à Newton qui, en 1687 publia « Philosophiae 
naturalis principia mathematicaon » que l’on put s’intéresser aux différentes interactions entre les 
corps. Dans cet ouvrage, Newton énonça ce que l’on appelle aujourd’hui les lois du mouvement de 
Newton. Grâce à celles-ci, on a pu étudier le déplacement de 2 corps orbitant l’un autour de l’autre 
dans l’espace et sans aucune autre interaction gravitationnelle extérieure [7].

Malheureusement, une fois que l’on veut appliquer les lois du mouvement dans un système à 3 
corps ou plus, le mouvement devient chaotique. De fait, c’est grâce à la publication du théorème de 
récurrence dans l’article « Sur le problème des trois corps et les équations de la dynamique » de Henri 
Pointcarré que l’on a pu affirmer qu’il n’existait pas de solution analytique au problème à 3 corps [6].
Par contre, cela n’implique pas que le problème est insoluble, mais il faut nécessairement avoir recours 
à des techniques d’approximation ou des techniques numériques pour pouvoir résoudre le problème.

Heureusement, la puissance des ordinateurs actuels permet aujourd’hui d’augmenter les capacités 
de calcul et donc de faire des simulations différentes très rapidement en fonction des conditions 
initiales du système.

En guise de conclusion, le problème à n corps consiste donc à étudier les différentes interactions 
entre les corps et à prédire le mouvement des planètes dans le temps pour certaines conditions 
initiales.

### Pourquoi le problème à n corps est intéressant et quelques exemples d’applications
Le problème à n corps est intéressant dans le domaine spatial. De plus, on peut aussi le retrouver 
dans les sciences biologiques ou encore le machine learning [5]. Cependant, la complexité des termes 
dans ces domaines ainsi que le manque d’articles scientifiques fondés, empêchent une bonne 
reformulation de l’utilisation du problème à n corps dans ces domaines et ne sera donc pas explicité 
ici. 

Tout d’abord, dans le domaine spatial, le problème à n corps peut être utilisé dans la prédiction du 
mouvement d’un astéroïde. Ce qui est très intéressant puisque plusieurs centaines d’astéroïdes frôlent 
ou rentrent en collision avec notre planète chaque année. 
La prédiction du mouvement des planètes est aussi très importante en ce qui concerne 
l’exploration spatiale. On peut comprendre l’utilité du problème à n corps dans l’exploration de la 
planète Mars. De fait, la planète Mars tourne autour du soleil beaucoup moins vite que la Terre ; la 
distance entre la Terre et Mars varie donc de plusieurs millions de kilomètres au cours d’une année. Il 
faut donc savoir précisément où se trouve la planète rouge lorsqu’elle est au plus proche de la Terre 
afin de pouvoir minimiser le trajet [1].

Enfin, le problème est aussi pris en compte dans les cas de calculs d’orbites de stationnement de 
certains satellites [3].

### Problème à n corps et théorie du chaos
Le problème à n corps fait partie de ce qu’on appelle la théorie du chaos. La plupart du temps, la 
théorie du chaos est plutôt présentée dans le cadre de la mécanique classique et non céleste. 
Cependant, il est intéressant de se pencher sur la théorie du chaos afin de pouvoir aborder
correctement l’impossibilité de prédiction du mouvement de plusieurs corps dans l’espace.

De ce fait, il est intéressant de se pencher sur un problème classique de la mécanique newtonienne 
afin de comprendre cette théorie du chaos. C’est-à-dire le cas du pendule double ou encore et 
simplement l’étude de la météo. Ces deux systèmes dépendent énormément des conditions initiales. 
Par exemple, en changeant l’angle de 1° entre deux systèmes contenant un pendule double, leurs 
trajectoires seront totalement différentes. On comprend dès lors aisément que pour prédire le 
mouvement du pendule il faudrait mesurer avec une infinie précision les conditions initiales du 
système.

En conclusion, aussi gros que les planètes puissent nous paraître, si l’on faisait des calculs de 
prédiction de leurs trajectoires avec un millimètre de différence aux conditions initiales, leurs 
mouvements en seraient grandement influencés. Par exemple, si l’on voulait calculer le mouvement 
des planètes du système solaire sur une dizaine de millions d’années, alors il faudrait donner la position 
initiale des planètes au mètre près sinon leurs mouvements en seraient totalement imprévisibles [4].
Il est dès lors très difficile d’en prédire l’allure. Il serait alors naturel de se dire que le problème est 
irrésolvable. Cependant, il existe certains outils mathématiques permettant d’approximer la solution 
du problème.


## Simulation du problème à n corps <a name="simulation"></a>
### Approche conceptuelle du problème
#### L’approche Particule-Particule
Tout d’abord, il est important de s’abstraire de l’implémentation du code python et d’aborder en 
premier lieu l’approche globale que l’on va utiliser pour simuler le système. En effet, il faut savoir qu’il 
existe une multitude de méthodes pour simuler le problème à n corps. L’approche la plus simple est la 
méthode Particule-Particule.

Cette méthode consiste à trouver toutes les forces qui s’exercent sur les différents corps du 
système pour ensuite trouver la force résultant de chaque système. De cette force, il sera possible d’en 
déduire l’accélération de chaque corps. Grâce à ces données, il suffira d’intégrer les équations de 
mouvements afin d’avoir les trajectoires de chaque corps [2]. 

#### Restriction au cas à 2 corps
Dans un premier temps, contentons-nous de l’interaction gravitationnelle entre 2 corps afin de 
pouvoir introduire l’origine des forces entre les corps. Comme dit précédemment, d’après l’énoncé de 
la loi de gravitation universelle, 2 corps s’attirent de par leurs masses. De manière moins vulgaire,
l’énoncé de la loi universelle est la suivante : « Deux corps ponctuels de masses respectives ma et mb
s'attirent avec des forces vectoriellement opposées et de même valeur absolue. Cette valeur est 
proportionnelle au produit des deux masses, et inversement proportionnelle au carré de la distance 
qui les sépare. » Cette loi adaptée au formalisme mathématique donne 𝐹 = 𝐺\*𝑚1\*𝑚2/𝑟^2, 𝐺 =6.67 × 10−11m3 kg-1 s-2
m1 et m2 représentent la masse respective des 2 corps (en kg) ; r est la distance entre les 2 corps (en 
mètre) ; G est appelée la constante gravitationnelle.

#### Généralisation de l’approche à plusieurs corps

### Mise en lien entre l’approche conceptuelle et l’implémentation python
#### Avant le code, qu’est-ce qu’un intégrateur numérique ?
#### Implémentation python

## Sources bibliographiques <a name="bib"></a>

## Remerciements <a name="merci"></a>

Pour la prise de photo sa se trouve dans Interface_entree
Pour modifier le nom du fichier que vous voulez il suffit de modifier la valeur de la variable filename dans la fontion Prendre_Photos

Pour les mouvements, tout est dans Interface_mouvement.
Les behaviors sont créé dans choregraphe et importé dans nao dans le dossier behaviors
On utilise un proxy qui les appelle.
Comme marquer dans les commentaire de la classe pour les mouvements pour le debut et fin de jeu ainsi que pour les actions de victoire et défaite il faut laisser un certain temps pour éviter des problèmes.

L'action défaite et dans la liste de la classe, mais pas encore créée sur nao c'est prévu jeudi si j'ai le temps. Sinon lundi après midi prochain.

lorsque vous attendez une reponse sur l'un des bumpers il faut rester appuyer 1secondes dessus.

Apres dans le Main_P4 j'ai import vos fichiers IA et plateau qui était sur le git. Mais j'ai pas finis d'insérer les fonctions dans le programmes.
Pareil dans le main il manque a la fin des tours la vérification des résultats.
Il manque la résolution de la photos aussi
J'ai pas finis de tester le main complétement lundi soir. Normalement jeudi je dois vérifier l'attente et la confirmation de fin de tour du joueur humain.
Pareil je vais amener le jeu du P4 et le faire tourner complètement avec le plateau.


Pour info sur nao cmake et make sont pas dispo c'est sur est certain. Le dossier OpenCV en version 3.00 et dans le dossier P4 mais du coup il sert a rien ....

Je me rapelle plus de la version d'openCV qui est sur nao.

Tenez moi informé par rapport la résolution de l'image si vous avez trouver une solution.

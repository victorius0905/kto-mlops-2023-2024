/*Des jeux de données plus grands peuvent nécessiter des batch sizes plus importants 
pour une convergence efficace, tandis que des modèles plus complexes peuvent nécessiter plus 
d'epochs pour une convergence optimale

Un batch size plus grand peut 
accélérer le processus d'entraînement 
car il exploite mieux les capacités de calcul parallèle des GPU. 
Cependant, des batch sizes trop grands peuvent également entraîner une convergence instable 
ou une surcharge de la mémoire GPU. Il faut donc essayer différentes valeurs de batch size pour trouver 
celle qui offre le meilleur compromis entre vitesse d'entraînement et stabilité de convergence.


Le nombre d'epochs détermine combien de fois l'ensemble de données d'entraînement sera parcouru 
pendant le processus d'entraînement. Augmenter le nombre d'epochs peut permettre au modèle 
de mieux s'ajuster aux données, 
mais cela peut également entraîner un surapprentissage si trop d'epochs sont utilisés. 

On peut modifier les paramètres présents dans le fichier train.py 
qui sont :
batch_size = args.batch_size
epochs = args.epochs
avec la commande :
python train.py --batch_size 32 --epochs 10

On modifie les paramètres dans ce fichier parce que c'est celui qui contient les données 
d'entrainement
*/

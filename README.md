# STL Export Shortcut for Blender

Addon Blender pour exporter rapidement la sélection en STL avec un raccourci clavier.

## 🎯 Fonctionnalités

- Raccourci clavier **Ctrl + Shift + E** pour ouvrir l'export STL
- "Sélection uniquement" activé automatiquement
- Nom de fichier suggéré basé sur l'objet sélectionné
- Logique intelligente pour les sélections multiples : l'objet avec le plus de vertices est utilisé pour le nom
- Compatible Blender 4.5+

## 🚀 Utilisation

1. Sélectionnez un ou plusieurs objets
2. Appuyez sur **Ctrl + Shift + E**
3. La fenêtre d'export STL s'ouvre avec "Sélection uniquement" activé
4. Validez ou modifiez le nom et exportez

### Convention de nommage

- **Un seul objet** : `[nom du fichier] - [nom de l'objet]` (ou juste `[nom de l'objet]` si non sauvegardé)
- **Plusieurs objets** : Le nom est basé sur l'objet ayant le plus de vertices

## ⚙️ Configuration

Le raccourci clavier peut être modifié dans :
`Edit` → `Preferences` → `Keymap` → recherchez "Export Selection to STL"

## 📋 Prérequis

- Blender 4.5 ou supérieur (LTS)
- Pas de dépendances externes

## 📝 Dernière mise à jour

**Commit** : "Enhance STL export operator with vertex count logic"
- Ajout de la fonctionnalité de détection de l'objet principal basée sur le nombre de vertices
- Mise à jour de la convention de nommage pour les fichiers exportés

## 📜 Licence

MIT License

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 💬 Support

Si vous rencontrez un problème, ouvrez une [issue](https://github.com/Gwabix/blender-stl-export-shortcut/issues).

– Réalisé à l'aide de Claude Sonnet 4.5 –

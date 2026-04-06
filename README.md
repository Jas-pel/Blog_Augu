
# 🇮🇹 100 Semaines à UWC
### Le journal de bord d'Augustin Tremblay

![Augustin UWC Adriatic Hero](hero.png)

Bienvenue sur le dépôt officiel du blog **"100 Semaines à UWC"**. Ce projet transforme les 113 pages de souvenirs, de réflexions et d'aventures d'Augustin au **Collège du Monde Uni de l'Adriatique** (Duino, Italie) en une expérience web immersive et élégante.

---

## ✨ Caractéristiques

- 📖 **Récit chronologique** : Navigation fluide à travers les 4 semestres (Terms) de 2023 à 2025.
- 🎨 **Design Premium** : Une esthétique minimaliste inspirée de la mer Adriatique, alliant typographie classique et modernité.
- 📱 **Entièrement Responsive** : Accessible sur tous les appareils, du smartphone à l'ordinateur de bureau.
- ⚡ **Statique & Rapide** : Propulsé par du Vanilla HTML/JS pour une performance optimale.

---

## 🛠️ Stack Technique

- **Frontend** : HTML5, CSS3, JavaScript (ES6+).
- **Processing** : Python 3.x avec `pypdf` pour l'extraction et la structuration des données.
- **Hosting** : GitHub Pages.

---

## 📂 Structure du Projet

```text
├── docs/             # Dossier du site (GitHub Pages)
│   ├── index.html    # Squelette de l'application
│   ├── styles.css    # Design system & styles
│   ├── app.js        # Moteur de rendu dynamique
│   ├── data.js       # Données structurées du journal
│   └── hero.png      # Illustration exclusive du blog
├── scripts/          # Outils de traitement Python
└── raw/              # Sources textuelles originales
```

---

## 🚀 Installation & Développement local

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Jas-pel/Blog_Augu.git
   ```
2. Ouvrez `index.html` (dans `/docs/`) dans votre navigateur ou lancez un serveur local :
   ```bash
   npx http-server ./docs
   ```

---

## 🔄 Mise à jour des données

Si vous souhaitez modifier le script d'extraction ou retraiter le texte source :
1. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
2. Placez votre fichier source dans `/raw/`.
3. Lancez le script de traitement :
   ```bash
   python scripts/process_journal.py
   ```
   *Note: Le script mettra à jour automatiquement `docs/data.js`.*

---

## 🌐 Déploiement GitHub Pages

Pour que le site soit visible en ligne :
1. Allez dans les **Settings** de votre dépôt sur GitHub.
2. Cliquez sur **Pages** (barre latérale).
3. Sous "Build and deployment" > "Branch", sélectionnez **Main** et le dossier **/docs**.
4. Cliquez sur **Save**.

---

## 📜 Crédits & Licence

- **Auteur** : Augustin Tremblay
- **Design & Développement** : Antigravity (Powered by Google DeepMind)
- **Institution** : UWC Adriatic (Duino, Italie)

---
*Fait avec ❤️ pour immortaliser deux années inoubliables.*

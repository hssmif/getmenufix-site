"""Guides in French for restaurant owners in France (SEO). Built by _build.py into fr/guides/*.html.
Adapted from the English guides, not translated word for word: euros, prix TTC, Deliveroo and Just Eat instead of
DoorDash and Menulog. Same rules: practical and honest, no invented numbers or promises, no dashes and never join words
with a hyphen (so no "best-seller", "vous-même", "c'est-à-dire"), French punctuation.
"alt" is the slug of the English guide on the same topic."""

GUIDES_FR = [
    {
        "slug": "plus-de-commandes-uber-eats",
        "alt": "get-more-orders-on-uber-eats",
        "answer": "Pour recevoir plus de commandes sur Uber Eats, rendez votre page facile à choisir : vos plats les plus vendus en premier, des photos lumineuses de vos vrais plats, des noms compréhensibles, une description courte pour chaque article et un menu court, toujours à jour.",
        "faq": [("Comment avoir plus de commandes sur Uber Eats ?", "Placez vos plats les plus vendus en haut, ajoutez des photos claires de vos vrais plats, écrivez des descriptions courtes, corrigez les fautes et gardez votre menu à jour. Votre page devient plus facile à choisir."),
                ("Les photos aident elles vraiment sur Uber Eats ?", "Oui. Un plat sans photo passe facilement inaperçu, et sans photo de votre part Uber Eats peut afficher des photos prises par des clients. Commencez par vos meilleures ventes."),
                ("Combien de catégories faut il sur un menu Uber Eats ?", "Le moins possible : regroupez les plats comme les clients commandent (entrées, plats, accompagnements, boissons, desserts) et supprimez les catégories vides ou en double.")],
        "title": "Plus de commandes sur Uber Eats : 9 améliorations pour votre menu",
        "short": "Plus de commandes sur Uber Eats",
        "desc": "Des conseils concrets pour les restaurants et cafés indépendants : rendre leur page Uber Eats plus appétissante et plus simple à commander. Photos, noms, descriptions, catégories.",
        "img": "spread",
        "related": ["descriptions-menu-uber-eats", "photo-banniere-uber-eats", "categories-menu-uber-eats"],
        "lead": "La plupart des clients décident en quelques secondes s'ils commandent chez vous. Ces neuf changements rendent votre page Uber Eats plus facile à choisir, et la plupart se font en une semaine.",
        "body": """
<h2>1. Mettez vos meilleures ventes en haut</h2>
<p>Les clients font défiler moins qu'on ne le pense. Uber Eats affiche une rangée « Populaires », mais votre première catégorie compte aussi. Placez y les cinq ou six plats les plus commandés, avec un nom clair comme <b>Les plus populaires</b> ou <b>Nos incontournables</b>.</p>

<h2>2. Une vraie photo pour chaque plat phare</h2>
<p>Un plat sans photo est facile à ignorer. Pas besoin de studio : un téléphone, la lumière d'une fenêtre et une assiette propre suffisent. Cadrez de légèrement en biais, remplissez l'image avec le plat et évitez la cuisine en arrière plan. Commencez par vos dix meilleures ventes.</p>

<h2>3. Des noms que tout le monde comprend</h2>
<p>« Formule 3 », « Menu BBQ L » ou un nom que seuls vos habitués connaissent n'aident pas un nouveau client. Dites ce que c'est : <b>Wrap poulet shawarma</b> plutôt que « Wrap », <b>Raviolis porc et ciboulette (10)</b> plutôt que « Raviolis 10p ». Gardez vos noms maison, mais ajoutez ce qu'est le plat.</p>

<h2>4. Une courte description pour chaque article</h2>
<p>Une ligne suffit : les ingrédients principaux et un détail qui fait la différence. « Bœuf effiloché cuit lentement, oignons pickles et mayo chipotle dans un brioché toasté » vend bien mieux qu'un vide. Notre <a href="/fr/guides/descriptions-menu-uber-eats.html">guide des descriptions de plats</a> donne des exemples à reprendre.</p>

<h2>5. Corrigez fautes et majuscules</h2>
<p>Les noms EN MAJUSCULES, les fautes et les mots manquants donnent une impression de travail bâclé, et les clients se demandent si la cuisine l'est aussi. Une relecture attentive prend vingt minutes et ne coûte rien.</p>

<h2>6. Des catégories courtes et logiques</h2>
<p>Dix catégories de deux plats chacune sont difficiles à parcourir. Organisez le menu comme les clients commandent : entrées, plats, accompagnements, boissons, desserts, ou petit déjeuner, déjeuner, cafés pour un café. Voir notre guide pour <a href="/fr/guides/categories-menu-uber-eats.html">organiser vos catégories</a>.</p>

<h2>7. Indiquez ce que chaque option comprend</h2>
<p>Tailles, nombre de pièces et contenu des formules doivent être clairs avant l'ajout au panier. « Grande (pour 2) » ou « avec frites et boisson » répond à la question avant qu'elle soit posée.</p>

<h2>8. Soignez la photo de bannière</h2>
<p>La grande photo en haut de votre page est la première chose que l'on voit. Choisissez une photo lumineuse et appétissante de votre plat le plus aimé, pas votre devanture ni un logo sur fond uni. Plus de conseils dans notre guide sur la <a href="/fr/guides/photo-banniere-uber-eats.html">photo de bannière</a>.</p>

<h2>9. Gardez le menu à jour</h2>
<p>Plats épuisés, anciens prix et plats que vous ne faites plus entraînent des commandes annulées et des avis déçus. Vérifiez votre menu à chaque changement, et mettez en pause un article épuisé au lieu de le laisser en ligne.</p>

<h2>Et les notes ?</h2>
<p>Votre note dépend de choses que vous ne maîtrisez pas entièrement : délais, livreur, tenue du plat pendant le trajet. Une page claire et exacte aide en donnant les bonnes attentes, pour que ce qui arrive corresponde à ce que le client a vu. C'est la partie sur laquelle nous travaillons.</p>
""",
    },
    {
        "slug": "descriptions-menu-uber-eats",
        "alt": "write-uber-eats-menu-descriptions",
        "answer": "Une bonne description de plat sur Uber Eats tient en 10 à 25 mots : dites ce qu'est le plat, citez ses ingrédients principaux et ajoutez un détail qui le rend unique, comme la cuisson ou l'origine d'un produit.",
        "faq": [("Quelle longueur pour une description sur Uber Eats ?", "En général une ou deux phrases courtes, environ 10 à 25 mots. Sur les applications de livraison, les clients survolent."),
                ("Que mettre dans une description de plat ?", "Ce qu'est le plat, ses ingrédients principaux et un détail qui le rend unique. Ajoutez le niveau d'épices, la portion et les mentions végétarien ou sans gluten quand c'est utile et vrai."),
                ("Quels mots éviter ?", "Les compliments vagues comme délicieux ou incroyable, les MAJUSCULES, les codes internes et les promesses que vous ne pouvez pas tenir.")],
        "title": "Écrire des descriptions de plats qui donnent envie sur Uber Eats (avec exemples)",
        "short": "Des descriptions de plats qui vendent",
        "desc": "Une méthode simple et des exemples concrets pour écrire des descriptions courtes et appétissantes sur Uber Eats : burgers, curry, pizza, café et plus.",
        "img": "desk",
        "related": ["plus-de-commandes-uber-eats", "categories-menu-uber-eats", "repondre-avis-uber-eats"],
        "lead": "Une bonne description est courte, précise et donne faim. Voici une méthode simple, avec des exemples avant et après à adapter.",
        "body": """
<h2>La méthode : ce que c'est, ce qu'il y a dedans, pourquoi c'est bon</h2>
<p>Les meilleures descriptions suivent trois étapes, en une ou deux phrases courtes :</p>
<ol><li><b>Ce qu'est le plat</b>, si le nom ne le dit pas déjà.</li><li><b>Les ingrédients principaux</b>, ceux qui comptent pour le client.</li><li><b>Un détail</b> qui vous ressemble : la cuisson, l'origine, la façon de servir.</li></ol>
<p>Visez 10 à 25 mots. Les clients survolent, alors commencez par les mots les plus gourmands.</p>

<h2>Exemples avant et après</h2>
<table class="compare"><tr><th>Avant</th><th>Après</th></tr>
<tr><td>Burger bœuf</td><td>Double steak smashé, cheddar affiné, pickles et sauce maison dans un pain brioché toasté.</td></tr>
<tr><td>Butter chicken</td><td>Poulet mijoté dans une sauce tomate et beurre onctueuse, légèrement épicée. Servi avec riz basmati.</td></tr>
<tr><td>Margherita</td><td>Tomate San Marzano, fior di latte et basilic frais sur notre pâte maturée, cuite au feu de bois.</td></tr>
<tr><td>Bo bun</td><td>Vermicelles de riz, bœuf sauté à la citronnelle, nems, crudités, herbes fraîches et cacahuètes.</td></tr>
<tr><td>Café crème</td><td>Notre espresso maison et un lait chauffé bien onctueux. Lait d'avoine possible, à préciser en note.</td></tr>
<tr><td>Brownie</td><td>Brownie fondant au chocolat noir, fait maison chaque matin.</td></tr></table>

<h2>Les mots qui aident, et ceux à éviter</h2>
<p><b>Utiles :</b> la cuisson (mijoté, au feu de bois, croustillant, grillé), la texture (croquant, onctueux, fondant), la fraîcheur (fait maison, préparé chaque jour) et les portions claires (pour 2, 10 pièces).</p>
<p><b>À éviter :</b> les compliments vagues (délicieux, incroyable, le meilleur du quartier), les MAJUSCULES, les codes internes et les promesses invérifiables. Laissez les ingrédients parler.</p>

<h2>N'oubliez pas les détails pratiques</h2>
<ul><li>Le niveau d'épices des plats relevés (doux, moyen, fort).</li><li>Les mentions végétarien, vegan ou sans gluten, uniquement si elles sont vraies.</li><li>Le contenu exact des formules et menus.</li></ul>

<h2>Restez honnête</h2>
<p>Décrivez le plat tel qu'il arrive. Si la photo ou le texte promet plus que l'assiette, le client le remarque, et cela se voit dans les avis.</p>

<p>Vous préférez que nous réécrivions tout votre menu ? Nous envoyons d'abord une maquette gratuite pour que vous voyiez la différence avant de décider.</p>
""",
    },
    {
        "slug": "photos-uber-eats-exigences",
        "alt": "uber-eats-photo-requirements",
        "title": "Photos Uber Eats : formats, tailles et raisons de refus (2026)",
        "short": "Les exigences photo d'Uber Eats",
        "desc": "Les règles photo d'Uber Eats pour les restaurants : format 5:4, 2880 × 2304 pixels, JPG de 10 Mo maximum, un seul article par photo, et les raisons de refus les plus fréquentes.",
        "img": "burger-after",
        "related": ["photos-plats-telephone", "photo-banniere-uber-eats", "modifier-menu-uber-eats-manager"],
        "lead": "Chaque photo sur Uber Eats est vérifiée avant sa mise en ligne. Voici ce que demande Uber, d'après ses propres pages d'aide pour les marchands, et comment éviter les refus.",
        "answer": "Uber Eats demande des photos en paysage au <b>format 5:4</b>, idéalement <b>2880 × 2304 pixels</b>, en <b>JPG de 10 Mo maximum</b> (PNG et GIF sont aussi acceptés pour les articles). Chaque photo montre <b>un seul article</b>, centré, tel qu'il est servi, <b>sans texte, prix, logo, filigrane ni visage</b> (les mains sont acceptées). Les photos sont vérifiées avant d'être publiées.",
        "faq": [
            ("Quelle taille pour les photos Uber Eats ?", "Uber recommande 2880 × 2304 pixels, soit un format 5:4. Les photos doivent faire au moins 550 pixels de large et 440 de haut, et 10 Mo au maximum."),
            ("Quel format d'image utilise Uber Eats ?", "5:4, en paysage. L'application affiche aussi des vignettes carrées : gardez le plat bien centré avec un peu d'espace autour."),
            ("Pourquoi ma photo Uber Eats a été refusée ?", "Les raisons habituelles : plusieurs articles sur la photo, du texte ou un logo sur l'image, un visage, une photo floue ou sombre, ou une photo de banque d'images au lieu de votre vrai plat."),
            ("Peut on utiliser des photos de banque d'images ?", "Non. Les photos doivent montrer votre propre plat, tel que le client le reçoit."),
            ("Peut on retoucher ses photos ?", "Oui, tant que la photo montre fidèlement votre vrai plat. Améliorer la lumière, les couleurs et le fond est possible ; modifier le plat ne l'est pas."),
        ],
        "body": """
<h2>Les exigences photo d'Uber Eats en un coup d'œil</h2>
<table class="compare"><tr><th>Quoi</th><th>Exigence</th></tr>
<tr><td>Format</td><td>5:4, paysage</td></tr>
<tr><td>Taille recommandée</td><td>2880 × 2304 pixels</td></tr>
<tr><td>Taille minimale</td><td>550 pixels de large, 440 de haut</td></tr>
<tr><td>Type de fichier</td><td>JPG (PNG et GIF acceptés pour les articles)</td></tr>
<tr><td>Poids maximal</td><td>10 Mo</td></tr>
<tr><td>Image de couverture</td><td>5:4, 2880 × 2304 pixels, JPG</td></tr></table>

<h2>Ce que chaque photo doit montrer</h2>
<ul><li>Un seul article, exactement tel que le client le reçoit.</li><li>Le plat centré dans l'image.</li><li>Une photo nette et bien éclairée de votre vrai plat.</li></ul>

<h2>Ce qui fait refuser une photo</h2>
<ul><li>Plusieurs articles sur la photo, sauf s'ils sont vendus ensemble.</li><li>Du texte, des prix, des promotions ou des bandeaux sur l'image.</li><li>Un logo ou un filigrane ajouté par dessus.</li><li>Des personnes ou des visages (des mains qui tiennent le plat sont acceptées).</li><li>Une photo floue, sombre ou trop petite.</li><li>Une photo de banque d'images ou qui ne montre pas votre plat.</li></ul>

<h2>Astuces pour gagner du temps</h2>
<ul><li><b>Cadrez large, recadrez en 5:4.</b> Prenez la photo avec de l'espace autour du plat, puis recadrez. C'est plus simple que de viser la bonne taille dès la prise de vue.</li><li><b>Restez centré.</b> L'application affiche de petites vignettes carrées : ce qui est près des bords peut être coupé.</li><li><b>Commencez par vos meilleures ventes.</b> Ce sont les plus vues.</li><li><b>Anticipez la vérification.</b> Les nouvelles photos sont contrôlées avant de s'afficher : envoyez les quelques jours avant un changement de carte.</li></ul>

<h2>Comment prendre les photos</h2>
<p>Pas besoin de photographe. Notre guide pour <a href="/fr/guides/photos-plats-telephone.html">prendre de belles photos au téléphone</a> explique la lumière, les angles et les fonds.</p>

<h2>Sources</h2>
<p>Ces règles viennent des pages d'aide d'Uber pour les marchands, dont les <a href="https://help.uber.com/en/merchants-and-restaurants/article/merchant-submitted-menu-catalog-photo-guidelines?nodeId=6985355b-0426-4523-94f2-89bb9b0566e9" rel="nofollow">règles pour les photos de menu</a>. Uber peut les modifier : consultez cette page si une photo est refusée.</p>

<p>Vous voulez des photos acceptées sans prise de tête ? Nous améliorons les photos de vos vrais plats et les livrons au format recommandé par Uber, 2880 × 2304. <a href="/fr/examples.html">Voir des exemples</a>.</p>
""",
    },
    {
        "slug": "photos-plats-telephone",
        "alt": "uber-eats-food-photos-phone",
        "answer": "Un téléphone suffit pour de bonnes photos Uber Eats : lumière du jour près d'une fenêtre, fond simple, bon angle selon le plat, plat centré qui remplit l'image, et retouches légères sans modifier la nourriture.",
        "faq": [("Peut on prendre ses photos Uber Eats au téléphone ?", "Oui. Un téléphone récent, la lumière d'une fenêtre et un fond propre suffisent pour de bonnes photos de menu."),
                ("Quel est le meilleur angle pour photographier un plat ?", "Par dessus pour les plats plats comme la pizza ou les bols, à environ 45 degrés pour la plupart des assiettes, et de côté pour ce qui est haut, comme les burgers et les boissons."),
                ("Faut il utiliser le flash ?", "Non. Le flash rend la nourriture brillante et plate. Préférez une lumière du jour douce, venant du côté.")],
        "title": "Prendre de belles photos de plats au téléphone pour Uber Eats",
        "short": "De belles photos au téléphone",
        "desc": "Des conseils simples pour les restaurateurs : prendre des photos de plats lumineuses et appétissantes au téléphone pour Uber Eats. Lumière, angle, fond, cadrage et retouches.",
        "img": "phone",
        "related": ["photos-uber-eats-exigences", "photo-banniere-uber-eats", "plus-de-commandes-uber-eats"],
        "lead": "Pas besoin de photographe pour avoir de bonnes photos sur Uber Eats. Avec la lumière du jour, un fond propre et quelques habitudes simples, un téléphone suffit.",
        "body": """
<p>Avant de commencer, consultez les <a href="/fr/guides/photos-uber-eats-exigences.html">exigences photo d'Uber Eats</a> (taille, format et motifs de refus), puis suivez ces conseils.</p>

<h2>La lumière du jour, pas celle de la cuisine</h2>
<p>Les lumières de cuisine sont souvent jaunes ou verdâtres et aplatissent les plats. Photographiez près d'une fenêtre, en journée, avec la lumière venant du côté. Coupez le flash : il rend la nourriture brillante et dure.</p>

<h2>Un fond simple</h2>
<p>Une table unie, une planche en bois ou une surface claire fonctionnent le mieux. Retirez bouteilles, torchons, tickets et tout ce qui n'est pas le plat. Le plat doit être la seule chose qu'on regarde.</p>

<h2>Le bon angle pour chaque plat</h2>
<ul><li><b>Par dessus</b> pour les plats plats : pizzas, bols, plateaux, salades.</li><li><b>À 45 degrés</b> pour la plupart des assiettes et des boîtes à emporter.</li><li><b>De côté</b> pour ce qui est haut : burgers, gâteaux à étages, boissons.</li></ul>

<h2>Remplissez l'image, avec un peu de marge</h2>
<p>Approchez vous pour que le plat occupe la plus grande partie de la photo, avec une petite marge autour. Uber Eats recadre les photos en plusieurs formats : gardez le plat au centre.</p>

<h2>Montrez la vraie portion</h2>
<p>Servez le plat exactement comme le client le reçoit, dans votre emballage ou votre assiette habituels. Une photo plus généreuse que la réalité crée des clients déçus.</p>

<h2>Gardez un style cohérent</h2>
<p>Utilisez le même fond et le même angle pour toutes vos photos. Un menu où toutes les photos se ressemblent paraît professionnel, même si chaque photo est simple.</p>

<h2>Retouchez légèrement</h2>
<p>L'éditeur intégré de votre téléphone suffit : un peu plus de luminosité, un peu de chaleur, une photo bien droite. Ne changez pas les couleurs de la nourriture et évitez les filtres forts.</p>

<h2>Commencez par vos dix meilleures ventes</h2>
<p>Inutile de tout photographier le même jour. Vos dix plats les plus vendus font la plus grande différence : commencez par eux.</p>

<p>Vos photos sont sombres ou peu lisibles ? Nous améliorons les photos de vos vrais plats : meilleure lumière, fond propre et format recommandé par Uber, sans modifier la nourriture. <a href="/fr/examples.html">Voir des exemples</a>.</p>
""",
    },
    {
        "slug": "modifier-menu-uber-eats-manager",
        "alt": "edit-menu-uber-eats-manager",
        "answer": "Pour modifier votre menu Uber Eats, connectez vous sur merchants.ubereats.com, ouvrez Menu, choisissez votre menu de livraison, cliquez sur un article pour changer son nom, sa description ou sa photo, puis enregistrez. Pour vous faire aider, ajoutez un utilisateur au lieu de partager votre mot de passe.",
        "faq": [("Comment changer mon menu sur Uber Eats ?", "Connectez vous à Uber Eats Manager sur merchants.ubereats.com, ouvrez Menu, cliquez sur l'article, modifiez le, puis enregistrez ou publiez."),
                ("Combien de temps pour voir les changements ?", "Les modifications de texte apparaissent en général en quelques minutes. Les nouvelles photos sont vérifiées d'abord, ce qui peut prendre plus longtemps."),
                ("Comment donner accès à Uber Eats Manager à quelqu'un ?", "Dans Uber Eats Manager, ouvrez Paramètres puis Utilisateurs, ajoutez son adresse email et donnez un accès au Menu uniquement. Vous pouvez le retirer à tout moment.")],
        "title": "Uber Eats Manager : modifier votre menu, vos photos et vos catégories",
        "short": "Modifier son menu dans Uber Eats Manager",
        "desc": "Un guide pas à pas pour les restaurateurs : modifier noms, descriptions, photos et catégories dans Uber Eats Manager, et ajouter quelqu'un pour vous aider.",
        "img": "tablet",
        "related": ["categories-menu-uber-eats", "photos-uber-eats-exigences", "descriptions-menu-uber-eats"],
        "lead": "Votre page Uber Eats se modifie dans Uber Eats Manager. Voici où trouver chaque réglage, étape par étape. Les écrans changent de temps en temps, mais les étapes principales restent les mêmes.",
        "body": """
<h2>Connectez vous à Uber Eats Manager</h2>
<p>Allez sur <b>merchants.ubereats.com</b> depuis un ordinateur et connectez vous avec le compte de votre restaurant. L'éditeur de menu est plus pratique sur ordinateur que sur téléphone.</p>

<h2>Modifier le nom ou la description d'un article</h2>
<ol><li>Cliquez sur <b>Menu</b> dans le menu de gauche.</li><li>Ouvrez le menu utilisé pour la livraison.</li><li>Cliquez sur l'article à modifier.</li><li>Changez le nom et la description, puis cliquez sur <b>Enregistrer</b>.</li></ol>

<h2>Ajouter ou remplacer une photo</h2>
<ol><li>Ouvrez l'article dans l'éditeur de menu.</li><li>Cliquez sur la zone photo.</li><li>Importez la nouvelle photo, en paysage, avec le plat au centre.</li><li>Enregistrez, puis vérifiez le rendu dans l'application une fois en ligne.</li></ol>

<h2>Réorganiser catégories et articles</h2>
<p>Dans l'éditeur, vous pouvez faire glisser catégories et articles dans un nouvel ordre. Placez vos meilleures ventes et votre catégorie la plus populaire en premier.</p>

<h2>Publier les changements</h2>
<p>Selon votre configuration, les changements s'enregistrent directement ou demandent un clic sur <b>Publier</b>. Ils apparaissent en général dans l'application en quelques minutes.</p>

<h2>Se faire aider sans partager son mot de passe</h2>
<p>Si quelqu'un vous aide sur votre page, ne donnez jamais votre mot de passe. Ajoutez plutôt un utilisateur :</p>
<ol><li>Dans Uber Eats Manager, ouvrez <b>Paramètres</b>, puis <b>Utilisateurs</b> (parfois appelé Équipe).</li><li>Ajoutez un utilisateur avec son adresse email.</li><li>Donnez un accès au <b>Menu</b> uniquement.</li></ol>
<p>Vous pouvez retirer cet accès à tout moment. C'est exactement ainsi que fonctionne notre service Clé en main.</p>

<h2>Vous préférez ne pas le faire vous même ?</h2>
<p>Avec notre <a href="/fr/pricing.html">Refonte Complète</a>, nous faisons chaque changement sur votre page Uber Eats à votre place. Avec Menu Fix et Menu et Photos, nous envoyons tout prêt à copier, avec un guide simple comme celui ci.</p>
""",
    },
    {
        "slug": "debuter-sur-uber-eats",
        "alt": "new-on-uber-eats-checklist",
        "answer": "Si vous débutez sur Uber Eats, avant vos premières commandes : des photos lumineuses pour vos plats phares, un nom clair et une courte description pour chaque article, des catégories courtes avec les meilleures ventes en premier, une bannière qui montre votre meilleur plat, et des horaires et prix exacts.",
        "faq": [("Que faire quand on démarre sur Uber Eats ?", "Ajoutez des photos à vos plats phares, écrivez des noms et descriptions clairs, mettez vos meilleures ventes en premier, choisissez une bannière appétissante et vérifiez vos horaires et vos prix."),
                ("Comment faire une bonne première impression ?", "Faites en sorte que ce que le client voit corresponde à ce qu'il reçoit : de vraies photos, des descriptions exactes et des plats qui voyagent bien."),
                ("Faut il commander dans son propre restaurant ?", "Une fois, c'est une bonne idée : vous voyez votre page et vos emballages comme vos clients.")],
        "title": "Nouveau sur Uber Eats ? La liste pour vos premières semaines",
        "short": "Débuter sur Uber Eats : la liste",
        "desc": "Vous venez d'arriver sur Uber Eats ? Une liste pratique pour les nouveaux restaurants et cafés : menu, photos, bannière, horaires et plus, pour une bonne première impression.",
        "img": "opening",
        "related": ["plus-de-commandes-uber-eats", "prix-menu-uber-eats", "photos-plats-telephone"],
        "lead": "Les premières semaines sur Uber Eats sont celles où beaucoup de clients vous essaient pour la première fois. Cette liste aide votre page à faire bonne impression.",
        "body": """
<h2>Avant la première commande</h2>
<ul class="ticks"><li>Chaque plat phare a une photo claire et lumineuse.</li><li>Chaque article a un nom compréhensible et une description d'une ligne.</li><li>Vos catégories sont courtes et dans un ordre logique, meilleures ventes en premier.</li><li>Votre bannière montre votre plat le plus appétissant.</li><li>Les prix, tailles et contenus des formules sont exacts.</li><li>Vos horaires correspondent aux moments où vous pouvez vraiment préparer et emballer.</li></ul>

<h2>La première semaine</h2>
<ul class="ticks"><li>Commandez une fois chez vous, pour voir la page et l'emballage comme un client.</li><li>Vérifiez que les plats voyagent bien : sauces fermées, éléments croustillants pas enfermés dans la vapeur.</li><li>Mettez en pause les articles épuisés dès qu'ils le sont, pour éviter les annulations.</li><li>Lisez chaque avis et notez ce qui revient deux fois.</li></ul>

<h2>Le premier mois</h2>
<ul class="ticks"><li>Regardez quels plats se vendent et remontez les dans le menu.</li><li>Remplacez les photos faibles, en commençant par vos dix meilleures ventes.</li><li>Retirez les plats que personne ne commande : un menu plus court est plus facile à choisir.</li><li>Gardez une page cohérente avec votre boutique, pour que vos habitués vous reconnaissent.</li></ul>

<h2>Une page claire donne les bonnes attentes</h2>
<p>Quand ce qui arrive correspond à ce que le client a vu, il a plus de chances d'être satisfait et de revenir. C'est l'idée derrière toute cette liste.</p>

<p>Vous venez de vous lancer ? Nous vous envoyons une maquette gratuite de votre future page, pour voir ce que nous changerions avant de décider quoi que ce soit.</p>
""",
    },
    {
        "slug": "prix-menu-uber-eats",
        "alt": "price-menu-uber-eats",
        "answer": "Pour fixer vos prix sur Uber Eats, partez du coût réel de chaque plat, ajoutez l'emballage et la commission prélevée sur chaque commande, et choisissez un prix de livraison qui vous laisse une marge correcte. Beaucoup de restaurants affichent des prix un peu plus élevés en livraison qu'en salle ; c'est possible, mais restez cohérent et clair sur les formules et les tailles.",
        "faq": [("Peut on vendre plus cher sur Uber Eats qu'au restaurant ?", "De nombreux restaurants appliquent des prix plus élevés sur les applications de livraison pour couvrir la commission et l'emballage. Vérifiez les conditions de votre contrat Uber Eats, et gardez un écart raisonnable pour ne pas surprendre vos habitués."),
                ("Comment calculer le prix d'un plat sur Uber Eats ?", "Additionnez le coût des ingrédients et de l'emballage, puis calculez ce qu'il vous reste après la commission de votre offre. Si ce reste est insuffisant, augmentez le prix, ajustez la portion ou retirez le plat de la livraison."),
                ("Faut il faire des promotions sur Uber Eats ?", "Seulement si les chiffres tiennent après la remise et la commission. Une promotion qui apporte des commandes à perte n'est pas une réussite. Testez en une à la fois et suivez les résultats dans Uber Eats Manager.")],
        "title": "Comment fixer les prix de votre menu sur Uber Eats",
        "short": "Fixer ses prix sur Uber Eats",
        "desc": "Un guide pratique et honnête pour les restaurants et cafés : fixer ses prix sur Uber Eats en tenant compte des coûts, de la commission, de l'emballage, des formules et des promotions.",
        "img": "pricing",
        "related": ["uber-eats-deliveroo-just-eat-conseils-menu", "plus-de-commandes-uber-eats", "categories-menu-uber-eats"],
        "lead": "Fixer ses prix sur Uber Eats, ce n'est pas comme au comptoir. La commission et l'emballage sont prélevés sur chaque commande : un prix rentable en salle peut faire perdre de l'argent en livraison. Voici une méthode simple.",
        "body": """
<h2>1. Connaissez le coût réel de chaque plat</h2>
<p>Commencez par ce que chaque plat vous coûte : les ingrédients, plus la boîte, le couvercle, le sac, les pots de sauce et les couverts. L'emballage s'oublie facilement et pèse vite sur une soirée chargée. Notez le total à côté de chacune de vos meilleures ventes.</p>

<h2>2. Vérifiez la commission de votre offre</h2>
<p>Uber Eats prélève un pourcentage sur chaque commande, et ce taux dépend de l'offre choisie et du mode de livraison (livreurs Uber ou vos propres livreurs). Consultez votre contrat ou Uber Eats Manager plutôt que ce que l'on vous a dit. Calculez ensuite, pour chaque plat, ce qu'il vous reste vraiment.</p>

<h2>3. Fixez votre prix de livraison</h2>
<p>Beaucoup de restaurants affichent des prix un peu plus élevés en livraison qu'en salle pour couvrir ces coûts. C'est un choix commercial courant. Quelques conseils :</p>
<ul class="ticks"><li>Appliquez la même logique à tout le menu, pour que les prix ne paraissent pas aléatoires.</li><li>Arrondissez à des prix simples, comme 14,50 € ou 15 €, plutôt qu'à des centimes au hasard.</li><li>Raisonnez en prix TTC, puisque c'est ce que le client voit et paie.</li><li>Vérifiez les éventuelles conditions de votre contrat sur les écarts de prix.</li><li>Soyez prêt à l'expliquer honnêtement si un habitué pose la question.</li></ul>

<h2>4. Repensez les plats qui voyagent mal</h2>
<p>Certains plats coûtent cher à bien emballer ou arrivent moins bons qu'au départ. Si un plat rapporte peu en livraison et reçoit des avis mitigés, il vaut sans doute mieux le garder pour la salle. Un menu de livraison plus court est aussi plus facile à choisir.</p>

<h2>5. Utilisez formules et tailles avec soin</h2>
<p>Les formules augmentent la valeur de chaque commande, ce qui aide quand la commission est un pourcentage. Assurez vous que la formule est clairement plus avantageuse que les articles séparés, et indiquez exactement ce qu'elle contient : « Burger, frites et canette ». Même chose pour les tailles : « Grande (pour 2) » aide à choisir sans hésiter.</p>

<h2>6. Faites payer les suppléments</h2>
<p>Fromage en plus, deuxième sauce, avocat : ils vous coûtent de l'argent. Les proposer en options payantes dans Uber Eats Manager est juste et courant, et permet au client de composer ce qu'il veut.</p>

<h2>7. Une promotion est un test, pas une habitude</h2>
<p>Remises et livraison offerte peuvent attirer de nouveaux clients, mais elles réduisent votre marge, et la commission reste due. Avant d'en lancer une, calculez ce qu'il vous reste par commande au prix promotionnel. Une promotion à la fois, suivez les résultats, et arrêtez la si elle ne rapporte pas.</p>

<h2>8. Revoyez vos prix régulièrement</h2>
<p>Le coût des produits change. Vérifiez vos prix de livraison tous les quelques mois, ou dès qu'un fournisseur important augmente ses tarifs, pour ne pas perdre d'argent sans le voir sur vos meilleures ventes.</p>

<h2>Le prix n'est qu'une partie du choix</h2>
<p>Les clients comparent ce qu'ils voient. Une photo claire, un nom compréhensible et une description qui dit ce qu'il y a dans le plat font paraître un prix juste. Notre <a href="/fr/guides/plus-de-commandes-uber-eats.html">guide pour recevoir plus de commandes</a> couvre le reste de votre page.</p>
""",
    },
    {
        "slug": "uber-eats-deliveroo-just-eat-conseils-menu",
        "alt": "uber-eats-doordash-menulog-menu-tips",
        "answer": "Uber Eats, Deliveroo et Just Eat récompensent les mêmes bases : de vraies photos, des noms clairs, des descriptions courtes, les meilleures ventes en premier et des prix exacts. Gardez un menu de référence unique, adaptez le à l'éditeur et aux règles photo de chaque application, et mettez les trois à jour à chaque changement.",
        "faq": [("Faut il être sur Uber Eats, Deliveroo et Just Eat en même temps ?", "Beaucoup de restaurants sont sur plusieurs applications. Cela peut toucher plus de clients, mais chaque application ajoute une tablette, un menu à tenir à jour et des frais. Commencez par ce que vous pouvez bien gérer."),
                ("Peut on utiliser le même menu sur toutes les applications ?", "En grande partie, oui. Gardez une liste de référence avec noms, descriptions, prix et photos, puis copiez la dans chaque application. Vérifiez les règles photo de chacune et la façon dont elle gère options et formules."),
                ("Peut on avoir des prix différents selon l'application ?", "C'est possible si les frais de vos contrats diffèrent. Vérifiez les conditions de chaque contrat, et gardez des écarts simples à gérer.")],
        "title": "Uber Eats, Deliveroo ou Just Eat : conseils menu pour les restaurants",
        "short": "Uber Eats, Deliveroo, Just Eat : conseils menu",
        "desc": "Vous êtes sur plusieurs applications de livraison ? Des conseils concrets pour vos menus Uber Eats, Deliveroo et Just Eat : ce qui est pareil, ce qui change, et comment tout garder à jour.",
        "img": "tablets",
        "related": ["prix-menu-uber-eats", "modifier-menu-uber-eats-manager", "photos-uber-eats-exigences"],
        "lead": "Si vous êtes sur Uber Eats, Deliveroo et Just Eat, vous gérez en réalité trois menus. Bonne nouvelle : ce qui fait vendre un menu est le même partout. Voici comment rester cohérent sans doubler votre travail.",
        "body": """
<h2>Ce qui est pareil partout</h2>
<p>Quelle que soit l'application, le client décide de la même façon : il fait défiler, regarde les photos et lit les noms. Sur les trois, ces bases comptent le plus :</p>
<ul class="ticks"><li>De vraies photos lumineuses de vos meilleures ventes.</li><li>Des noms compréhensibles, en gardant votre nom maison si vous y tenez.</li><li>Une description d'une ligne qui dit ce qu'il y a dans le plat.</li><li>Des catégories courtes et logiques, meilleures ventes en premier.</li><li>Des prix, tailles, horaires et ruptures toujours exacts.</li></ul>

<h2>Gardez un menu de référence</h2>
<p>Le plus simple pour rester cohérent : un seul document ou tableur avec le nom, la description, le prix, les options et la photo de chaque article. Faites les changements là d'abord, puis reportez les dans chaque application. Vous évitez ainsi le plat retiré d'une application mais toujours en vente sur une autre.</p>

<h2>Ce qui change d'une application à l'autre</h2>
<p>Chaque application a son éditeur de menu, ses règles photo et sa façon d'afficher votre page. Avant d'importer, vérifiez les règles photo actuelles de chacune : taille, format et ce qui est autorisé, comme le texte ou les logos sur l'image. Recadrez à partir de vos photos d'origine pour chaque application plutôt que de réutiliser une version déjà recadrée.</p>
<p>Options, formules et suppléments se configurent aussi différemment. Construisez les avec soin sur chaque application et passez une commande test si possible, pour qu'aucun client ne paie le mauvais montant ou ne reçoive une commande incomplète.</p>
<p>Les frais et les offres varient selon l'application et évoluent dans le temps. Référez vous à vos propres contrats plutôt qu'aux comparatifs généraux : ce qui compte, c'est ce que vous payez vraiment.</p>

<h2>Conseils pour Uber Eats</h2>
<p>Uber Eats Manager permet de modifier articles, photos et catégories, et d'ajouter des membres d'équipe avec un accès au menu uniquement. Si un article n'a pas de photo, Uber Eats peut afficher des photos de clients : ajoutez les vôtres à vos meilleures ventes. Voir notre guide pour <a href="/fr/guides/modifier-menu-uber-eats-manager.html">modifier votre menu dans Uber Eats Manager</a>.</p>

<h2>Conseils pour Deliveroo</h2>
<p>Le menu Deliveroo se gère depuis l'espace partenaire Deliveroo. Comme partout, placez vos plats les plus commandés en premier et donnez leur une photo. Après chaque enregistrement, regardez comment catégories et options s'affichent sur un téléphone : ce qui paraît juste dans l'éditeur ne l'est pas toujours dans l'application.</p>

<h2>Conseils pour Just Eat</h2>
<p>Just Eat existe depuis longtemps et certains clients l'utilisent par habitude. Les changements de menu passent par les outils partenaires de Just Eat, et certains peuvent être traités par leurs équipes. Prévoyez du temps pour les mises à jour, et vérifiez votre page une fois en ligne.</p>

<h2>Les prix sur plusieurs applications</h2>
<p>Si les frais de vos contrats diffèrent, vous pouvez choisir des prix différents selon l'application. C'est votre décision, mais restez simple : une règle claire par application se gère mieux que des écarts plat par plat. Notre guide pour <a href="/fr/guides/prix-menu-uber-eats.html">fixer vos prix sur Uber Eats</a> explique comment calculer un prix de livraison.</p>

<h2>Ne vous dispersez pas</h2>
<p>Chaque application ajoute une tablette sur le comptoir, un menu à mettre à jour et des commandes à emballer. Mieux vaut une seule application avec une page excellente et exacte que trois avec d'anciens prix et des photos manquantes. Ajoutez une application quand vous êtes sûr de pouvoir la tenir à jour.</p>
""",
    },
    {
        "slug": "photo-banniere-uber-eats",
        "alt": "uber-eats-banner-photo",
        "answer": "Votre bannière Uber Eats doit être une photo lumineuse et rapprochée de votre plat le plus appétissant, prise à la lumière du jour, le plat remplissant l'image. Évitez logos, texte, devanture et photos sombres de cuisine, et vérifiez le recadrage sur téléphone avant de publier.",
        "faq": [("Quelle photo choisir pour sa bannière Uber Eats ?", "Une photo lumineuse et rapprochée de votre plat le plus vendu ou le plus appétissant. C'est la première chose que voit le client : elle doit donner faim tout de suite."),
                ("Peut on mettre son logo ou du texte sur la bannière ?", "Consultez les règles actuelles dans Uber Eats Manager. En général, une photo de plat sans texte ni logo est plus nette, et votre nom apparaît déjà sur la page."),
                ("Pourquoi ma bannière est elle coupée dans l'application ?", "La bannière s'affiche dans des formats différents sur téléphone, tablette et ordinateur. Gardez le plat au centre avec de l'espace autour, pour que rien d'important ne soit coupé.")],
        "title": "Votre photo de bannière Uber Eats : comment bien la choisir",
        "short": "Choisir sa photo de bannière Uber Eats",
        "desc": "Comment les restaurants et cafés peuvent choisir et prendre la photo de bannière de leur page Uber Eats : quel plat montrer, comment le photographier, le recadrage et les erreurs courantes.",
        "img": "banner",
        "related": ["photos-plats-telephone", "photos-uber-eats-exigences", "plus-de-commandes-uber-eats"],
        "lead": "La grande photo en haut de votre page Uber Eats est la première chose que voient les clients. Elle donne le ton pour tout le reste : elle mérite qu'on s'y attarde.",
        "body": """
<h2>1. Choisissez le bon plat</h2>
<p>Prenez le plat que les clients préfèrent, ou celui qui rend le mieux en photo. Ce n'est pas forcément le plus cher. Les plats colorés et généreux fonctionnent bien : un burger garni, une pizza qui sort du four, un bol de nouilles aux herbes fraîches, une pile de pancakes.</p>

<h2>2. De la vraie nourriture, de près</h2>
<p>Les clients veulent voir ce qu'ils vont manger. Le plat doit occuper la plus grande partie de l'image. Une devanture, une salle vide ou un logo sur fond uni en disent peu sur votre cuisine.</p>

<h2>3. La lumière du jour</h2>
<p>Photographiez près d'une fenêtre, en journée, avec la lumière sur le côté. Éteignez les plafonniers qui jaunissent l'image. Notre guide pour <a href="/fr/guides/photos-plats-telephone.html">photographier vos plats au téléphone</a> détaille chaque étape.</p>

<h2>4. Prévoyez le recadrage</h2>
<p>Uber Eats affiche la bannière dans plusieurs formats selon l'écran, et votre logo peut en recouvrir une partie. Gardez le plat au centre avec de l'espace autour. Prenez la photo en paysage, puis vérifiez la sur votre propre téléphone après publication.</p>

<h2>5. Soignez les détails</h2>
<p>Essuyez le bord de l'assiette, retirez bouteilles, torchons et tickets, et utilisez un fond simple comme une planche en bois ou un plan de travail uni. Au format bannière, chaque détail se voit.</p>

<h2>6. Montrez ce qui arrive vraiment</h2>
<p>Votre bannière doit ressembler à ce que reçoit le client. Une photo qui promet plus que le plat crée de la déception. Uber Eats attend aussi des photos de vos vrais plats.</p>

<h2>7. Changez la de temps en temps</h2>
<p>Si votre carte change ou qu'un nouveau plat devient le préféré, mettez la bannière à jour. Un plat de saison peut aussi faire l'affaire, tant qu'il reste à la carte pendant qu'il est en bannière.</p>

<h2>Les erreurs courantes</h2>
<ul class="ticks"><li>Une photo sombre prise le soir sous les lumières de la cuisine.</li><li>Toute une table de plats prise de loin, où rien ne ressort.</li><li>Un logo ou du texte sur la nourriture.</li><li>Un plat qui n'est plus à la carte.</li></ul>
""",
    },
    {
        "slug": "categories-menu-uber-eats",
        "alt": "uber-eats-menu-categories",
        "answer": "Organisez votre menu Uber Eats en peu de catégories claires, dans l'ordre du repas : une catégorie meilleures ventes en premier, puis vos plats principaux, puis accompagnements, boissons et desserts. Utilisez des noms simples, évitez les catégories d'un seul article et supprimez tout ce qui est vide ou en double.",
        "faq": [("Dans quel ordre mettre ses catégories sur Uber Eats ?", "Une catégorie meilleures ventes en premier, puis les plats pour lesquels on vient chez vous, puis accompagnements, suppléments, boissons et desserts à la fin."),
                ("Un article peut il être dans plusieurs catégories ?", "Oui, Uber Eats Manager permet de placer le même article dans plusieurs catégories. C'est pratique pour mettre les meilleures ventes en haut sans les retirer de leur place habituelle."),
                ("Comment nommer ses catégories ?", "Avec les mots qu'utilisent déjà les clients : Burgers, Pizzas, Nouilles, Accompagnements, Boissons. Un nom créatif peut plaire en boutique, mais un nom simple se lit plus vite sur téléphone.")],
        "title": "Comment organiser les catégories de votre menu Uber Eats",
        "short": "Organiser ses catégories Uber Eats",
        "desc": "Un guide pratique sur les catégories de menu Uber Eats pour restaurants et cafés : combien en avoir, comment les nommer, dans quel ordre les placer et quoi supprimer.",
        "img": "menuboard",
        "related": ["modifier-menu-uber-eats-manager", "plus-de-commandes-uber-eats", "descriptions-menu-uber-eats"],
        "lead": "Un menu bien structuré aide les clients affamés à trouver vite ce qu'ils veulent. Voici comment organiser vos catégories pour une page facile à parcourir sur téléphone.",
        "body": """
<h2>1. Commencez par une catégorie meilleures ventes</h2>
<p>Créez une première catégorie <b>Les plus populaires</b>, <b>Meilleures ventes</b> ou <b>Nos incontournables</b>, avec vos cinq ou six plats les plus commandés. Beaucoup de clients ne font pas défiler très loin : vos meilleurs plats doivent être là.</p>

<h2>2. Suivez l'ordre du repas</h2>
<p>Après les meilleures ventes, placez les plats pour lesquels on vient chez vous, puis le reste. Un ordre classique :</p>
<ol><li>Meilleures ventes</li><li>Vos plats principaux, répartis par type si vous en avez beaucoup (Burgers, Wraps, Bowls)</li><li>Accompagnements et suppléments</li><li>Boissons</li><li>Desserts</li></ol>
<p>Un café utilisera plutôt Petit déjeuner, Déjeuner, Cafés, Boissons fraîches et Pâtisseries. Regroupez comme vos clients pensent.</p>

<h2>3. Des noms simples</h2>
<p>Les noms de catégories sont des panneaux indicateurs. <b>Soupes de nouilles</b> se comprend plus vite que « Du côté de la marmite ». Si vous tenez à un nom créatif, ajoutez le mot simple : <b>La cuisine de Nonna : pâtes</b>.</p>

<h2>4. Ni trop, ni trop peu</h2>
<p>Trop de petites catégories obligent à faire défiler des titres au lieu des plats. Une seule énorme catégorie cache vos meilleurs plats. Visez quelques articles par catégorie, et regroupez celles qui n'en ont qu'un ou deux.</p>

<h2>5. Supprimez le vide, l'ancien et les doublons</h2>
<p>Les catégories d'une ancienne carte, les catégories vides et les quasi doublons (« Boissons » et « Rafraîchissements ») donnent une impression de page délaissée. Cinq minutes dans Uber Eats Manager suffisent pour faire le ménage.</p>

<h2>6. Le meilleur article en tête de chaque catégorie</h2>
<p>L'ordre à l'intérieur d'une catégorie compte aussi. Commencez chaque catégorie par son plat le plus populaire ou le plus photogénique, et gardez les articles avec photo vers le haut.</p>

<h2>7. Utilisez des menus selon l'heure</h2>
<p>Si vous servez le petit déjeuner et le dîner, Uber Eats permet de définir des menus selon le moment de la journée. Les clients ne voient ainsi que ce que vous pouvez préparer à cette heure là.</p>

<h2>Besoin d'aide ?</h2>
<p>Notre guide pour <a href="/fr/guides/modifier-menu-uber-eats-manager.html">modifier votre menu dans Uber Eats Manager</a> montre où changer les catégories. Nous pouvons aussi restructurer tout le menu pour vous avec notre offre <a href="/fr/pricing.html">Menu Fix</a>.</p>
""",
    },
    {
        "slug": "repondre-avis-uber-eats",
        "alt": "reply-to-uber-eats-reviews",
        "answer": "Répondez aux avis Uber Eats brièvement, poliment et personnellement : remerciez le client, reconnaissez le problème sans argumenter, dites ce que vous avez fait, et restez court. Corrigez ensuite la cause sur votre menu ou en cuisine, pour que la même remarque ne revienne pas.",
        "faq": [("Peut on répondre aux avis sur Uber Eats ?", "Uber Eats Manager permet aux restaurants de répondre aux retours clients, selon le compte et le pays. Regardez dans la rubrique Avis ou Retours d'Uber Eats Manager."),
                ("Faut il répondre aux avis négatifs ?", "Oui, quand vous pouvez le faire calmement. Une réponse courte et polie qui reconnaît le problème montre aux autres clients que vous êtes attentif. Ne vous disputez jamais et ne partagez aucune information privée."),
                ("Peut on supprimer un mauvais avis ?", "En général non. Si un avis enfreint les règles d'Uber Eats, par exemple avec des propos injurieux, vous pouvez le signaler via Uber Eats Manager ou l'assistance. Sinon, la meilleure réponse est de corriger la cause.")],
        "title": "Comment répondre aux avis Uber Eats (avec exemples)",
        "short": "Répondre aux avis Uber Eats",
        "desc": "Comment les restaurants et cafés peuvent répondre aux avis Uber Eats : quoi dire aux bons et aux mauvais avis, des exemples à adapter, et quoi corriger sur votre menu.",
        "img": "counter",
        "related": ["plus-de-commandes-uber-eats", "descriptions-menu-uber-eats", "debuter-sur-uber-eats"],
        "lead": "Un avis négatif peut faire mal, surtout quand le problème venait de la livraison et non de votre cuisine. Une réponse courte et calme, puis une correction rapide de la cause, changent beaucoup de choses.",
        "body": """
<h2>1. Lisez chaque avis</h2>
<p>Consultez régulièrement vos retours dans Uber Eats Manager. Une remarque isolée, c'est l'avis d'une personne ; la même remarque deux fois, c'est un signal à prendre au sérieux.</p>

<h2>2. Des réponses courtes et personnelles</h2>
<p>Deux ou trois phrases suffisent. Utilisez le prénom du client s'il apparaît, citez le plat et signez de votre prénom. Une réponse copiée collée sous chaque avis donne l'impression que personne n'écoute.</p>

<h2>3. Remerciez pour les bons avis</h2>
<p>Un merci rapide suffit :</p>
<p><i>« Merci beaucoup Sarah ! Ravis que le bo bun vous ait plu. À bientôt. Minh, Pho Corner »</i></p>

<h2>4. Face à une plainte, reconnaissez et restez calme</h2>
<p>Ne vous disputez pas, même si vous êtes sûr d'avoir raison. Reconnaissez le problème, dites ce que vous avez fait et laissez la porte ouverte :</p>
<p><i>« Désolé que vos frites soient arrivées molles, Thomas. Nous sommes passés à des boîtes ventilées pour qu'elles restent croustillantes pendant le trajet. Nous serions ravis d'avoir une autre chance. Sam »</i></p>
<p>Si le souci venait de la livraison, vous pouvez le dire avec tact, sans accuser personne : <i>« Désolé pour le retard. Nous faisons remonter l'information, et nous emballons toujours les plats chauds pour qu'ils voyagent au mieux. »</i></p>

<h2>5. Aucune information privée</h2>
<p>Ne mentionnez jamais de numéro de commande, d'adresse ou de détail personnel dans une réponse publique. Si quelque chose doit être réglé, passez par les options de remboursement et d'assistance d'Uber Eats Manager.</p>

<h2>6. Corrigez la cause</h2>
<p>Beaucoup de plaintes pointent vers quelque chose sur votre page :</p>
<ul class="ticks"><li><b>« Pas ce à quoi je m'attendais »</b> : réécrivez la description pour dire ce qu'il y a dans le plat et sa taille.</li><li><b>« Plus petit que sur la photo »</b> : reprenez la photo pour montrer une vraie portion.</li><li><b>« Article manquant »</b> : vérifiez que formules et options disent exactement ce qui est inclus.</li><li><b>« Froid » ou « mou »</b> : revoyez l'emballage, et envisagez de retirer de la livraison les plats qui voyagent mal.</li></ul>
<p>Notre guide pour <a href="/fr/guides/descriptions-menu-uber-eats.html">écrire vos descriptions de plats</a> aide pour les deux premiers cas.</p>

<h2>7. Signalez les avis qui enfreignent les règles</h2>
<p>Les avis injurieux ou offensants peuvent être signalés via Uber Eats Manager ou l'assistance. Les retours négatifs honnêtes restent en général en ligne, et c'est là qu'une bonne réponse et une vraie correction comptent le plus.</p>
""",
    },
]

# ---------------------------------------------------------------- newer guides (October 2026)

GUIDES_FR_A = [
    {
        "slug": "inscrire-restaurant-uber-eats-france",
        "alt": None,
        "key": "signup",
        "answer": "Pour inscrire votre restaurant sur Uber Eats en France, faites une demande sur le site marchands d'Uber Eats, préparez vos documents (licence commerciale, identifiants fiscaux, SIREN et SIRET, TVA, coordonnées bancaires et de facturation, extrait Kbis) et lisez votre <b>bon de commande</b>, qui fixe vos frais. Uber étudie chaque demande. Préparez ensuite votre menu, vos photos et vos horaires.",
        "faq": [("Comment inscrire mon restaurant sur Uber Eats en France ?", "Faites une demande sur le site Uber Eats pour les marchands en France, puis fournissez les documents demandés : licence commerciale, identifiants fiscaux, informations de TVA, coordonnées bancaires et de facturation, numéros SIREN et SIRET. Uber étudie chaque demande et ne peut pas accepter tous les établissements."),
                ("Combien coûte l'inscription sur Uber Eats pour un restaurant ?", "Les conditions d'Uber Eats pour la France prévoient des frais d'activation et des frais de service, dont les montants figurent dans votre bon de commande. Nous n'avons trouvé aucun montant public publié par Uber France : demandez vos chiffres avant de signer."),
                ("Combien de temps avant la première commande ?", "Personne ne peut vous donner de délai fiable : cela dépend de l'étude de votre demande par Uber et du temps que vous mettez à préparer votre menu. Une demande complète et un menu prêt à l'avance évitent les allers et retours.")],
        "title": "Inscrire son restaurant sur Uber Eats en France : étapes et documents",
        "short": "Inscrire son restaurant sur Uber Eats",
        "desc": "Inscrire votre restaurant ou café sur Uber Eats en France : la demande, les documents à préparer (Kbis, SIRET, TVA), les frais et votre première semaine.",
        "img": "shopfront",
        "related": ["debuter-sur-uber-eats", "commission-uber-eats-restaurant-france", "ajouter-photos-menu-uber-eats"],
        "lead": "Rejoindre Uber Eats, c'est surtout de l'administratif, puis la mise en place de votre menu. Voici les étapes pour un restaurant ou un café en France, ce qu'il faut préparer, ce que cela coûte et quoi faire la première semaine.",
        "body": """
<h2>Les étapes de l'inscription</h2>
<ol><li><b>Faites votre demande sur le site d'Uber.</b> Allez sur le <a href="https://merchants.ubereats.com/fr/fr/" rel="nofollow">site Uber Eats pour les marchands en France</a> et renseignez votre établissement, son adresse et vos coordonnées. Uber étudie chaque demande et ne peut pas accepter tous les établissements.</li>
<li><b>Fournissez les documents demandés.</b> La liste figure dans les conditions d'Uber Eats pour la France, détaillée plus bas.</li>
<li><b>Lisez votre bon de commande.</b> C'est le document qui fixe vos frais : prenez le temps de le lire avant de signer.</li>
<li><b>Préparez votre menu.</b> Plats, prix, catégories, descriptions, photos et horaires.</li>
<li><b>Passez votre première semaine à ajuster.</b> Vos premiers clients découvrent votre page : elle doit être complète et exacte.</li></ol>

<h2>Les documents à préparer</h2>
<p>Les <a href="https://www.uber.com/fr/fr/legal/uber-eats-merchant-terms-and-conditions/" rel="nofollow">conditions complémentaires Uber Eats pour les partenaires</a> en France prévoient une « documentation requise » qui comprend :</p>
<ul class="ticks"><li>votre licence commerciale ;</li><li>vos identifiants fiscaux ;</li><li>les informations sur votre régime de TVA ;</li><li>vos coordonnées bancaires ;</li><li>vos informations de facturation.</li></ul>
<p>Ces mêmes conditions vous demandent de garder vos numéros <b>SIREN</b> et <b>SIRET</b> exacts et à jour. Uber peut aussi vous demander un <b>extrait Kbis</b> : sa <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/quest-ce-quun-extrait-kbis-et-comment-puis-je-me-le-procurer%C2%A0?nodeId=6691b88b-3a42-4a49-bc87-e2890b2f0d14" rel="nofollow">page d'aide sur le Kbis</a> explique ce que c'est et comment l'obtenir, et précise que ces documents supplémentaires sont demandés en raison de la révision de la directive européenne sur les services de paiement.</p>

<h2>Ce qu'il est pratique d'avoir sous la main</h2>
<p>Ce n'est pas une liste d'Uber, mais ces éléments vous feront gagner du temps au moment de créer votre page :</p>
<ul class="ticks"><li>votre menu à jour, avec les prix TTC que vous voulez afficher en livraison ;</li><li>vos horaires, ceux où vous pouvez vraiment préparer et emballer les commandes ;</li><li>des photos de vos plats phares ;</li><li>une courte description pour chaque plat.</li></ul>
<p>Uber recommande d'ajouter une description détaillée et une photo quand vous créez un article (<a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/modifier-votre-menu-uber-eats?nodeId=49fa4c19-7c4f-408f-97a3-42dbdc56ffbe" rel="nofollow">page d'aide sur la modification du menu</a>). Les règles à respecter sont dans ses <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/merchant-submitted-menu-catalog-photo-guidelines?nodeId=6985355b-0426-4523-94f2-89bb9b0566e9" rel="nofollow">consignes pour les photos de menu</a>, et notre guide pour <a href="/fr/guides/ajouter-photos-menu-uber-eats.html">ajouter des photos à votre menu</a> détaille chaque étape.</p>

<h2>Ce que cela coûte</h2>
<p>Les <a href="https://www.uber.com/fr/fr/legal/uber-eats-merchant-terms-and-conditions/" rel="nofollow">conditions d'Uber Eats pour la France</a> prévoient deux frais principaux :</p>
<ul class="ticks"><li><b>Les frais d'activation</b>, payés pour l'activation de votre compte sur l'application Uber Eats.</li><li><b>Les frais de service</b>, payés à Uber France pour l'utilisation des services Uber Eats. Leur taux dépend du mode, par exemple la livraison par les coursiers Uber ou le retrait par le client.</li></ul>
<p>Les montants sont écrits dans votre <b>bon de commande</b>. Nous n'avons trouvé aucune grille tarifaire publique d'Uber France : ne vous fiez pas aux chiffres qui circulent en ligne, et demandez les vôtres avant de signer. Notre guide sur la <a href="/fr/guides/commission-uber-eats-restaurant-france.html">commission Uber Eats en France</a> explique le calcul et les questions à poser.</p>

<h2>Fixez vos prix avant d'ouvrir</h2>
<p>Les frais de service sont calculés sur chaque commande : un prix qui fonctionne au comptoir peut vous faire perdre de l'argent en livraison. Faites le calcul plat par plat avec notre guide pour <a href="/fr/guides/prix-menu-uber-eats.html">fixer vos prix sur Uber Eats</a>.</p>

<h2>Votre première semaine</h2>
<ul class="ticks"><li>Vos meilleures ventes en premier, chacune avec une photo claire de votre vrai plat.</li><li>Une courte description pour chaque plat. Testez les vôtres avec notre <a href="/fr/outils/verificateur-description-menu.html">vérificateur de description de plat</a> gratuit.</li><li>Des horaires qui correspondent aux moments où vous pouvez vraiment cuisiner et emballer.</li><li>Une commande passée chez vous, pour voir votre page et vos emballages comme vos clients.</li></ul>
<p>La liste complète est dans notre guide pour <a href="/fr/guides/debuter-sur-uber-eats.html">débuter sur Uber Eats</a>.</p>

<p>Besoin d'aide pour le menu et les photos ? Nous commençons par une <a href="/fr/contact.html">maquette gratuite</a> de votre future page, pour que vous décidiez sans rien payer.</p>
""",
    },
    {
        "slug": "commission-uber-eats-restaurant-france",
        "alt": None,
        "key": "commission",
        "answer": "Uber France ne publie pas de taux de commission que nous ayons pu trouver. Vos frais de service sont un pourcentage du prix de vente TTC de vos articles, avec un taux par mode (livraison par les coursiers Uber, retrait par le client) fixé dans votre <b>bon de commande</b>. Le contrat prévoit aussi des frais d'activation, dont le montant figure dans ce même document.",
        "faq": [("Quel est le taux de commission Uber Eats en France ?", "Nous n'avons trouvé aucun taux public. Les conditions d'Uber Eats pour la France indiquent que le taux des frais de service de chaque mode, par exemple la livraison par les coursiers Uber ou le retrait, est fixé dans le bon de commande de chaque restaurant. Votre taux est celui écrit dans le vôtre."),
                ("Comment se calculent les frais de service Uber Eats ?", "Pour les commandes passées sur l'application, les frais de service sont égaux au prix de vente des articles, TVA incluse, multiplié par le pourcentage prévu dans votre bon de commande."),
                ("Combien coûtent les frais d'activation Uber Eats ?", "Les conditions d'Uber Eats pour la France les définissent comme ce que paie le restaurant pour l'activation de son compte sur l'application, sans en donner le montant. Nous n'avons trouvé aucun montant public : il figure dans votre bon de commande. Posez la question avant de signer.")],
        "title": "Commission Uber Eats en France : taux et frais d'activation",
        "short": "Commission Uber Eats en France",
        "desc": "Commission Uber Eats pour les restaurants en France : frais de service, frais d'activation, leur calcul, et où trouver votre taux dans votre bon de commande.",
        "img": "fees",
        "related": ["prix-menu-uber-eats", "inscrire-restaurant-uber-eats-france", "uber-eats-deliveroo-just-eat-conseils-menu"],
        "lead": "Avant de fixer vos prix ou de lancer une promotion, il faut savoir ce qu'Uber Eats prélève sur chaque commande. Voici ce que disent les conditions d'Uber pour la France, ce qu'elles ne disent pas, et comment faire le calcul avec votre propre taux.",
        "body": """
<h2>Les frais prévus par le contrat</h2>
<p>Les <a href="https://www.uber.com/fr/fr/legal/uber-eats-merchant-terms-and-conditions/" rel="nofollow">conditions complémentaires Uber Eats pour les partenaires</a> en France regroupent trois choses sous le mot « Frais » :</p>
<ul class="ticks"><li><b>Les frais de service</b> : ce que vous payez à Uber France pour utiliser les services Uber Eats. C'est ce que l'on appelle couramment la commission.</li><li><b>Les frais d'activation</b> : ce que vous payez pour l'activation de votre compte sur l'application Uber Eats.</li><li><b>Les indemnités</b> : le contrat les compte aussi parmi les frais. Demandez à Uber dans quels cas elles s'appliquent.</li></ul>

<h2>Comment se calculent les frais de service</h2>
<p>Pour les commandes passées sur l'application (les commandes Marketplace), les conditions donnent la formule :</p>
<p><b>frais de service = prix de vente des articles, TVA incluse × votre pourcentage de frais de service</b></p>
<p>Le calcul se fait donc sur le prix TTC que paie le client pour vos plats. Et le pourcentage n'est pas forcément le même partout : les conditions précisent que le taux de chaque mode, par exemple la livraison par les coursiers Uber ou le retrait par le client, est fixé dans votre <b>bon de commande</b>.</p>

<h2>Pourquoi vous ne trouverez pas de taux officiel</h2>
<p>Les conditions d'Uber pour la France ne donnent ni taux, ni montant de frais d'activation. Nous n'avons pas non plus trouvé de grille tarifaire publique d'Uber France. Les pourcentages que vous lirez sur des blogs ou des forums peuvent venir d'autres pays, d'autres offres ou d'anciens contrats : ils ne disent pas ce que vous paierez. Le seul chiffre qui compte est celui de votre contrat.</p>

<h2>Où trouver vos chiffres</h2>
<ul class="ticks"><li><b>Votre bon de commande.</b> C'est le document qui fixe votre taux pour chaque mode et le montant des frais d'activation. Gardez une copie à portée de main.</li><li><b>La partie paiements d'Uber Eats Manager.</b> Après vos premières commandes, comparez les frais prélevés avec le taux de votre bon de commande. Si quelque chose ne correspond pas, contactez Uber.</li></ul>

<h2>Faire le calcul avec votre taux</h2>
<p>Prenez une de vos meilleures ventes. Dans cet exemple fictif, le plat est vendu 15,00 € TTC sur l'application et livré par un coursier Uber. Le taux n'est volontairement pas chiffré : remplacez « votre taux » par celui écrit dans votre bon de commande pour ce mode.</p>
<table class="compare"><tr><th>Étape</th><th>Calcul</th></tr>
<tr><td>Prix payé par le client</td><td>15,00 € TTC</td></tr>
<tr><td>Frais de service</td><td>15,00 € × votre taux</td></tr>
<tr><td>Ingrédients et emballage (exemple)</td><td>5,00 €</td></tr>
<tr><td>Ce qu'il vous reste</td><td>15,00 € moins les frais de service, moins 5,00 €</td></tr></table>
<p>Concrètement, si votre bon de commande indique un taux de X %, les frais de service sont de 15,00 € × X ÷ 100. Ce qui reste doit encore couvrir la TVA due sur la vente, le loyer et les salaires.</p>
<p>Faites ce calcul pour vos dix meilleures ventes, puis une seconde fois avec le taux du retrait si vous proposez ce mode. Si un plat vous laisse trop peu, changez son prix ou sa portion, ou ne le proposez plus en livraison.</p>

<h2>Les questions à poser avant de signer</h2>
<ul class="ticks"><li>Demandez votre taux de frais de service pour chaque mode : livraison par les coursiers Uber, retrait par le client.</li><li>Demandez le montant des frais d'activation et la façon dont ils sont payés.</li><li>Demandez dans quels cas des indemnités s'appliquent.</li><li>Demandez si d'autres frais peuvent s'ajouter, par exemple quand vous lancez une promotion.</li><li>Gardez une copie de votre bon de commande signé.</li></ul>

<h2>Ensuite : vos prix</h2>
<p>Une fois votre taux connu, vous pouvez fixer vos prix de livraison plat par plat. Notre guide pour <a href="/fr/guides/prix-menu-uber-eats.html">fixer les prix de votre menu sur Uber Eats</a> explique la méthode, et notre guide pour <a href="/fr/guides/inscrire-restaurant-uber-eats-france.html">inscrire votre restaurant sur Uber Eats</a> reprend les étapes de l'inscription.</p>
""",
    },
    {
        "slug": "ajouter-photos-menu-uber-eats",
        "alt": "how-to-add-photos-to-uber-eats-menu",
        "answer": "Pour ajouter une photo à un plat sur Uber Eats, ouvrez Menu Maker dans Uber Eats Manager, cliquez sur Overview puis sur l'article, ajoutez la photo dans la section Photo, enregistrez, puis demandez l'approbation. Uber indique vérifier les photos dans un délai de 72 heures. Utilisez un JPG ou un PNG de 10 Mo maximum, au format 5:4, d'au moins 550 × 440 pixels.",
        "faq": [("Comment ajouter des photos à mon menu Uber Eats ?", "Dans Uber Eats Manager, ouvrez Menu Maker, cliquez sur Overview, choisissez l'article, ajoutez la photo dans la section Photo, enregistrez, puis demandez l'approbation. La photo s'affiche une fois approuvée par Uber."),
                ("Pourquoi ma nouvelle photo n'apparaît pas encore sur Uber Eats ?", "Les photos doivent être approuvées avant d'apparaître. Uber indique les vérifier dans un délai de 72 heures : patientez avant d'envoyer une seconde fois la même photo."),
                ("Quelle taille pour une photo de plat sur Uber Eats ?", "Uber recommande le format 5:4 (jusqu'à 6:4), au moins 550 × 440 pixels, en JPG ou PNG de 10 Mo maximum. L'image de couverture doit faire 2880 × 2304 pixels, en JPEG.")],
        "title": "Ajouter des photos à votre menu Uber Eats, étape par étape",
        "short": "Ajouter des photos sur Uber Eats",
        "desc": "Pas à pas pour les restaurateurs : ajouter ou remplacer les photos de vos plats dans Uber Eats Manager, les règles d'Uber et que faire si une photo bloque.",
        "img": "flatlay",
        "related": ["photos-uber-eats-exigences", "photo-uber-eats-ne-se-charge-pas", "photos-plats-telephone"],
        "lead": "Les photos s'ajoutent article par article dans Uber Eats Manager. Voici les étapes tirées des pages d'aide d'Uber, les règles que votre photo doit respecter et comment la vérifier avant l'envoi.",
        "body": """
<h2>Avant de commencer : vérifiez la photo</h2>
<p>D'après les <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/merchant-submitted-menu-catalog-photo-guidelines?nodeId=6985355b-0426-4523-94f2-89bb9b0566e9" rel="nofollow">consignes d'Uber pour les photos de menu</a>, une photo d'article doit :</p>
<ul class="ticks"><li>montrer un seul article, centré ;</li><li>être de préférence au format 5:4 (jusqu'à 6:4) ;</li><li>ne montrer personne, à part des mains ;</li><li>n'avoir ni logo, ni filigrane, ni texte ;</li><li>être nette, sans ombres dures ;</li><li>être un JPG ou un PNG de 10 Mo maximum, d'au moins 550 × 440 pixels.</li></ul>
<p>Notre <a href="/fr/outils/verificateur-photo-uber-eats.html">vérificateur de photo Uber Eats</a> gratuit contrôle le type de fichier, le poids, la taille et le format dans votre navigateur, et peut recadrer la photo en 5:4. Rien n'est envoyé. Toutes les règles sont réunies dans notre guide des <a href="/fr/guides/photos-uber-eats-exigences.html">exigences photo d'Uber Eats</a>.</p>

<h2>Ajouter une photo à un plat</h2>
<p>Ces étapes suivent la <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/adding-cover-images-and-menu-catalog-photos?nodeId=b2dfa2b7-20f2-4f5f-81a3-32fa4c2aea89" rel="nofollow">page d'aide d'Uber sur l'ajout de photos</a>. Les noms des boutons peuvent varier selon la langue et la version de votre interface.</p>
<ol><li>Ouvrez Uber Eats Manager et allez dans <b>Menu Maker</b>.</li><li>Cliquez sur <b>Overview</b> (la vue d'ensemble), puis sélectionnez l'article.</li><li>Allez dans la section <b>Photo</b>.</li><li>Glissez votre photo dans la zone, ou parcourez vos fichiers pour la choisir.</li><li>Enregistrez (<b>Save</b>).</li><li>Demandez l'approbation (<b>Request approval</b>).</li></ol>

<h2>Ajouter l'image de couverture</h2>
<p>La grande photo en haut de votre page se gère à part : d'après la même <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/adding-cover-images-and-menu-catalog-photos?nodeId=b2dfa2b7-20f2-4f5f-81a3-32fa4c2aea89" rel="nofollow">page d'aide</a>, elle s'importe depuis l'onglet de la page <b>Stores</b>, celle de vos établissements. Ses règles sont plus strictes (<a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/merchant-submitted-menu-catalog-photo-guidelines?nodeId=6985355b-0426-4523-94f2-89bb9b0566e9" rel="nofollow">consignes photo d'Uber</a>) :</p>
<ul class="ticks"><li>un JPEG au format 5:4, en 2880 × 2304 pixels ;</li><li>des produits que vous vendez ;</li><li>pas de devanture, pas de texte, pas de personnes identifiables.</li></ul>
<p>Notre guide sur la <a href="/fr/guides/photo-banniere-uber-eats.html">photo de bannière</a> vous aide à choisir le bon plat.</p>

<h2>Après l'envoi : la vérification</h2>
<p>Une photo ajoutée doit être approuvée avant d'apparaître. Sur sa <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/modifier-votre-menu-uber-eats?nodeId=49fa4c19-7c4f-408f-97a3-42dbdc56ffbe" rel="nofollow">page d'aide sur la modification du menu</a>, Uber indique que les photos envoyées sont vérifiées dans un délai de 72 heures. Avant de renvoyer une photo, regardez de nouveau l'article dans Uber Eats Manager. Et si vous changez de carte, envoyez vos photos quelques jours avant.</p>

<h2>La photo ne se charge pas ?</h2>
<p>Un fichier trop lourd, un format absent de la liste d'Uber (comme le HEIC de l'iPhone) ou une photo trop petite sont les causes habituelles. Notre guide <a href="/fr/guides/photo-uber-eats-ne-se-charge-pas.html">photo Uber Eats qui ne se charge pas</a> reprend chaque solution.</p>

<h2>Par quels plats commencer</h2>
<p>Commencez par vos dix meilleures ventes, puis le reste du menu. Uber recommande d'ajouter une description détaillée et une photo à chaque nouvel article (<a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/modifier-votre-menu-uber-eats?nodeId=49fa4c19-7c4f-408f-97a3-42dbdc56ffbe" rel="nofollow">modifier votre menu</a>). En France, sa <a href="https://www.uber.com/fr/fr/legal/merchant-success-score-policy/" rel="nofollow">politique Merchant Success Score</a> comprend d'ailleurs une mesure du menu : la part des articles qui ont une photo et une description.</p>
<p>Prenez vos photos à la lumière du jour, avec le même fond et le même angle pour chaque plat. Notre guide pour <a href="/fr/guides/photos-plats-telephone.html">photographier vos plats au téléphone</a> montre comment.</p>
<p>Vous préférez déléguer ? Notre offre <a href="/fr/pricing.html">Menu et Photos</a> améliore les photos de vos vrais plats et vous les livre au bon format.</p>
""",
    },
    {
        "slug": "ameliorer-note-uber-eats",
        "alt": "improve-uber-eats-rating-restaurant",
        "answer": "Pour améliorer la note de votre restaurant sur Uber Eats, faites en sorte que ce qui arrive corresponde à ce que le client a vu : photos et descriptions fidèles, emballages adaptés, plats épuisés retirés à temps et commandes vérifiées avant le départ. Lisez vos retours dans Uber Eats Manager et corrigez ce qui revient. Personne ne peut promettre une note, mais ces points dépendent de vous.",
        "faq": [("Comment améliorer la note de mon restaurant sur Uber Eats ?", "Faites correspondre votre page à ce qui arrive : vraies photos, descriptions exactes, bon emballage, plats épuisés retirés et commandes vérifiées avant le départ. Lisez ensuite vos retours dans Uber Eats Manager et corrigez ce qui se répète."),
                ("Comment fonctionne la note d'un restaurant sur Uber Eats ?", "Les clients notent leur commande de 1 à 5 étoiles. D'après la page d'aide d'Uber sur les notes, la note de votre établissement repose sur les notes récentes : vos améliorations se voient donc avec le temps."),
                ("Où voir les avis de mes clients sur Uber Eats ?", "Dans Uber Eats Manager. La page d'aide d'Uber explique où trouver la note de votre établissement, les notes de chaque article et les commentaires écrits des clients.")],
        "title": "Améliorer la note de votre restaurant sur Uber Eats",
        "short": "Améliorer sa note Uber Eats",
        "desc": "Des moyens concrets pour améliorer la note de votre restaurant sur Uber Eats : photos et descriptions fidèles, emballage, ruptures, lecture des avis.",
        "img": "handover",
        "related": ["repondre-avis-uber-eats", "plus-de-commandes-uber-eats", "descriptions-menu-uber-eats"],
        "lead": "Votre note dépend de ce qui se passe après la commande. Vous ne maîtrisez ni la circulation ni le livreur, mais une bonne partie reste entre vos mains. Voici ce qu'un restaurant peut faire, sans promesse.",
        "body": """
<h2>Comment fonctionne la note sur Uber Eats</h2>
<p>Une fois la commande reçue, le client la note de 1 à 5 étoiles. La <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/ratings-faq?nodeId=142bda2b-1760-4570-8130-64cadc93eaee" rel="nofollow">page d'aide d'Uber sur les notes</a> précise que la note de votre établissement repose sur les notes récentes : vos changements se voient avec le temps, pas du jour au lendemain. Votre note, les notes de chaque article et les commentaires écrits sont visibles dans Uber Eats Manager (<a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/how-can-i-view-customer-reviews-and-feedback-in-uber-eats-manager?nodeId=25a280eb-2e90-4124-b52d-c79a83263ba1" rel="nofollow">où les trouver</a>).</p>

<h2>1. Une page qui correspond à ce qui arrive</h2>
<p>Une déception vient souvent d'un écart entre ce que le client attendait et ce qu'il reçoit. Montrez de vraies photos de vos plats, en vraies portions, et des descriptions qui disent ce qu'il y a dans le plat et sa taille. Notre guide pour <a href="/fr/guides/descriptions-menu-uber-eats.html">écrire vos descriptions</a> vous aide, et le <a href="/fr/outils/verificateur-description-menu.html">vérificateur de description de plat</a> repère les mots vagues.</p>

<h2>2. Un emballage qui supporte le trajet</h2>
<ul class="ticks"><li>Des boîtes ventilées pour les frites et les panures, pour qu'elles restent croustillantes.</li><li>Les sauces et vinaigrettes dans des pots fermés, à part.</li><li>Le chaud et le froid séparés, la glace ou la salade dans leur propre contenant.</li><li>Un sac fermé, pour que rien ne se renverse en route.</li></ul>

<h2>3. Retirez tout de suite les plats épuisés</h2>
<p>Un article manquant, c'est une commande modifiée ou annulée, et un client mécontent. Dès qu'un plat est épuisé, rendez cet article indisponible dans Uber Eats Manager, puis réactivez le plat quand vous pouvez de nouveau le préparer.</p>

<h2>4. Vérifiez chaque commande avant le départ</h2>
<p>Un coup d'œil au ticket et au sac évite la boisson, l'accompagnement ou la sauce oubliés, une cause de mauvaise note facile à éviter. Prévoyez un endroit au comptoir où chaque sac est contrôlé avant d'être remis au livreur.</p>

<h2>5. Lisez vos retours et corrigez ce qui revient</h2>
<p>Un commentaire isolé, c'est l'avis d'une personne. Le même commentaire deux fois mérite qu'on agisse. S'il porte sur le plat, revoyez la recette ou la portion. S'il porte sur les attentes, corrigez la photo ou la description. Notre guide pour <a href="/fr/guides/repondre-avis-uber-eats.html">répondre aux avis Uber Eats</a> donne des exemples de réponses.</p>

<h2>6. Des horaires honnêtes</h2>
<p>N'acceptez des commandes que lorsque vous pouvez bien les préparer et les emballer. Les coups de feu sont les moments où les erreurs arrivent : si la cuisine est débordée, mieux vaut prendre moins de commandes un moment que d'envoyer des plats bâclés.</p>

<h2>Ce que vous ne maîtrisez pas</h2>
<p>La circulation, le livreur et la météo jouent sur certaines notes, et c'est frustrant. Gardez votre énergie pour ce que vous pouvez changer : une page claire et exacte, et des plats qui voyagent bien.</p>
""",
    },
]

GUIDES_FR_B = [
    {
        "slug": "exemples-descriptions-menu-uber-eats",
        "alt": "uber-eats-menu-description-examples",
        "answer": "Voici 30 exemples de descriptions de plats pour Uber Eats, classés en 10 cuisines : burgers, pizzas, bistrot, boulangerie, café, cuisine asiatique, kebab, cuisine indienne, tacos et desserts. Chacune respecte notre repère de 140 à 260 caractères, soit environ deux phrases courtes, et cite les ingrédients principaux, la cuisson et ce qui accompagne le plat.",
        "faq": [("Quelle longueur pour une description de plat sur Uber Eats ?", "Uber ne fixe pas de longueur précise. Notre repère : entre 140 et 260 caractères, soit environ deux phrases courtes. Assez pour citer les ingrédients, assez court pour être lu sur un téléphone."),
                ("Que doit contenir une bonne description de plat ?", "Ce qu'est le plat, ses ingrédients principaux, un détail qui vous ressemble, et ce que le client doit savoir avant de commander : la taille, le niveau d'épices ou ce qui est servi avec."),
                ("Reprendre ces exemples tels quels, c'est possible ?", "Utilisez ces exemples comme point de départ. Changez les ingrédients, les tailles et les accompagnements pour qu'ils correspondent exactement à ce que vous servez, afin que chaque mot soit vrai.")],
        "title": "30 exemples de descriptions de plats pour votre menu Uber Eats",
        "short": "30 exemples de descriptions de plats",
        "desc": "30 exemples de descriptions de plats pour Uber Eats, par cuisine : burgers, pizzas, bistrot, boulangerie, café, asiatique, kebab, indien, tacos et desserts.",
        "img": "notebook",
        "related": ["descriptions-menu-uber-eats", "meilleures-ventes-ordre-menu-uber-eats", "ameliorer-note-uber-eats"],
        "lead": "Le plus rapide pour écrire de bonnes descriptions, c'est de partir de bons exemples. En voici 30, classés par cuisine. Remplacez les ingrédients, les tailles et les accompagnements par les vôtres pour que chaque mot soit vrai.",
        "body": """
<h2>Comment ces exemples sont écrits</h2>
<p>Uber recommande d'ajouter une description à vos articles, car elle aide les clients à choisir (<a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/quelles-informations-dois-je-fournir-concernant-mon-menu-pour-uber-eats?nodeId=83ae0158-34aa-45d7-9fff-6bab96354072" rel="nofollow">informations à fournir pour votre menu</a>). Uber ne fixe pas de longueur. Notre repère : <b>entre 140 et 260 caractères</b>, soit environ deux phrases courtes. Tous les exemples plus bas le respectent.</p>
<p>Chaque description dit ce qu'est le plat, cite ses ingrédients principaux, ajoute un détail qui vous ressemble et répond à une question avant qu'elle soit posée : la taille, le niveau d'épices ou ce qui est servi avec. Collez la vôtre dans notre <a href="/fr/outils/verificateur-description-menu.html">vérificateur de description de plat</a> gratuit pour contrôler la longueur et les mots.</p>

<h2>Burgers, pizzas, kebab et tacos</h2>
<h3>Burgers</h3>
<table class="compare"><tr><th>Plat</th><th>Description</th></tr>
<tr><td>Cheeseburger</td><td>Steak de bœuf haché grillé, cheddar fondu, pickles, oignons, ketchup et moutarde dans un pain brioché toasté. Cuit à la commande. Ajoutez du bacon ou un second steak dans les options.</td></tr>
<tr><td>Burger poulet croustillant</td><td>Haut de cuisse de poulet mariné au lait ribot puis frit, salade de chou, pickles et mayonnaise chipotle dans un pain brioché. Croustillant dehors, juteux dedans, avec une légère pointe piquante.</td></tr>
<tr><td>Burger végétarien</td><td>Galette maison de haricots noirs et maïs, avocat, salade, tomate et sauce fumée dans un pain toasté. Entièrement végétarien, et vegan sans la mayonnaise, à préciser en note.</td></tr></table>
<h3>Pizzas</h3>
<table class="compare"><tr><th>Plat</th><th>Description</th></tr>
<tr><td>Margherita</td><td>Sauce tomate maison, mozzarella fior di latte, basilic frais et filet d'huile d'olive sur notre pâte maturée, cuite au four à bois. Pizza de 30 cm, coupée en 6 parts.</td></tr>
<tr><td>Reine</td><td>Sauce tomate, mozzarella, jambon blanc, champignons de Paris et olives noires sur notre pâte fine et croustillante. Le classique des pizzerias françaises. Pizza de 30 cm, 6 parts.</td></tr>
<tr><td>Quatre fromages</td><td>Mozzarella, gorgonzola, chèvre et emmental sur une base crème, avec un tour de poivre noir à la sortie du four. Généreuse et fondante. Pizza de 30 cm, filet de miel en option.</td></tr></table>
<h3>Kebab et grillades</h3>
<table class="compare"><tr><th>Plat</th><th>Description</th></tr>
<tr><td>Kebab galette</td><td>Viande de veau et dinde grillée à la broche, salade, tomates, oignons et sauce blanche, le tout roulé dans une galette toastée. Servi avec des frites. Sauce samouraï ou harissa au choix.</td></tr>
<tr><td>Assiette grillades</td><td>Brochettes de poulet et d'agneau grillées au charbon, riz pilaf, salade, crudités et sauce blanche à part, avec du pain chaud. Un repas complet dans une seule boîte.</td></tr>
<tr><td>Sandwich falafels</td><td>Falafels maison croustillants, houmous, taboulé, crudités et sauce tahini dans un pain pita chaud. Entièrement vegan et préparé à la commande. Ajoutez du piment si vous aimez relevé.</td></tr></table>
<h3>Tacos et cuisine mexicaine</h3>
<table class="compare"><tr><th>Plat</th><th>Description</th></tr>
<tr><td>French tacos poulet</td><td>Galette de blé garnie de poulet mariné, de frites et de sauce fromagère maison, pliée puis grillée à la plancha. Taille M avec une viande ou L avec deux. Sauce algérienne, samouraï ou blanche au choix.</td></tr>
<tr><td>Burrito bœuf</td><td>Grande tortilla de blé, bœuf haché épicé, riz, haricots rouges, cheddar, crème et pico de gallo. Moyennement relevé. Version végétarienne aux légumes grillés dans les options.</td></tr>
<tr><td>Tacos al pastor</td><td>Trois tortillas de maïs garnies de porc mariné à l'ananas, oignon, coriandre fraîche et citron vert. Salsa verde piquante servie à part, pour doser comme vous voulez.</td></tr></table>

<h2>Bistrot, boulangerie et café</h2>
<h3>Cuisine française de bistrot</h3>
<table class="compare"><tr><th>Plat</th><th>Description</th></tr>
<tr><td>Bœuf bourguignon</td><td>Bœuf mijoté plusieurs heures au vin rouge avec carottes, oignons, champignons et lardons. Servi avec des pommes de terre vapeur. Une portion pour une personne, à réchauffer si besoin.</td></tr>
<tr><td>Confit de canard</td><td>Cuisse de canard confite, peau dorée et croustillante, servie avec des pommes de terre sautées à l'ail et au persil. Livrée dans une boîte ventilée pour garder le croustillant.</td></tr>
<tr><td>Salade de chèvre chaud</td><td>Toasts de chèvre gratinés au miel sur salade verte, noix, tomates cerises et lardons, vinaigrette à la moutarde à part. Version végétarienne sans lardons, à préciser en note.</td></tr></table>
<h3>Boulangerie et viennoiseries</h3>
<table class="compare"><tr><th>Plat</th><th>Description</th></tr>
<tr><td>Croissant</td><td>Croissant pur beurre, façonné chaque nuit et cuit le matin même jusqu'à ce qu'il soit bien doré. Croustillant dehors et moelleux dedans. Vendu à l'unité ou par lot de 4.</td></tr>
<tr><td>Pain au chocolat</td><td>Pâte feuilletée pur beurre et deux barres de chocolat noir, le tout cuit chaque matin dans notre fournil. Croustillant et fondant à la fois. À l'unité, ou par lot de 4 pour le petit déjeuner.</td></tr>
<tr><td>Jambon beurre</td><td>Baguette tradition, beurre doux et jambon blanc supérieur, préparé à la commande pour rester croustillant. Simple et bien garni. Ajoutez de l'emmental ou des cornichons dans les options.</td></tr></table>
<h3>Café et petit déjeuner</h3>
<table class="compare"><tr><th>Plat</th><th>Description</th></tr>
<tr><td>Petit déjeuner complet</td><td>Deux œufs brouillés, bacon grillé, pain de campagne toasté, beurre et confiture, avec un jus d'orange pressé. Les œufs arrivent dans leur propre boîte pour rester chauds.</td></tr>
<tr><td>Avocado toast</td><td>Avocat écrasé au citron, feta, tomates cerises et graines de sésame sur une tranche de pain au levain toastée. Végétarien. Ajoutez un œuf poché ou du saumon fumé dans les options.</td></tr>
<tr><td>Latte glacé</td><td>Notre espresso maison versé sur des glaçons avec du lait froid, en grand format de 40 cl. Lait d'avoine ou d'amande au choix, et sirop vanille ou caramel en option.</td></tr></table>

<h2>Cuisines asiatique et indienne</h2>
<h3>Cuisine asiatique : bo bun, ramen, poke</h3>
<table class="compare"><tr><th>Plat</th><th>Description</th></tr>
<tr><td>Bo bun bœuf</td><td>Vermicelles de riz, bœuf sauté à la citronnelle, deux nems, salade, carottes, concombre, menthe et cacahuètes. Sauce nuoc mam à part, à verser au dernier moment pour garder le croquant.</td></tr>
<tr><td>Ramen tonkotsu</td><td>Bouillon de porc mijoté, nouilles de blé, chashu de porc, œuf mollet mariné, maïs, oignons verts et nori. Bouillon et nouilles livrés séparément, à réunir juste avant de manger.</td></tr>
<tr><td>Poke bowl saumon</td><td>Saumon frais mariné au soja, riz vinaigré, avocat, edamame, concombre, chou rouge et graines de sésame, sauce à part. Remplacez le saumon par du tofu dans les options.</td></tr></table>
<h3>Cuisine indienne</h3>
<table class="compare"><tr><th>Plat</th><th>Description</th></tr>
<tr><td>Butter chicken</td><td>Poulet mariné cuit au tandoor puis mijoté dans une sauce tomate, beurre et crème, doux et parfumé. Servi avec du riz basmati. Ajoutez un cheese naan dans les options.</td></tr>
<tr><td>Biryani poulet</td><td>Riz basmati cuit avec du poulet mariné, des oignons frits, du safran et des épices entières, servi avec un raïta au concombre à part. Moyennement épicé : demandez doux ou fort en note.</td></tr>
<tr><td>Dal</td><td>Lentilles jaunes mijotées au curcuma, à l'ail et au gingembre, relevées de cumin et de feuilles de curry. Plat doux et végétarien, servi avec du riz basmati.</td></tr></table>

<h2>Desserts et pâtisseries</h2>
<table class="compare"><tr><th>Plat</th><th>Description</th></tr>
<tr><td>Tarte au citron meringuée</td><td>Pâte sablée maison, crème au citron jaune acidulée et meringue italienne dorée au chalumeau. Une part généreuse, livrée dans une boîte rigide pour bien voyager.</td></tr>
<tr><td>Fondant au chocolat</td><td>Fondant au chocolat noir, cœur coulant après quelques minutes au four. Livré avec une crème anglaise maison à part. Pour une personne, ou deux si vous aimez partager.</td></tr>
<tr><td>Tiramisu</td><td>Biscuits imbibés de café, crème au mascarpone légère et cacao amer, monté chaque matin. Servi en pot individuel fermé, à garder au frais jusqu'au dessert.</td></tr></table>

<h2>Adaptez ces exemples à votre carte</h2>
<ul class="ticks"><li>Gardez le nom que vos clients connaissent, puis expliquez le plat.</li><li>Ne citez que les ingrédients vraiment présents.</li><li>Indiquez tailles, poids et nombre de pièces exacts.</li><li>N'écrivez végétarien, vegan ou sans gluten que si c'est vrai.</li><li>Évitez les mots vagues comme délicieux ou incroyable : les ingrédients en disent plus.</li></ul>
<p>Les photos et descriptions comptent aussi pour Uber : sa politique Merchant Success Score inclut une mesure du menu, le pourcentage d'articles qui ont une photo et une description (<a href="https://www.uber.com/fr/fr/legal/merchant-success-score-policy/" rel="nofollow">politique Merchant Success Score</a>).</p>
<p>Pour la méthode derrière ces exemples, voir notre guide pour <a href="/fr/guides/descriptions-menu-uber-eats.html">écrire des descriptions de plats qui donnent envie</a>. Si vous préférez déléguer l'écriture, notre offre <a href="/fr/pricing.html">Menu Fix</a> réécrit chaque plat de votre menu.</p>
""",
    },
    {
        "slug": "meilleures-ventes-ordre-menu-uber-eats",
        "alt": "best-sellers-uber-eats-menu-order",
        "answer": "Mettez vos meilleures ventes en premier : une première catégorie courte avec vos cinq ou six plats les plus commandés, puis les autres catégories dans l'ordre du repas (plats, accompagnements, boissons, desserts), et le plat le plus populaire en tête de chaque catégorie. Revoyez cet ordre quand vos ventes changent.",
        "faq": [("Comment mettre ses meilleures ventes en premier sur Uber Eats ?", "Créez une première catégorie, par exemple Les plus populaires, avec vos cinq ou six plats les plus commandés, puis placez cette catégorie tout en haut de votre menu dans Uber Eats Manager."),
                ("Comment savoir quels plats se vendent le mieux ?", "Regardez vos commandes passées dans Uber Eats Manager et les chiffres de votre caisse. Retenez les plats que les clients commandent vraiment, pas ceux que vous aimeriez vendre davantage."),
                ("À quelle fréquence revoir l'ordre du menu ?", "Toutes les quelques semaines, et à chaque changement de carte ou de saison, ou quand vous ajoutez un nouveau plat.")],
        "title": "Menu Uber Eats : mettre vos meilleures ventes en premier",
        "short": "Meilleures ventes en premier",
        "desc": "Comment ordonner les catégories et les plats de votre menu Uber Eats pour que vos meilleures ventes soient vues en premier, et quand revoir cet ordre.",
        "img": "bestsellers",
        "related": ["categories-menu-uber-eats", "plus-de-commandes-uber-eats", "exemples-descriptions-menu-uber-eats"],
        "lead": "Beaucoup de clients ne font pas défiler très loin. L'ordre de votre menu décide des plats qu'ils voient en premier. Voici comment le régler pour que vos meilleurs plats soient tout en haut.",
        "body": """
<h2>1. Trouvez vos vraies meilleures ventes</h2>
<p>Regardez vos commandes passées dans Uber Eats Manager et les chiffres de votre caisse. Retenez les cinq ou six plats les plus commandés. Prenez ce qui se vend vraiment, pas ce que vous aimeriez vendre davantage.</p>
<p>Uber Eats Manager affiche aussi les notes par article et les commentaires écrits des clients (<a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/how-can-i-view-customer-reviews-and-feedback-in-uber-eats-manager?nodeId=25a280eb-2e90-4124-b52d-c79a83263ba1" rel="nofollow">voir les avis dans Uber Eats Manager</a>). Un plat très commandé et bien noté est un candidat idéal pour le haut du menu.</p>

<h2>2. Créez une catégorie meilleures ventes, tout en haut</h2>
<p>Créez une catégorie <b>Les plus populaires</b>, <b>Nos incontournables</b> ou <b>Les préférés de nos clients</b>, ajoutez ces plats et placez cette catégorie en premier. Gardez la courte : cinq ou six plats, pas toute la carte. Notre guide pour <a href="/fr/guides/modifier-menu-uber-eats-manager.html">modifier votre menu dans Uber Eats Manager</a> montre où réorganiser les catégories.</p>

<h2>3. Rangez les autres catégories dans l'ordre du repas</h2>
<ol><li>Meilleures ventes</li><li>Vos plats principaux, répartis par type si vous en avez beaucoup</li><li>Entrées, accompagnements et suppléments</li><li>Boissons</li><li>Desserts</li></ol>
<p>Une boulangerie ou un café utilisera plutôt Viennoiseries, Sandwichs, Formules du midi, Boissons chaudes et Pâtisseries. Plus de détails dans notre guide pour <a href="/fr/guides/categories-menu-uber-eats.html">organiser les catégories de votre menu Uber Eats</a>.</p>

<h2>4. Le meilleur plat en tête de chaque catégorie</h2>
<p>L'ordre à l'intérieur d'une catégorie compte aussi. Commencez par le plat le plus populaire ou le plus photogénique, et gardez les articles avec photo vers le haut. Une rangée qui commence par une belle photo attire le regard.</p>

<h2>5. Les meilleures photos et descriptions pour les plats du haut</h2>
<p>Vos meilleures ventes sont les plats les plus vus : c'est là qu'une photo claire et une bonne description comptent le plus. Uber en tient compte aussi : sa politique Merchant Success Score inclut le pourcentage d'articles du menu qui ont une photo et une description (<a href="https://www.uber.com/fr/fr/legal/merchant-success-score-policy/" rel="nofollow">politique Merchant Success Score</a>).</p>
<p>Voir <a href="/fr/guides/ajouter-photos-menu-uber-eats.html">comment ajouter des photos à votre menu</a> et nos <a href="/fr/guides/exemples-descriptions-menu-uber-eats.html">30 exemples de descriptions de plats</a>.</p>

<h2>6. Revoyez l'ordre toutes les quelques semaines</h2>
<p>Les plats préférés changent avec les saisons et les nouveautés. Regardez vos ventes toutes les quelques semaines, et faites monter ou descendre les plats en conséquence. Un plat de saison peut prendre la tête de la catégorie meilleures ventes, tant qu'il reste à la carte.</p>

<h2>Les erreurs courantes</h2>
<ul class="ticks"><li>Les boissons ou les suppléments en première catégorie.</li><li>Une première catégorie trop longue, qui reprend toute la carte.</li><li>Une meilleure vente perdue en bas d'une grande catégorie.</li><li>D'anciennes catégories d'une carte précédente encore en haut.</li><li>Un plat épuisé laissé en tête de menu au lieu d'être mis en pause.</li></ul>
""",
    },
    {
        "slug": "photo-uber-eats-ne-se-charge-pas",
        "alt": "uber-eats-photo-upload-not-working",
        "answer": "Quand une photo ne se charge pas sur Uber Eats ou qu'elle est refusée, la cause est presque toujours la même : un fichier de plus de 10 Mo, un format autre que JPG ou PNG (comme le HEIC des iPhone), une image de moins de 550 × 440 pixels, ou une photo avec du texte, un logo ou plusieurs articles. Corrigez le fichier, puis importez la photo de nouveau dans Uber Eats Manager.",
        "faq": [("Pourquoi ma photo ne se charge pas sur Uber Eats ?", "Vérifiez d'abord le fichier : JPG ou PNG, 10 Mo au maximum, au moins 550 × 440 pixels, au format 5:4 de préférence. Essayez ensuite depuis un ordinateur avec un navigateur à jour."),
                ("Pourquoi ma photo Uber Eats a été refusée ?", "Le plus souvent à cause de texte, d'un logo ou d'un filigrane sur l'image, de plusieurs articles sur la même photo, d'une personne visible (les mains sont acceptées), ou d'une photo floue ou aux ombres dures."),
                ("Combien de temps avant de voir ma nouvelle photo ?", "Les photos doivent être approuvées. D'après l'aide d'Uber, elles sont examinées sous 72 heures. Vérifiez dans Uber Eats Manager avant de l'envoyer une seconde fois.")],
        "title": "Photo Uber Eats qui ne se charge pas ou refusée : causes et solutions",
        "short": "Photo Uber Eats qui ne se charge pas",
        "desc": "Votre photo Uber Eats ne se charge pas ou est refusée ? Les causes fréquentes et leurs solutions : poids, format, taille, cadrage, texte et logos.",
        "img": "laptop",
        "related": ["photos-uber-eats-exigences", "photos-plats-telephone", "ajouter-photos-menu-uber-eats"],
        "lead": "Vous avez une belle photo, mais Uber Eats Manager ne l'accepte pas, ou elle n'apparaît jamais sur votre page. Voici les causes habituelles, une par une, d'après les règles photo d'Uber.",
        "body": """
<h2>1. Le fichier est trop lourd</h2>
<p>Les <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/merchant-submitted-menu-catalog-photo-guidelines?nodeId=6985355b-0426-4523-94f2-89bb9b0566e9" rel="nofollow">règles d'Uber pour les photos de menu</a> acceptent des fichiers de <b>10 Mo</b> au maximum. Une photo qui sort d'un téléphone récent peut dépasser cette limite.</p>
<p><b>Solution :</b> exportez la photo dans une taille plus petite ou avec un peu plus de compression. À 2880 × 2304 pixels, un JPG reste en général bien en dessous de la limite.</p>

<h2>2. Le format n'est pas accepté</h2>
<p>Uber accepte les fichiers <b>JPG</b> et <b>PNG</b>. Les iPhone enregistrent souvent les photos en <b>HEIC</b>, et certaines applications en WEBP : ces formats ne font pas partie de la liste.</p>
<p><b>Solution :</b> enregistrez ou partagez la photo en JPG. Sur iPhone, vous pouvez régler l'appareil photo pour enregistrer en JPG : Réglages, puis Appareil photo, puis Formats, puis Le plus compatible.</p>

<h2>3. La photo est trop petite ou mal cadrée</h2>
<p>Uber demande au moins <b>550 pixels de large et 440 pixels de haut</b>, et recommande un format <b>5:4</b> en paysage (jusqu'à 6:4). Une capture d'écran, une photo récupérée dans une messagerie ou une photo en portrait posent souvent problème.</p>
<p><b>Solution :</b> repartez de la photo d'origine, pas d'une copie reçue sur WhatsApp, et recadrez la photo en 5:4 avec le plat au centre. Notre guide des <a href="/fr/guides/photos-uber-eats-exigences.html">exigences photo d'Uber Eats</a> réunit toutes les tailles.</p>

<h2>4. Le bouton ne fait rien, ou vous ne trouvez pas où importer</h2>
<p>D'après <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/adding-cover-images-and-menu-catalog-photos?nodeId=b2dfa2b7-20f2-4f5f-81a3-32fa4c2aea89" rel="nofollow">l'aide d'Uber pour ajouter des photos</a>, une photo d'article s'ajoute dans Uber Eats Manager : ouvrez Menu Maker, puis la vue d'ensemble (Overview), sélectionnez l'article, allez dans la section Photo, glissez la photo ou parcourez vos fichiers, enregistrez, puis <b>demandez l'approbation</b>. L'image de couverture, elle, s'ajoute depuis la page Stores de votre établissement.</p>
<p><b>Solution :</b> utilisez un ordinateur, mettez votre navigateur à jour ou essayez un autre navigateur, puis rechargez la page. Si rien ne change, contactez l'assistance Uber Eats depuis Uber Eats Manager.</p>

<h2>5. La photo est envoyée, puis refusée</h2>
<p>Chaque photo est vérifiée. Les règles d'Uber demandent un seul article, centré, sur chaque photo d'article. Une photo qui ne les respecte pas risque d'être refusée, par exemple avec :</p>
<ul class="ticks"><li>Du texte, un logo ou un filigrane sur l'image.</li><li>Plusieurs articles sur la même photo.</li><li>Des personnes visibles (des mains qui tiennent le plat sont acceptées).</li><li>Une photo floue.</li><li>Des ombres dures.</li></ul>
<p><b>Solution :</b> reprenez la photo de votre vrai plat, seul, sans rien ajouter sur l'image. Notre guide pour <a href="/fr/guides/photos-plats-telephone.html">photographier vos plats au téléphone</a> vous aide.</p>

<h2>6. La photo est envoyée, mais pas encore visible</h2>
<p>Les photos doivent être approuvées avant de s'afficher. D'après la page d'Uber pour <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/modifier-votre-menu-uber-eats?nodeId=49fa4c19-7c4f-408f-97a3-42dbdc56ffbe" rel="nofollow">modifier votre menu Uber Eats</a>, elles sont examinées sous <b>72 heures</b>.</p>
<p><b>Solution :</b> vérifiez que vous avez bien cliqué sur la demande d'approbation, puis patientez. Contrôlez l'article dans Uber Eats Manager avant d'envoyer une seconde copie.</p>

<h2>7. L'image de couverture ne passe pas</h2>
<p>L'image de couverture en haut de votre page a ses propres règles, toujours d'après les <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/merchant-submitted-menu-catalog-photo-guidelines?nodeId=6985355b-0426-4523-94f2-89bb9b0566e9" rel="nofollow">règles photo d'Uber</a> : <b>JPEG</b>, format <b>5:4</b>, <b>2880 × 2304 pixels</b>, des produits que vous vendez, sans devanture, sans texte et sans personne identifiable.</p>
<p><b>Solution :</b> recadrez une photo de plat en paysage exactement à cette taille. Voir notre guide pour <a href="/fr/guides/photo-banniere-uber-eats.html">choisir votre photo de bannière</a>.</p>

<h2>8. Vérifiez la photo dans votre navigateur</h2>
<p>Notre <a href="/fr/outils/verificateur-photo-uber-eats.html">vérificateur de photo Uber Eats</a> est gratuit. Il contrôle le type de fichier, le poids, la taille en pixels et le format, et peut recadrer la photo en 5:4 à 2880 × 2304 pixels. Tout se passe dans votre navigateur : aucune photo n'est envoyée.</p>

<h2>La liste avant d'importer</h2>
<ul class="ticks"><li>JPG ou PNG, 10 Mo au maximum.</li><li>Au moins 550 × 440 pixels, au format 5:4.</li><li>Un seul vrai plat, centré, sans texte ni logo.</li><li>Une photo nette, sans ombres dures.</li><li>Enregistrez, puis demandez l'approbation.</li></ul>
""",
    },
    {
        "slug": "cout-photos-plats-uber-eats",
        "alt": "uber-eats-food-photography-cost",
        "answer": "Le coût des photos de plats pour Uber Eats dépend de la voie choisie. Uber propose une séance photo aux restaurants partenaires, mais ce qu'elle comprend et son éventuel coût ne sont pas publiés : demandez à l'assistance. Un photographe facture selon son devis, et des photos prises au téléphone puis améliorées restent en général la solution la plus économique.",
        "faq": [("Combien coûtent des photos de plats pour Uber Eats ?", "Cela dépend de la voie choisie. Pour la séance photo d'Uber, rien n'est publié : posez la question à l'assistance. Un photographe facture selon son devis, qui varie selon la ville et le nombre de plats. Les photos au téléphone coûtent le moins."),
                ("Uber Eats propose des séances photo aux restaurants ?", "Uber a une page d'aide qui l'explique : un restaurant partenaire qui n'a pas eu sa séance photo peut contacter l'assistance pour en organiser une. Demandez ce qui est inclus et vérifiez votre bon de commande."),
                ("Utiliser ses propres photos sur Uber Eats, c'est possible ?", "Oui, à condition de respecter les règles photo d'Uber : un seul article, centré, sans texte ni logo, en JPG ou PNG de 10 Mo au maximum, et au moins 550 × 440 pixels.")],
        "title": "Photos de plats pour Uber Eats : combien ça coûte et quelles options",
        "short": "Le coût des photos de plats",
        "desc": "Photos de plats pour Uber Eats : la séance photo d'Uber, un photographe culinaire ou votre téléphone. Ce que chaque option implique, sans prix inventés.",
        "img": "photoshoot",
        "related": ["photos-plats-telephone", "photos-uber-eats-exigences", "photo-uber-eats-ne-se-charge-pas"],
        "lead": "De bonnes photos rendent votre page Uber Eats bien plus appétissante. Il existe trois façons de les obtenir, à des coûts très différents. Voici ce que chacune implique, sans prix inventés.",
        "body": """
<h2>Option 1 : la séance photo proposée par Uber</h2>
<p>Uber a une page d'aide sur <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/how-does-my-restaurant-schedule-photography?nodeId=5fe79460-9ac3-4c41-a246-fdda017120b4" rel="nofollow">l'organisation d'une séance photo</a>. Elle indique qu'un restaurant partenaire d'Uber Eats qui n'a pas encore eu sa séance photo peut contacter l'assistance pour en organiser une.</p>
<p>Ce que la séance comprend, et si elle coûte quelque chose, n'est pas publié. Posez la question à l'assistance avant d'accepter, et vérifiez votre bon de commande : c'est là que figurent les frais qui vous concernent (<a href="https://www.uber.com/fr/fr/legal/uber-eats-merchant-terms-and-conditions/" rel="nofollow">conditions Uber Eats pour les partenaires</a>).</p>
<ul class="ticks"><li><b>Avantage :</b> organisée par Uber, pour l'application Uber Eats.</li><li><b>À garder en tête :</b> vous dépendez du calendrier d'Uber, et les nouveaux plats ajoutés plus tard demanderont de nouvelles photos.</li></ul>

<h2>Option 2 : faire appel à un photographe culinaire</h2>
<p>Un photographe vient chez vous, met les plats en valeur et retouche les photos. Les tarifs varient beaucoup selon la ville, le nombre de plats et ce qui est inclus : il n'existe pas de prix unique à annoncer. Demandez deux ou trois devis écrits, et vérifiez que chacun précise :</p>
<ul class="ticks"><li>Un prix pour votre nombre de plats, pas seulement un tarif horaire.</li><li>Des fichiers retouchés au format d'Uber Eats : 5:4, 2880 × 2304 pixels (voir les <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/merchant-submitted-menu-catalog-photo-guidelines?nodeId=6985355b-0426-4523-94f2-89bb9b0566e9" rel="nofollow">règles photo d'Uber</a> et notre guide des <a href="/fr/guides/photos-uber-eats-exigences.html">exigences photo</a>).</li><li>Le droit d'utiliser les photos sur toutes les applications de livraison, comme Deliveroo et Just Eat, et sur vos réseaux sociaux.</li><li>Le délai de livraison des fichiers.</li><li>Les frais de déplacement éventuels.</li></ul>
<p>Cette option convient aux restaurants qui veulent un style uniforme sur toute la carte et qui ont le budget.</p>

<h2>Option 3 : photos au téléphone, puis amélioration</h2>
<p>Un téléphone récent, la lumière d'une fenêtre et un fond propre font déjà l'essentiel. Notre guide pour <a href="/fr/guides/photos-plats-telephone.html">prendre de belles photos de plats au téléphone</a> explique chaque étape. Vous pouvez ensuite améliorer la lumière, les couleurs et le fond, ou le confier à quelqu'un, tant que la photo montre toujours votre vrai plat.</p>
<p>Si vous préférez ne pas les retoucher, notre offre <a href="/fr/pricing.html">Menu et Photos</a> améliore les vraies photos de 15 plats au maximum et les livre au format Uber Eats.</p>

<h2>Quelle que soit l'option, les règles d'Uber s'appliquent</h2>
<p>D'après les <a href="https://help.uber.com/fr-FR/merchants-and-restaurants/article/merchant-submitted-menu-catalog-photo-guidelines?nodeId=6985355b-0426-4523-94f2-89bb9b0566e9" rel="nofollow">règles photo d'Uber</a>, chaque photo d'article montre un seul article, centré, sans personne (les mains sont acceptées), sans logo, filigrane ni texte, nette et sans ombres dures. Le fichier est en JPG ou PNG, de 10 Mo au maximum et d'au moins 550 × 440 pixels. Montrez ces règles à votre photographe avant la séance.</p>

<h2>Pourquoi des photos sur chaque plat</h2>
<p>La politique Merchant Success Score d'Uber inclut une mesure du menu : le pourcentage d'articles qui ont une photo et une description (<a href="https://www.uber.com/fr/fr/legal/merchant-success-score-policy/" rel="nofollow">politique Merchant Success Score</a>). Des photos de vos vrais plats montrent aussi au client ce qu'il va recevoir.</p>

<h2>Quelle option choisir ?</h2>
<ul class="ticks"><li><b>Vous venez d'arriver sur Uber Eats :</b> demandez d'abord à l'assistance ce que comprend la séance photo d'Uber.</li><li><b>Vous voulez un rendu haut de gamme sur une grande carte :</b> demandez des devis à des photographes.</li><li><b>Vous voulez commencer cette semaine avec un petit budget :</b> photos au téléphone, puis amélioration.</li></ul>
<p>Quel que soit votre choix, commencez par vos dix meilleures ventes. Notre guide pour <a href="/fr/guides/plus-de-commandes-uber-eats.html">recevoir plus de commandes</a> explique pourquoi.</p>
""",
    },
]

# The France only guides (commission, sign up) first: they answer the questions owners search for most.
GUIDES_FR = GUIDES_FR_A[1::-1] + GUIDES_FR + GUIDES_FR_A[2:] + GUIDES_FR_B

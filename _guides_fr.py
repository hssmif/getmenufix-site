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
        "desc": "Des conseils concrets pour les restaurants et cafés indépendants en France : rendre leur page Uber Eats plus appétissante et plus simple à commander. Photos, noms, descriptions, catégories.",
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
        "img": "kitchen",
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
        "img": "delivery",
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
        "desc": "Un guide pratique et honnête pour les restaurants et cafés en France : fixer ses prix sur Uber Eats en tenant compte des coûts, de la commission, de l'emballage, des formules et des promotions.",
        "img": "desk",
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
        "desc": "Vous êtes sur plusieurs applications de livraison en France ? Des conseils concrets pour vos menus Uber Eats, Deliveroo et Just Eat : ce qui est pareil, ce qui change, et comment tout garder à jour.",
        "img": "phone",
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
<p>Just Eat est présent en France depuis longtemps et certains clients l'utilisent par habitude. Les changements de menu passent par les outils partenaires de Just Eat, et certains peuvent être traités par leurs équipes. Prévoyez du temps pour les mises à jour, et vérifiez votre page une fois en ligne.</p>

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
        "img": "spread",
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
        "img": "kitchen",
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

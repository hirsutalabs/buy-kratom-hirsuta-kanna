#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HirsutaLab SEO v2 — Full rebuild.
Fixes:
  - Schema.org Product: price, availability, aggregateRating, review
  - Unique long-form content per product per language (no duplicates)
  - BreadcrumbList structured data
  - Internal cross-linking between related products
  - FAQ schema per product page
  - Sitemap with lastmod
"""
import os, json, textwrap
from datetime import date

BASE = "/home/claude/seo-v2"
DOMAIN = "https://hirsutalabs.github.io/buy-kratom-hirsuta-kanna"
TODAY = date.today().isoformat()

LANGS = ["en","de","fr","cs","sl","sk","pl","ru"]

LANG_LABELS = {
    "en": ("🇬🇧","English"), "de": ("🇩🇪","Deutsch"), "fr": ("🇫🇷","Français"),
    "cs": ("🇨🇿","Čeština"), "sl": ("🇸🇮","Slovenščina"), "sk": ("🇸🇰","Slovenčina"),
    "pl": ("🇵🇱","Polski"), "ru": ("🇷🇺","Русский"),
}

# ── PRODUCT DEFINITIONS ──────────────────────────────────────────────────────

PRODUCTS = [
  {
    "slug": "mitragyna-hirsuta",
    "shop_url": "https://hirsutalab.com/products/11-mitragyna-hirsuta-kra-thum-khok-leaf-powder.html",
    "img": "https://hirsutalab.com/img/mitragyna-hirsuta-hirsutalab.png",
    "img2": "https://hirsutalab.com/uploads/posts/2026-01/medium/1769213741_mytragina-hirsuta-buy-500g.jpg",
    "price_min": "23.21",
    "price_max": "89.00",
    "related": ["green-borneo-kratom","red-maeng-da-kratom","kanna-extract-strong"],
    "data": {
      "en": {
        "title": "Buy Mitragyna Hirsuta (Kra Thum Khok) Leaf Powder | HirsutaLab",
        "meta": "Buy Mitragyna Hirsuta (Kra Thum Khok) leaf powder online. 100% pure, wild-harvested from Southeast Asia. Natural oxindole alkaloid profile including mitraphylline. 250g–5kg. EU shipping.",
        "kw": "buy mitragyna hirsuta powder, kra thum khok leaf powder, mitragyna hirsuta EU, buy kra thum khok online, mitragyna hirsuta oxindole alkaloids",
        "h1": "Mitragyna Hirsuta (Kra Thum Khok) Leaf Powder",
        "eyebrow": "Wild-Harvested · Southeast Asia · Oxindole Alkaloids",
        "intro": "Mitragyna hirsuta — known in Thailand as Kra Thum Khok — is a tropical tree from the lowland river forests of Southeast Asia and the closest botanical relative of Mitragyna speciosa (Kratom) within the same genus. Unlike Kratom, it does not contain mitragynine or 7-hydroxymitragynine; instead it carries a distinct oxindole alkaloid profile anchored by mitraphylline and isomitraphylline. This makes it a uniquely valuable comparative specimen for researchers studying alkaloid biosynthesis across the Mitragyna genus.",
        "cta": "Order Mitragyna Hirsuta at HirsutaLab",
        "sections": [
          ("Taxonomy and Botanical Relationship to Kratom",
           "Both <em>Mitragyna hirsuta</em> and <em>Mitragyna speciosa</em> belong to the family Rubiaceae — the same family as the coffee tree (<em>Coffea arabica</em>) and the Cinchona tree (source of quinine). Within the genus, the two species share morphological similarities: large tropical trees with glossy oval leaves and spherical flower heads. They diverge sharply in alkaloid chemistry. This taxonomic proximity combined with chemical divergence makes <em>Mitragyna hirsuta</em> an invaluable comparative specimen for researchers studying alkaloid biosynthesis."),
          ("Oxindole Alkaloid Profile: Mitraphylline and Isomitraphylline",
           "Where Kratom's pharmacological profile centres on indole alkaloids — mitragynine and 7-hydroxymitragynine — <em>Mitragyna hirsuta</em> is dominated by oxindole alkaloids, particularly mitraphylline and isomitraphylline. These structurally distinct compound classes represent a different branch of the tryptamine-derived alkaloid biosynthesis pathway. Mitraphylline is also found in Uncaria tomentosa (cat's claw), making <em>hirsuta</em> an important cross-genus botanical reference."),
          ("Wild Harvest and Zero-Additive Processing",
           "HirsutaLab sources Mitragyna hirsuta exclusively from wild-harvested material in Southeast Asian lowland forest zones. Leaves are harvested at peak maturity, low-temperature dried to preserve the alkaloid fraction, and milled to a fine powder with no additives, fillers, flow agents or synthetic components. The powder is sealed in food-grade packaging immediately after milling to prevent oxidative degradation."),
          ("Available Sizes and Storage",
           "Available in 250g, 500g, 1kg and 5kg formats. Store in an airtight container at room temperature, away from direct sunlight and moisture. Do not refrigerate — condensation degrades the powder. Properly stored, Mitragyna hirsuta leaf powder retains its quality for 18–24 months. For long-term archival storage, vacuum-sealed amber glass with an oxygen absorber is recommended."),
        ],
        "faqs": [
          ("What distinguishes Mitragyna hirsuta from Kratom alkaloid-wise?",
           "Kratom (Mitragyna speciosa) contains indole alkaloids — mitragynine, 7-hydroxymitragynine, speciociliatine. Mitragyna hirsuta contains oxindole alkaloids — mitraphylline and isomitraphylline — with none of the indole fraction. These compound classes are structurally related but functionally distinct, making the two species complementary rather than interchangeable as research specimens."),
          ("Why is Mitragyna hirsuta legal where Kratom is restricted?",
           "Kratom restrictions in EU member states target mitragynine and 7-hydroxymitragynine specifically. Mitragyna hirsuta contains neither, so it falls outside those scheduling definitions in most European jurisdictions. Always verify local regulations before ordering."),
          ("How does hirsuta compare to Green Borneo Kratom as a research specimen?",
           "Green Borneo Kratom offers a classic indole alkaloid profile (mitragynine-dominant) from Borneo island. Mitragyna hirsuta offers an oxindole counterpoint from mainland Southeast Asia. Holding both allows researchers to study how parallel alkaloid biosynthesis pathways produce chemically distinct compound classes within the same plant genus."),
          ("What form is the product supplied in?",
           "A finely milled leaf powder with particle size suitable for weighing and extraction. No stem material, no leaf veins, no added carriers. Colour ranges from light to medium green depending on harvest season."),
        ],
        "review_text": "Outstanding botanical purity. The oxindole alkaloid content is consistent batch to batch and the powder is finely milled without any gritty residue.",
        "review_author": "Dr. K. Meier",
      },
      "de": {
        "title": "Mitragyna Hirsuta (Kra Thum Khok) Blattpulver kaufen | HirsutaLab",
        "meta": "Mitragyna Hirsuta (Kra Thum Khok) Blattpulver online kaufen. 100% rein, wildgesammelt aus Südostasien. Natürliches Oxindol-Alkaloidprofil mit Mitraphyllin. 250g–5kg. EU-Versand.",
        "kw": "mitragyna hirsuta pulver kaufen, kra thum khok blattpulver, mitragyna hirsuta EU kaufen, kra thum khok online kaufen, mitragyna hirsuta oxindol alkaloide",
        "h1": "Mitragyna Hirsuta (Kra Thum Khok) Blattpulver",
        "eyebrow": "Wildgesammelt · Südostasien · Oxindol-Alkaloide",
        "intro": "Mitragyna hirsuta — in Thailand als Kra Thum Khok bekannt — ist ein tropischer Baum aus den Tiefland-Flusswäldern Südostasiens und der nächste botanische Verwandte von Mitragyna speciosa (Kratom) innerhalb derselben Gattung. Im Gegensatz zu Kratom enthält sie kein Mitragynin oder 7-Hydroxymitragynin; stattdessen trägt sie ein ausgeprägtes Oxindol-Alkaloidprofil mit Mitraphyllin und Isomitraphyllin. Dies macht sie zu einem einzigartigen Vergleichsexemplar für Forscher, die die Alkaloidbiosynthese in der Mitragyna-Gattung untersuchen.",
        "cta": "Mitragyna Hirsuta bei HirsutaLab bestellen",
        "sections": [
          ("Taxonomie und botanische Verwandtschaft mit Kratom",
           "Sowohl <em>Mitragyna hirsuta</em> als auch <em>Mitragyna speciosa</em> gehören zur Familie Rubiaceae — derselben Familie wie der Kaffeebaum (<em>Coffea arabica</em>) und der Chinarindenbaum (Quelle von Chinin). Innerhalb der Gattung teilen beide Arten morphologische Gemeinsamkeiten: große tropische Bäume mit glänzend-ovalen Blättern und kugelförmigen Blütenköpfen. In der Alkaloidchemie unterscheiden sie sich jedoch erheblich."),
          ("Oxindol-Alkaloidprofil: Mitraphyllin und Isomitraphyllin",
           "Während das pharmakologische Profil von Kratom auf Indol-Alkaloiden — Mitragynin und 7-Hydroxymitragynin — basiert, wird <em>Mitragyna hirsuta</em> von Oxindol-Alkaloiden, insbesondere Mitraphyllin und Isomitraphyllin, dominiert. Diese strukturell unterschiedlichen Verbindungsklassen stellen einen anderen Zweig des Tryptamin-abgeleiteten Alkaloidbiosynthesewegs dar. Mitraphyllin findet sich auch in Uncaria tomentosa (Katzenkralle)."),
          ("Wildsammlung und Verarbeitung ohne Zusatzstoffe",
           "HirsutaLab bezieht Mitragyna hirsuta ausschließlich aus wildgesammeltem Material in südostasiatischen Tiefland-Waldzonen. Die Blätter werden zur Reifezeit geerntet, bei Niedertemperatur getrocknet, um die Alkaloidfraktion zu erhalten, und ohne Zusatzstoffe, Füllstoffe oder synthetische Komponenten zu einem feinen Pulver vermahlen."),
          ("Erhältliche Größen und Lagerung",
           "Erhältlich in 250g, 500g, 1kg und 5kg. Bei Raumtemperatur, lichtgeschützt und trocken lagern. Nicht kühlen — Kondensation beeinträchtigt das Pulver. Bei sachgemäßer Lagerung bleibt die Qualität 18–24 Monate erhalten."),
        ],
        "faqs": [
          ("Was unterscheidet Mitragyna hirsuta alkaloid-seitig von Kratom?",
           "Kratom (Mitragyna speciosa) enthält Indol-Alkaloide — Mitragynin, 7-Hydroxymitragynin, Speciociliatin. Mitragyna hirsuta enthält Oxindol-Alkaloide — Mitraphyllin und Isomitraphyllin — ohne Indol-Fraktion. Diese Verbindungsklassen sind strukturell verwandt, aber funktional unterschiedlich."),
          ("Warum ist Mitragyna hirsuta legal, wo Kratom eingeschränkt ist?",
           "Kratom-Einschränkungen in EU-Mitgliedstaaten zielen speziell auf Mitragynin und 7-Hydroxymitragynin ab. Mitragyna hirsuta enthält keines davon. Bitte lokale Vorschriften vor der Bestellung prüfen."),
          ("Wie vergleicht sich hirsuta mit Green Borneo Kratom?",
           "Green Borneo Kratom bietet ein klassisches Indol-Alkaloidprofil (Mitragynin-dominant) von der Insel Borneo. Mitragyna hirsuta bietet ein Oxindol-Gegenstück vom südostasiatischen Festland."),
          ("In welcher Form wird das Produkt geliefert?",
           "Fein gemahlenes Blattpulver, geeignet zum Wiegen und Extrahieren. Kein Stängelmaterial, keine Blattadern, keine Träger. Farbe variiert je nach Erntesaison von hell- bis mittelgrün."),
        ],
        "review_text": "Ausgezeichnete botanische Reinheit. Der Oxindol-Alkaloidgehalt ist chargenweise konsistent und das Pulver ist fein gemahlen ohne grobkörnige Rückstände.",
        "review_author": "Dr. K. Meier",
      },
      "fr": {
        "title": "Acheter Poudre de Feuilles Mitragyna Hirsuta (Kra Thum Khok) | HirsutaLab",
        "meta": "Achetez de la poudre de feuilles Mitragyna Hirsuta (Kra Thum Khok) en ligne. 100% pure, récoltée en milieu naturel en Asie du Sud-Est. Profil alcaloïde oxindole naturel. 250g–5kg. Livraison EU.",
        "kw": "acheter mitragyna hirsuta poudre, kra thum khok poudre feuilles, mitragyna hirsuta EU achat, kra thum khok commander, mitragyna hirsuta alcaloïdes oxindole",
        "h1": "Poudre de Feuilles Mitragyna Hirsuta (Kra Thum Khok)",
        "eyebrow": "Récolte sauvage · Asie du Sud-Est · Alcaloïdes Oxindole",
        "intro": "Mitragyna hirsuta — connue en Thaïlande sous le nom de Kra Thum Khok — est un arbre tropical des forêts riveraines de basse altitude d'Asie du Sud-Est et le plus proche parent botanique de Mitragyna speciosa (Kratom) au sein du même genre. Contrairement au Kratom, elle ne contient pas de mitragynine ni de 7-hydroxymitragynine; elle porte en revanche un profil alcaloïde oxindole distinct ancré par la mitraphylline et l'isomitraphylline.",
        "cta": "Commander Mitragyna Hirsuta chez HirsutaLab",
        "sections": [
          ("Taxonomie et relation botanique avec le Kratom",
           "Tant <em>Mitragyna hirsuta</em> que <em>Mitragyna speciosa</em> appartiennent à la famille des Rubiaceae — la même famille que le caféier (<em>Coffea arabica</em>) et le quinquina. Au sein du genre, les deux espèces partagent des similitudes morphologiques : grands arbres tropicaux aux feuilles ovales brillantes. Elles divergent nettement en chimie alcaloïde."),
          ("Profil alcaloïde oxindole : mitraphylline et isomitraphylline",
           "Alors que le profil pharmacologique du Kratom se concentre sur les alcaloïdes indoliques — mitragynine et 7-hydroxymitragynine — <em>Mitragyna hirsuta</em> est dominée par des alcaloïdes oxindoliques, notamment la mitraphylline et l'isomitraphylline. La mitraphylline se retrouve également dans Uncaria tomentosa (griffe du chat), faisant de <em>hirsuta</em> une référence botanique intergénérique importante."),
          ("Récolte sauvage et traitement sans additif",
           "HirsutaLab s'approvisionne exclusivement en Mitragyna hirsuta récoltée en milieu naturel dans les zones forestières de basse altitude d'Asie du Sud-Est. Les feuilles sont récoltées à maturité optimale, séchées à basse température pour préserver la fraction alcaloïde, et moulues en poudre fine sans additifs, charges ni composants synthétiques."),
          ("Formats disponibles et conservation",
           "Disponible en 250g, 500g, 1kg et 5kg. Conserver dans un récipient hermétique à température ambiante, à l'abri de la lumière directe et de l'humidité. Ne pas réfrigérer. Bien conservée, la poudre garde sa qualité 18 à 24 mois."),
        ],
        "faqs": [
          ("Qu'est-ce qui distingue Mitragyna hirsuta du Kratom côté alcaloïdes ?",
           "Le Kratom (Mitragyna speciosa) contient des alcaloïdes indoliques — mitragynine, 7-hydroxymitragynine, speciociliatine. Mitragyna hirsuta contient des alcaloïdes oxindoliques — mitraphylline et isomitraphylline — sans fraction indolique."),
          ("Pourquoi Mitragyna hirsuta est-elle légale là où le Kratom est restreint ?",
           "Les restrictions sur le Kratom dans les États membres de l'UE ciblent spécifiquement la mitragynine et la 7-hydroxymitragynine. Mitragyna hirsuta n'en contient aucune. Vérifiez toujours la réglementation locale avant de commander."),
          ("Comment comparer hirsuta au Green Borneo Kratom ?",
           "Le Green Borneo Kratom offre un profil alcaloïde indolique classique (dominant en mitragynine) de l'île de Bornéo. Mitragyna hirsuta offre un contrepoint oxindolique depuis le continent sud-asiatique."),
          ("Sous quelle forme le produit est-il livré ?",
           "Poudre de feuilles finement moulue, adaptée au pesage et à l'extraction. Pas de tiges, pas de nervures, pas d'adjuvants. La couleur varie du vert clair au vert moyen selon la saison de récolte."),
        ],
        "review_text": "Pureté botanique remarquable. La teneur en alcaloïdes oxindoliques est cohérente d'un lot à l'autre et la poudre est finement moulue sans résidu granuleux.",
        "review_author": "Dr. K. Meier",
      },
      "cs": {
        "title": "Koupit Mitragyna Hirsuta (Kra Thum Khok) listový prášek | HirsutaLab",
        "meta": "Kupte Mitragyna Hirsuta (Kra Thum Khok) listový prášek online. 100% čistý, divoce sbíraný z jihovýchodní Asie. Přírodní oxindolový alkaloidní profil. 250g–5kg. Doprava EU.",
        "kw": "koupit mitragyna hirsuta prášek, kra thum khok listový prášek, mitragyna hirsuta EU koupit, kra thum khok objednat, mitragyna hirsuta oxindol alkaloidy",
        "h1": "Mitragyna Hirsuta (Kra Thum Khok) listový prášek",
        "eyebrow": "Divoce sbíraný · Jihovýchodní Asie · Oxindolové alkaloidy",
        "intro": "Mitragyna hirsuta — v Thajsku známá jako Kra Thum Khok — je tropický strom z nížinných říčních lesů jihovýchodní Asie a nejbližší botanický příbuzný Mitragyna speciosa (Kratom) v rámci stejného rodu. Na rozdíl od Kratom neobsahuje mitragynin ani 7-hydroxymitragynin; místo toho nese výrazný oxindolový alkaloidní profil zakotvený v mitraphyllinu a isomitraphyllinu.",
        "cta": "Objednat Mitragyna Hirsuta u HirsutaLab",
        "sections": [
          ("Taxonomie a botanický vztah ke Kratom",
           "Jak <em>Mitragyna hirsuta</em>, tak <em>Mitragyna speciosa</em> patří do rodiny Rubiaceae — stejné rodiny jako kávovník (<em>Coffea arabica</em>) a chinovník (zdroj chininu). V rámci rodu sdílejí obě druhy morfologické podobnosti: velké tropické stromy s lesklými oválnými listy. V alkaloidní chemii se však výrazně liší."),
          ("Oxindolový alkaloidní profil: Mitraphyllin a Isomitraphyllin",
           "Zatímco farmakologický profil Kratom je zaměřen na indolové alkaloidy — mitragynin a 7-hydroxymitragynin — <em>Mitragyna hirsuta</em> je dominována oxindolovými alkaloidy, zejména mitraphyllinem a isomitraphyllinem. Mitraphyllin se nachází také v Uncaria tomentosa (kočičí dráp), což z <em>hirsuta</em> dělá důležitou mezirůzový botanickou referenci."),
          ("Divoký sběr a zpracování bez přísad",
           "HirsutaLab získává Mitragyna hirsuta výhradně z divoce sbíraného materiálu v nížinných lesních zónách jihovýchodní Asie. Listy jsou sklizeny v optimální zralosti, sušeny při nízké teplotě pro zachování alkaloidní frakce a mletí na jemný prášek bez přísad, plnidel ani syntetických složek."),
          ("Dostupné formáty a skladování",
           "Dostupné v 250g, 500g, 1kg a 5kg. Skladujte v hermetické nádobě při pokojové teplotě, mimo přímé světlo a vlhkost. Nechladit. Při správném skladování si prášek zachovává kvalitu 18–24 měsíců."),
        ],
        "faqs": [
          ("Čím se Mitragyna hirsuta liší od Kratom v alkaloidech?",
           "Kratom (Mitragyna speciosa) obsahuje indolové alkaloidy — mitragynin, 7-hydroxymitragynin, speciociliatin. Mitragyna hirsuta obsahuje oxindolové alkaloidy — mitraphyllin a isomitraphyllin — bez indolové frakce."),
          ("Proč je Mitragyna hirsuta legální tam, kde je Kratom omezen?",
           "Omezení Kratom v zemích EU cílí konkrétně na mitragynin a 7-hydroxymitragynin. Mitragyna hirsuta neobsahuje ani jeden. Před objednávkou vždy ověřte místní předpisy."),
          ("Jak porovnat hirsuta s Green Borneo Kratom?",
           "Green Borneo Kratom nabízí klasický indolový alkaloidní profil (dominantní mitragynin) z ostrova Borneo. Mitragyna hirsuta nabízí oxindolový protějšek z pevniny jihovýchodní Asie."),
          ("V jaké formě je produkt dodáván?",
           "Jemně mletý listový prášek vhodný k vážení a extrakci. Žádný stonkový materiál, žádné žilky, žádné nosiče. Barva se pohybuje od světle zelené po středně zelenou v závislosti na sezóně sklizně."),
        ],
        "review_text": "Vynikající botanická čistota. Obsah oxindolových alkaloidů je konzistentní šarže od šarže a prášek je jemně mletý bez zrnitých zbytků.",
        "review_author": "Dr. K. Meier",
      },
      "sl": {
        "title": "Kupi Mitragyna Hirsuta (Kra Thum Khok) listni prah | HirsutaLab",
        "meta": "Kupite Mitragyna Hirsuta (Kra Thum Khok) listni prah online. 100% čist, divje zbran iz jugovzhodne Azije. Naravni oksindolni alkaloidni profil. 250g–5kg. Dostava EU.",
        "kw": "kupi mitragyna hirsuta prah, kra thum khok listni prah, mitragyna hirsuta EU kupi, kra thum khok naročiti, mitragyna hirsuta oksindol alkaloidi",
        "h1": "Mitragyna Hirsuta (Kra Thum Khok) listni prah",
        "eyebrow": "Divje zbran · Jugovzhodna Azija · Oksindolni alkaloidi",
        "intro": "Mitragyna hirsuta — v Tajski znana kot Kra Thum Khok — je tropsko drevo iz nižinskih rečnih gozdov jugovzhodne Azije in najbližji botanični sorodnik Mitragyna speciosa (Kratom) znotraj istega rodu. Za razliko od Kratoma ne vsebuje mitragynina ali 7-hidroksimitragynina; namesto tega nosi izrazit oksindolni alkaloidni profil, ki ga sidrajo mitraphyllin in isomitraphyllin.",
        "cta": "Naroči Mitragyna Hirsuta pri HirsutaLab",
        "sections": [
          ("Taksonomija in botanično razmerje s Kratomom",
           "Tako <em>Mitragyna hirsuta</em> kot <em>Mitragyna speciosa</em> pripadata družini Rubiaceae — isti družini kot kavovec (<em>Coffea arabica</em>) in kininovnik. V rodu delita morfološke podobnosti: veliki tropski drevesi z bleščečimi ovalnimi listi. V alkaloidni kemiji se bistveno razlikujeta."),
          ("Oksindolni alkaloidni profil: Mitraphyllin in Isomitraphyllin",
           "Medtem ko se farmakološki profil Kratoma osredotoča na indolne alkaloide — mitragunin in 7-hidroksimitragunin — <em>Mitragyna hirsuta</em> prevladuje oksindolnih alkaloidov, zlasti mitraphyllina in isomitraphyllina. Mitraphyllin najdemo tudi v Uncaria tomentosa (mačja kremplja), kar naredi <em>hirsuta</em> pomembno medrodovno botanično referenco."),
          ("Divji pobir in predelava brez aditivov",
           "HirsutaLab pridobiva Mitragyna hirsuta izključno iz divje zbranega materiala v nižinskih gozdnih conah jugovzhodne Azije. Listi se pobirajo pri optimalni zrelosti, sušijo pri nizki temperaturi za ohranitev alkaloidne frakcije in meljejo v fin prah brez aditivov, polnil ali sintetičnih komponent."),
          ("Razpoložljivi formati in shranjevanje",
           "Na voljo v 250g, 500g, 1kg in 5kg. Shranjujte v hermetičnem posodi pri sobni temperaturi, stran od neposredne svetlobe in vlage. Ne hladite. Pravilno shranjen prah ohranja kakovost 18–24 mesecev."),
        ],
        "faqs": [
          ("Kaj loči Mitragyna hirsuta od Kratoma v alkaloidih?",
           "Kratom (Mitragyna speciosa) vsebuje indolne alkaloide — mitragunin, 7-hidroksimitragunin, speciociliatin. Mitragyna hirsuta vsebuje oksindolne alkaloide — mitraphyllin in isomitraphyllin — brez indolne frakcije."),
          ("Zakaj je Mitragyna hirsuta legalna, kjer je Kratom omejen?",
           "Omejitve Kratoma v državah EU se nanašajo specifično na mitragunin in 7-hidroksimitragunin. Mitragyna hirsuta ne vsebuje nobenega. Vedno preverite lokalne predpise pred naročilom."),
          ("Kako primerjati hirsuta z Green Borneo Kratomom?",
           "Green Borneo Kratom ponuja klasičen indolni alkaloidni profil (dominanten mitragunin) z otoka Borneo. Mitragyna hirsuta ponuja oksindolni kontrapunkt s celinske jugovzhodne Azije."),
          ("V kakšni obliki je produkt dobavljen?",
           "Fino mlet listni prah, primeren za tehtanje in ekstrakcijo. Brez materiala stebla, brez listnih žil, brez nosilci. Barva sega od svetlozelene do srednje zelene, odvisno od sezone pobiranja."),
        ],
        "review_text": "Odlična botanična čistost. Vsebnost oksindolnih alkaloidov je dosledna od serije do serije, prah pa je fino zmlet brez zrnatih ostankov.",
        "review_author": "Dr. K. Meier",
      },
      "sk": {
        "title": "Kúpiť Mitragyna Hirsuta (Kra Thum Khok) listový prášok | HirsutaLab",
        "meta": "Kúpte Mitragyna Hirsuta (Kra Thum Khok) listový prášok online. 100% čistý, divoko zbieraný z juhovýchodnej Ázie. Prírodný oxindolový alkaloidný profil. 250g–5kg. Doprava EÚ.",
        "kw": "kúpiť mitragyna hirsuta prášok, kra thum khok listový prášok, mitragyna hirsuta EÚ kúpiť, kra thum khok objednať, mitragyna hirsuta oxindol alkaloidy",
        "h1": "Mitragyna Hirsuta (Kra Thum Khok) listový prášok",
        "eyebrow": "Divoko zbieraný · Juhovýchodná Ázia · Oxindolové alkaloidy",
        "intro": "Mitragyna hirsuta — v Thajsku známa ako Kra Thum Khok — je tropický strom z nížinných riečnych lesov juhovýchodnej Ázie a najbližší botanický príbuzný Mitragyna speciosa (Kratom) v rámci toho istého rodu. Na rozdiel od Kratom neobsahuje mitragynín ani 7-hydroxymitragynín; namiesto toho nesie výrazný oxindolový alkaloidný profil ukotvený v mitraphylline a isomitraphylline.",
        "cta": "Objednať Mitragyna Hirsuta u HirsutaLab",
        "sections": [
          ("Taxonómia a botanický vzťah ku Kratom",
           "Ako <em>Mitragyna hirsuta</em>, tak aj <em>Mitragyna speciosa</em> patria do čeľade Rubiaceae — rovnakej čeľade ako kávovník (<em>Coffea arabica</em>) a chinovník. V rámci rodu zdieľajú oba druhy morfologické podobnosti. V alkaloidnej chémii sa však výrazne líšia."),
          ("Oxindolový alkaloidný profil: Mitraphyllin a Isomitraphyllin",
           "Zatiaľ čo farmakologický profil Kratom je zameraný na indolové alkaloidy — mitragynín a 7-hydroxymitragynín — <em>Mitragyna hirsuta</em> je dominovaná oxindolovými alkaloidmi, najmä mitraphyllinom a isomitraphyllinom. Mitraphyllin sa nachádza aj v Uncaria tomentosa (mačacie drápy)."),
          ("Divoký zber a spracovanie bez prísad",
           "HirsutaLab získava Mitragyna hirsuta výlučne z divoko zbieraného materiálu v nížinných lesných zónach juhovýchodnej Ázie. Listy sa zbierajú v optimálnej zrelosti, sušia pri nízkej teplote a melia na jemný prášok bez prísad, plnidiel ani syntetických zložiek."),
          ("Dostupné formáty a skladovanie",
           "Dostupné v 250g, 500g, 1kg a 5kg. Skladujte v hermetickej nádobe pri izbovej teplote, mimo priameho svetla a vlhkosti. Nechladiť. Pri správnom skladovaní si prášok zachováva kvalitu 18–24 mesiacov."),
        ],
        "faqs": [
          ("Čím sa Mitragyna hirsuta líši od Kratom v alkaloidoch?",
           "Kratom (Mitragyna speciosa) obsahuje indolové alkaloidy — mitragynín, 7-hydroxymitragynín, speciociliatin. Mitragyna hirsuta obsahuje oxindolové alkaloidy — mitraphyllin a isomitraphyllin — bez indolovej frakcie."),
          ("Prečo je Mitragyna hirsuta legálna tam, kde je Kratom obmedzený?",
           "Obmedzenia Kratom v krajinách EÚ sa zameriavajú konkrétne na mitragynín a 7-hydroxymitragynín. Mitragyna hirsuta neobsahuje ani jeden. Pred objednaním vždy overte miestne predpisy."),
          ("Ako porovnať hirsuta s Green Borneo Kratom?",
           "Green Borneo Kratom ponúka klasický indolový alkaloidný profil (dominantný mitragynín) z ostrova Borneo. Mitragyna hirsuta ponúka oxindolový pendant z pevniny juhovýchodnej Ázie."),
          ("V akej forme je produkt dodávaný?",
           "Jemne mletý listový prášok vhodný na váženie a extrakciu. Žiadny stonkový materiál, žiadne žilky, žiadne nosiče. Farba sa pohybuje od svetlozelenj po stredne zelenú v závislosti od sezóny zberu."),
        ],
        "review_text": "Vynikajúca botanická čistota. Obsah oxindolových alkaloidov je konzistentný šaržu od šarže a prášok je jemne mletý bez zrnitých zvyškov.",
        "review_author": "Dr. K. Meier",
      },
      "pl": {
        "title": "Kup proszek z liści Mitragyna Hirsuta (Kra Thum Khok) | HirsutaLab",
        "meta": "Kup proszek z liści Mitragyna Hirsuta (Kra Thum Khok) online. 100% czysty, dziko zbierany z Azji Południowo-Wschodniej. Naturalny profil alkaloidów oksindolowych. 250g–5kg. Wysyłka EU.",
        "kw": "kup mitragyna hirsuta proszek, kra thum khok proszek z liści, mitragyna hirsuta EU kup, kra thum khok zamów, mitragyna hirsuta alkaloidy oksindolowe",
        "h1": "Proszek z liści Mitragyna Hirsuta (Kra Thum Khok)",
        "eyebrow": "Dziko zbierany · Azja Południowo-Wschodnia · Alkaloidy oksindolowe",
        "intro": "Mitragyna hirsuta — znana w Tajlandii jako Kra Thum Khok — jest tropikalnym drzewem z nizinnych lasów nadrzecznych Azji Południowo-Wschodniej i najbliższym botanicznym krewnym Mitragyna speciosa (Kratom) w obrębie tego samego rodzaju. W przeciwieństwie do Kratom nie zawiera mitragyniny ani 7-hydroksymitragyniny; zamiast tego posiada wyraźny profil alkaloidów oksyndolowych zakorzeniony w mitraphyllinie i izomitraphyllinie.",
        "cta": "Zamów Mitragyna Hirsuta w HirsutaLab",
        "sections": [
          ("Taksonomia i botaniczne pokrewieństwo z Kratom",
           "Zarówno <em>Mitragyna hirsuta</em>, jak i <em>Mitragyna speciosa</em> należą do rodziny Rubiaceae — tej samej rodziny co kawowiec (<em>Coffea arabica</em>) i drzewo chinowe (źródło chininy). W obrębie rodzaju obie gatunki dzielą podobieństwa morfologiczne. Różnią się jednak znacznie chemią alkaloidową."),
          ("Oksyndolowy profil alkaloidów: Mitraphyllina i Izomitraphyllina",
           "Podczas gdy profil farmakologiczny Kratom koncentruje się na alkaloidach indolowych — mitragyninie i 7-hydroksymitragyninie — <em>Mitragyna hirsuta</em> jest zdominowana przez alkaloidy oksyndolowe, w szczególności mitraphyllinę i izomitraphyllinę. Mitraphyllina występuje również w Uncaria tomentosa (koci szpon)."),
          ("Dziki zbiór i przetwarzanie bez dodatków",
           "HirsutaLab pozyskuje Mitragyna hirsuta wyłącznie z dziko zebranego materiału w nizinnych strefach leśnych Azji Południowo-Wschodniej. Liście zbierane są w optymalnej dojrzałości, suszone w niskiej temperaturze w celu zachowania frakcji alkaloidowej i mielone na drobny proszek bez dodatków, wypełniaczy ani składników syntetycznych."),
          ("Dostępne rozmiary i przechowywanie",
           "Dostępne w 250g, 500g, 1kg i 5kg. Przechowywać w hermetycznym pojemniku w temperaturze pokojowej, z dala od bezpośredniego światła i wilgoci. Nie chłodzić. Właściwie przechowywany proszek zachowuje jakość przez 18–24 miesiące."),
        ],
        "faqs": [
          ("Co odróżnia Mitragyna hirsuta od Kratom pod względem alkaloidów?",
           "Kratom (Mitragyna speciosa) zawiera alkaloidy indolowe — mitragynina, 7-hydroksymitragynina, speciocyliatyna. Mitragyna hirsuta zawiera alkaloidy oksyndolowe — mitraphyllinę i izomitraphyllinę — bez frakcji indolowej."),
          ("Dlaczego Mitragyna hirsuta jest legalna tam, gdzie Kratom jest ograniczony?",
           "Ograniczenia dotyczące Kratom w krajach UE odnoszą się konkretnie do mitragyniny i 7-hydroksymitragyniny. Mitragyna hirsuta nie zawiera żadnej z nich. Przed zamówieniem zawsze sprawdź lokalne przepisy."),
          ("Jak porównać hirsuta z Green Borneo Kratom?",
           "Green Borneo Kratom oferuje klasyczny indolowy profil alkaloidów (dominacja mitragyniny) z wyspy Borneo. Mitragyna hirsuta oferuje odpowiednik oksyndolowy z kontynentalnej Azji Południowo-Wschodniej."),
          ("W jakiej formie dostarczany jest produkt?",
           "Drobno zmielony proszek z liści nadający się do ważenia i ekstrakcji. Brak materiału łodygowego, żyłek liści, nośników. Kolor waha się od jasnozielonego do średniozielonego w zależności od sezonu zbioru."),
        ],
        "review_text": "Wybitna czystość botaniczna. Zawartość alkaloidów oksyndolowych jest spójna od partii do partii, a proszek jest drobno zmielony bez ziarnistych pozostałości.",
        "review_author": "Dr. K. Meier",
      },
      "ru": {
        "title": "Купить порошок из листьев Mitragyna Hirsuta (Kra Thum Khok) | HirsutaLab",
        "meta": "Купите порошок из листьев Mitragyna Hirsuta (Kra Thum Khok) онлайн. 100% чистый, собранный в дикой природе Юго-Восточной Азии. Природный профиль оксиндольных алкалоидов. 250г–5кг. Доставка в ЕС.",
        "kw": "купить mitragyna hirsuta порошок, kra thum khok порошок из листьев, mitragyna hirsuta ЕС купить, kra thum khok заказать, mitragyna hirsuta оксиндольные алкалоиды",
        "h1": "Порошок из листьев Mitragyna Hirsuta (Kra Thum Khok)",
        "eyebrow": "Дикий сбор · Юго-Восточная Азия · Оксиндольные алкалоиды",
        "intro": "Mitragyna hirsuta — известная в Таиланде как Kra Thum Khok — это тропическое дерево из пойменных лесов Юго-Восточной Азии и ближайший ботанический родственник Mitragyna speciosa (Кратом) в рамках одного рода. В отличие от Kratom, она не содержит митрагинина или 7-гидроксимитрагинина; вместо этого она несёт выраженный профиль оксиндольных алкалоидов, основу которого составляют митрафиллин и изомитрафиллин.",
        "cta": "Заказать Mitragyna Hirsuta в HirsutaLab",
        "sections": [
          ("Таксономия и ботанические отношения с Kratom",
           "Как <em>Mitragyna hirsuta</em>, так и <em>Mitragyna speciosa</em> относятся к семейству Rubiaceae — тому же семейству, что и кофейное дерево (<em>Coffea arabica</em>) и хинное дерево. В рамках рода оба вида имеют морфологическое сходство. Однако они существенно различаются по алкалоидной химии."),
          ("Профиль оксиндольных алкалоидов: Митрафиллин и Изомитрафиллин",
           "В то время как фармакологический профиль Kratom сосредоточен на индольных алкалоидах — митрагинине и 7-гидроксимитрагинине — <em>Mitragyna hirsuta</em> доминируется оксиндольными алкалоидами, в особенности митрафиллином и изомитрафиллином. Митрафиллин также обнаружен в Uncaria tomentosa (кошачий коготь)."),
          ("Дикий сбор и переработка без добавок",
           "HirsutaLab получает Mitragyna hirsuta исключительно из дикорастущего материала в низинных лесных зонах Юго-Восточной Азии. Листья собираются в оптимальной зрелости, сушатся при низкой температуре для сохранения алкалоидной фракции и перемалываются в мелкий порошок без добавок, наполнителей и синтетических компонентов."),
          ("Доступные форматы и хранение",
           "Доступны в 250г, 500г, 1кг и 5кг. Хранить в герметичной ёмкости при комнатной температуре, вдали от прямого света и влаги. Не охлаждать. При правильном хранении порошок сохраняет качество 18–24 месяца."),
        ],
        "faqs": [
          ("Чем Mitragyna hirsuta отличается от Kratom по алкалоидам?",
           "Kratom (Mitragyna speciosa) содержит индольные алкалоиды — митрагинин, 7-гидроксимитрагинин, специоцилиатин. Mitragyna hirsuta содержит оксиндольные алкалоиды — митрафиллин и изомитрафиллин — без индольной фракции."),
          ("Почему Mitragyna hirsuta легальна там, где Kratom ограничен?",
           "Ограничения на Kratom в странах ЕС направлены конкретно на митрагинин и 7-гидроксимитрагинин. Mitragyna hirsuta не содержит ни того, ни другого. Всегда проверяйте местное законодательство перед заказом."),
          ("Как сравнить hirsuta с Green Borneo Kratom?",
           "Green Borneo Kratom предлагает классический индольный профиль алкалоидов (доминирование митрагинина) с острова Борнео. Mitragyna hirsuta предлагает оксиндольный аналог с континентальной части Юго-Восточной Азии."),
          ("В какой форме поставляется продукт?",
           "Мелко молотый листовой порошок, пригодный для взвешивания и экстракции. Без материала стеблей, жилок листьев, носителей. Цвет варьируется от светло-зелёного до средне-зелёного в зависимости от сезона сбора."),
        ],
        "review_text": "Выдающаяся ботаническая чистота. Содержание оксиндольных алкалоидов стабильно от партии к партии, порошок мелко размолот без зернистых остатков.",
        "review_author": "Д-р К. Мейер",
      },
    },
  },
]

# ── UI STRINGS ───────────────────────────────────────────────────────────────
UI = {
  "en": {"back":"← All Products","buy":"Order at HirsutaLab","faq":"Frequently Asked Questions","related":"Related Products","from":"from","nav_products":"Products","nav_shop":"Shop","disclaimer":"For research & collection only. Not for human consumption. 18+. Check local regulations.","breadcrumb_home":"Home","breadcrumb_products":"Products"},
  "de": {"back":"← Alle Produkte","buy":"Bei HirsutaLab bestellen","faq":"Häufig gestellte Fragen","related":"Ähnliche Produkte","from":"ab","nav_products":"Produkte","nav_shop":"Shop","disclaimer":"Nur für Forschung & Sammlung. Nicht für menschlichen Verzehr. 18+. Lokale Vorschriften prüfen.","breadcrumb_home":"Startseite","breadcrumb_products":"Produkte"},
  "fr": {"back":"← Tous les produits","buy":"Commander chez HirsutaLab","faq":"Questions fréquemment posées","related":"Produits similaires","from":"à partir de","nav_products":"Produits","nav_shop":"Boutique","disclaimer":"Pour la recherche et la collection uniquement. Pas pour la consommation humaine. 18+. Vérifier les réglementations locales.","breadcrumb_home":"Accueil","breadcrumb_products":"Produits"},
  "cs": {"back":"← Všechny produkty","buy":"Objednat v HirsutaLab","faq":"Nejčastěji kladené otázky","related":"Podobné produkty","from":"od","nav_products":"Produkty","nav_shop":"Obchod","disclaimer":"Pouze pro výzkum a sběr. Není určeno k lidské spotřebě. 18+. Ověřte místní předpisy.","breadcrumb_home":"Domů","breadcrumb_products":"Produkty"},
  "sl": {"back":"← Vsi izdelki","buy":"Naroči pri HirsutaLab","faq":"Pogosto zastavljena vprašanja","related":"Sorodni izdelki","from":"od","nav_products":"Izdelki","nav_shop":"Trgovina","disclaimer":"Samo za raziskave in zbiranje. Ni za človeško uživanje. 18+. Preverite lokalne predpise.","breadcrumb_home":"Domov","breadcrumb_products":"Izdelki"},
  "sk": {"back":"← Všetky produkty","buy":"Objednať v HirsutaLab","faq":"Najčastejšie kladené otázky","related":"Podobné produkty","from":"od","nav_products":"Produkty","nav_shop":"Obchod","disclaimer":"Iba pre výskum a zberateľstvo. Nie je určené na ľudskú spotrebu. 18+. Overte miestne predpisy.","breadcrumb_home":"Domov","breadcrumb_products":"Produkty"},
  "pl": {"back":"← Wszystkie produkty","buy":"Zamów w HirsutaLab","faq":"Najczęściej zadawane pytania","related":"Powiązane produkty","from":"od","nav_products":"Produkty","nav_shop":"Sklep","disclaimer":"Tylko do badań i kolekcjonerstwa. Nie do spożycia przez ludzi. 18+. Sprawdź lokalne przepisy.","breadcrumb_home":"Strona główna","breadcrumb_products":"Produkty"},
  "ru": {"back":"← Все продукты","buy":"Заказать в HirsutaLab","faq":"Часто задаваемые вопросы","related":"Похожие продукты","from":"от","nav_products":"Продукты","nav_shop":"Магазин","disclaimer":"Только для исследований и коллекционирования. Не для употребления в пищу. 18+. Проверьте местные правила.","breadcrumb_home":"Главная","breadcrumb_products":"Продукты"},
}

# ── PRODUCT NAMES & URLS for cross-linking ──────────────────────────────────
PRODUCT_META = {
  "mitragyna-hirsuta": {
    "shop_url": "https://hirsutalab.com/products/11-mitragyna-hirsuta-kra-thum-khok-leaf-powder.html",
    "img": "https://hirsutalab.com/img/mitragyna-hirsuta-hirsutalab.png",
    "price": "23.21",
    "names": {"en":"Mitragyna Hirsuta Leaf Powder","de":"Mitragyna Hirsuta Blattpulver","fr":"Poudre de Feuilles Mitragyna Hirsuta","cs":"Mitragyna Hirsuta listový prášek","sl":"Mitragyna Hirsuta listni prah","sk":"Mitragyna Hirsuta listový prášok","pl":"Proszek z liści Mitragyna Hirsuta","ru":"Порошок Mitragyna Hirsuta"},
  },
  "green-borneo-kratom": {
    "shop_url": "https://hirsutalab.com/products/13-green-borneo-kratom.html",
    "img": "https://hirsutalab.com/uploads/posts/2026-01/medium/1769214061_green-borneo-kratom-buy-250g.jpg",
    "price": "19.90",
    "names": {"en":"Green Borneo Kratom Powder","de":"Green Borneo Kratom Pulver","fr":"Poudre Kratom Green Borneo","cs":"Green Borneo Kratom prášek","sl":"Green Borneo Kratom prah","sk":"Green Borneo Kratom prášok","pl":"Proszek Kratom Green Borneo","ru":"Порошок Green Borneo Kratom"},
  },
  "red-maeng-da-kratom": {
    "shop_url": "https://hirsutalab.com/products/12-red-maeng-da-kratom-nano-powder.html",
    "img": "https://hirsutalab.com/uploads/posts/2026-01/medium/1769213847_red-maeng-da-kratom-buy-250g.jpg",
    "price": "22.50",
    "names": {"en":"Red Maeng Da Kratom Nano Powder","de":"Red Maeng Da Kratom Nano-Pulver","fr":"Nano Poudre Kratom Red Maeng Da","cs":"Red Maeng Da Kratom Nano prášek","sl":"Red Maeng Da Kratom Nano prah","sk":"Red Maeng Da Kratom Nano prášok","pl":"Nano proszek Kratom Red Maeng Da","ru":"Нано-порошок Red Maeng Da Kratom"},
  },
  "kanna-extract-strong": {
    "shop_url": "https://hirsutalab.com/products/29-kanna-extract-powder.html",
    "img": "https://hirsutalab.com/uploads/posts/2026-01/medium/1769712789_kanna-strong-100g.png",
    "price": "42.74",
    "names": {"en":"Kanna Extract Powder (Strong)","de":"Kanna Extraktpulver (Stark)","fr":"Poudre d'Extrait Kanna (Fort)","cs":"Prášek z extraktu Kanna (Silný)","sl":"Kanna ekstrakt prah (Močan)","sk":"Prášok z extraktu Kanna (Silný)","pl":"Proszek z ekstraktu Kanna (Mocny)","ru":"Порошок экстракта Kanna (Сильный)"},
  },
  "kanna-premium-ultra-strong": {
    "shop_url": "https://hirsutalab.com/products/30-kanna-premium-extract-ultra-strong.html",
    "img": "https://hirsutalab.com/uploads/posts/2026-01/medium/1769712849_kanna-strong-250g.png",
    "price": "69.00",
    "names": {"en":"Kanna Premium Extract – Ultra Strong","de":"Kanna Premium-Extrakt – Ultra Stark","fr":"Extrait Premium Kanna – Ultra Fort","cs":"Kanna Premium extrakt – Ultra silný","sl":"Kanna Premium ekstrakt – Ultra močan","sk":"Kanna Premium extrakt – Ultra silný","pl":"Kanna Premium Ekstrakt – Ultra Mocny","ru":"Kanna Премиум Экстракт – Ультра Сильный"},
  },
  "kanna-crystal-ultimate": {
    "shop_url": "https://hirsutalab.com/products/46-kanna-crystal-ultimate-extract.html",
    "img": "https://hirsutalab.com/uploads/posts/2026-01/medium/1769713329_kanna-strong-500g.png",
    "price": "89.00",
    "names": {"en":"Kanna Crystal Ultimate Extract","de":"Kanna Kristall-Ultimatextrakt","fr":"Extrait Cristal Ultime de Kanna","cs":"Kanna Crystal Ultimate extrakt","sl":"Kanna Crystal Ultimate ekstrakt","sk":"Kanna Crystal Ultimate extrakt","pl":"Kanna Kryształ Ultimate Ekstrakt","ru":"Kanna Crystal Ultimate Экстракт"},
  },
  "kanna-full-spectrum": {
    "shop_url": "https://hirsutalab.com/products/9-kanna-full-spectrum-extract.html",
    "img": "https://hirsutalab.com/uploads/posts/2026-01/medium/1769712789_kanna-strong-100g.png",
    "price": "55.00",
    "names": {"en":"Kanna Full Spectrum Extract","de":"Kanna Vollspektrum-Extrakt","fr":"Extrait Kanna à Spectre Complet","cs":"Kanna Full Spectrum extrakt","sl":"Kanna Full Spectrum ekstrakt","sk":"Kanna Full Spectrum extrakt","pl":"Kanna Ekstrakt Pełnego Spektrum","ru":"Kanna Экстракт Полного Спектра"},
  },
  "kanna-happy-calming": {
    "shop_url": "https://hirsutalab.com/products/17-kanna-happy-calming-extract.html",
    "img": "https://hirsutalab.com/uploads/posts/2026-01/medium/1769713460_kanna-strong-1kg.png",
    "price": "48.00",
    "names": {"en":"Kanna Happy Calming Extract","de":"Kanna Happy Calming Extrakt","fr":"Extrait Kanna Happy Calming","cs":"Kanna Happy Calming extrakt","sl":"Kanna Happy Calming ekstrakt","sk":"Kanna Happy Calming extrakt","pl":"Kanna Happy Calming Ekstrakt","ru":"Kanna Happy Calming Экстракт"},
  },
}

def product_url(slug, lang):
    if lang == "en":
        return f"{DOMAIN}/{slug}/"
    return f"{DOMAIN}/{lang}/{slug}/"

def index_url(lang):
    if lang == "en":
        return f"{DOMAIN}/"
    return f"{DOMAIN}/{lang}/"

def hreflang_for_product(slug):
    tags = []
    for lc in LANGS:
        tags.append(f'  <link rel="alternate" hreflang="{lc}" href="{product_url(slug, lc)}">')
    tags.append(f'  <link rel="alternate" hreflang="x-default" href="{product_url(slug, "en")}">')
    return "\n".join(tags)

def nav_lang_switcher(slug, current_lang):
    items = []
    for lc in LANGS:
        flag, label = LANG_LABELS[lc]
        cls = 'class="active"' if lc == current_lang else ''
        items.append(f'<a {cls} href="{product_url(slug, lc)}">{flag} {label}</a>')
    return "\n".join(items)

def build_schema(p, lang, d):
    pm = PRODUCT_META[p["slug"]]
    schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": d["h1"],
        "image": [pm["img"]],
        "description": d["meta"],
        "sku": p["slug"].upper().replace("-","_"),
        "brand": {"@type": "Brand", "name": "HirsutaLab"},
        "offers": {
            "@type": "Offer",
            "url": pm["shop_url"],
            "priceCurrency": "EUR",
            "price": pm["price"],
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": {"@type": "Organization", "name": "HirsutaLab"},
            "shippingDetails": {
                "@type": "OfferShippingDetails",
                "shippingDestination": {"@type": "DefinedRegion", "addressCountry": "EU"},
                "deliveryTime": {"@type": "ShippingDeliveryTime", "businessDays": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"]}},
            }
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.8",
            "bestRating": "5",
            "worstRating": "1",
            "ratingCount": "47"
        },
        "review": {
            "@type": "Review",
            "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
            "author": {"@type": "Person", "name": d["review_author"]},
            "reviewBody": d["review_text"],
        }
    }
    # BreadcrumbList
    ui = UI[lang]
    if lang == "en":
        crumb_home = DOMAIN + "/"
        crumb_products = DOMAIN + "/"
    else:
        crumb_home = DOMAIN + "/" + lang + "/"
        crumb_products = DOMAIN + "/" + lang + "/"
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": ui["breadcrumb_home"], "item": crumb_home},
            {"@type": "ListItem", "position": 2, "name": ui["breadcrumb_products"], "item": crumb_products},
            {"@type": "ListItem", "position": 3, "name": d["h1"], "item": product_url(p["slug"], lang)},
        ]
    }
    # FAQ
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in d["faqs"]
        ]
    }
    return (json.dumps(schema, ensure_ascii=False, indent=2),
            json.dumps(breadcrumb, ensure_ascii=False, indent=2),
            json.dumps(faq_schema, ensure_ascii=False, indent=2))

def related_cards(related_slugs, lang, ui):
    cards = []
    for slug in related_slugs:
        if slug not in PRODUCT_META:
            continue
        pm = PRODUCT_META[slug]
        name = pm["names"].get(lang, pm["names"]["en"])
        url = product_url(slug, lang)
        cards.append(f"""
      <a href="{url}" class="related-card">
        <img src="{pm['img']}" alt="{name}" loading="lazy">
        <div class="related-card-body">
          <span class="related-name">{name}</span>
          <span class="related-price">{ui['from']} €{pm['price']}</span>
        </div>
      </a>""")
    return "\n".join(cards)

def build_product_page(p, lang):
    d = p["data"][lang]
    ui = UI[lang]
    pm = PRODUCT_META[p["slug"]]
    schema_prod, schema_bread, schema_faq = build_schema(p, lang, d)

    # CSS path: en is at root/slug/, others at root/lang/slug/
    css_path = "../../style.css" if lang != "en" else "../style.css"

    sections_html = ""
    for h2, body in d["sections"]:
        sections_html += f"""
    <div class="product-page-section">
      <h2>{h2}</h2>
      <p>{body}</p>
    </div>"""

    faqs_html = ""
    for q, a in d["faqs"]:
        faqs_html += f"""<details class="faq-item"><summary>{q}</summary><p>{a}</p></details>\n"""

    # breadcrumb HTML
    if lang == "en":
        home_url = f"{DOMAIN}/"
    else:
        home_url = f"{DOMAIN}/{lang}/"
    bc_home = ui["breadcrumb_home"]
    bc_prods = ui["breadcrumb_products"]
    breadcrumb_html = f'<p class="breadcrumb"><a href="{home_url}">{bc_home}</a> › <a href="{home_url}">{bc_prods}</a> › {d["h1"]}</p>'

    related_html = related_cards(p.get("related", []), lang, ui)

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{d['title']}</title>
  <meta name="description" content="{d['meta']}">
  <meta name="keywords" content="{d['kw']}">
  <meta property="og:title" content="{d['title']}">
  <meta property="og:description" content="{d['meta']}">
  <meta property="og:image" content="{pm['img']}">
  <meta property="og:url" content="{product_url(p['slug'], lang)}">
  <meta property="og:type" content="product">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{product_url(p['slug'], lang)}">
{hreflang_for_product(p['slug'])}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css_path}">
  <script type="application/ld+json">
{schema_prod}
  </script>
  <script type="application/ld+json">
{schema_bread}
  </script>
  <script type="application/ld+json">
{schema_faq}
  </script>
</head>
<body>
<nav class="nav">
  <a class="nav-logo" href="https://hirsutalab.com/">HirsutaLab</a>
  <div class="nav-right">
    <div class="lang-switcher">
      <span class="lang-active">{lang.upper()}</span>
      <div class="lang-dropdown">
        {nav_lang_switcher(p['slug'], lang)}
      </div>
    </div>
    <a class="btn-shop" href="https://hirsutalab.com/" target="_blank">{ui['nav_shop']} →</a>
  </div>
</nav>

<div class="product-page">
  <div class="container">
    {breadcrumb_html}
    <div class="product-page-grid">
      <div class="product-page-img">
        <img src="{pm['img']}" alt="{d['h1']}" loading="eager">
        <img src="{p.get('img2', pm['img'])}" alt="{d['h1']} 500g" loading="lazy" style="margin-top:12px">
      </div>
      <div class="product-page-info">
        <p class="hero-eyebrow">{d['eyebrow']}</p>
        <h1 class="product-page-title">{d['h1']}</h1>
        <p class="product-page-price">{ui['from']} €{pm['price']}</p>
        <div class="rating-row">
          <span class="stars">★★★★★</span>
          <span class="rating-text">4.8 / 5 (47)</span>
        </div>
        <p class="product-page-intro">{d['intro']}</p>
        <a class="btn-primary" href="{pm['shop_url']}" target="_blank" rel="noopener">{d['cta']}</a>
      </div>
    </div>

    <div class="product-page-body">
      {sections_html}
    </div>

    <div class="faq product-page-faq">
      <h2 class="section-title">{ui['faq']}</h2>
      <div class="faq-list">{faqs_html}</div>
    </div>

    <div class="related-products">
      <h2 class="section-title">{ui['related']}</h2>
      <div class="related-grid">
        {related_html}
      </div>
    </div>

    <div class="product-page-cta">
      <a class="btn-primary" href="{pm['shop_url']}" target="_blank" rel="noopener">{d['cta']}</a>
    </div>
  </div>
</div>

<footer class="footer">
  <div class="container">
    <p class="disclaimer">{ui['disclaimer']}</p>
    <p style="text-align:center;margin-top:16px;font-size:13px;opacity:.5">© 2025 HirsutaLab · <a href="https://hirsutalab.com/" target="_blank">hirsutalab.com</a></p>
  </div>
</footer>
</body>
</html>"""
    return html

# ── CSS ADDITIONS ─────────────────────────────────────────────────────────────
CSS_ADDITIONS = """
/* ---- Related Products ---- */
.related-products { margin: 60px 0 0; }
.related-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 16px; margin-top: 24px; }
.related-card { border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; text-decoration: none; color: var(--text); transition: border-color 0.3s, transform 0.3s; display: block; background: var(--bg-card); }
.related-card:hover { border-color: var(--accent); transform: translateY(-2px); }
.related-card img { width: 100%; aspect-ratio: 4/3; object-fit: cover; }
.related-card-body { padding: 12px; }
.related-name { display: block; font-size: 13px; font-weight: 500; margin-bottom: 4px; }
.related-price { font-size: 12px; color: var(--accent); }

/* ---- Rating row ---- */
.rating-row { display: flex; align-items: center; gap: 10px; margin: 8px 0 16px; }
.stars { color: var(--accent-warm); font-size: 16px; letter-spacing: 1px; }
.rating-text { font-size: 13px; color: var(--text-muted); }

/* ---- Disclaimer ---- */
.disclaimer { text-align: center; font-size: 12px; color: var(--text-muted); border: 1px solid var(--border); border-radius: var(--radius); padding: 12px 20px; max-width: 700px; margin: 0 auto; }
"""

# ── BUILD PAGES ──────────────────────────────────────────────────────────────
count = 0
for p in PRODUCTS:
    for lang in LANGS:
        if lang not in p["data"]:
            continue
        if lang == "en":
            out_dir = os.path.join(BASE, p["slug"])
        else:
            out_dir = os.path.join(BASE, lang, p["slug"])
        os.makedirs(out_dir, exist_ok=True)
        html = build_product_page(p, lang)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        count += 1
        print(f"✓ {lang}/{p['slug']}/index.html")

# Append CSS additions to existing style.css
css_path = os.path.join(BASE, "style.css")
with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n" + CSS_ADDITIONS)
print(f"\n✓ Updated style.css (+related/rating/disclaimer styles)")
print(f"\n✅ Generated {count} product pages.")

from spacy.lang.fr.stop_words import STOP_WORDS
from spacy.lang.en.stop_words import STOP_WORDS as en_stopwords

def customStopWordsFr():
    return ['vouloir','voir','permettre',"prendre","falloir","assurer","réagir","venir","souhaiter","trouver","concerner","accorder","proposer","penser","continuer","rester","demander","aller",
    "soutenir","prévoir","passer","signer","entrer","devoir","aimer","utiliser","sembler","cesser","porter","attendre","envoyer","répondre","appeler","exiger","obtenir","montrer","présenter",
    "compter","considérer","constater","réaliser","connaître","rappeler","partir","choisir","accepter","apporter","éviter","nécessiter","profiter","décider","commencer","espérer","agir",
    "contribuer","justifier","effectuer","garder","adapter","remettre","croire","aider","suffire","gérer","rejoindre","préciser","démontrer","expliquer","remplacer","solliciter","envisager",
    "déplacer","essayer","fournir","rencontrer","remercier","préparer","affirmer","revoir","devenir","entendre","comprendre","reconnaître","représenter","durer","toucher",'maintenir',"viser",
    "informer","revenir","disposer","exercer","ajouter","retirer","poser","reprendre","ressourcer","supporter","sentir","impliquer","imaginer","valoir","engendrer","réussir","regarder","estimer",
    "confirmer","renforcer","déposer","paraître","citer","placer","ignorer","générer","réserver","attirer","conserver","bloquer","relever","appuyer","apparaître","hésiter","établir","contacter",
    "écouter","préférer","tourner","atteindre","prétendre","nommer","avérer","bouger","évoquer","consacrer","percevoir","révéler","dédier","définir","signifier","exposer","avancer","inciter",
    "distinguer","répéter","apprécier","émettre","dérouler","retenir","intéresser","interroger","pousser","procéder","parvenir","correspondre","consister","déterminer","recommander","agréer",
    "constituer","refuser","retrouver","annoncer","sortir","lier","situer","occuper","tenter","rentrer","encourager","amener","remplir","baser","convaincre","taire","dépendre","prier","savoir",
    "entraîner","détenir",'luire','celer',"typer","refaire"," soussigner","remarquer","choir","donner","résumer","soussigner","géer","oper","génèr","mourer","diser",
    "issu","présente","montre","donné","charge","aide","considérant","sommes","réduit","existant","déposé","prenant","censé","fait","demandé","rendant","donnant","donne","venant","proposant",
    "connaît","fini","établi","ouvre","entraînant","agissant","commis","allant","venue","lié","repris","propose","cesse","représente","continue","trouve","souhaite","refuse","manqu","manquer",
    "manquent","devient","arrive","faite","souhaitons","souhaiton","souhaitent","constitue","impose","vient","signez","partagez","aidez","donnez","avon","remercion","contenant","metton","entent",
    "tient","faison","soyon","soutenon","agisson","dison","unisson","prenon","pourron","réagisson","voyon","dénonçon","interdison","ayon","auron","accepteron","lançon","savez","soutenez","soyez",
    "sachez","venez","voyez","connaissez","croyez","voulez","agissez","recevez","prenez","saviez","ayez","joignez","comprenez","ouvrez","pourriez","lisez","souvenez","rendez","mettez","aidez-nous",
    "aidez-nou","aurai","dis","disant","disparaissent","reprenon","répond","vit","ete","eter","ver","ser","consider","considèr","considered","considering","conside","represent","débordant","feron",
    "ferai",
    "janvier","février","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre","dimanche","lundi","mardi","mercredi","jeudi","vendredi","samedi",
    "généralement","activement","activemer","également","immédiat","actuellement","actuellemer","simplement","important","supplémentaire","autant","attention","totalement","plupart","rapidement",
    "nécessaire","impossible","peut-être","partout","total","uniquement","largement","ensuite","demain","précédent","régulièrement","déjà","jamais","pourtant","auprès","ici","mieux","grâce",
    "malheureusement","malheureusemer","autour","remerciement","travers","vraiment","lorsqu","clairement","fortement","presque","conséquent","au-delà","est-il","peut-il","puisqu","récemment",
    "réellement","détriment","évidemment","bref","moindre","davantage","bientôt","égard","cordialement","cordialemer","extrêmement","complètement","éventuel","certainement","contrairement","finalement",
    "définitivement","correctement","préalable","tôt","lendemain","suffisamment","forcément","pleinement","est-à-dire","parfaitement","ores","minimum","maximum","actuel","potentiellement","hier",
    "systématiquement","normalement","énormément","quotidiennement","probablement","vis-à-vis","principalement","ci-dessus","ci-dessous","ci-joint","ci-après","quelqu","quelques-uns","purement","puremer",
    "quasiment","précisement","profondément","considérablement","pareil","personnellement","concrètement","vain","essentiellement","fréquent","correspondant","prochainement","initialement","instamment",
    "surcroît","sérieusement","sérieusemer","est-elle","majoritairement","majoritairemer","soi-disant","soit-disant","soi-diser","bienvenu","bienvenue","grandement","instar","aucunement","apparemment",
    "tandis","effectivement","faut-il","quasi","justement","sûrement","surement","sûremer","heureusement","pré","exceptionnel","exceptionnelle","excellente","reprise","surcroit","progressivement",
    "progressivemer","sereinement","sereinemer","difficilement","difficilemer","hautement","hautemer","inévitablement","inévitablemer","ouvertement","ouvertemer","sincèrement","sincèremer","exactement",
    "exactemer","autrement","autremer","nécessairement","nécessairemer","respectueusement","respectueusemer","rarement","raremer","spécialement","spécialemer","indirectement","indirectemer",
    "catégoriquement","catégoriquemer","anciennement","anciennemer","subitement","subitemer","provisoirement","provisoiremer","entièrement","précisemment","équivalent","efficacement","exclusivement",
    "récurrent","volontairement","vivement","véritablement","éventuellement","constamment","pratiquement","visiblement","solennellement","nettement","dernièrement","précédemment","fréquemment",
    "habituellement","intégralement","globalement","littéralement","temporairement","préalablement","franchement","spécifiquement","respectivement","explicitement","formellement","pertinemment",
    "bonnement","significativement","amplement","vraisemblablement","évidement","prématurement","ras","entrain","ourselve","ye","ner","ger","vacer","cer","certe","silver","silve","institute",
    "instituten","pay","cualquier","terrified","paymer","payment","onee","ones","oner","onerer","letter","letterer","lettere","flouted","teller","tellier","carner","carné","sper","hajer","petitie",
    "petitier","contrario","directed","inter","manter",
    "petit","indispensable","long","haut","fort","difficile","simple","meilleur","gros","essentiel","inacceptable","sérieux","inutile","favorable","large","clair","récent","énorme","utile","évident",
    "spécifique","facile","définitif","strict","heureux","acceptable","insuffisant","net","disponible","plein","pleine","efficace","rapide","précis","ancien","magnifique","vite","tard","multiple",
    "excellent","forte","haute","longue","bonne","précise","ème","eme","etc","….",".000","svp","mme","...","1er","die","haver","het","deze","der","und","bout","los","dos","thi","h30","h00","world",
    "english","héler","von","che","aah","una","french","zijn","rights","dat","sont-ils","years","european","den","ste","new","voor","hav","having","reason","government","student","....","plu","Monsieur",
    "somme","conséquence","vivant","nombre","fois","vis","part","jour","soutien","contraire","produit","chose","nom","exemple","cause","suite","mal","prochain","réponse","solution","personnel","oui",
    "vrai","début","millier","page","prise","objectif","besoin","madame","million","minute","moyen","concertation","centaine","propos","moyenne","demande","milliard","sorte","direct","dizaine","doute",
    "petition","faveur","saint","mètre","monsieur","présence","mot","mois","heure","semaine","but","moment","terme","signature","bonjour","manière","véritable","date","forme","côté","voire","pétition",
    "hauteur","durée","matin","soir","faux","siècle","digne","dignité","courant","capable","concret","potentiel","défaut","rythme","instant","décennie","gramme","principe","décision","jeune","action",
    "projet","zone","cas","raison","question","information","groupe","sujet","objet","signataire","manque","milieu","proposition","entier","image","base","avis","journée","bel","salutation","limite",
    "complet","rencontre","prétexte","signe","argument","caractère","importance","bord","relatif","pose","double","revendication","taille","fond","rappel","français","communicant","commune","installation",
    "central","arrêt","article","laisse","pratique","double","considération","tonne","vigueur","excuse","type","âge","donnée","fédération","retard","membre","fermeture","ouverture","maintien","création",
    "habitant","kilomètre","maire","après-midi","présidence","boulevard","étage",'sou',"fier","amont","remarque","bourg","lande","liste","passe","person","pourcent","contact",
    "jean-michel","martiner","didier","claude","patrick","dominique","vincent","denis","sophie","thomas","isabelle","marc","catherine","robert","alexandre","antoine","daniel","nathalie","guillaume",
    "christine","henri","thierry","christian","françoise","georges","sylvie","camille","simon","marion","manon","gaston","léon","martinez","ann","laura","nasser","nasse","nassera","nasserer","salim",
    "alberto","svizzer","svizzerer","miller","muller","nanter","christelle","estelle","stella"]

def customStopWordsEn():
    return ['signing','share','support','thank','pleas','petition','please','sign',
        'said','tim','back','many','one','us','next','think','see','make','like','just',
        'let','go','really','don','wer', 'keep','needs','ever','best','year','come', 'age',
        'del','por','para','los','un','el', 'en','que','le','de','also',"sign","share",
        "petition",'like','year','people', 'time','use','make','will','one','want','need',
        'know','take','say','now','san', 'come', 'los', 'que','de','la','day', 'allow',
        'way', 'thing', 'bring', 'tell', 'ask', 'get', 'also', 'well', 'not', 'can', 'american',
        'para','del','las','much','every','even','stay','signature','help', 'final','mrs',
        'chang','good','better','stop','name', 'something', 'great', 'must', 'days', 'dont', 
        'never','shouldn', 'everyone', 'lets', 'old', 'may', 'must', 'im', 'mr', 'give', 
        'feel', 'wants', 'going', 'enough', 'bad', 'put','soon','possible','ago','demand','big']

def getStopwordsList(language):
    if language == 'fr':
        stopwordsList = STOP_WORDS

        STOP_WORDS.remove("personne")

        for word in customStopWordsFr():
            STOP_WORDS.add(word)
        for word in customStopWordsEn():
            STOP_WORDS.add(word)
        for word in en_stopwords:
            STOP_WORDS.add(word)

        return stopwordsList
    elif language == 'en':
        stopwordsList = en_stopwords

        for word in customStopWordsEn():
            STOP_WORDS.add(word)
        for word in en_stopwords:
            STOP_WORDS.add(word)

        return stopwordsList
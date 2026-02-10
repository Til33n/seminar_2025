#### Seminar iz narčtovanja in razvoja programske opreme v TK #### 

Pri omenjenem predmetu sem za projekt izdelal preprosto mobilno/spletno aplikacijo imenovano Flappy Plane. Mobilna igra,
zelo preprosta, je izdelana v programskem okolju Android Studio (mobile_app). Osnova njenega delovanje je "collision detection". Ta
ob detekciji ustavi igro in pošlje igralčev dosežek na zalednji del spletne aplikacije oziroma "end_point".

  Spletna aplikacija je sestavljena iz dveh sklopov "front_end" in "back_end". Kot vidimo iz zgornjih datotek "front_end" sestavlja 
predvsem pogramski jezik HTML (ta poskrbi za vizualni del spletne strani), imamo pa tudi dinamičen jezik JavaScript (ta obdeluje 
JSON podatke in podobno). Spletni strežnik Uvicorn je ASGI strežnik. Implementiran je v Python jeziku in poganja naš "back_end". 

#### heli_app.java ####
Za mobilno aplikacijo imamo več datotek (.java, .xml) v Android Studio projektu:
- "heli_app.java" glavna datoteka, kjer se mobilna igra poganja

#### front_end ####
Za "front end" imamo (trenutno) dve datoteki: 
- "index.html" se uporablja za logiranje in sicer vnos uporabniškega imena (Ang. username) in gesla (Ang. password).
- "main_2.html" pa predstavlja osnovno spletno domačo stran igralčeve statistike, urejanja in njegovih podatkov. 

#### back_end ####
Za "back end" imamo tri datoteke:
- "server_2.py" na njej teče glavni spletni strežnik z vsemi GET, PUT, POST, DELETE končnimi točkami (Ang. endpoints).
- "database_main.py" vsebuje vse funkcije za povezavo, vnos, izbris in manipulacijo podatkovnih baz. 
- "database_2.db" predstavlja našo podatkovno bazo, ta vsebuje vse podatke o igralcih, igranih iger, administrativnih privilegijih itd.



Zalednji del (Ang. back_end) vsebuje GET, POST, PUT in DELETE (API endpoints):
  
  # # 1 GET
  Uporabnik odpre spletno stran na referenčnem IP naslovu (npr. "http:192.168.64.15/5000" ). Prvi API mu vrne spletno stran 
  "index.html", katera omogoča vnos uporabniškega imena in gesla za postopek avtentikacije in prijave v spletno aplikacijo.

  # # 2 POST
  API ob proceduri prijave sprejme dva podatka ("user" in "password"). V Python funkciji API-ja POST nato preveri, če "user" obstaja. Če dobi 
  pozitiven odziv, generira za omenjenega "user"-ja njegova pripadajoča ključa ("key" in "tmp_ključ"). Nato sledi še avtentikacija 
  gesla ("password") uporabnika in če je pozitivna, naključno generirana ključa shrani v podatkovno bazo pravkar prijavljenega uporabnika. 
  Imamo torej postopek ročno generiranega piškotka (Ang. manually generated token). Po končanih avtentikacijah API pošlje podatke uporabnika ("user", "key" in "tmp_key") nazaj na 
  front_end ("index_2.html"), ki te podatke shrani v lokalni spomin browserja (Ang. Local storage) pravkar avtentificiranega uporabnika.

  Poleg generiranja ključev, se generira tudi vzporedni časovnik, ki skrbi za časovno obstojnost teh ključev (v izdelavi).
  
  # # 3 GET
  Na podlagi uspešne avtentikacije, generiranja ključev, logiranja uporabnika in povratne informacije prejšnega API-ja (# 2) k "front_end", ga "index_2.html" preusmeri na novi API GET (# 3).
  Ta nam na podlagi začasnega ključa (ob predpostavki, da je pravilen) poda novo datoteko "main_2.html" in uporabnika po uspešni prijavi preusmeri na njegovo domačo stran.
  
  # # 4 GET
  Podobno kot zgornji primer, tukaj na podlagi pravilnega ključa ("tmp_key") preverjamo avtentifikacijo uporabnikove zahteve na naš Uvicorn strežnik. Če ključ ni pravilen ali mankajoč,
  se bo zahteva v vsakem primeru zavrnila in preusmerila na osnovno stran za prijavo uporabnika (index_2.html).

  # # 5 POST
  Ta API sprejme dva JSON elementa ("user" in "key"). Na podlagi poslane zahteve uporabnika (Ang. Client) posreduje osnovne podatke iz podatkovne baze kot so: email, trenutni dosežek uporabnika .. itd
  ampak samo v primeru pozitivno opravljenje avtentifikacije uporabnika na podlagi identite in začasnega ključa. 
  
  # # 6 POST
  Funkcija tega API-ja nam omogoča aktivno spremembo naših podatkov, kot so posodobitev email naslova, sprememba gesla in podobno. API POST sprejme JSON objekt z šestimi elementi ( "key",
  "selection", "updated_email","updated_password" in "current_password"). Na podlagi podanega "user", "key" in "current_password" strežnik opravi avtentifikacijo verodostojnosti zahteve. Na podlagi "selection" 
  podatka ustrezno izbere izbor podatkov namenjenih za posodobitev v podatkovnih bazah. Če funkcija uspešno opravi posodobitev podatkov vrne temu preimerno statusno kodo na "main_2.html".

  # # 7 PUT
  API PUT na podlagi posredovanja pravilnega naključnega ključa (podobno kot pri #3 in #4) in uporabniškega imena, funkcija opravi avtentikacijo zahteve od "main_2.html" (lahko tudi od kjerkoli) in 
  resetira trenutni dosežek (Ang. score) prijavljenega uporabnika.
  
  # # 8 POST
  Ta API POST je povezan z spodnjim API-jem (# 8.1). Skupaj tvorita administrativno orodje za brisanje registriranih uporabnikov iz spletne aplikacije. Prva faza je pridobivanje podatkov vseh registriranih  uporabnikov v spletni aplikaciji. POST API sprejme dva JSON elementa ("user" in "tmp_key") in na podlagi nju opravi avtentikacijo zahteve. Če je avtentikacija pozitivna, posreduje seznam registriranih uporabnikov nazaj na "main_2.html" (pošlje na "fornt end").
  
  # # 8.1 DELETE
  Brisanje registriranih uporabnikov pa opravlja API DELETE. Pri takšnih API-jih je verodostojnost in avtentifikacija zelo pomembna, saj lahko ne-avtoriziran dostop povzroči precej škode in podobno. Tukaj API sprejme dva JSON elementa in sicer ("key" in "tmp_key"). Ti dve naključno generirani vrednosti se morata v podatkovni bazi medsebojno ujemati in tudi obstajati, drugače bo strežnik zavrnil zahtevo. Če se medsebojno ujemata, mora hkrati uporabnik, ki je tudi lastnik tih dveh ključeh imeti administrativne privilegije. Če so vsi pogoji izpolnjeni, lahko odstranjuje registrirane uporabnike iz spletne aplikacije ("admin" = True).

  # # 9 DELETE
  Odjava iz spletne aplikacije (Ang. Log out) opravlja API DELETE. Ko se odjavimo iz spletne aplikacije, moramo izbrisati aktivno sejo (v našem primeru uničimo ključa "tmp_key" in "key"). API sprejme 3 podatke ("username" in dva JSON elementa), na katerih opravlja avtentifikacijo. Če je zahteva na odjavo avtentificirana, funkcija uniči (izbriše) ključa in uporabnika preusmeri na "index_2.html"

  
  # # 10 POST
  Api se uporabi za proceduro registracije novega računa.
  
  # # 11 PUT
  Api se uporabi za ponastavitev gesla. Če uporabnik izgubi geslo, ga lahko re-generira na podlagi avtentikacije preko prvotno posrednovanega EMAIL naslova uporabnika.


#### ZAKLJUČEK #####

Seja uporabnika temelji na nakjučno generiranih vrednostih ("key" in "tmp_key"), ki morajo biti časovno omejeni. To pomeni, da ko se ključa generirata, se mora njun čas obstojnosti začeti manjšati (ob predpostavki, da uporabnik vmes ne klikne nič). Če uporabnik med aktivno sejo klikne novo povezavo, se čas obstojnosti ključev resetira. Implementacija časovnika, ki vzporedno odšteva čas vsem izdanim ključom je nujna za uporabnost in varnost spletne aplikacije. Ob odjavi iz sistema se ključa avtomatsko uničita skupaj z pripadajočim časovnikom. Vzporedni časovnik je v fazi izdelave.









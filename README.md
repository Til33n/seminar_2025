#### Seminar iz narčtovanja in razvoja programske opreme v TK #### 

Pri omenjenem predmetu sem za projekt izdelal preprosto mobilno/spletno aplikacijo imenovano Flappy Plane. Mobilna igra,
zelo preprosta, je izdelana v programskem okolju Android Studio (mobile_app). Osnova njenega delovanje je "collision detection". Ta
ob detekciji ustavi igro in pošlje igralčev dosežek na zalednji del spletne aplikacije oziroma "end_point".

  Spletna aplikacija je sestavljena iz dveh sklopov "front_end" in "back_end". Kot vidimo iz zgornjih datotek "front_end" sestavlja 
predvsem pogramski jezik HTML (ta poskrbi za vizualni del spletne strani), imamo pa tudi dinamičen jezik JavaScript (ta obdeluje 
JSON podatke in podobno). Spletni strežnik Uvicorn, ki je ASGI spletni strežnik implementiran v Python jeziku, pa poganja naš "back_end". 

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
- "database_main.py" vsebuje vse funkcije za povezavo, vnos, izbris in manipulacijo podatkov igralcev in podobno. 
- "database_2.db" predstavlja našo podatkovno bazo, ki vsebuje vse podatke o igralcih, igranih iger itd.



Zalednji del (Ang. back_end) vsebuje GET, POST, PUT in DELETE (API endpoints):
  
  # # 1 GET
  Uporabnik odpre spletno stran na referenčnem IP naslovu (npr. http:192.168.64.15/5000), ta prvi API mu vrne spletno stran 
  "index.html", katera mu omogoča vnos uporabniškega imena in gesla za psotopek avtentikacije in logiranja v sistem.

  # # 2 POST
  API ob proceduri logiranja sprejme dva podatka ("user" in "password").V Python funckiji API-ja POST nato preveri, če "user" obstaja. Če dobi 
  pozitiven odziv, generira za omenjenega "user"-ja njegov pripadajoči naključni ključ ("key") in začasni ključ ("tmp_ključ"). Nato sledi še avtentikacija 
  gesla ("password") omenjenega uporabnika in če je pozitivna, naključno generirana ključa shrani v podatkovno bazo pravkar logiranjega uporabnika. 
  Ročno generirani piškotek (Ang. manually generated token). Po končani avtentikaciji, API pošlje podatke uporabnika ("user") z njegovima ključema ("key" in "tmp_key") nazaj na 
  front_end (inde_2.html), ki te podatke shrani v lokalni spomin browserja (Ang. Local storage) pravkar avtenticiranega uporabnika.

  Poleg generiranja ključev, se generira tudi vzporedni časovnik, ki skrbi za časovno obstojnost teh ključev.
  
  # # 3 GET
  Na podlagi uspešne avtentikacije, generiranja ključev, logiranja uporabnika in povratne informacije prejšnega API-ja (# 2) k "front_end", ga "index_2.html" preusmeri na novi API GET (# 3).
  Ta nam na podlagi začasnega ključa (če je seveda pravilen) poda novo datoteko "main_2.html" in uporabnika po uspešnem logiranju preusmeri na njegovo domačo stran.
  
  # # 4 GET
  Podobno kot zgornji primer, tukaj na podlagi pravilnega začasnega ključa ("tmp_key") preverjamo avtentikacijo uporabnikove zahteve na naš Uvicorn strežnik. Če ključ ni pravilen ali mankajoč,
  se bo zahteva v vsakem primeru zavrnala in preusmerilo na osnovno stran za logiranje.

  # # 5 POST
  Ta API sprejme dva JSON podatka ("user" in "key")in  na podlagi poslane zahteve uporabnika (Ang. Client) posreduje osnovne podatke kot so email naslov, trenutni dosežek uporabnika itd. Ampak podobno kot v prejšnih primerih, na podlagi
  unikatnega ključa (Ang. Key) opravi avtentikacijo uporabnika in če je pozitivni odziv posreduje omenjene podatke na "main_2.html" spletno stran za prikaz. 
  
  # # 6 POST
  Funkcija tega API-ja nam omogoča aktivno spremembo naših podatkov kot so posodobitev email naslova, sprememba gesla in podobno. API kot vidimo sprejme 6 podatkov ("key","selection","updated_email","updated_password" in "current_password").
  Na podlagi podanega "user", "key" in "current_password" strežnik opravi avtentikacijo zahteve okrog teh treh podatkov. Na podlagi "selection" ustrezno spremeni podatke v podatkovnih bazah. Na podlagi uspešne zahteve API vrne statusno kodo nazaj
  k "main_2.html".

  # # 7 PUT
  Pri tem API-ju na podlagi pravilno posredovanega naključnega ključa (podobno kot pri #3 in #4) in uporabniškega imena funkcija opravi avtentikacijo zahteve od "main_2.html" (lahko tudi od kjerkoli) in resetira trenutni dosežek (Ang. score) 
  trenutnega uporabnika.
  
  # # 8 POST
  Ta API je povezan z spodnjim API-jem (# 8.1), skupaj tvorita administrativno orodje za brisanje registriranih uporabnikov iz spletne aplikacije. Prva faza je pridobivanje podatkov vseh registriranih uporabnikov v spletni aplikaciji. 
  POST API sprejme dva JSON podatka ("user" in "tmp_key") in na podlagi nju opravi avtentikacijo zahteve. Če je avtentikacija pozitivna, posreduje seznam registriranih uporabnikov k "main_2.html" (pošlje na "fornt end").
  
  # # 8.1 DELETE
  Brisanje registriranih uporabnikov pa opravlja API DELETE. Pri takšnih API-jih je pa verodostojnost in avtentikacija zelo pomembna, saj lahko ne-avtoriziran dostop povzroči precej škode in podobno. Tukaj API sprejme dva objekta JSON in sicer
  ("key" in "tmp_key"). Ti dve nakjlučno generirani vrednosti se morata v podatkovni bazi medsebojno ujemati in tudi obstajati, drugače bo strežnik zavrnil zahtevo. Če se medsebojno ujemata, mora hkrati uporabnik, ki je tudi lastnik tih dveh ključeh 
  imeti tudi administrativne privilegije, da lahko odstranjuje registrirane uporabnike iz spletne aplikacije ("admin" = True).

  # # 9 DELETE
  Odjava iz spletne aplikacije (Ang. Log out) opravlja API DELETE. Ko se odjavimo iz sistema pobrišemo aktivno sejo (v našem primeru uničimo naša ključa "tmp_key" in "key"). API sprejme 3 podatke ("username" 
  in JSON objekt) opravi njuno avtentikacijo in če je izid pozitiven, uniči uporabnikova naključno generirana ključa in preusmeri na "index_2.html"
  
  
  # # 10 POST
  Api se uporabi za proceduro registracije novega računa.
  
  # # 11 PUT
  Api se uporabi za ponastavitev gesla. Če uporabnik izgubi geslo, ga lahko re-generira na podlagi avtentikacije preko prvotno posrednovanega EMAIL naslova uporabnika.


#### ZAKLJUČEK #####

Seja uporabnika temelji na nakjučno generiranih vrednostih ("key" in "tmp_key"), ki morajo biti časovno omejeni. To pomeni, da ko se ključa generirata, se mora njun čas obstojnosti začeti manjšati (ob predpostavki, da uporabnik vmes ne klikne nič). Če uporabnik med aktivno sejo klikne novo povezavo, se čas obstojnosti ključev resetira. Implementacija časovnika, ki vzporedno odšteva čas vsem izdanim ključom je nujna za uporabnost in varnost spletne aplikacije. Ob odjavi iz sistema se ključa avtomatsko uničita skupaj z pripadajočim časovnikom. Vzporedni časovnik je v fazi izdelave.









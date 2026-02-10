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
  
  # 1 GET
  Uporabnik odpre spletno stran na referenčnem IP naslovu (npr. http:192.168.64.15/5000), ta prvi API mu vrne spletno stran 
  "index.html", katera mu omogoča vnos uporabniškega imena in gesla za psotopek avtentikacije in logiranja v sistem.

  # 2 POST
  API ob proceduri logiranja sprejme dva podatka ("user" in "password").V Python funckiji API-ja POST nato preveri, če "user" obstaja. Če dobi 
  pozitiven odziv, generira za omenjenega "user"-ja njegov pripadajoči naključni ključ ("key") in začasni ključ ("tmp_ključ"). Nato sledi še avtentikacija 
  gesla ("password") omenjenega uporabnika in če je pozitivna, naključno generirana ključa shrani v podatkovno bazo pravkar logiranjega uporabnika. 
  Ročno generirani piškotek (Ang. manually generated token). Po končani avtentikaciji, API pošlje podatke uporabnika ("user") z njegovima ključema ("key" in "tmp_key") nazaj na 
  front_end (inde_2.html), ki te podatke shrani v lokalni spomin browserja (Ang. Local storage) pravkar avtenticiranega uporabnika.
  
  
  
  # 3 fdsfds
  
  # 4 fdsfdss
  # 5 dfsfsdsdf
  # 6
  
  # 7
  # 8
  # 8.1
  # 9
  # 10
  # 11












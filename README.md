#### Seminar iz narčtovanja in razvoja programske opreme v TK #### 

Pri omenjenem predmetu sem za projekt izdelal preprosto mobilno/spletno aplikacijo imenovano Flappy Plane. Mobilna igra,
zelo preprosta, je izdelana v programskem okolju Android Studio (mobile_app). Osnova njenega delovanje je "collision detection". Ta
ob detekciji ustavi igro in pošlje igralčev dosežek na zalednji del spletne aplikacije oziroma "end_point".

  Spletna aplikacija je sestavljena iz dveh sklopov "front_end" in "back_end". Kot vidimo iz zgornjih datotek "front_end" sestavlja 
predvsem pogramski jezik HTML (ta poskrbi za vizualni del spletne strani), imamo pa tudi dinamičen jezik JavaScript (ta obdeluje 
JSON podatke in podobno). Spletni strežnik Uvicorn, ki je ASGI spletni strežnik implementiran v Python jeziku, pa poganja naš "back_end". 


#### front_end ####
Za "front end" imamo (trenutno) dve datoteki: 
- "index.html" se uporablja za logiranje in sicer vnos uporabniškega imena (Ang. username) in gesla (Ang. password)
- "main_2.html" pa predstavlja osnovno spletno domačo stran igralčeve statistike, urejanja in njegovih podatkov. 

#### back_end ####
Za "back end" imamo tri datoteke:
- "server_2.py"
- "database_main.py"
- "database_2










Seminar iz narčtovanja in razvoja programske opreme v TK 

Pri omenjenem predmetu sem za projekt izdelal preprosto mobilno/spletno aplikacijo imenovano Flappy Plane. Mobilna igra,
zelo preprosta, je izdelana v programskem okolju Android Studio (mobile_app). Osnova njenega delovanje je "collision detection", ki
ob detekciji ustavi igro in pošlje igralčev dosežek na zalednji del spletne aplikacije.


Spletna aplikacije je sestavljena iz dveh sklopov "front_end" in "back_end". Kot vidimo iz zgornjih datotek "front_end" sestavlja 
predvsem pogramski jezik HTML (ta poskrbi za vizualni del spletne strani), imamo pa tudi dinamičen jezik JavaScript (ta obdeluje 
JSON podatke in podobno). "back end" poganja spletni strežnik Uvicorn, ki je ASGI spletni strežnik implementiran v Python jeziku. 
Za podatkovno bazo sem izbral SQLite3, saj je Python-u prijazna podatkovna baza







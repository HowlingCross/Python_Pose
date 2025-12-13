Python Pose: Valós idejű Edzésanalitikai AI Rendszer
Cél
Egy valós idejű, mélytanuláson alapuló rendszer létrehozása az emberi testtartás és mozgásforma precíz elemzésére fitness edzések során. A cél a helytelenül végzett gyakorlatok azonnali szűrése, ezzel a sérülések megelőzése és az edzéshatékonyság növelése.

Felhasznált Modell
Típus: YOLOv8-Pose (State-of-the-Art, SOTA) neurális hálózat.

Elv: Single-Shot Detection.

Működés: Képes 17 kritikus emberi kulcspont (keypoint) valós idejű, gyors és pontos detektálására a videóképen. De ebből mi csak azokat használjuk ami egy fekvőhöz kellhet.

Számítás: A kinyert kulcspontokból geometriai számítások (koszinusztétel, vektoranalízis) segítségével meghatározzuk a kritikus ízületi szögeket (pl. térd-csípő-boka).

Értékelés: Az ízületi szögek alapján történik a kiválasztott gyakorlat (most fekvőtámasz) helyességének valós idejű mérése.

Kimenet és Alkalmazás
Visszajelzés: Azonnali, vizuális visszajelzés egy számban.

Kód: A projekt kódja és demója nyilvános GitHub repóban érhető el.

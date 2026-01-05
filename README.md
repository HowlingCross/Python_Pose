Python Pose: Valós idejű Edzésanalitikai AI Rendszer
Cél
Egy valós idejű, mélytanuláson alapuló rendszer létrehozása az emberi testtartás és mozgásforma precíz elemzésére fitness edzések során. A cél a helytelenül végzett gyakorlatok azonnali szűrése, ezzel a sérülések megelőzése és az edzéshatékonyság növelése.

Felhasznált Modell
Típus: YOLOv8-Pose (State-of-the-Art, SOTA) neurális hálózat. A projekt során NEM történt egyedi tanítás (fine-tuning). A rendszer az Ultralytics által biztosított, COCO dataset-en előtanított (pretrained) YOLOv8n-pose.pt modellt használja. Ez a modell "out-of-the-box" képes a 17 emberi kulcspont detektálására, amiből a szoftver a fekvőtámaszhoz szükséges pontokat nyeri ki.

Elv: Single-Shot Detection.

Működés: Képes 17 kritikus emberi kulcspont (keypoint) valós idejű, gyors és pontos detektálására a videóképen. De ebből mi csak azokat használjuk ami egy fekvőhöz kellhet.

Számítás: A kinyert kulcspontokból geometriai számítások (koszinusztétel, vektoranalízis) segítségével meghatározzuk a kritikus ízületi szögeket (pl. térd-csípő-boka).

Értékelés: Az ízületi szögek alapján történik a kiválasztott gyakorlat (most fekvőtámasz) helyességének valós idejű mérése.

Kimenet és Alkalmazás
Visszajelzés: Azonnali, vizuális visszajelzés egy számban.

Kód: A projekt kódja és demója nyilvános GitHub repóban érhető el.




Telepítés és Futtatás (Windows)
A projekt futtatásához Python 3.10+ környezet javasolt.

1. Környezet beállítása
Virtuális környezet létrehozása
python -m venv venv

majd, 

.\venv\Scripts\activate

3. Ultralytics telepítése telepítése
PowerShell-be vagy VS-codeon belül a terminálba:

pip install ultralytics opencv-python numpy

3. Futtatás
A fő program indítása (alapértelmezett webkamerával vagy videófájllal):

python main.py**

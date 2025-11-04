# Python_Pose
Ez a projekt egy valós idejű, mesterséges intelligencia alapú rendszert valósít meg, amely képes az emberi testtartás és mozgásforma precíz elemzésére a fitness edzések során. A projekt célja, hogy megoldást nyújtson a sportolók és edzők számára a helytelenül végzett gyakorlatokból eredő sérülések  és a csökkent edzéshatékonyság problémájára.


A megvalósítás alapját a mélytanulás képezi. Egy SOTA (State-of-the-Art) neurális hálózatot, a YOLOv8-Pose modellt használtuk, mely a Single-Shot Detection elvét követve , kiváló sebességgel és pontossággal képes a 17 kritikus emberi kulcspont (keypoint) valós idejű detektálására. Az adathalmaz tekintetében átviteli tanulást (Transfer Learning) alkalmaztunk, kihasználva a modell előzetes betanítását nagyméretű, nyilvános adathalmazokon (pl. COCO Keypoints Dataset).





A detektálás után a rendszer a jármű-mechatronikában is alkalmazott pozícióelemzési elveket ülteti át a fitness világába. A kinyert kulcspontokból geometriai számítások (koszinusztétel, vektoranalízis) segítségével kritikus ízületi szögeket (pl. térd-csípő-boka) számítunk, ezzel mérve a kiválasztott gyakorlat (pl. guggolás) helyességét. Az eredmények azonnali, vizuális visszajelzés formájában jelennek meg a felhasználó számára.

A projekt a BME Gépjárműtechnológia Tanszékének fókuszához illeszkedve a mesterséges intelligencia és a valós idejű kiértékelés fontosságát hangsúlyozza. A kód és a demó egy nyilvános GitHub repóban érhető el.

import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullisten_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_edullisilla_jos_raha_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)  
        self.assertEqual(self.kassapaate.edulliset, 1) 
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10) 
        
    def test_kateisosto_ei_toimi_edullisilla_jos_raha_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)
        
    def test_kateisosto_toimii_maukkailla_jos_raha_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)  
        self.assertEqual(self.kassapaate.maukkaat, 1)  
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        
    def test_kateisosto_ei_toimi_maukkailla_jos_raha_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(350), 350)
        
    def test_korttiosto_toimii_edullisilla_jos_raha_riittava(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  
        self.assertEqual(self.kassapaate.edulliset, 1) 
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        
    def test_korttiosto_ei_toimi_edullisilla_jos_raha_ei_riittava(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        
    def test_korttiosto_toimii_maukkailla_jos_raha_riittava(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  
        self.assertEqual(self.kassapaate.maukkaat, 1) 
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        
    def test_korttiosto_ei_toimi_maukkailla_jos_raha_ei_riittava(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000) 
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        
    def test_kortille_ladattaessa_saldo_ja_kassa_muuttuu(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 250)
        self.assertEqual(str(self.maksukortti), "saldo: 12.5")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100250)
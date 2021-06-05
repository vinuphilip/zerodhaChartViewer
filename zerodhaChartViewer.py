from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import Select
#from webdriver_manager.chrome import ChromeDriverManager
import time

loginid = "Put your zerodha user id here"
password = "Put your zerodha password here"
# write your Zerodha Token PIN below IF IT IS static
loginpin = "Put your zerodha PIN here"



#driver=webdriver.Firefox()
driver=webdriver.Chrome()


driver.get("https://kite.zerodha.com")
def loginkite():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"userid"))).send_keys(loginid)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"password"))).send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']"))).click()
    
    
#   if the PIN is static you can enter the pin and uncomment these 2 lines to ensure that even your authentication with PIN is also seamless . If
#   not then comment these 2 lines and let it prompt you to enter PIN    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"pin"))).send_keys(loginpin)          
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']"))).click()     



loginkite()
time.sleep(10)





links = [
"https://kite.zerodha.com/chart/ext/ciq/BSE/AARTIDRUGS/134233092",
"https://kite.zerodha.com/chart/ext/ciq/BSE/APLLTD/136594692",
"https://kite.zerodha.com/chart/ext/ciq/BSE/ABCAPITAL/138416900",
"https://kite.zerodha.com/chart/ext/ciq/BSE/ADORWELD/132362500",
"https://kite.zerodha.com/chart/ext/ciq/BSE/ADVENZYMES/138246404",
"https://kite.zerodha.com/chart/ext/ciq/BSE/AJANTPHARM/136276740",
"https://kite.zerodha.com/chart/ext/ciq/BSE/AJANTSOY/132919300",
"https://kite.zerodha.com/chart/ext/ciq/NSE/ALEMBICLTD/20225",
"https://kite.zerodha.com/chart/ext/ciq/NSE/AMBUJACEM/325121",
"https://kite.zerodha.com/chart/ext/ciq/BSE/ALUFLUOR/134306308",
"https://kite.zerodha.com/chart/ext/ciq/NSE/AMBUJACEM/325121",
"https://kite.zerodha.com/chart/ext/ciq/BSE/ANDHRSUGAR/151055876",
"https://kite.zerodha.com/chart/ext/ciq/BSE/ANUHPHR/129602564",
"https://kite.zerodha.com/chart/ext/ciq/NSE/APCOTEXIND/39425",
"https://kite.zerodha.com/chart/ext/ciq/NSE/APOLLOPIPE/3676417",
"https://kite.zerodha.com/chart/ext/ciq/BSE/APOLLOTRI/137872900",
"https://kite.zerodha.com/chart/ext/ciq/NSE/ASHIANA/6247169",
"https://kite.zerodha.com/chart/ext/ciq/NSE/ASIANPAINT/60417",
"https://kite.zerodha.com/chart/ext/ciq/NSE/ATULAUTO/7685889",
"https://kite.zerodha.com/chart/ext/ciq/NSE/AUROPHARMA/70401",
"https://kite.zerodha.com/chart/ext/ciq/NSE/AVANTIFEED/2031617",
"https://kite.zerodha.com/chart/ext/ciq/BSE/AVTNPL/132890884",
"https://kite.zerodha.com/chart/ext/ciq/BSE/AXISBANK/136247044",
"https://kite.zerodha.com/chart/ext/ciq/BSE/BAJAJHCARE/138207236",
"https://kite.zerodha.com/chart/ext/ciq/NSE/BAJFINANCE/81153",
"https://kite.zerodha.com/chart/ext/ciq/BSE/BBTC/128364804",
"https://kite.zerodha.com/chart/ext/ciq/NSE/BERGEPAINT/103425",
"https://kite.zerodha.com/chart/ext/ciq/NSE/BHARATFORG/108033",
"https://kite.zerodha.com/chart/ext/ciq/NSE/BODALCHEM/6404353",
"https://kite.zerodha.com/chart/ext/ciq/BSE/BOROLTD/139062276",
"https://kite.zerodha.com/chart/ext/ciq/BSE/BORORENEW/128568068",
"https://kite.zerodha.com/chart/ext/ciq/BSE/BSOFT/136294404",
"https://kite.zerodha.com/chart/ext/ciq/NSE/CADILAHC/2029825",
"https://kite.zerodha.com/chart/ext/ciq/NSE/CAMLINFINE/1591297",
"https://kite.zerodha.com/chart/ext/ciq/BSE/CANFINHOME/130866180",
"https://kite.zerodha.com/chart/ext/ciq/BSE/CAPPL/134333956",
"https://kite.zerodha.com/chart/ext/ciq/NSE/CDSL/5420545",
"https://kite.zerodha.com/chart/ext/ciq/BSE/CHEMCON/139067652",
"https://kite.zerodha.com/chart/ext/ciq/BSE/CIPLA/128022276",
"https://kite.zerodha.com/chart/ext/ciq/NSE/COROMANDEL/189185",
"https://kite.zerodha.com/chart/ext/ciq/NSE/CYIENT/1471489",
"https://kite.zerodha.com/chart/ext/ciq/BSE/DABUR/128024580",
"https://kite.zerodha.com/chart/ext/ciq/BSE/DECCANCE/128547076",
"https://kite.zerodha.com/chart/ext/ciq/BSE/DEEPAKNI/129638660",
"https://kite.zerodha.com/chart/ext/ciq/NSE/DIVISLAB/2800641",
"https://kite.zerodha.com/chart/ext/ciq/BSE/DSSL/136285444",
"https://kite.zerodha.com/chart/ext/ciq/NSE/EIDPARRY/234497",
"https://kite.zerodha.com/chart/ext/ciq/BSE/FERMENTA/129641988",
"https://kite.zerodha.com/chart/ext/ciq/NSE/FDC/1253889",
"https://kite.zerodha.com/chart/ext/ciq/BSE/FIBERWEB/130024964",
"https://kite.zerodha.com/chart/ext/ciq/BSE/FINOLEXIND/128240644",
"https://kite.zerodha.com/chart/ext/ciq/BSE/FORTIS/136407812",
"https://kite.zerodha.com/chart/ext/ciq/NSE/FEDERALBNK/261889",
"https://kite.zerodha.com/chart/ext/ciq/NSE/GAEL/2259969",
"https://kite.zerodha.com/chart/ext/ciq/NSE/GICRE/70913",
"https://kite.zerodha.com/chart/ext/ciq/NSE/GLENMARK/1895937",
"https://kite.zerodha.com/chart/ext/ciq/BSE/GNFC/128171524",
"https://kite.zerodha.com/chart/ext/ciq/BSE/GOACARBON/130449156",
"https://kite.zerodha.com/chart/ext/ciq/BSE/GODREJAGRO/138430212",
"https://kite.zerodha.com/chart/ext/ciq/NSE/GRANULES/3039233",
"https://kite.zerodha.com/chart/ext/ciq/NSE/GRAPHITE/151553",
"https://kite.zerodha.com/chart/ext/ciq/BSE/GRASIM/128076804",
"https://kite.zerodha.com/chart/ext/ciq/BSE/GRAUWEIL/129461764",
"https://kite.zerodha.com/chart/ext/ciq/NSE/GREENPOWER/5148161",
"https://kite.zerodha.com/chart/ext/ciq/BSE/GTPL/138394116",
"https://kite.zerodha.com/chart/ext/ciq/NSE/GUJALKALI/324353",
"https://kite.zerodha.com/chart/ext/ciq/NSE/HAPPSTMNDS/12289",
"https://kite.zerodha.com/chart/ext/ciq/NSE/HARRMALAYA/336129",
"https://kite.zerodha.com/chart/ext/ciq/NSE/HATSUN/996353",
"https://kite.zerodha.com/chart/ext/ciq/NSE/HAVELLS/2513665",
"https://kite.zerodha.com/chart/ext/ciq/BSE/HBLPOWER/132421380",
"https://kite.zerodha.com/chart/ext/ciq/BSE/HDFCAMC/138682628",
"https://kite.zerodha.com/chart/ext/ciq/NSE/HDFCBANK/341249",
"https://kite.zerodha.com/chart/ext/ciq/NSE/HDFCLIFE/119553",
"https://kite.zerodha.com/chart/ext/ciq/NSE/HIKAL/2475009",
"https://kite.zerodha.com/chart/ext/ciq/NSE/HINDCOPPER/4592385",
"https://kite.zerodha.com/chart/ext/ciq/NSE/ICICIPRULI/4774913",
"https://kite.zerodha.com/chart/ext/ciq/BSE/ICICIGI/138423300",
"https://kite.zerodha.com/chart/ext/ciq/BSE/ICICIBANK/136236548",
"https://kite.zerodha.com/chart/ext/ciq/NSE/ITI/428801",
"https://kite.zerodha.com/chart/ext/ciq/NSE/IRCTC/3484417",
"https://kite.zerodha.com/chart/ext/ciq/NSE/IPCALAB/418049",
"https://kite.zerodha.com/chart/ext/ciq/NSE/IOLCP/5225729",
"https://kite.zerodha.com/chart/ext/ciq/NSE/IOC/415745",
"https://kite.zerodha.com/chart/ext/ciq/NSE/INFY/408065",
"https://kite.zerodha.com/chart/ext/ciq/BSE/INDTONER/134038020",
"https://kite.zerodha.com/chart/ext/ciq/BSE/INDNIPPON/136253444",
"https://kite.zerodha.com/chart/ext/ciq/NSE/INDIACEM/387841",
"https://kite.zerodha.com/chart/ext/ciq/NSE/IGPL/3606017",
"https://kite.zerodha.com/chart/ext/ciq/NSE/IEX/56321",
"https://kite.zerodha.com/chart/ext/ciq/NSE/IDFCFIRSTB/2863105",
"https://kite.zerodha.com/chart/ext/ciq/NSE/HSCL/3669505",
"https://kite.zerodha.com/chart/ext/ciq/NSE/HINDZINC/364545",
"https://kite.zerodha.com/chart/ext/ciq/BSE/JUBLINGREA/139077380",
"https://kite.zerodha.com/chart/ext/ciq/NSE/JUBLPHARMA/931073",
"https://kite.zerodha.com/chart/ext/ciq/NSE/JSWSTEEL/3001089",
"https://kite.zerodha.com/chart/ext/ciq/NSE/JSL/2876417",
"https://kite.zerodha.com/chart/ext/ciq/NSE/JMCPROJECT/1134081",
"https://kite.zerodha.com/chart/ext/ciq/NSE/JINDALSTEL/1723649",
"https://kite.zerodha.com/chart/ext/ciq/BSE/JHS/136389380",
"https://kite.zerodha.com/chart/ext/ciq/BSE/JBMA/136346884",
"https://kite.zerodha.com/chart/ext/ciq/NSE/JBCHEPHARM/441857",
"https://kite.zerodha.com/chart/ext/ciq/NSE/JAMNAAUTO/5319169",
"https://kite.zerodha.com/chart/ext/ciq/BSE/KEI/132497668",
"https://kite.zerodha.com/chart/ext/ciq/BSE/KILPEST/136209156",
"https://kite.zerodha.com/chart/ext/ciq/NSE/KIRIINDUS/4259585",
"https://kite.zerodha.com/chart/ext/ciq/BSE/KOPRAN/134215684",
"https://kite.zerodha.com/chart/ext/ciq/NSE/LAURUSLABS/4923905",
"https://kite.zerodha.com/chart/ext/ciq/NSE/LINDEINDIA/416513",
"https://kite.zerodha.com/chart/ext/ciq/NSE/LUPIN/2672641",
"https://kite.zerodha.com/chart/ext/ciq/NSE/MASTEK/543745",
"https://kite.zerodha.com/chart/ext/ciq/NSE/MGL/4488705",
"https://kite.zerodha.com/chart/ext/ciq/NSE/MINDACORP/6629633",
"https://kite.zerodha.com/chart/ext/ciq/NSE/MOREPENLAB/578305",
"https://kite.zerodha.com/chart/ext/ciq/NSE/NATCOPHARM/1003009",
"https://kite.zerodha.com/chart/ext/ciq/NSE/NCLIND/3709441",
"https://kite.zerodha.com/chart/ext/ciq/NSE/NMDC/3924993",
"https://kite.zerodha.com/chart/ext/ciq/NSE/NOCIL/625153",
"https://kite.zerodha.com/chart/ext/ciq/BSE/NUCLEUS/135989508",
"https://kite.zerodha.com/chart/ext/ciq/BSE/ONGC/128079876",
"https://kite.zerodha.com/chart/ext/ciq/BSE/ORIENTREF/136723460",
"https://kite.zerodha.com/chart/ext/ciq/BSE/PANACEABIO/136025348",
"https://kite.zerodha.com/chart/ext/ciq/BSE/PANAMAPET/134353924",
"https://kite.zerodha.com/chart/ext/ciq/BSE/PANCARBON/130288900",
"https://kite.zerodha.com/chart/ext/ciq/NSE/PARAGMILK/4385281",
"https://kite.zerodha.com/chart/ext/ciq/NSE/PHILIPCARB/678145",
"https://kite.zerodha.com/chart/ext/ciq/NSE/PNB/2730497",
"https://kite.zerodha.com/chart/ext/ciq/BSE/POLYCAB/138918916",
"https://kite.zerodha.com/chart/ext/ciq/NSE/RAIN/3926273",
"https://kite.zerodha.com/chart/ext/ciq/BSE/RELIANCE/128083204",
"https://kite.zerodha.com/chart/ext/ciq/NSE/SUVENPHAR/4593921",
"https://kite.zerodha.com/chart/ext/ciq/BSE/SUVEN/135741188",
"https://kite.zerodha.com/chart/ext/ciq/NSE/SUPPETRO/860161",
"https://kite.zerodha.com/chart/ext/ciq/NSE/SUNPHARMA/857857",
"https://kite.zerodha.com/chart/ext/ciq/NSE/STLTECH/2383105",
"https://kite.zerodha.com/chart/ext/ciq/BSE/STAR/136327940",
"https://kite.zerodha.com/chart/ext/ciq/NSE/SRIPIPES/3821313",
"https://kite.zerodha.com/chart/ext/ciq/NSE/SPICEJET/2930177",
"https://kite.zerodha.com/chart/ext/ciq/BSE/SONATSOFTW/136248580",
"https://kite.zerodha.com/chart/ext/ciq/BSE/SOLARA/138634244",
"https://kite.zerodha.com/chart/ext/ciq/BSE/SHILPAMED/135820548",
"https://kite.zerodha.com/chart/ext/ciq/BSE/SHBCLQ/131352836",
"https://kite.zerodha.com/chart/ext/ciq/BSE/SEQUENT/131207428",
"https://kite.zerodha.com/chart/ext/ciq/NSE/SBIN/779521",
"https://kite.zerodha.com/chart/ext/ciq/BSE/SBICARD/139024900",
"https://kite.zerodha.com/chart/ext/ciq/BSE/TCS/136330244",
"https://kite.zerodha.com/chart/ext/ciq/BSE/TATASTEEL/128120324",
"https://kite.zerodha.com/chart/ext/ciq/BSE/TATAMTRDVR/145920260",
"https://kite.zerodha.com/chart/ext/ciq/NSE/TATACONSUM/878593",
"https://kite.zerodha.com/chart/ext/ciq/NSE/TATACOFFEE/185345",
"https://kite.zerodha.com/chart/ext/ciq/NSE/TATACHEM/871681",
"https://kite.zerodha.com/chart/ext/ciq/NSE/TECHM/3465729",
"https://kite.zerodha.com/chart/ext/ciq/NSE/THYROCARE/4360193",
"https://kite.zerodha.com/chart/ext/ciq/NSE/TINPLATE/894209",
"https://kite.zerodha.com/chart/ext/ciq/NSE/TIRUMALCHM/894977",
"https://kite.zerodha.com/chart/ext/ciq/BSE/TORNTPHARM/128107524",
"https://kite.zerodha.com/chart/ext/ciq/BSE/TRENT/128064260",
"https://kite.zerodha.com/chart/ext/ciq/NSE/UJJIVAN/4369665",
"https://kite.zerodha.com/chart/ext/ciq/BSE/ULTRAMAR/129711364",
"https://kite.zerodha.com/chart/ext/ciq/NSE/UPL/2889473",
"https://kite.zerodha.com/chart/ext/ciq/BSE/VALIANTORG/138277124",
"https://kite.zerodha.com/chart/ext/ciq/BSE/VEDL/128075524",
"https://kite.zerodha.com/chart/ext/ciq/NSE/VINATIORGA/4445185",
"https://kite.zerodha.com/chart/ext/ciq/NSE/VINYLINDIA/4306177",
"https://kite.zerodha.com/chart/ext/ciq/NSE/VISAKAIND/1080577",
"https://kite.zerodha.com/chart/ext/ciq/NSE/VOLTAS/951809",
"https://kite.zerodha.com/chart/ext/ciq/NSE/WOCKPHARMA/1921537",
"https://kite.zerodha.com/chart/ext/ciq/NSE/XCHANGING/2996481",
"https://kite.zerodha.com/chart/ext/ciq/BSE/YESBANK/136357892",
"https://kite.zerodha.com/chart/ext/ciq/BSE/ZENSARTECH/129041156",
"https://kite.zerodha.com/chart/ext/ciq/NSE/ZENTEC/1922049",
"https://kite.zerodha.com/chart/ext/ciq/NSE/BALAMINES/3712257",
"https://kite.zerodha.com/chart/ext/ciq/NSE/SRF/837889"


]


for link in links:
  driver.get(link)
  time.sleep(5)

driver.close()

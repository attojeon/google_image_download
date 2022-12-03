
from google_images_download import google_images_download   #importing the library

# 키워드 구분은 쉼표(,)로 함
# 쉼표 다음에 공간이 있으면 안됨 => 폴더생성 에러 발생함
keywords = "워너원 강다니엘,엑소 백현,박보검,송중기," 
keywords += "워너원 황민현,엑소 시우민,강동원,이종석,이준기,"
keywords += "마동석,조진웅,조세호,안재홍,"
keywords += "조진웅,조세호,안재홍,"
keywords += "윤두준,이민기,김우빈,육성재,공유,"
keywords += "방탄소년단 정국,아이콘 바비,워너원 박지훈,엑소 수호"
arguments = {
            "keywords": keywords,
            "limit": 100,
            "color": "green",
            "print_urls": True,
            "format": "jpg" 
        }


response = google_images_download.googleimagesdownload()   #class instantiation
# arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}
paths = response.download(arguments)  
print(paths)
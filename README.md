# 2022/12/9일 현재 정상적으로 동작하지 않음. 
  - 라이브러리 nonetype 에러 발생함. 
  - bing이미지다운로드 모듈로 교체 https://pypi.org/project/bing-image-downloader/

  
# 구글의 이미지 검색 후 자동 다운로드 하기
  - 구글이미지 다운로드는 구글의 정책상 오랫동안 제대로 작동하기가 어려움
  - 2022년 12월 현재, 아래의 git의 소스를 사용하는 것은 정상적으로 작동하는 버전임.

# 이 모듈을 사용하는 목적
  - 인공지능 연습을 위해 라벨링된 이미지가 필요할 경우 가장 쉽게 라벨링과 이미지를 수집할 수 있다. 
  - 저작권이 없는 점을 반드시 명심!
  

## google_images_download 사용시 에러가 발생할 때
* 2022.05.10 현재, 
* google_images_download 패키지 이용시 에러 발생
* url: git clone https://github.com/hardikvasa/google-images-download.git
​
### 해결 방법
1. 기존에 설치한 패키지 삭제
```bash
$ pip uninstall google_images_download
```
​

2. 아래의 명령으로 수정된 패키지 설치
``` bash
$ pip install git+https://github.com/Joeclinton1/google-images-download.git
```

 
3. 재실행 (기존 소스코드 변경할 필요 없으나, 다운로드는 100개까지만 가능함)

``` python
from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()

arguments = {"keywords":"고양이","limit":20,"print_urls":True}
paths = response.download(arguments)
print(paths)  
```  

3.1 확장자 지정 예제
``` python 
from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()

arguments = {"keywords":"boracay","limit":100,"print_urls":True,"format":"jpg"}
paths = response.download(arguments)
print(paths)
```
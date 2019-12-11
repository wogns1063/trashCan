# 자동화 테이크아웃 컵 분리수거함(Smart Recycling Bin)

딥러닝 기술과 하드웨어를 접목하여 테이크아웃 컵을 자동으로 분리 해주는 수거함을 제안한다. 커피 전문점을 이용하는 소비자가 증가함에 따라 테이크아웃 컵 쓰레기양 또한 증가하는 추세이다. 정부는 테이크아웃 컵 전용 쓰레기 수거함을 도입했지만, 목적과는 다르게 그 이외의 쓰레기들이 투기되고, 컵 안에 잔존하는 액체로 인해 제대로 분리수거가 이루어지지 않는 실상이다. 또한 길거리에 버려진 테이크아웃 컵들은 도시의 미관을 해칠 뿐만 아니라, 수거 과정에도 어려움을 겪게 한다. 이에 따라 제안하는 시스템은 카페를 이용하는 소비자의 편의성 제고 및 업체의 번거로움을 줄여주고 최근 화두 되는 환경적 문제에도 긍정적 영향이 미칠 것으로 기대된다.  

# 설정

## 1. 라즈베리 파이 (Raspberry Pi)

### 1.1 라즈베리파이란?
![라즈베리](https://user-images.githubusercontent.com/48484193/70628534-aa274480-1c6b-11ea-887d-cc14f659e960.PNG)

라즈베리파이는 초소형, 초저가 싱글 보드 컴퓨터(single-board computer)이다.
일반 컴퓨터와 달리 외부 회로나 기기를 직접 제어할 수 있도록 GPIO(General Purpose Input Output, 범용 입출력) 포트를 갖고 있다.
크기는 대략 신용카드 크기이며, 가격도 $35로서 일반 PC의 1/10 이하로 아주 저렴한 편이다.

라즈베리파이의 활용도는 매우 높다.
> 활용예시
- 인터넷 서핑
- 워드프로세서와 스프레드쉬트 작업
- 사진 편집
- 음악, 비디오 재생
- 로봇 제작
- 프로그래밍
- GPIO를 통한 회로 연결
- 감시 카메라 시스템

### 1.2 라즈베리파이3 주요부 명칭

![캡처15](https://user-images.githubusercontent.com/48484193/70630391-d8f2ea00-1c6e-11ea-84f8-08bfd5751790.PNG) [그림1]

### 1.3 라즈베리파이 연결하기

| 번호 | 품명 | 모양 |
|:------|:------|:------
1 | Raspberry Pi 3 | [그림1] 참고
2 | micro SD 메모리 카드(Class 10, 16GB 이상 권장) 및 리더 | ![캡처16](https://user-images.githubusercontent.com/48484193/70631750-02147a00-1c71-11ea-8fc1-13df64141973.PNG)
3 | USB 충전 어댑터(5V에서 2.5A 이상) 및 micro USB 케이블 | ![캡처17](https://user-images.githubusercontent.com/48484193/70631920-4142cb00-1c71-11ea-94f9-ab8e4dee2aa8.PNG)
4 | USB 키보드 및 마우스 | (범용)
5 | 디스플레이(TV or 모니터) | HDMI 또는 DVI 단자 있는 것
6 | HDMI 케이블 | ![캡처18](https://user-images.githubusercontent.com/48484193/70634484-a698bb00-1c75-11ea-9798-800b76f0a2f5.PNG)
7 |이더넷케이블(랜선) 또는 WiFi 동글 | ![캡처19](https://user-images.githubusercontent.com/48484193/70634650-eeb7dd80-1c75-11ea-9404-a7aef8498a38.PNG)
[표1]

### 1.4 라즈베리파이 기본 연결

![캡처20](https://user-images.githubusercontent.com/48484193/70635226-e90ec780-1c76-11ea-8e25-a8081bc24d9a.PNG)
[표1]의 구성품을 가지고 그림과 같이 연결한다.
<br>

## 2. OpenCV 

### 2.1 OpenCV란?
![OpenCV](https://user-images.githubusercontent.com/48484193/70624096-df7b6480-1c62-11ea-9fda-ce191593a90e.PNG) 
<br>
[사진출처] <https://ko.wikipedia.org/wiki/OpenCV>

실시간 컴퓨터 비전을 목적으로 실시간 이미지 프로세싱에 중점을 둔 라이브러리이다.
Windows, Linux, Android, iOS에서 사용할 수 있다.
비교적 최신 기술이 구현되어 있기 대문에 비전문가도 전문가 수준의 영상/동영상 처리 프로젝트를 수행할 수 있게 해준다.

> 응용 기술의 예
- 인간과 컴퓨터 상호 작용 
- 물체 인식
- 안면 인식
- 제스처 인식

> 프로그래밍 언어

C/C++ 프로그래밍 언어로 개발 되었으며 Python, Java 및 MATLAB에서 프로그래머에게 개발 환경을 지원한다.

### 2.2 설치방법
 **※ 설치전 주의사항**
- OpenCV를 설치하기 위해 16GB의 microSD가 필요하다.
- 라즈비안을 설치한 SD카드가 16GB 이상이면 된다.
- **기존에 OpenCV가 있다면 새로 설치할 OpenCV가 제대로 동작하지 않기 때문에 이전 버전 삭제 후 진행한다.**


아래의 주소로 들어가 진행하면 설치를 완료할 수 있다.
<br>
<https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/>

<br/>

## 3. PiCam
(a) 8M 화소 PiCam
<br>

![파이캠1](https://user-images.githubusercontent.com/48484193/70625573-06876580-1c66-11ea-8ac2-d52b95f74604.PNG)

### 3.1 PiCam 장착을 위한 라즈베리 파이 준비
1\) PiCam을 연결하지 않은 상태에서 Pi에 전원을 공급한다.
2\) 터미널 프롬프트에서 소프트웨어를 업그레이드 한다.
```shell
$ sudo apt-get update && sudo apt-get upgrade -y
```
3\) 설정 화면으로 들어간다.
```shell
$ sudo raspi-config
```
4\) "Enable Camera" 옵션으로 이동해서 선택하고, ENTER를 누른다. (방향키로 이동한다.)
![파이캠4](https://user-images.githubusercontent.com/48484193/70626728-4d765a80-1c68-11ea-89c9-aa582e74e046.PNG)

5\) 대화상자에서 "Enable support for Raspberry Pi camera?" 질문에 대해 Tab키로 Enable을 선택하고 Enter키를 누른다.
![파이캠5](https://user-images.githubusercontent.com/48484193/70626965-b52ca580-1c68-11ea-9d74-92cf3500a851.PNG)

6\) Raspi-Config 유틸리티를 빠져 나와서 Pi를 리부트한다.
```shell
$ sudo shutdown -r now
```
7\) 리부트에서 돌아오면, PiCam 장착 준비를 위해 시스템을 셧다운한다.
```shell
$ sudo shutdown -h now
```

### 3.2 PiCam 장착하기
**※ 취급시 주의사항**
- 전력 소모는 100mA @ 1.5V 이다.
- PiCam은 정전기에 민감하기 때문에 취급 전에 PC의 금속 케이스 같은 것들을 만져서 몸을 접지시키도록 한다.
- 설치 시 CSI 커넥터에 무리한 힘을 가하지 않도록 한다.
- 리본 케이블이 비틀리지 않도록 주의한다.
- 렌즈 부를 만지지 않도록 한다.

(a) PiCam 연결 커넥터(CSI) 위치
카메라  전용 인터페이스로 설계된 CSI-2(camera serial interface 2) 카메라 커넥터로 Pi에 연결된다.
![파이캠2](https://user-images.githubusercontent.com/48484193/70625801-89102500-1c66-11ea-8771-840bd0f6897a.PNG)   ![파이캠3](https://user-images.githubusercontent.com/48484193/70626358-9c6fc000-1c67-11ea-8c22-b4a670968b2f.PNG =440x)
[사진출처] <https://kocoafab.cc/tutorial/view/334>

(b) 고정 클립을 들어 올리고 CSI-2 인터페이스에 리본 케이블 끼우기
![파이캠6](https://user-images.githubusercontent.com/48484193/70627389-8105b480-1c69-11ea-9328-006829a8b0f1.PNG)![파이캠7](https://user-images.githubusercontent.com/48484193/70627480-a1357380-1c69-11ea-84dc-11342cec00bb.PNG =210x)
이 과정을 완료하면 전원을 연결한다.

### 3.3 PiCam 테스트
다음 명령으로 PiCam을 테스트할 수 있다.
```shell
$ raspistill -k
```
[x + Enter]키를 누르면 프리뷰가 꺼진다. (``` $ pkill raspistill ``` 또는 [Ctrl + c])

SSH나 VNC로 연결되어 있는 원격 모니터에는 카메라 화면이 보이지 않는다.
단, 실행은 되므로 서버의 모니터에서는 볼 수 있다.
```shell
$ brew update
$ brew install fvcproductions
```

# 소프트웨어

## 4. 딥러닝(Deep Learning) 모델 - Tiny YOLOv3

물체 탐지로 사용되는 YOLO 알고리즘은 You Only Look Once의 약자이다.

### 4.1.1 How It Works?
이전 탐지 시스템은 classifier나 localizer를 사용해 탐지를 수행한다.
하지만 YOLO는 하나의 신경망을 전체 이미지에 적용한다. 
이 신경망은 이미지를 영역으로 분할하고 각 영역의 Bounding Box와 확률을 예측한다.
이런 Bounding Box는 예측된 확률에 의해 가중치가 적용된다.

### 4.1.2 Advantage
- 테스트할 때 이미지의 전체를 보고 예측 정보를 알려준다.
- 수천개의 이미지가 필요한 R-CNN과 달리 하나의 네트워크 평가로 예측할 수 있다.
- R-CNN보다는 1000배 이상 빠르고, Fast R-CNN보다는 100배 빠르다.
- 이미지로부터 bounding box와 class들을 동시에 찾아낸다.
 <img  src="https://user-images.githubusercontent.com/48309721/70613186-8b18ba80-1c4b-11ea-89bb-aec5189172a9.PNG">
 class confidence score = box confidence score X conditional class probability
___
- 다른 detection 모델과 비교할 때 M40과 TitanX와 같은 GPU를 사용하지만 YOLOv3는 성능 면에서 훨씬 빠르다.

<img  src="https://user-images.githubusercontent.com/48309721/70607152-46882180-1c41-11ea-8cb5-d18d1bf8f705.PNG"  width="466px">
<img  src="https://user-images.githubusercontent.com/48309721/70607155-46882180-1c41-11ea-8e7f-d004bb5797b8.PNG"  width="450px">
<img  src="https://user-images.githubusercontent.com/48309721/70607154-46882180-1c41-11ea-83dd-73f57a13d622.PNG"  height="260px">

- 평균 AP metric 관점에서 SSDvariants와 동등하지만 3배 더 빠르고 다른 것들과 비교해 했을 때는 뒤쳐진다.
하지만 차트의 AP50에서 검출 메트릭의 mAP를 볼 때 YOLOv3가 RetinaNet과 동등하며 SSD보다 위에 있다. 이것은 YOLOv3가 물체에 대한 적절한 상자를 만드는 데 뛰어난 탐지기임을 나타낸다.
-   AP50 metric에서 정확도와 속도를 생각해 볼 때 더 빠르다는 점에서 다른 탐지 시스템에 비해 상당한 이점이 있다.
- 
___
- 이전 버전에서는 Darknet-19네트워크를 사용했지만 YOLOv3부터 53개의 컨볼루션 레이어가 있는 다크넷-53 네트워크를 이용하여 특징 추출을 수행한다.
- 이 네트워크는 연속적인 3X3 과 1X1 컨볼루션 레이어를 사용한다.
<img  src="https://user-images.githubusercontent.com/48309721/70607153-46882180-1c41-11ea-9202-82bf1e26160d.PNG">
 
- 이 새로운 네트워크는 Darknet-19보다 훨씬 강렬하지만 ResNet-101 또는 ResNet-152보다 훨씬 효율적이다.
<img  src="https://user-images.githubusercontent.com/48309721/70609652-805b2700-1c45-11ea-8419-1285bfbbffda.PNG" width="450">

___
<img  src="https://user-images.githubusercontent.com/48309721/70607156-4720b800-1c41-11ea-9c02-6fa766d43d38.PNG"  width="400px">
<img  src="https://user-images.githubusercontent.com/48309721/70607265-720b0c00-1c41-11ea-9557-faa1d4da9740.PNG"  width="420px">

- mAP50에서 YOLOv3는 다른 탐지 시스템에 비해 Execution time은 빠르고 FPS는 크다는 것을 알 수 있다.

## 4.2 Selenium Library를 활용한 image Crawling
machine learning을 학습하기 전 학습할 이미지를 Selenium, Chromedriver를 사용하여 수집한다.

### 4.2.1 anaconda prompt설치

[아나콘다 프롬프트 설치](https://www.anaconda.com/distribution/)
위 링크로 들어가 자신의 버전에 맞게 아나콘다 프롬프트를 설치한다.

### 4.2.2 Jupyter
anaconda prompt를 실행하고 jupyter notebook을 입력하면 jupyter가 실행된다.
```shell
> jupyter notebook
```
<img  src="https://user-images.githubusercontent.com/48309721/70628346-54529c80-1c6b-11ea-8c2b-579db2dd9cc4.PNG">
<img  src="https://user-images.githubusercontent.com/48309721/70628648-df339700-1c6b-11ea-8874-8c6a50a4ad44.PNG"  width="700px">

## Selenium Library
- selenium 이란 브라우저 자동화, 크롤링과 관련된 라이브러리이다. 보통 Explorer의 경우 DOM 이라는 것을 통해 제어할 수 있지만, chrome이나 Firefox같은 경우 웹드라이버를 따로 지원해줘서 selenium을 통해 제어가 가능하다.
- 간단한 웹 접속, 스크롤하는것 부터 웹사이트 로그인, 버튼 누르기, 특정 하이퍼링크 누르기 등의 기능으로 크롤링(Crawling)이나 웹 매크로(Macro)등 다양한 작업을 할 수 있다.

  

### 4.2.3 Selenium 설치
pip 명령어를 이용해서 python에 selenium을 설치해 준다.
```
> pip install selenium
```

<img  src="https://user-images.githubusercontent.com/48309721/70629037-a21bd480-1c6c-11ea-928c-630f8edb1218.PNG"><br>

```shell
>>> import selenium
```
<img  src="https://user-images.githubusercontent.com/48309721/70629145-d4c5cd00-1c6c-11ea-99f6-ce1ee8fd2203.PNG">
그 다음, python을 실행하고 정상적으로 설치가 되었는지 확인하기 위해 import selenium을 입력해본다.<br>
오류가 나지 않으면 정상적으로 설치된 것이다.

### 4.2.4 크롬드라이버(Chrome Driver) 설치
다음으로, 크롬드라이버를 설치한다.

설치되어있는 크롬 버전에 맞게 크롬드라이버를 설치해야하기 때문에 크롬 버전을 확인하기 위해
오른쪽 위의 메뉴 → 도움말 → chrome 정보에 들어간다.
<img  src="https://user-images.githubusercontent.com/48309721/70629506-72210100-1c6d-11ea-914b-be10be037954.PNG">
위와 같이 크롬의 버전을 확인한다.

크롬 드라이버 정식 사이트에 들어간다. http://chromedriver.chromium.org/
Downloads에서 동일한 버전을 선택하고 윈도우를 선택해서 다운받으면 된다.

다운받은 파일은 다음과 같이 C드라이브에 압축을 푼다.
<img  src="https://user-images.githubusercontent.com/48309721/70630165-76015300-1c6e-11ea-8d14-61052e219cb0.PNG">

### 4.2.5 코드
개발환경: Jupyter-notebook
> 코드 1
```python
# 밑으로 홈페이지를 내렷을 때 정보가 나오는 경우 selenium 사용
#!pip install selenium

from selenium import webdriver
import os
import time

#찾고자 하는 검색어를 url로 만들어 준다.
searchterm = 'take out cup'
url = "https://www.google.com/search?q=take+out+cup&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjI_9S9tK3mAhXKIqYKHcbFAsYQ_AUoAXoECAoQAw&biw=958&bih=878"

#chrome webdriver 사용하여 브라우저를 실행
browser = webdriver.Chrome("C:/chromedriver.exe")
browser.get(url)
```
1. 변수 searchterm에 찾고자 하는 검색어를 입력해준다.
2. 변수 url에 검색어를 입력하고 이미지를 클릭했을 때의 url주소를 넣어준다.
3.  chrome webdriver 사용하여 chrome 브라우저가 자동으로 실행된다.

<img  src="https://user-images.githubusercontent.com/48309721/70614750-6d992000-1c4e-11ea-9b47-5f23466d61aa.PNG" width="700">

![딥러닝](https://user-images.githubusercontent.com/41332126/70641459-ffba1c00-1c80-11ea-9db9-60f8d3d4fd90.gif =700x)
<br>
> 코드 2
```python
# 검색 결과를 늘리기 위하여 스크롤 다운
for _ in range(10):
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(5)

# 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.
# (이미지 저장 폴더를 위해)
if not os.path.exists(searchterm):
	os.mkdir(searchterm)
	
succounter = 0	#현재 수집된 이미지 수를 나타내는 변수

#class name 이 THL인 요소를 모두 가지고 온다.
img_list = browser.find_elements_by_class_name('THL2l')
for idx, x in enumerate(img_list):
	try:
		save_path = os.path.join(searchterm, str(idx)+".png")
		x.screenshot(save_path)	    #이미지 저장
		succounter = succounter + 1
		ranning_test = "ranning: " +str(succounter)+"/" +str(len(img_list))
		print(ranning_test)
	except:
		print("can't get img")

print(succounter, "succesfully download")
```
1. chrome브라우저가 실행된 후 스크롤 다운 코드를 적용하여 자동으로 스크롤바를 내려가며 이미지를 저장할 수 있도록 해준다.
2. 보여지는 페이지에서 이미지 파일을 저장하기 위해 해당 사이트의 태그를 분석해야 한다.
3. 키보드의 [F12]키를 누르거나 브라우저 오른쪽 상단의 [메뉴→도구더보기→개발자 도구]를 클릭하여 이미지 부분에 해당하는 클래스명을 확인한다.

![딥러닝1](https://user-images.githubusercontent.com/41332126/70642905-6cceb100-1c83-11ea-85a8-32ab2caff919.png)

4. 이미지를 'searchterm'과 동일한 폴더에 저장한다. 이때 폴더가 존재하지 않으면 자동으로 생성한다.

### 4.2.6 결과
이미지가 폴더에 다음과 같이 저장된다.

<img  src="https://user-images.githubusercontent.com/48309721/70631810-18bad100-1c71-11ea-8fb4-cedf795021d7.PNG" width="700">
<img  src="https://user-images.githubusercontent.com/48309721/70632432-27ee4e80-1c72-11ea-839a-828f39dfe239.PNG" width="700">

## 4.3 Tiny YOLOv3 학습 환경

### 4.3.1.  **적용 모델 컴퓨터 사양**
1.1 OS : Windows 10 Home
1.2 GPU : GeForce-1080Ti
1.3 CPU : intel(R) Core(TM) i7-7700K
1.4 RAM : 32GB
1.5 시스템 종류 : 64비트 운영체제, x64 기반 프로세서

### 4.3.2  **학습에 필요한 프로그램 설치**
2.1 MS Visual Studio 2015(v140) : https://go.microsoft.com/fwlink/?LinkId=532606&clcid=0x409
2.2 CUDA 9.1 : https://developer.nvidia.com/cuda-91-download-archive
2.3 cuDNN 7.0 : https://developer.nvidia.com/cudnn
2.4 OpenCV 3.3.0 : https://sourceforge.net/projects/opencvlibrary/files/opencv-win/3.3.0/opencv-3.3.0-vc14.exe/download
<br>

### 4.3.3.  **설치 파일 경로 (PATH)**
3.1 OpenCV 경로
<img src = "https://user-images.githubusercontent.com/48505947/70606273-73d3d000-1c3f-11ea-93c4-84cd3a7328f7.png" width = "800px" ></img>

3.2 Visual Studio 경로
<img src = "https://user-images.githubusercontent.com/48505947/70606661-4fc4be80-1c40-11ea-9a5a-7590ed9e88ba.png" width = "800px"></img>

3.3 CUDA 경로
<img src = "https://user-images.githubusercontent.com/48505947/70606732-74b93180-1c40-11ea-9e64-376e20894e96.png" width = "800px"></img>

### 4.3.4.  **install YOLO-Marker, darknet from git**
4.1 Git Bash Run
<img  src = "https://user-images.githubusercontent.com/48505947/70607119-36704200-1c41-11ea-977a-f9e45ccd6927.PNG"  width = "550px"></img>

4.2 Command
	```shell
	$ mkdir /c/yolo
	$ cd /c/yolo
	$ git clone https://github.com/AlexeyAB/darknet.git
	$ git clone https://github.com/AlexeyAB/Yolo_mark.git
	```
	
4.3 Result
<img  src = "https://user-images.githubusercontent.com/48505947/70607600-15f4b780-1c42-11ea-89cc-c325a5035320.png"  width = "800px" ></img>
4.4 Insert Image Data
<img  src = "https://user-images.githubusercontent.com/48505947/70608238-222d4480-1c43-11ea-834e-53138bcdb1b2.png"  width = "650px"  height="500px"></img>

## 4.4 윈도우 환경에서 Tiny YOLOv3 모델 이미지 학습

### 4.4.1.  **Data Labeling - YOLO Marker**
1.1. Run yolo_mark.sln
- Open C:\yolo\Yolo_mark
- Run yolo_mark.sln
<img  src = "https://user-images.githubusercontent.com/48505947/70608888-42113800-1c44-11ea-8a04-35fa3128bc1a.png"  height="280px"></img>

1.2. **yolo_mark Project Properties 수정 및 Yolo_mark.sln Build**
- Debug, x64 => Release, x64 로 변경
<img  src = "https://user-images.githubusercontent.com/48505947/70609710-9b2d9b80-1c45-11ea-9ace-b9c9f1486aac.png"   height="250px"></img>
- yolo_mark -> Project -> Properties 클릭
<img  src = "https://user-images.githubusercontent.com/48505947/70610140-61a96000-1c46-11ea-96da-812bc7f6c6c4.png"  width = "640px"  height="350px"></img>
- yolo_mark Property Pages
	(1) Configuration : Active(Release), Platform : Active(x64)
	
	(2) VC++ Directories
	- Include Directories : C:\opencv\build\include;
	- Library Directories : C:\opencv\build\x64\vc14\lib;
	
	(3) C/C++ -> General
	- Additional Include Directories : C:\opencv\build\include;
	
	(4) Linker -> General
	- Additional Library Directories : C:\opencv\build\x64\vc14\lib;
		
	(5) Linker -> Input
	- Additional Dependencies : opencv_world330.lib;opencv_world330d.lib
	- 컴파일시 OpenCV Library 를 사용하기 위해 설정.
<img  src = "https://user-images.githubusercontent.com/48505947/70619739-fae17200-1c58-11ea-849d-abee63197aea.png"  width = "700px"  height="550px"></img>

- Yolo_mark.sln Build (ctrl+shift+B)
(1) cd opencv build x64 vc14 bin
(2) cp opencv_world330.dll, opencv_world330d.dll c:\/yolo/Yolo_mark/x64/Realease
(3) cd c:/yolo/Yolo_mark/x64/Realease/data/img
			- 해당 파일 샘플 이미지 모두 삭제(Delete all example image)
			- 학습시키려는 이미지 모두 추가(Insert all image)
(4) cd c:/yolo/Yolo_mark/x64/Release
(5) Yolo_mark.cmd run
<img  src = "https://user-images.githubusercontent.com/48505947/70613853-bbad2400-1c4c-11ea-9252-dd21fefc9c1e.png"   height="350px"></img>

1.3. Image Labeling

마우스로 사진의 좌표를 잡아준다.
<img  src = "https://user-images.githubusercontent.com/48505947/70614373-c4eac080-1c4d-11ea-9957-18a8dc77721e.PNG"  width = "600x"  height="500px"></img>

메모장에는 4꼭지점의 좌표로 저장된다.
<img  src = "https://user-images.githubusercontent.com/48505947/70614456-f4013200-1c4d-11ea-98e0-777a6e6a48f5.PNG"  height="130px"></img>
<img  src = "https://user-images.githubusercontent.com/48505947/70614552-1430f100-1c4e-11ea-8196-5ea401248d5a.PNG"  width = "800px" ></img>

C:\yolo\Yolo_mark\x64\Release\data 이동
<img  src = "https://user-images.githubusercontent.com/48505947/70615181-47c04b00-1c4f-11ea-988f-93f6b1684162.PNG"  height="150px"></img>

obj.names 는 Class Name을 입력 (ex. take out cup을 Detecting 하기 위하여 Class Name을 take-out-cup으로 설정)
obj.data는 Classes 갯수를 설정 (ex. take-out-cup Class 1개 이기 때문에 1로 설정)
<img  src = "https://user-images.githubusercontent.com/48505947/70615257-6b839100-1c4f-11ea-953f-e1d4d059c02a.png"  height="170px"></img>

Labeling 된 image의 경로는 train.txt에 자동 저장됨.
<img  src = "https://user-images.githubusercontent.com/48505947/70615373-9a9a0280-1c4f-11ea-9cda-3834c061f691.PNG"  width = "230px" ></img>
<br>

### 4.4.2  **Set Model (Image Data 학습)**
2.1 Darknet 네트워크 환경 설정
- Open C:\yolo\darknet\build\darknet
- Run darknet.vcxproj
- CUDA 버전 default인 10.0을 9.1로 변경(line 55, 306)
<img  src = "https://user-images.githubusercontent.com/48505947/70622364-20717a00-1c5f-11ea-81e6-316d75ebf1a0.png"  width = "500px"  height="400px"></img>
<img  src = "https://user-images.githubusercontent.com/48505947/70622394-3121f000-1c5f-11ea-8f56-51f0ca1f5f28.png"  width = "580px"  height="400px"></img>

2.2 darknet Properties 변경
- Open C:\yolo\darknet\build\darknet
- Run darknet.sln
<img  src = "https://user-images.githubusercontent.com/48505947/70622828-1a2fcd80-1c60-11ea-89c5-da038237ec75.png"  height="350px"></img>

- darknet -> Project -> Properties 클릭
<img  src = "https://user-images.githubusercontent.com/48505947/70623058-8d394400-1c60-11ea-85fa-4b23d7293bdf.png"  width = "650px"  height="400px"></img>

- darknet Property Pages
(1) C/C++ -> General
	- Additional Include Directories : C:\opencv\build\include;C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\include

	(2) CUDA C/C++ -> Device
	- Code Generation : Delete all content

	(3) Linker -> General
	- Additional Library Directories : C:\opencv\build\x64\vc14\lib;C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\lib\x64
	- 컴파일시 openCV, CUDA library를 사용하기 위해 설정
	<img  src = "https://user-images.githubusercontent.com/48505947/70624073-ce325800-1c62-11ea-8e18-fc32a0025baa.png"  width = "650px" ></img>

	- darknet.sln Build (ctrl+shift+B)
(1) cd C:\opencv\build\x64\vc14\bin
(2) cp opencv_world330.dll C:\yolo\darknet\build\darknet\x64
(3) cd C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\bin
(4) cp cudnn64_7.dll C:\yolo\darknet\build\darknet\x64
(5) cd C:\yolo\darknet\cfg
(6) yolov3 tiny_obj.cfg C:\yolo\darknet\build\darknet\x64
		- Darknet 네트워크를 실행시키기 위해 dll(동적 연결 library) 를 참조하기 위해 실행 폴더에 집어 넣는다.
		- 네트워크 환경 설정이 되어있는 cfg 파일 역시 실행 폴더로 가져온다.

2.3 Labeling 한 파일 darknet으로 이동
C:\yolo\Yolo_mark\x64\Release\data 경로에 Labeling 과정을 마친 
파일들을 불러와 C:\yolo\darknet\build\darknet\x64\data에 붙여넣는다.
<img  src = "https://user-images.githubusercontent.com/48505947/70625270-6df0e580-1c65-11ea-9817-5c0b7dd55f8f.png"  width = "950px"  height="450px"></img>

2.4 이미지 학습을 위한 세팅
```shell
> cd C:\yolo\darknet\build\darknet\x64\cfg
> Run yolov3-tiny.cfg
```
(line 3) → batch=64 로 변경
(line 4) → subdivisions=8 로 변경
(line 135, 177) → classes=1 로 변경(Class의 수)
(line 127,171) → filters=18 로 변경(class의 수 + 5) * 3 = 18

<img  src = "https://user-images.githubusercontent.com/48505947/70627290-4e5bbc00-1c69-11ea-85a3-aa61fa3f89cf.png"  width = "900px"  height="500px"></img>

- 학습에 필요한 (Pretrained Weight)가중치 파일 yolov3-tiny.weights 다운받기 https://pjreddie.com/media/files/yolov3-tiny.weights
- C:\yolo\darknet\build\darknet\x64 경로에 yolov3-tiny.weights 파일 옮기기
<img  src = "https://user-images.githubusercontent.com/48505947/70627796-32a4e580-1c6a-11ea-8f05-2bad4fe725c0.png"  width = "650px" height="300"></img>

- 아래 명령어를 실행하여 weight를 추출
	```shell
	> .\darknet.exe partial cfg/yolov3-tiny.cfg yolov3-tiny.weights yolov3-tiny.conv.15 15
	```
	<img  src = "https://user-images.githubusercontent.com/48505947/70628171-00e04e80-1c6b-11ea-95b0-357174d142b2.png"  height="180px"></img>

- 생성된 weight, Convolution 및 학습하려는 클래스에 맞게 설정한 yolov3-tiny.cfg, labeling 한 데이터의 정보가 담긴 obj.data 파일을 기반으로 학습 시작
	```shell
	> .\darknet.exe detector train data/obj.data cfg/yolov3-tiny.cfg yolov3-tiny.conv.15
	```
	

2.5 이미지 학습 결과
- 그래프
<img  src = "https://user-images.githubusercontent.com/48505947/70630131-6550dd00-1c6e-11ea-8d3c-a7ed3409e30c.PNG"  width = "350px" ></img>

- 이미지 테스트
```shell
> cd C:\yolo\darknet\build\darknet\x64
> ./darknet detector test data/obj.data cfg/yolov3-tiny.cfg backup/yolov3-tiny_last.weights data/cuptest.jpg
```
<img  src = "https://user-images.githubusercontent.com/48505947/70633330-badbb880-1c73-11ea-90b2-51733a1bb6bd.png"  height="450px"></img>

- 동영상 테스트
```shell
> cd C:\yolo\darknet\build\darknet\x64
> ./darknet detector demo data/obj.data cfg/yolov3-tiny.cfg backup/yolov3-tiny_last.weights
```
![실시간사물인식](https://user-images.githubusercontent.com/48505947/70638878-f929a580-1c7c-11ea-860e-6461a67f169b.gif)
참고한 사이트(https://pjreddie.com/darknet/yolo/)
<br>

### 4.4.3  **Raspberry PI에 Tiny YOLOv3 적용하기**
3.1 Python Script의 구성
- Tiny YOLOv3 학습된 model(weight)와 네트워크(cfg) 파일을 사용
- openCV에 결합, 동영상을 Frame 단위로 분활하여 객체 탐지
- 실시간 물체 감지를 통해 해당 물체가 감지되면 쓰레기통 문을 열어준다.
- Tiny YOLOv3 적용 파일 위치 : (/home/pi/yolo/video/object_detection_yolo.py)
- 테이크 아웃 컵을 감지하면 서보모터를 구동 파일 위치 : (/home/pi/yolo/video/servo.py)

3.2 필요한 라이브러리 및 패키지 import 과정, obj.names 파일 불러오기 및 변수 설정
```python
import cv2 as cv
from operator import eq
import argparse
import sys
import numpy as np
import os.path
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
from multiprocessing import Queue
from multiprocessing import Process
#import sysv_ipc #shared Memory
import time
import base64
from PIL import Image
from io import BytesIO

#Initialize the parameters
confThreshold = 0.5 #Confidence threshold
nmsThreshold = 0.4 #Non-maximum suppression threshold
inpWidth = 320 #416 #Width of network's input image
inpHeight = 320 #416 #Height of network's input image

# Load names of classes
classesFile = "/home/pi/yolo/video/obj.names";
classes = None
searchObj = None
imageByte = "basic"
with open(classesFile, 'rt') as f:
classes = f.read().rstrip('\n').split('\n')
```

3.3 서보모터 구동 파일에서 Class를 import하여 사용하기 위한 Class 구성 및 weight, cfg 설정
```python
def getSearchObj():
	return searchObj
	
def setSearchObj():
	global searchObj
	searchObj = None

class ObjectDetection_YOLO():
	def __init__(self,q):
		global imageByte
		
		modelConfiguration = "/home/pi/yolo/video/yolov3-tiny.cfg";
		modelWeights = "/home/pi/yolo/video/yolov3-tiny_last.weights";
		
		net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
		net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
		net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)
```
참고한 사이트(https://docs.opencv.org/3.4/d6/d0f/group__dnn.html)<br>
<img src = "https://user-images.githubusercontent.com/48505947/70639403-c6cc7800-1c7d-11ea-8cc7-18806afe87c5.PNG" width = "600px"></img>
<img src = "https://user-images.githubusercontent.com/48505947/70640010-a355fd00-1c7e-11ea-8dd1-2829bd748d3d.PNG" width = "600px" ></img>
<img src = "https://user-images.githubusercontent.com/48505947/70640318-1e1f1800-1c7f-11ea-8706-1f04381cafad.PNG" width = "600px" ></img>

3.4 Queue를 사용한 동영상 스트리밍
```python
inputQueue = Queue(maxsize=1)
outputQueue = Queue(maxsize=1)
detections = None

p = Process(target=self.classify_frame, args=(net, inputQueue, outputQueue,))
p.daemon = True
p.start()

vs = VideoStream(src=0).start()
time.sleep(2.0)

fps = FPS().start()
```
- Multi Processing을 사용할 때 데이터(Frame) 전송을 위해 Queue 사용.
- VideoStram을 통해 RaspCamera 동작 실행.
- 참고한 사이트(https://www.pyimagesearch.com/2017/10/16/raspberry-pi-deep-learning-object-detection-with-opencv/)

3.5 getOutputsNames 함수 설명
```python
# Get the names of the output layers
def getOutputsNames(self,net):

# Get the names of all the layers in the network
layersNames = net.getLayerNames()

# Get the names of the output layers, i.e. the layers with unconnected outputs
return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
```
output Layer에서 이름을 가져온다. (obj.names => take-out-cup)

3.6 classify_frame 함수 설명
```python
def classify_frame(self, net, inputQueue, outputQueue):
	while True:
		if not inputQueue.empty():
			frame = inputQueue.get()
			frame = cv.resize(frame, (300, 300))
			blob = cv.dnn.blobFromImage(frame, 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop=False)
			net.setInput(blob)
			detections = net.forward(self.getOutputsNames(net))
			outputQueue.put(detections)
```
- inputQueue에 frame이 포함되어 있으면 사이즈를 조절한다.
- 이미지를 blob 형식으로 변환 후 네트워크에 새로운 입력 값을 넣어준다.
- 네트워크에서 이름이 있는 Layer를 계산한 후 OutputQueue에 집어 넣는다.

3.7 postprocess 함수 설명
```python
def postprocess(self, frame, outs):
	frameHeight = frame.shape[0]
	frameWidth = frame.shape[1]

	classIds = []
	confidences = []
	boxes = []

	# Scan through all the bounding boxes output from the network and keep only the
	# ones with high confidence scores. Assign the box's class label as the class with the highest score.
	classIds = []
	confidences = []
	boxes = []

	for out in outs:
		for detection in out:
			scores = detection[5:]
			classId = np.argmax(scores)
			confidence = scores[classId]

			if confidence > confThreshold:
				center_x = int(detection[0] * frameWidth)
				center_y = int(detection[1] * frameHeight)
				width = int(detection[2] * frameWidth)
				height = int(detection[3] * frameHeight)
				left = int(center_x - width / 2)
				top = int(center_y - height / 2)

				classIds.append(classId)
				confidences.append(float(confidence))
				boxes.append([left, top, width, height])
```
object가 탐지될 때 보여줄 값을 배열화 감지된 object의 확률이 50% 이상이라면, classID(take-out-cup), 높이와 넓이, 사각형의 꼭지점 좌표를 반환후 배열에 저장

3.8 drawped 함수 설명
```python
def drawPred(self, frame ,classId, conf, left, top, right, bottom):

	# Draw a bounding box.
	cv.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)

	label = '%.2f' % conf

	global classes
	global searchObj

	if classes:
		label = '%s:%s' % (classes[classId], label)
		searchObj = classes[classId]

	if eq(searchObj, "take-out-cup"):
		labelSize, baseLine = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, 0.5, 1)
		top = max(top, labelSize[1])
		cv.rectangle(frame, (left, top - round(1.5*labelSize[1])), (left + round(1.5*labelSize[0]), top + baseLine), (255, 255, 255), cv.FILLED)
		cv.putText(frame, label, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 1)
```
만약 classes[classId]인 take-out-cup이 있다면 frame의 object에 labeling을 해준다.

3.9 결과
<img  src = "https://user-images.githubusercontent.com/48505947/70644206-e7003500-1c85-11ea-8eda-c3125944b999.jpg"  width = "300px"  height="250px"></img>
<br>

### 4.4.4 **서보모터 구동하기**
```python
import os
import threading
import object_detection_yolo as yolo
import time
import RPi.GPIO as GPIO

th_yolo = threading.Thread(target = yolo.ObjectDetection_YOLO, args=('r'))
th_yolo.start()

def Motor():
pin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.setwarnings(False)

p = GPIO.PWM(pin, 50)
p.start(0)
p.ChangeDutyCycle(12)

while True:
search = yolo.getSearchObj()

if (search == 'take-out-cup'):
	print(search)

	p.ChangeDutyCycle(7.5)
	time.sleep(10)
	p.ChangeDutyCycle(12)

	yolo.setSearchObj()
	th_Motor = threading.Thread(target = Motor, args=())
	th_Motor.start()
```
- Class화 한 object Detection 실행 및 모터 구동.
- 만약 classID인 take-out-cup이 감지되면 모터의 각도 변경.
<br>


---
# 하드웨어
## 5. 알고리즘
### 5.1 순서도
![순서도](https://user-images.githubusercontent.com/41332126/70551886-bc49aa00-1bbb-11ea-83e7-7e53ed05e08b.png)

### 5.2 회로도 & 코드
하단부와 상단부의 오프너 서브 모터(부품 3.), 조도 센서는 아두이노 우노 호환보드를 통해 제어한다.
이외의 상단부는 라즈베리파이로 제어한다.
> 아두이노

![아두이노1](https://user-images.githubusercontent.com/41332126/70627631-ec4f8680-1c69-11ea-9ce1-dbcb51250fca.jpg =450x) ![아두이노2](https://user-images.githubusercontent.com/41332126/70627637-efe30d80-1c69-11ea-881c-fb4ff8e7d40a.jpg =450x)

![아두이노 회로도](https://user-images.githubusercontent.com/41332126/70626055-050a6d00-1c67-11ea-8177-dadf31c9aafb.png)

> 라즈베리파이

![라즈베리파이1](https://user-images.githubusercontent.com/41332126/70628748-10ac6280-1c6c-11ea-95c8-6123a388d533.jpg =500x)

![라즈베리파이 회로도](https://user-images.githubusercontent.com/41332126/70626205-50bd1680-1c67-11ea-9223-4dcd36918da6.png)

<br>

- #### 모듈 가져오기(import)
```python
import RPi.GPIO as GPIO   #GPIO 제어를 위한 모듈 
from time import sleep
import threading    #별도의 쓰레드(Sub thread)를 생성하기 위한 모듈
import serial       #아두이노와 시리얼 통신을 하기위한 모듈
```
- #### GPIO.setup 
```python
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)   #핀 번호를 지정할 때 GPIO번호 참조

GPIO.setup(23, GPIO.IN)  #IR SENSOR Vout

openershaft = 19  #opener shaft
GPIO.setup(openershaf, GPIO.OUT)
OpenerShaft = GPIO.PWM(openershaft, 50)
OpenerShaft.start(0)

gripper = 16  #grippers
GPIO.setup(gripper, GPIO.OUT)
Gripper = GPIO.PWM(gripper, 50)
Gripper.start(0)
Gripper.ChangeDutyCycle(6)  #default value

leftshaft = 13  #left shaft
GPIO.setup(leftshaft, GPIO.OUT)
LeftShaft = GPIO.PWM(leftshaft, 50)
LeftShaft.start(0)

rightshaft = 18  #right shaft
GPIO.setup(rightshaft, GPIO.OUT)
RightShaft = GPIO.PWM(rightshaft, 50)
RightShaft.start(0)

complete = 0
```
- #### 시리얼 통신 ( 라즈베리파이 ↔ 아두이노 )
- > 아두이노
    ```c
    #include <Servo.h>

    Servo opener;
    Servo bottom;

    int cds = A0;
    int pos;

    void setup() {
        Serial.begin(9600);

        opener.attach(9);
        opener.write(60);

        bottom.attach(6);
        bottom.write(0);
    }
    ```
    시리얼 통신에서 초당 몇 비트의 속도로 통신을 할 지 설정해준다

    ```c
    void loop() {
        String c = Serial.readStringUntil('\n');

        if( c == "opener on" ){  // OPENER ON
            for (pos=60; pos<=250; pos+=1){
                opener.write(pos);
                delay(1);
            }
        }
        if( c == "return" ){  // OPENER return
            for (pos=250; pos>=60; pos-=1){
                opener.write(pos);
                delay(1);
            }
        }    
        if( c == "liquid" ){  // liquid
            bottom.write(0);
        }
        if( c == "paper" ) {  // paper
            bottom.write(90);
        }
        if( c == "plastic" ){  // plastic
            bottom.write(180); 
        }

        while( c == "ReadCdsVal" ) {   // read of sensor value
            int val = analogRead(cds);
            Serial.println(val);
            delay(1);

            String c = Serial.readStringUntil('\n');  
            if( c == "break" ) {
                break;
            }
        }
    }
    ```
    String 변수 c 에 시리얼 통신을 통해 들어오는 값을 저장한 후에<br>
    c 로 들어오는 값에 따라 서보모터를 작동하거나 조도센서 값을 받아온다.<br><br>

- >라즈베리파이

    ```python
    ser = serial.Serial('/dev/ttyACM0', 9600)  # serial communication setup
    ```
    설정을 통해 사용하는 아두이노의 포트와 통신 속도로 맞춰준다.

    >
    ```python
    『 arg = "opener on"
       ser.write(arg.encode()) 』
    ```
    
    arg 변수에 아두이노로 전달한 값을 넣어준 후에 바이트로 인코딩해서 넘겨준다.

    - #### thread 객체 상속
        파이썬 프로그램은 기본적으로 하나의 쓰레드(Single Thread)에서 실행된다. 즉, 하나의 메인 쓰레드가 파이썬 코드를 순차적으로 실행한다. 코드를 병렬로 실행 하기 위해서는 별도의 쓰레드(Sub thread)를 생성해야 하기 때문에 threading 모듈을 사용해야한다.

        서브 쓰레드는 함수 혹은 메서드를 실행하는데, 구현방식으로는 크게 두가지 방식이 있다. 쓰레드가 실행할 함수 혹은 메서드를 작성하거나 또는 threading.Thread로 부터 파생된 파생클래스를 작성하여 사용하는 방식이 있다. 아래 코드에서는 쓰레드를 원할 때 시작하고 종료시켜주기 위해 후자의 방식을 사용했다.
        ```python
        class IrSensor(threading.Thread):     #IRsensor thread class
            def __init__(self):
                threading.Thread.__init__(self)
                self.__exit = False

            def run(self):
                while True:
                    if self.__exit:
                        break
                    else:
                        val = GPIO.input(23)    #IRsensor value       
                        step1 (val)

            def myExit(self):   #exit thread
                self.__exit = True

        class PhotoResistor(threading.Thread):  #photoresistor thread class
            def __init__(self):
                threading.Thread.__init__(self) #생성자 재정의
                self.__exit = False

            #쓰레드에서 실제로 실행하는 메서드이며, self.__exit 을 확인한 후에 False 면 else문이 실행되고, True 면 thread 를 종료 시킨다. 
            def run(self):
                while True:
                    if self.__exit:
                        break      
                    else:
                        val = ser.readline()    # 아두이노로부터 조도 센서값을 받아온다.
                        Cdsval = int(val.decode('utf-8')) # 조도 센서값을 int로 형태 변환
                        step2(Cdsval) 

            def myExit(self):   #exit thread
                self.__exit = True
        ```

    - #### IR sensor로부터 값을 받아와 step1 메서드 실행
        ```python
        def step1(val): #val = GPIO.input(23) <= IRsensor value
            global complete

            Irval = val
            print(Irval)

            if Irval == 1:  #컵이 상단부에 들어오면
                th.myExit() #th = IrSensor() 감지 중단

                Gripper.ChangeDutyCycle(6)  #컵을 넣을 수 있도록 그리퍼를 벌려주고
                sleep(2)
                Gripper.ChangeDutyCycle(3)  #고정되도록 컵을 잡는다
                sleep(2)  

                # 1. 뚜껑(플라스틱)
                arg = "plastic"
                ser.write(arg.encode())
                sleep(1)

                OpenerShaft.ChangeDutyCycle(4)  #오프너축.컵쪽으로 회전
                sleep(2)

                arg = "opener on"
                ser.write(arg.encode()) #(아두이노)오프너 제어
                sleep(2)

                OpenerShaft.ChangeDutyCycle(8)  #오프너축.원위치
                sleep(2)

                arg = "return"
                ser.write(arg.encode())
                sleep(2)

                # 2. 음료(액체)
                arg = "liquid"
                ser.write(arg.encode())  #(아두이노)수거함 회전
                sleep(5)

                #컵 약 180˚회전해서 음료 버리고
                LeftShaft.ChangeDutyCycle(10)
                RightShaft.ChangeDutyCycle(4)
                sleep(5)
                # 원위치로 돌아오기
                LeftShaft.ChangeDutyCycle(1)
                RightShaft.ChangeDutyCycle(13)  

                complete = 1
        ```

    - #### 조도센서로부터 값을 받아와 step2 메서드 실행
        ```python
        def step2(val):  # val = ser.readline()
            global complete

            Cdsval = val
            print(Cdsval)
            
            th2.myExit()    #photoresistor thread exit

            # 3. 컵(플라스틱 or 종이)
            if Cdsval > 20: #플라스틱
                print('plastic cup')

                arg = "break"
                ser.write(arg.encode())
                sleep(1)

                Gripper.ChangeDutyCycle(3)
                sleep(1)

                arg = "plastic"
                ser.write(arg.encode()) #(아두이노)수거함 회전
                sleep(3)

                #컵 약 180˚회전해서 
                LeftShaft.ChangeDutyCycle(10)
                RightShaft.ChangeDutyCycle(4)
                sleep(2)

                #그리퍼 벌리고 컵 떨어뜨리기
                Gripper.ChangeDutyCycle(6)
                sleep(2)

                #그리퍼 원위치로 돌아오기
                LeftShaft.ChangeDutyCycle(1)
                RightShaft.ChangeDutyCycle(13)

                complete = 0

            elif Cdsval < 20:   #종이
                print('paper cup')      

                arg = "break"
                ser.write(arg.encode())
                sleep(1)

                Gripper.ChangeDutyCycle(3)
                sleep(1)

                arg = "paper"
                ser.write(arg.encode())
                sleep(3)

                LeftShaft.ChangeDutyCycle(10)
                RightShaft.ChangeDutyCycle(4)
                sleep(2)

                Gripper.ChangeDutyCycle(6)
                sleep(2)

                LeftShaft.ChangeDutyCycle(1)
                RightShaft.ChangeDutyCycle(13)

                arg = "liquid"
                ser.write(arg.encode())    

                complete = 0
        ```
        
    - #### 전체 동작 알고리즘
        ```python
        while True:
            #컵이 들어오는 동작 감지
            print('step1 start')
            th = IrSensor()
            th.start()  #step1() - 뚜껑 따기, 액체 버리기

            while True:
                if complete == 1 :  #step1() 동작이 성공적으로 완료되면 
                    print('step2 start')

                    arg = "ReadCdsVal"  #read cds val at arduino
                    ser.write(arg.encode())

                    th2 = PhotoResistor()
                    th2.start()   #PhotoResistor thread start - 컵 버리기
                    sleep(15)

                    break
        ```
<br/>

### 5.3 사용된 부품들
1. [![디지털 모션 센서](http://www.devicemart.co.kr/data/collect_img/kind_0/goods/large/38487.jpg =100x)](http://www.devicemart.co.kr/goods/view?no=38487) 디지털 적외선 모션 센서 [SEN0018] - 물체 동작 감지

2. [![조도 센서](http://www.devicemart.co.kr/data/collect_img/kind_0/goods/large/33235.jpg =100x)](http://www.devicemart.co.kr/goods/view?no=33235) CdS 20파이 조도센서 (GL20528) - 빛 투과율 감지

3. [![서보 모터](http://www.devicemart.co.kr/data/collect_img/kind_0/goods/large/1265392.jpg =100x)](http://www.devicemart.co.kr/goods/view?no=1265392) 최고급형 메탈 서보모터-DT2100 - 뚜껑 열기

4. [![서보 모터](http://robomecha.co.kr/web/product/big/robomecha_49.jpg =100x)](http://robomecha.co.kr/product/servo-motor-mts-a410se/49/) Servo Motor (MTS-A410SE) - 

5. [![서보 모터](http://www.devicemart.co.kr/data/collect_img/kind_0/goods/large/200803051448440.jpg =100x)](http://www.devicemart.co.kr/goods/view?no=11225) 서보모터(HS-311) - 그리퍼 제어, 그리퍼 회전, 수거함 회전

6. [![로봇팔](http://www.devicemart.co.kr/data/collect_img/kind_0/fogoods/large/1278810.jpg =100x)](http://www.devicemart.co.kr/goods/view?no=1278810) Standard Gripper Kit A (637094) [ROB-13174] - 컵 고정

7. [![서보 모터](https://user-images.githubusercontent.com/41332126/70533270-19356800-1b9c-11ea-89f4-d5958f5ed757.png =100x)](http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=822576342) NTS0090 아날로그 서보모터 - 그리퍼 제어

8. ![미니 랜턴](http://image.auction.co.kr/itemimage/12/0c/27/120c278486.jpg =100x) 미니 랜턴 - 컵에 빛 투과

9. [![아두이노](http://www.devicemart.co.kr/data/collect_img/kind_0/goods/detail/1245596_3.jpg =100x)](http://www.devicemart.co.kr/goods/view?no=1245596) 아두이노 우노 R3 호환보드 [SZH-EK002]

10. [![서보 모터](http://www.devicemart.co.kr/data/collect_img/kind_0/goods/detail/1137914_2.jpg =100x)](http://www.devicemart.co.kr/goods/view?no=1128421) TowerPro 호환 9g 미니 서보모터 SG-90 - 투입구 여닫이

11. [![라즈베리파이](http://www.devicemart.co.kr/data/collect_img/kind_0/goods/detail/1311414_1.jpg =100x)](http://www.devicemart.co.kr/goods/view?no=1311414) 라즈베리파이3 (Raspberry Pi 3 Model B) + 방열판

12. [![브레드보드](http://www.devicemart.co.kr/data/collect_img/kind_0/goods/large/1328148_1.jpg =100x)](http://www.devicemart.co.kr/goods/view?no=1328148) 브레드보드 400핀 Half Size Breadboard [SZH-BBAD-005]

13. ![점퍼 케이블](http://www.devicemart.co.kr/data/collect_img/kind_0/goods/large/1329628.jpg =100x) 점퍼와이어 M/M, M/F, F/F

14. [![배터리홀더](http://www.devicemart.co.kr/data/editor/goods/1/2004/06/3102_15508130374427.PNG =100x)](http://www.devicemart.co.kr/goods/view?no=3102) AA배터리 건전지홀더 전원타입[4개입] - 서보모터에 전원 공급

15. [![건전지](https://user-images.githubusercontent.com/41332126/70554192-0af94300-1bc0-11ea-8305-ae3375adecb6.png =100x)](http://www.devicemart.co.kr/goods/view?no=10843304) KC인증 정품 알카라인 AA건전지/AA배터리 AA LR06 벌크형

16. [![카메라](http://www.devicemart.co.kr/data/collect_img/kind_0/goods/large/1077951.jpg =100x)](http://www.devicemart.co.kr/goods/view?no=1077951) 라즈베리파이 카메라모듈 V2 8MP - 물체 감지

17. [![티코블러](http://www.nulsom.com/design/default/images/p02-17-img-01.jpg =100x)]() T-Cobbler GPIO 확장보드 + 40핀 플랫케이블 - 라즈베리파이로 모터/센서 제어

18. [![고무](https://user-images.githubusercontent.com/41332126/70539949-bc3faf00-1ba7-11ea-99e4-64b091022261.png =100x)](https://search.shopping.naver.com/search/all.nhn?query=%EB%AF%B8%ED%82%A4%EB%A7%88%EC%9A%B0%EC%8A%A4+%EB%85%BC%EC%8A%AC%EB%A6%BD%ED%8C%A8%EB%93%9C+%EC%8A%AC%EB%A6%BC%ED%98%95&cat_id=&frm=NVSHATC) 미키마우스 논슬립패드(슬림형) - 컵에 닿는 그리퍼 부분에 부착하여 미끄럼 방지

<!--
[![폼보드](http://www.devicemart.co.kr/data/collect_img/kind_0/goods/large/200707141834210.jpg =100x)](http://www.devicemart.co.kr/goods/view?no=10114) 3T 포맥스(검정색) 450x450(mm) - 외관 제작[![접착제](http://www.devicemart.co.kr/data/collect_img/kind_0/goods/large/201007121425170.jpg =100x)](http://www.devicemart.co.kr/goods/view?no=24965) 우드락 접착제 UHU-Por 50ml
[![컷터기](http://www.devicemart.co.kr/data/goods/1/2019/02/10846950_tmp_9f3b60f3cb0528b2b7a42cb4742ffcf11898view.jpg =100x)](http://www.devicemart.co.kr/goods/view?no=10846950) USB 헤드교체형 폼커터 열컷터기 열선 우드락커터기
![우드락](http://gdimg.gmarket.co.kr/1469532215/still/300 =100x) 우드락 5T 300x450mm
-->
<br>

## 6. 동작
![전체동작](http://img.youtube.com/vi/vKi94sMjuI0/0.jpg)](https://youtu.be/vKi94sMjuI0) 전체 동작

<!--[![롯데리아](http://img.youtube.com/vi/HyUIKzlGqmU/1.jpg)](https://www.youtube.com/watch?v=HyUIKzlGqmU) 롯데리아 [![스타벅스](http://img.youtube.com/vi/tz4IzEW01kU/1.jpg)](https://www.youtube.com/watch?v=tz4IzEW01kU) 스타벅스 [![빽다방](http://img.youtube.com/vi/mZxCZR2VMDo/1.jpg)](https://www.youtube.com/watch?v=mZxCZR2VMDo) 뻭다방 [![팬도로시(ICE)](http://img.youtube.com/vi/lh_GckbTddM/1.jpg)](https://www.youtube.com/watch?v=lh_GckbTddM) 팬도로시(ICE) [![팬도로시(HOT)](http://img.youtube.com/vi/GYUEwOkC71I/1.jpg)](https://www.youtube.com/watch?v=GYUEwOkC71I) 팬도로시(HOT)-->

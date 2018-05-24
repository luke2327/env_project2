# Crawler

##Framework

> ##### Scrapy 
>
> > 기반언어 : Python
> >
> > 구글 검색 결과 : 481,000
>
> ##### Nutch
>
> >기반언어 : Java
> >
> >구글 검색 결과 : 476,000
>
> ##### Crawler4j
>
> > 기반언어 : Java
> >
> > 구글 검색 결과 : 20,600

# Scrapy architecture 

Scrapy는 웹에 존재하는 정보를 크롤링하기 위한 파이썬 기반의 애플리케이션 프레임워크다. 프레임워크라는 말에서 알 수 있듯이, Scrapy는 파이썬 코드에 대해 조금만 알고 있다면 설정을 통해 충분히 웹을 스크랩할 수 있다. 그렇다면 어떻게 작동하는지 Scrapy의 아키텍처를 알아보자. 

```
![Scrapy](http://www.dbguide.net/publishing/img/dbguide/bigdata_technology/123_bigdata_01.gif)
```

Scrapy의 아키텍처 구조는 수집 주기를 설정하는 스케줄러가 존재하고, 수집할 항목을 정의하는 아이템과 수집 데이터의 저장 형식을 정의하는 파이프라인이 출력을 담당하는 형태다. 스파이를통해 월드와이드웹 정보를 수집하는 형태다. 

● **스케쥴러** : 스케쥴러는 수집주기, 프록시설정, 멀티 에이전트 설정 기능을 가지고 있어 Scrapy 엔진의 수집에 관련된 정책사항을 설정하는 역할을 담당한다. 

● **아이템 파이프라인** : 아이템 파이프라인은 수집하려는 데이터의 입출력을 담당한다. 수집하려는 항목을 아이템으로 정의하고 수집한 데이터의 형태를 파일 혹은 DBMS로 직접 입력이 가능하도록 설정할 수도 있다. 

● **스파이더** : 수집하는 데이터를 크롤링하는 역할을 한다. 스파이더는 스케쥴러로부터 프로젝트에서 크롤링하는 정책에 따라 설정 값을 요청하여 다운로더로부터 받은 크롤링 데이터를 아이템형태로 아이템 파이프라인으로 전송한다. 

● **다운로더** : http, ftp 프로토콜을 해석하여 웹에 있는 데이터를 다운로드 하는 역할을 담당한다. 



# Scrapy 설치

## □ **윈도우에서의 Scrapy 설치**

Scrapy는 파이썬이 먼저 설치된 환경에서 설치해야 한다. 파이썬의 패키지 매니저인 PIP을 설치한 후 Scrapy를 설치한다. 주의할 점은 `2.7.X.X` 버전이 Scrapy에 가장 안정적이므로 가급적 2.7버전을 설치하기를 바란다.

### ■ 파이썬 설치

윈도우에 설치할 경우 [파이썬 공식 홈페이지](http://python.org/download/)에서 다운로드한다.

`2.7.XX`버전을 다운로드해 windows installer 파일을 받아 실행하면 된다. 환경변수를 설정한다. 먼저 환경변수의 경로를 설정 한 후 파이썬 버전을 확인한다. 

****

```
C:\Python2.7;C:\Python2.7\Scripts\;
python - version
```



### ■ PIP 설치

파이썬 패키지 인스톨러를 설치하기 위해 easy_install의 홈피에서 setuptools을 다운로드 받는다. [https://pypi.python.org/pypi/setuptools](https://pypi.python.org/pypi/setuptools) 페이지에서 윈도우의 링크를 추적하면 [https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py](https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py) 가 나온다. 링크를 클릭해 ez_setup.py 파일을 다운로드한다. 다운로드 후 윈도우 커맨드 창에서 다음과 같은 명령을 실행한다. 

****

```
python ez_setup.py build
python ez_setup.py install
```

easy_install의 설치가 끝나면 pip를 설치한다. 커맨드 창에서 다음과 같이 입력한다. 

****

```
easy_install scrapy
```



###■ Scrapy를 설치하기 위해 필요한 기타 패키지 설치

http://slproweb.com/products/Win32OpenSSL.html 에서 win32OpenSSL과 Visual C++ 2008 redistributables을 다운받아 실행한다. 주의할 점은 OpenSSL lite를 받으면 안된다는 것이다. 또한 bin file은 OpenSSL 로컬 폴더에 설치해야 한다. 이후 C:\openssl-win32\bin을 환경변수에 추가한다. 다음으로 필요한 패키지들을 설치해 준다. 필요한 패키지와 다운로드 주소는 다음과 같다. 해당 링크를 다운로드한 후에 윈도우에서 실행한다. 

### 필요 패키지

> pywin32 [http://sourceforge.net/projects/pywin32/files/pywin32/ ](http://sourceforge.net/projects/pywin32/files/pywin32/ ) 
>
> twisted [http://twistedmatrix.com/trac/wiki/Downloads ](http://twistedmatrix.com/trac/wiki/Downloads )
>
> zope.interface [https://pypi.python.org/pypi/zope.interface/4.0.5$downloads ](https://pypi.python.org/pypi/zope.interface/4.0.5$downloads )
>
> lxml [https://pypi.python.org/pypi/lxml/ ](https://pypi.python.org/pypi/lxml/ )
>
> pyOpenSSL [https://launchpad.net/pyopenssl/+download ](https://launchpad.net/pyopenssl/+download )



### ■ Scrapy 설치 확인

윈도우 설치에서 앞의 모든 과정이 정상적으로 끝났을 경우 커맨드 창에서 다음과 같이 치면 오류 없이 Scrapy가 설치될 것이다. 

****

```
easy_install scrapy
```


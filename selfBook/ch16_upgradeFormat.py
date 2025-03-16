# 백신 커널 및 플러그인 엔진 테스트를 위해서는, 다양한 파일에 대한 검사가 가능해야 함 -> 권한 & 파일 포멧
## ex: zipfile 모듈을 이용하면, zip 파일 압축 및 해제가 가능함
### 이전에 작성한 플러그인 백신 엔진 구조는 아래와 같다.
#### - 아래 -
#### [1. init, 2. uninit, 3.scan, 4. disinfect, 5. listvirus 6. getinfo] < 하나의 클래스 : KavMain

##### => 기존 엔진의 scan 함수만으로는 압축 파일 내부에 존재하는 악성코드를 검사할 수 없다. (file)

###### => 함수 보강 [ 7. format / 8. arclist / 9. unarc ]


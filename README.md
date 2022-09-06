# security_door
## 1. server
### ㅤ1) server.py
### ㅤㅤ문과 네트워크로 상호작용하여 RFID 값을 문으로부터 가져와서
### ㅤㅤ펀별 후 다시 값(이름과 성공여부)를 다시 보내 준다.
### ㅤ2) server_regist.py
### ㅤㅤ등록해주는 라즈베리파이와 상호작용하여 RFID 값(id와 name)을 csv파일로 저장한다.
### ㅤ3) web/web.py
### ㅤㅤ누가 얼마나 들어왔었는지 웹사이트 상에서 보여주다.
### ㅤㅤhttp://01234.shop:30000
### <a href="http://01234.shop:30000"><img width="852" alt="image" src="https://user-images.githubusercontent.com/80575942/188352172-d372035e-9bbe-4547-bcb2-84c30e67fc65.png"></a>
### ㅤ4) shell
### ㅤㅤstart.sh
#### ㅤㅤㅤ처음 컴퓨터가 시작할떄 위 3개의 python 실행
### ㅤㅤcheck.sh
#### ㅤㅤㅤ1분간격으로 위 3개의 python이 잘 실행되고 있는지 확인후 프로세스가 죽어 있으면 다시 실행

## 2. door
### ㅤproject.py
### ㅤㅤ소캣 통신을 하며 문울 열어주는 역할을 한다.
## 3. register
### ㅤㅤ소캣 통신을 하며 정보를 등록하게 해준다.
## ![image](https://user-images.githubusercontent.com/80575942/188752404-1fdabf4a-46a6-4e78-965e-464c1d7c4814.png)
## ![image](https://user-images.githubusercontent.com/80575942/188754457-eed05fb8-3d89-4acc-ada7-3e7a47ca6f18.png)


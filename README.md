# security_door
## 1. server
### ㅤ1) server.py
### ㅤㅤ문과 네트워크로 상호작용하여 RFID 값을 문으로부터 가져와서
### ㅤㅤ펀별 후 다시 값(이름과 성공여부)를 다시 보내 준다.
### ㅤ2) server_regist.py
### ㅤㅤ등록해주는 라즈베리파이와 상호작용하여 RFID 값(id와 name)을 csv파일로 저장한다.
### ㅤ3) web/web.py
### ㅤㅤ누가 얼마나 들어왔었는지 웹사이트 상에서 보여주다.
### ㅤㅤhttp://01234.shop:20000
### <a href="http://01234.shop:20000"><img width="852" alt="image" src="https://user-images.githubusercontent.com/80575942/188352172-d372035e-9bbe-4547-bcb2-84c30e67fc65.png"></a>
### ㅤ4) shell
### ㅤㅤstart.sh
#### ㅤㅤㅤ처음 컴퓨터가 시작할떄 위 3개의 python 실행
### ㅤㅤcheck.sh
#### ㅤㅤㅤ1분간격으로 위 3개의 python이 잘 실행되고 있는지 확인후 프로세스가 죽어 있으면 다시 실행

## 2. door
### ㅤproject.py
### ㅤㅤ1) socket
### ㅤㅤㅤ
### ㅤㅤ2) rfid
### ㅤㅤㅤ
### ㅤㅤ3) serbo
### ㅤㅤㅤ
### ㅤㅤ4) lazer, cds
### ㅤㅤㅤ

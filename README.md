# Piro20_CardGame_5
## 0. 게임소개
- 로그인(카카오, 구글, 네이버, 아이디) 을 한다.
  * 네이버는 아이디를 등록해야 로그인 가능합니다.
- 5개의 랜덤 숫자 중 하나를 고르고, 상대를 골라 공격한다.
  - 상대가 게임을 받아들여 숫자를 골랐다면, 더 크거나 작은(랜덤) 수를 가진 사람이 승리!
  - 상대가 게임을 받아들이지 않았다면, 게임은 진행 중이며 취소할 수 있다.
- 게임에서 승리했다면 자신의 카드 숫자만큼의 포인트를 얻고, 패배했다면 카드 숫자만큼의 포인트을 잃는다.
- 게임을 할때마다 유저의 포인트가 업데이트되고, 유저 순위를 볼 수 있다!


## 1. 팀 협업 툴
1) Figma
  - 초기 로직 overview 그리면서 역할 분배
  - 각자의 로직 구상 및 구현
  - https://www.figma.com/file/Zwq12kUAtiIEsnGZV3TnNx/CardGame?type=design&node-id=0-1&mode=design&t=CTb4PnQraLoF15jf-0
2) ERD-diagram
  - 다함께 model의 이름, 타입, 속성 정의 후 개인 작업 돌입
  - https://www.erdcloud.com/d/WwSPT9D6F7qrGMvzz
3) GitHub
  -  개인 브랜치로 작업 → main merge
  -  commit 형식 통일
  -  Here!


## 2. 역할 분배
 강민주 - 백엔드
    - 공격하기 구현
    - 🔥추가기능🔥 계정 수정,삭제 구현 (소셜로그인 계정도 삭제 가능)

  석우진 - 백엔드
    - django 로그인 / 소셜로그인 (구글, 네이버, 카카오)
    - 🔥추가기능🔥 모든 계정은 닉네임 설정 가능 (중복체크 가능)

  정예진 - 프론트
    - 전체적인 html, css 구현

  황지우 - 백엔드
    - 게임 list 구현
    - 게임 detail 구현
    - 반격하기 구현

## 3. 게임 로직
![Group 1](https://github.com/Pirogramming-20/Piro20_CardGame_5/assets/94210833/1d51da0a-fe10-4bc5-a804-39cf60152942)
![Group 2](https://github.com/Pirogramming-20/Piro20_CardGame_5/assets/94210833/05e56cef-549b-4a76-ac81-89ce1fcb75ce)
![Group 3](https://github.com/Pirogramming-20/Piro20_CardGame_5/assets/94210833/437e57f4-909e-44e9-9d7e-36e0ffccab81)

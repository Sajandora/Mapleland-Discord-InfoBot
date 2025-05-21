<div align="center">
  <h1>🗺️ 메이플랜드 디스코드 봇</h1>
  <p>메이플스토리 몬스터, 아이템, 맵, 경매장 정보 조회</p>
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/discord.py-2.5.2-blue?logo=discord" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
</div>

---

## 📌 프로젝트 소개

> 해당 프로젝트는 지인들의 편한 메이플랜드 생활을 위해 제작되었습니다. <br>
> 메이플랜드 디스코드 봇은 **메이플랜드 데이터를 기반으로 몬스터, 아이템, 맵 정보, 경매장 시세**를  
> 디스코드 채팅창에서 실시간으로 검색할 수 있도록 도와주는 봇입니다.  
> 일일이 웹 브라우저를 열지 않고도 명령어만으로 빠르게 원하는 정보를 확인할 수 있습니다.

---

## 🧩 주요 기능

- 🔍 몬스터 정보 검색 
- 🪙 아이템 정보 검색 
- 🗺️ 맵 정보 검색 
- 💰 경매장 시세 조회
- 📋 다중 결과 리스트 출력 + 버튼으로 선택 가능

---

## 🖼️ 사용 방법 및 예시

> 아래와 같은 명령어로 데이터를 조회할 수 있습니다:


기본 정보(몬스터, 아이템의 드랍테이블 등의 기본 정보)
```
!(몬스터 or 아이템 or 맵 이름)
```
<br>경매장 정보 확인
```
!경매장 아이템이름
```
<br>사이트 바로가기
```
!메랜디비 or !메랜지지
```
<br>도움말
```
!도움 or !도움말
```
* 위의 명령어가 아니여도 작동할 수 있게 예외처리를 해두었습니다.<br>도움말 명령어를 확인해주세요!


<br>결과는 아래처럼 디스코드 임베드 메시지로 표시되며,  
**복수 결과일 경우 버튼을 눌러 항목을 선택**할 수 있습니다.

> **경매장** 사용 예시<br>
> ![image](https://github.com/user-attachments/assets/e5600867-60d0-420e-a5e2-47388bde48de)<br><br>
> **아이템 검색** 사용 예시<br>
> ![image](https://github.com/user-attachments/assets/47eba45f-dd01-417c-9c28-43dd55a30045)<br><br>
> **복수 결과** 예시<br>
> ![image](https://github.com/user-attachments/assets/8b2a5bea-cd26-483f-be6a-88e39012c79d) =>
> ![image](https://github.com/user-attachments/assets/d31a26a7-1e50-4be7-b1f2-c9d4caa5d48f)



---

## 🔧 설치 방법

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정

1. `.env.example` 파일을 열고 `DISCORD_BOT_TOKEN`에 봇 토큰을 입력합니다.

```env
DISCORD_BOT_TOKEN=your_real_token_here
```

2. 파일명을 `.env`로 변경합니다.

---

## ⚠️ 주의 사항

* 이 봇은 [메랜지지](https://mapleland.gg/)와 [메이플랜드 데이터베이스](https://mapledb.kr/)의 데이터를 참고합니다.
* **비공식 프로젝트**입니다.

---
## 📜 라이선스

이 프로젝트는 [MIT License](LICENSE)를 따릅니다.

---

## 🙌 기여 및 문의
* 질문, 버그 리포트는 [Issues 탭](https://github.com/yourusername/mapleland-discord-bot/issues)에서 남겨주세요.

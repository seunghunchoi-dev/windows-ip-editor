# Windows IP 편집기

Windows 네트워크 어댑터의 IP 주소, 서브넷 마스크, 기본 게이트웨이, DNS를 창 하나에서 바꾸는 프로그램입니다.
자주 쓰는 설정을 파일로 저장해 두었다가 다시 불러올 수 있습니다.

## 실행

Windows의 네트워크 설정을 바꾸므로 **관리자 권한**이 필요합니다. Python 3과 Pillow가 필요합니다.

```
pip install -r requirements.txt
python my_program.py
```

## 실행 파일 만들기

```
pip install pyinstaller pillow
pyinstaller my_program.spec
```

결과물은 `dist` 폴더에 생깁니다.

## 사용한 구성요소

- [Pillow](https://python-pillow.org/) (MIT-CMU 라이선스): 창 아이콘 표시
- Python 표준 라이브러리, Tkinter

## 라이선스

[MIT](LICENSE) © 최승훈

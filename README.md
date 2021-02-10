## [ HUFS WEB project ] Notion &amp; Slack 연동

### Introduction
> 해당 레포지토리에는 한국외대 웹 페이지 제작 프로젝트의 효율적인 진행을 위해 AWS Lambda를 활용하여 Notion과 Slack를 연동한 Python 소스 코드가 있습니다. 아래 GIF와 같이 동작합니다.

![](00.gif)

### How to work
> 아래 글을 통해서 동작 원리에 대한 자세한 설명을 확인할 수 있습니다.
0. [AWS Lambda에 관한 기본 개념](https://bit.ly/2Z7CciN)
1. [비공식 Notion API를 확인하고 사용하는 방법](https://bit.ly/2Zb1lJb)
2. [AWS Lambda를 통해 Notion 정보를 Slack에 연동하는 방법](https://bit.ly/3tFbZGe)

### config
> 개인 정보가 작성된 파일입니다.
1. `config.py`: 실제 AWS Lambda를 작동할 때 필요한 정보가 들어 있는 파일입니다. 개인 정보가 담긴 파일로 `.gitignore` 를 통해 본 레포지토리에는 업로드 되어 있지 않습니다.
2. `config_example.py`: `config.py` 파일에서 실제 정보를 제거하여 올린 파일입니다. 동작 원리를 참고할 수 있게 만들어 첨부하였습니다.

### main
> 실제 AWS Lambda가 작동하는 함수가 작성된 파일입니다.
1. `get_cookie()`: Notion API를 사용하기 위해 필요한 쿠키를 생성하는 함수입니다.
2. `get_notion_response()`: Notion API의 Response를 `return` 하는 함수입니다.
3. `get_notion_value()`: 실제 Notion에 담긴 데이터를 정제하여 `return` 하는 함수입니다.
4. `lambda_handler()`: 실제 AWS  Lambda에서 동작하는 함수로 `get_notion_value()` 함수로부터 반환 받은 데이터를 `return`하여 Slack에 보여줍니다.

### library
> `requirements.txt` 또는 `python.zip` 을 통해서도 필요 라이브러리 및 패키지를 확인할 수 있습니다.
1. `pip install requests`
# ra9+ 添付ファイル保存ツール

これは、[らくらく連絡網+](https://ra9plus.jp/) から添付ファイルを自動でダウンロードするためのツールです。

## 機能

*   指定されたグループのメールに添付されたファイルをダウンロードします。
*   一度ダウンロードしたファイルは、再度ダウンロードしません。

## 使い方

1.  `.env` ファイルを作成し、以下の内容を記述します。
    ```
    DOWNLOAD_DIRECTORY="/path/to/your/download/directory/"
    SELENIUM_PROFILE_DIRECTORY="/path/to/your/selenium/profile/directory"
    ORGANIZATION_ID="your_organization_id"
    ```
2.  `ra9plus.py` を実行します。
    ```bash
    uv sync
    uv run ra9plus.py
    ```

## 依存関係

*   Python 3.13+
*   dotenv
*   selenium

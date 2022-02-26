# VSCodeでPythonを実行する

1. 同一folderに「.devcontainer」folderを作成する
1. 「.devcontainer」folderに「devcontainer.json」を作成する

    ```devcontainer.json
    {
        "name": "Python Sample",
        // Dockerfileでイメージ・コンテナの作成
        "dockerFile":"Dockerfile",
        // リモート先のVS Codeにインストールする拡張機能
        "extensions": [
            "ms-python.python"
        ],
    }
    ```

1. 「.devcontainer」folderに「Dockerfile」を作成する

    ```Dockerfile
    From python3.9.10-slim
    ```

1. VSCodeの左下緑色の「><」を押下してRemote
1. Open Folder in Container...を選択
1. .devcontainerがあるfolderを選択
1. イメージとコンテナが自動で生成される

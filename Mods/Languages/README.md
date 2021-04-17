# Phantom Brigade 日本語化Mod

Copyright (c) 2020-2021 Ichihito Ohi

## 必要
- Git（ `git apply` コマンドを使用します．代替手段は検証していません．）

---
## 適用方法
1. エクスプローラーでゲームのインストール先を開く
    既定では `C:\Program Files\Epic Games\PhantomBrigade`

2. Modファイルをコピーする
    `Mods` フォルダすべてを`Configs` フォルダと同じ階層にコピーしてください．

3. コマンドプロンプトまたはPowerShellを起動する

4. ゲームのインストール先に移動する
    ```
    $ cd C:\Program Files\Epic Games\PhantomBrigade
    ```

5. パッチファイルを適用する
    オプション `-p2` を省略せずに指定してください．
    ```
    $ git apply -p2 Mods/Languages/jp-051-20210416.patch
    ```
    `error: ` が表示された場合は失敗です．エラー内容をよく読んでください．
    以下の警告は無視してください．
    - `trailing whitespace`
    - `warning: ... whitespace errors`

6. 追加ファイルを確認する
    `Configs\Text` フォルダに `Japanese` フォルダが追加されていれば成功です．

---
## 既知の問題
### 言語設定を切り替えても表示が英語（日本語）のまま
- 希望する言語を選択・適用した後でゲームを再起動してください．

---
## 更新履歴
### jp-051-20210416.patch
- ゲーム中の一部を日本語化しました

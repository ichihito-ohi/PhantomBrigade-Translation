# Mod システム
アプリケーションフォルダー内のファイルを改造せずにデータとコードを変更できる mod システムの概要．

---

# 前書き
設定ファイルが公開されているデータ駆動型構造のおかげで， Phantom Brigade はいつでもかなり簡単に改造することができます． `Configs` フォルダー内の任意のファイルを改造することで，さまざまな mod を作成することができます．（シナリオ変更，装備の再調整，新しい機体やローカライゼーションの追加，など．）しかし，この改造方法にはいくつかの問題と制約があります：

- アプリケーションディレクトリのコンテンツを改造する必要があります．
    - すべてのユーザーがそのようなコンテンツを改造できるわけではありません―システムによっては，ゲームは保護ディレクトリにインストールされている場合があります．
    - ゲームのアップデートで改造されたファイルが上書きされ， mod が失われる可能性があります．
    - 追加ファイルなどの変更がゲームアップデートでそのまま残り，バグの原因になる可能性があります．
- 同じ設定を改造する複数の mod をインストールすることは不可能です．
    - ある mod が `simulation.yaml` のようなとあるファイルを改造した場合，ほかの mod はそのファイルに依存するいかなる改造もできません．
- ゲームロジックを改造することができません．
- その他様々な問題の原因（mod の優先順位を制御できない， mod とは直接関係のない大量のデータを複製する必要性，など．）


# はじめに
この新しい mod システムはこれらの問題すべてを解決するための試みです．人気のある改造可能な Unity ゲームの mod システムにかなり近いものです．はじめるには，以下の操作を行う必要があります：

![](https://wiki.braceyourselfgames.com/mods/mods_config_01.png)
![](https://wiki.braceyourselfgames.com/mods/mods_config_02.png)
![](https://wiki.braceyourselfgames.com/mods/mod_config_01.png)

- `mods.yaml` ファイルを作成するかダウンロードして，ユーザーフォルダーの `My Games/Phantom Brigade/Settings` に配置してください．
    - `enabled` が `true` となっていることを確認してください．
    - `loadFromApplicationPath` が `false` となっていることを確認してください．
    - `list` が空欄か，既存のフォルダーと所定のフォーマットで一致していることを確認してください．（詳細は後述）

![](https://wiki.braceyourselfgames.com/mods/mods_folder_01.png)
![](https://wiki.braceyourselfgames.com/mods/mods_folder_02.png)

- ユーザーフォルダーの `My Games/Phantom Brigade/Mods` に mod を展開します．
    - `Mods/MyMod1`, `Mods/MyMod2`... のように mod は別々のフォルダーにします．

![](https://wiki.braceyourselfgames.com/mods/mod_metadata_02.png)

- それぞれの mod フォルダーには， mod の内容について基本的な情報をゲームに伝える `metadata.yaml` ファイルが必ず必要で，これにより読み込みと mod 管理 UI の描画が可能になります．
    - バージョン
    - 識別子 (詳細は後述)
    - 名前
    - 説明
    - 含まれる内容（詳細は後述）
    - 互換性のあるゲームバージョン（形式は `a.b.c`，例えば `0.14.2`， `0.16.0` のようになります．ビルド情報の透かしで見られる `-b3103E` のような接尾辞は含めないでください．）

![](https://wiki.braceyourselfgames.com/mods/mod_manager_01.png)

- `mods.yaml` の `enabled` 項目が `true` に設定されると，新しいメインメニュー設定として Mods メニューがゲームに現れます．
    - このメニューでは，検出された mod フォルダーすべてのリストが左に表示されます．
    - それぞれの mod をクリックすると，指定されたフォルダー内の `metadata.yaml` から取得された詳細が表示されます．
    - Mod を選択リストに追加するには，追加ボタン（右矢印）をクリックします．
    - Mod が選択リストに追加されると，右側のウィンドウに表示されます．
    - 選択リストの任意の項目は有効化/無効化および上下の移動ができます．これにより，あとからリストを作り直すことなく， mod の順番を設定したり一時的に一部の mod を無効化したりすることができます．ボタン（左矢印 [^1] ）をクリックすることで任意の項目を除外する（左側のリストに戻す）こともできます．
    - `mods.yaml` の `list` 項目を編集することで，選択 mod のリストや有効化，ロード順番を直接制御できます―　UI は単に設定内の項目を変更するインターフェースに過ぎません．
    - "Reset" をクリックすると， `mods.yaml` がディスクからロードされ，それに応じて UI が更新されます．
    - "Save" をクリックすると，更新された `mods.yaml` がディスクに書き込まれます．
    - "Apply" をクリックすると，現在有効な設定に基づいて mod の再ロードが試みられます．（変更を適用する場合は，こちらではなくゲームを再起動することをおすすめします．）

**警告！** （その時点での設定に基づいて）起動時にゲームは既に mod を適用しています．上記のメニューで使用可能な "Apply Mods" オプションは， mod 設定の変更を適用する際に推奨される方法ではなく，予期しない問題を引き起こす可能性があります． Mod メニューで mod の無効化，有効化，順番変更のような変更をおこない効果を確認する場合は， "Save Config" を押してゲームを再起動することをおすすめします．さらに，ランタイムで生じ得る予期せぬ変更を元に戻すことは不可能なため，ライブラリ mod （コード注入 mod）をセッション中に複数回ロードすることには対応していません―現在のセッションで既にゲームがコード mod をロードしている場合，そのような mod はスキップされます．ただし，このオプションは設定 mod を開発中に変更を素早く確認する場合などに役立つことがあります．

`mods.yaml` 内の `list` 項目に列挙された（Mod メニューまたは設定の手動編集で追加，有効化された） mod ディレクトリは，ゲーム起動時に解析されます． `metadata.yaml` で与えられた情報に基づいて，ゲームは現在のバージョンと mod との互換性を確認してフォルダーの内容を走査し，ロードを試みます．対応する mod コンテンツタイプについて詳細は以降の節を参照してください．


# Mod コンテンツタイプ
Mod にはいくつかのコンテンツタイプを含めることができます．これらは mod フォルダー内でサブフォルダーとして分けられ，その存在は `metadata.yaml` 内で宣言します．対応するコンテンツタイプは今後拡張していく予定（ローカライゼーションなど）ですが，現在は以下の4タイプに対応しています．

## 設定上書き

![](https://wiki.braceyourselfgames.com/mods/mod_content_overrides_02.png)

- Metadata フラグ： `includesConfigOverrides`
- フォルダー： `ConfigOverrides/`

これは， Configs フォルダーを直接編集するのとよく似た，最も単純な種類の mod コンテンツです．

- Configs フォルダーの階層構造を `Mods/[ModName]/ConfigOverrides` 以下に複製すると，ファイルを置き換えたり新しく追加したりできます．
- そこに配置するファイルはゲームからコピーした `.yaml` ファイルを改造した物である必要があり，まったく同じ場所に配置する必要があります．
- 変更内容は，ゲームの初期化時だけではなくデータベースが読み込まれるたびに挿入されるため，後々のデータベース読み込みや複数回のデータベース読み込みなどにも耐えられます．
- 例えば，新しい武器を `Mods/[ModName]/ConfigOverrides/DataDecomposed/Equipment/Part_Presets/my_new_weapon.yaml` に追加するとゲームはそれを読み込みます．
- 別の例：独自バージョンのグローバル設定ファイルを `Mods/[ModName]/ConfigOverrides/Data/Settings/simulation.yaml` に配置すると，ゲームはそのバージョンのグローバル設定を使用した状態で起動します．
- 制限： `Data` と `DataDecomposed` フォルダーの内容のみ対応しています． `Configs` の中には他にもファイルがありますが，現時点ではこの mod コンテンツタイプで改造することはできません． Config overrides を用いた mod 適用は `PB/Configs` ディレクトリのファイルを直接改造するディスク操作ではなく， DataLinker および DataMultiLinker データマネージャーの読み込み段階における挿入操作です．ですが，通常みなさんが改造したいであろうファイルは上書き可能です―それ以外のファイルはごく少数で改造には適していません．（古いバイナリファイル，現在のデータベースシステムより前から存在する使われていない設定など）

## 設定編集

![](https://wiki.braceyourselfgames.com/mods/mod_content_edits_02.png)

- Metadata フラグ： `includesConfigEdits`
- フォルダー： `ConfigEdits/`

このコンテンツタイプを使うと，複数の mod による同一ファイルの改造やアップデート時のファイル構造変化に耐性のある，よりきめ細やかな改造が可能になります．

- 表面上は config overrides に似ています： Configs フォルダーの階層構造を `Mods/[ModName]/ConfigEdits` に複製して，既存のパスおよびファイル名と一致するように `.yaml` ファイルを配置してください．
- ただし，これらのファイルの中身は異なります．内部的には，これらのファイルは構造が異なります．同じパスに同じ名前の設定ファイルそのものを複製する代わりに，変更リストを格納します． Config edits を使用すると，削除を要求するだけでなく，さらにエキサイティングなことに，同じ名前の設定ファイルについて個別のフィールドや項目を編集できるようになります．
- これは設定 mod の大きなゲームチェンジャーとなるでしょう．改造における大きな弱点のひとつは，同じファイルを改造している異なる mod 間の衝突や，開発者がゲームを更新するたびにファイルを抽出して改造したコピーを更新し続ける必要があることです．例えば，本作の `simulation.yaml` には何百ものパラメータが含まれており，物理シミュレーション設定の部隊サイズや戦利品生成の倍率など何かしらを変更するため，様々な mod がこれを改造しようとするでしょう．
- 通常，すべての変更を手動で統合して別の合作 mod としてまとめる必要がありました―同じファイルを変更する複数 mod を共存させる方法は他にありませんでした．本機能なら，ある mod が `squadSize` と呼ばれる行を改造する一行だけの `simulation.yaml` ファイルを持ち，また別の mod が複数フィールドの変更を指示する `simulation.yaml` ファイルを持つということが可能です―そしてすべての変更がシームレスに統合されます．まるで本作の設定のすべての項目やフィールドをそれぞれ個別の `.yaml` や個別のフォルダーのように扱えるようになり，非常に的を絞った変更が可能になります．
- もうひとつの良い例が，私たちの `#phantom-modding` チャンネル [^2] でもよく話題に挙がる部隊サイズの変更リクエストです．この機能を使わないと，それにはゲーム中の全シナリオひとつひとつとシミュレーション全体設定ファイルのコピーを管理する必要があり，これは良い方法とは言えませんしそれらのファイルに関連し得る無数の mod を邪魔してしまいます． Config edit 機能を使えば，部隊サイズ mod は他の多くと競合しなくなり，開発者が新しいリリースでシミュレーション設定やシナリオを編集しても mod を更新する必要がなくなります．

Config edits の形式は比較的単純です．

- 対象の設定ファイルをゲームから削除するには `removed` を `true` に設定してください．（例えば，あなたの mod が武器の部品を置き換え，既存の武器をゲームから削除する必要がある場合）
- 対象の設定ファイルにおいて細かな変更をおこなうには， `edits` フィールドに記入してください．
    - 他の設定ファイルに見られるシリアル化された `List<T>` と同じように，必ず各行を `- ` [^3] で始めてください．
    - 必ず各行をクオーテーションマークで囲んでください．例： `- 'hidden: true'` これにより行内の任意の場所で予約文字 [^4] が使えるようになります．
    - 各編集はコロン `:` で分割された二辺で構成されます―左辺がパス，右辺が値（バリュー）です．
        - 最上位フィールドの場合，パスはフィールド名だけです．例えば， `squadSize` という名前の最上位フィールドを `3` という値に改造するには，次のように入力します．
            ```yaml
            - 'squadSize: 3'
            ```
        - 他のフィールドと入れ子になっているフィールドもあります―これに到達するには，パスに全ての階層（ステップ）を含め，ピリオド `.` で区切ってください．―例えば，1層の入れ子になったフィールドの改造はこちら：
            ```yaml
            - 'customPlayerSlot.spawnTagsUsed: true'
            ```
        - フィールドの名前が辞書型のキーやリスト型の番号 [^5] の場合でも指定できます．例：
            ```yaml
            - 'states.no_hostiles.visible: false'   # no_hostiles は辞書のキー
            - 'unitChecks.0.value: 1'               # 0 はリストの番号
            ```
    - `edits` フィールドは辞書型ではないので，同じパスについて複数回編集を繰り返すこともできます．例えば，タグフィールドを一度改造（何かを削除するなど）した後でもう一度改造（何かを追加するなど）しても，まったく問題ありません．
- 現在，解析できる変数の型は以下のものに限られています．
    - `string`, `bool`, `int` , `float`, `Vector2`, `Vector3`, `Vector4`
    - 文字列（ `string` ）型フィールドの場合，右辺の値はそのまま使用されます．
    - ブール（ `bool` ）型の場合， `true` との等価を用いて使用されます．
    - 浮動小数点（ `float` ）型や整数（ `int` ）型の場合，C#仕様書の `int.TryParse` や `float.TryParse` で想定されている文字列書式を参照してください．例を挙げると `6` や `8.62` などです．
    - ベクトル（各種Vector）型の場合，浮動小数点（ `float` ）型に準拠した既定数の `float` をカンマで区切って括弧で囲んだものが想定される書式です．例を挙げると `(3.1, 4, 7.2)` などです．
    - ただし，すべての場合で解析が必要になるわけではありません．例えば，ある型の新しいインスタンスで参照フィールドを埋めるなど，フィールドを既定値で埋めたいだけの場合はどうなるでしょうか？ `!d` （"default" の d）が専用の予約キーワードです．以下のように使用します：
        ```yaml
        - 'customExitBehaviour: !d'
        ```
- 通常のフィールドの場合，以下の処理に対応しています．
    - 指定した新しい値で上書きする
        ```yaml
        - 'field: 7'    # 'field' という名前のフィールドを 7 で上書き
        ```
- `List<T>` の場合 [^5] ，以下の処理に対応しています．
    - 指定した新しい値で上書きする
        ```yaml
        - 'list.4: 7'   # 'list' という名前のリストの4番を 7 で上書き
        ```
    - 指定した番号に新たな値を追加する
        ```yaml
        - 'list.0: 7 !+'    # リストの一番最初に値が 7 の項目を挿入
        - 'list.8: 7 !+'    # リストの8番に値が 7 の項目を挿入（それ以上項目がある場合）または一番最後に挿入（項目が8個未満の場合）
        ```
    - 指定した番号を削除する
        ```yaml
        - 'list.3: !-'  # 3番の項目を削除
        ```
- `HashSet<string>` の場合，以下の処理に対応しています．
    - 値を追加する
        ```yaml
        - 'tags: context_facility !+'   # ハッシュセット 'tags' に文字列を 'context_facility' の挿入を試行
        ```
    - 値を削除する
        ```yaml
        - 'tags: context_fort !-'   # ハッシュセット 'tags' から文字列を 'context_facility' の削除を試行
        ```
- `Dictionary<T>` の場合，以下の処理に対応しています．
    - 指定した新しい値で上書きする
        ```yaml
        - 'dictionary.existing_key: true'   # 辞書 'dictionary' のキー 'existing_keyin' に対応する値（バリュー）を 'true' で上書き
        ```
    - 新しい項目を追加する
        ```yaml
        - 'dictionary.new_key: true !+' # 辞書にキー 'new_key' と対応する値 'true' の挿入を試行
        ```
    - 項目を削除する
        ```yaml
        - 'dictionary.existing_key: !-' # キー 'existing_key' に対応する項目の削除を試行
        ```
- 対応操作は今後時間をかけて拡張されていきます．ただし， config edit system に大きな変更を加える必要がある場合（複雑なデータタイプを解析する機能が必要な場合など）は， config edits の前にライブラリ mod を使用して必要機能の実装から始めることを検討してください．

## ライブラリ

![](https://wiki.braceyourselfgames.com/mods/mod_content_libraries_01.png)

- Metadata フラグ： `includesLibraries`
- フォルダー： `Libraries/`

これは，C#/Unity が依存する編集可能な中間言語（IL; interpreted language）によって可能になる非常に強力なタイプの mod コンテンツです．ゲームロジックにパッチを適用し新たなコードを実行できるライブラリをロードできる機能です．

- この機能の一部は，人気のあるライブラリである [Harmony](https://harmony.pardeike.net) で利用可能になっています―すでに私たちは Harmony を使ってきましたが，それは Unity Editor の UI にパッチを適用するなど内部用に限られていました．
- ライブラリ mod の作成に興味があるプログラマーの方は， [Harmony documentation](https://harmony.pardeike.net/articles/intro.html) をご一読ください．
- Mod システムは `Mods/[ModName]/Libraries/MyLibrary.dll` のような `Libraries` フォルダー内のアセンブリをすべて検出しようとします．
- 次に，そのアセンブリから型を取得して `ModLink` という特殊なクラスを継承しているクラスを探します―見つかった場合，インスタンス化され，データが入力され，特殊なエントリーメソッドが呼び出されます．
- `ModLink` は mod 製作者にエントリーポイントを提供します． `OnLoad` メソッドのオーバーライドを宣言して，任意のコードを実行できます． Mod のメタデータすべて（作業ディレクトリ，どの mod を操作しているか，他に何の mod がロードされているか）および Harmony patcher オブジェクトにアクセス可能で， PB 内のコードを改造できるようになります． 

![](https://wiki.braceyourselfgames.com/mods/mods_content_libraries_02.png)

新規ライブラリの一般的な立ち上げ方法は以下の通りです．

- Visual Studio Community や Rider などの .NET 統合開発環境（IDE）で， クラスライブラリ (.NET Framework) プロジェクトを作成して，ターゲットフレームワークに .NET Framework 4.7.2 を指定します． [^6]
- 参照に以下のものを追加してください
    - `0Harmony.dll` は， [Harmony web サイトの 2.1 リリース](https://github.com/pardeike/Harmony/releases) をダウンロードしてください（Phantom Brigade の今後のリリースで上層の `Manage` フォルダーに直接含められる可能性があります）
    - `Assembly-CSharp.dll` ， `Assembly-CSharp-firstpass.dll` ， `System.dll` ， `UnityEngine.dll` は，インストールフォルダー（例： `PB/PhantomBrigade_Data/Managed/`）から入手してください
    - `Entitas.dll`　は，インストールフォルダーから入手してください
- `ModLink.cs` ファイルを作成してください
    - その中で，すべてを独自の名前空間でラップしてください． `ModTest` のような， `metadata.yaml` の `id` フィールドと一致する名前が理想的です
        ```csharp
        namespace ModTest {}
        ```
    - `ModLink` を継承するクラスを宣言してください
        ```csharp
        namespace ModTest
        {
            public class ModTestLink : ModLink {...}
        }
        ```
        - このクラス内で，以下のシグネチャ（署名）を用いて `OnLoad` のオーバーライドメソッドを宣言してください
            ```csharp
            public class ModTestLink : ModLink
            {
                public override void OnLoad (Harmony harmonyInstance) {...}
            }
            ```
        - 必要に応じて，この開始位置を起点に独自のロジックを実装してください．例えば， `metadata` フィールドにアクセスして作業ディレクトリやどの mod がこのライブラリを読み込んでいるかなどの情報を取得したり， `ModManager.loadedMods` にアクセスして他の mod と連動したり，任意のゲーム内クラスにアクセスしたり，メソッドに渡された `Harmony` オブジェクトを用いて独自のパッチ処理手順を実行したりすることができます．
    - `Patches` というプレーンクラスを宣言してください
        - そのクラス内で，必要な数のサブクラスを　Harmony のパッチ属性と共に宣言してください． [^7]
            ```csharp
            public class Patches
            {
                [HarmonyPatch (typeof (PhantomBrigade.GameController), MethodType.Normal)]
                [HarmonyPatch ("Initialize")]
                public class ModPatch
                {
                    public static void Prefix() {...}
                    public static void Postfix() {...}
                }
            }
            ```
        - `OnLoad` のオーバーライドを宣言してその中で `base.OnLoad(harmony Instance)` の呼び出しをコメントアウトしない限り，自動的に上記のパッチがすべて適用されます．
    - `.dll` をビルドして， mod の `Libraries` フォルダーに配置してください
    - シナリオの機体を設定するロジックに入り込み機体の生成方法を変更することができます．データコンテナでの逆シリアル化コードの挙動をオーバーライドして， AI に伝える武器効率について変更することも可能です．どんなメソッドでも前処理，後処理の追加や完全な置き換えが可能です．限界はありません． Rimworld， Oxygen not Included， KSP やその他の Unity 製ゲームでロジックを変更したり新しいシステムを実装したりしている mod のほとんどが同様の原理で動作しています．

## テクスチャー

- Metadata フラグ： `includesTextures`
- フォルダー： `Textures/`

このコンテンツタイプを使うと，既存のテクスチャーを上書きしたり使用可能なテクスチャーセットを拡張したりすることができます．

- テクスチャーを `Mods/[ModName]/Textures` に配置してください．
- フォルダーがゲームに認識されない場合，それはスキップされます．（ゲームが検知するフォルダーとその内容例については `PhantomBrigade_Data/StreamingAssets/UI` を参照してください）
- ゲームが対象のフォルダーに対して定義する要件にテクスチャーが合致しない場合，それはスキップされます．（必要な形式を確認するには `StreamingAssets` 内のテクスチャーを調べるか以下を参照してください）
- 同じ名前のテクスチャーが（対象のフォルダーで）既に読み込まれている場合，それは置き換えられます．それまでに同じ名前が存在しなかった場合，新しいテクスチャーとして登録されます．
- 現在対応しているフォルダー
    - `Textures/UI/OverworldEvents`
        - 全体マップ（オーバーワールド）のイベント UI に使われる画像（（ `Configs/DataDecomposed/Overworld/Events` フォルダー） `DataContainerOverworldEvent` の `steps` にある `image` フィールドで制御されます）
        - 解像度は必ず 1024x512 にしてください
    - `Textures/UI/OverworldEntities`
        - 全体マップ（オーバーワールド）の存在（エンティティ） [^8] 情報 UI に使われる画像（（ `Configs/DataDecomposed/Overworld/Entities` フォルダー） `DataContainerOverworldEntityBlueprint` の `image` フィールドで制御されます）
        - 解像度は必ず 512x256 にしてください
    - `Textures/UI/PilotPortraits`
        - パイロット写真に使われる画像（基地でパイロットを編集するときにプレイヤーに制御されます）
        - 解像度は必ず 256x256 にしてください

## ローカライゼーション編集

![](https://wiki.braceyourselfgames.com/mods/mod_language_edits.jpg)
*（右上）新しいアイテム設定ファイルをゲームデータのフォルダーのパスと一致させる．*
*（左下）追加または改造されたローカライゼーションデータについて，パスを言語と一致させ，ファイル名を `Text` セクターと一致させる．キーとなる接頭辞を新しいアイテム設定と一致させる．*
*（右下）テキストの登録に成功するとゲーム内ログで通知される．*

- Metadata フラグ： `includesLocalizationEdits`
- フォルダー： `LocalizationEdits/`

このタイプのコンテンツペイロードによって，ローカライゼーション・データベースにテキストを追加できるようになります． `Confgs/Data` や `Configs/DataDecomposed` のデータファイルにプレイヤーが目にするテキストが含まれることはまれ（今後さらにまれになるでしょう）ですが，これはそのような方法でテキストを格納するとローカライゼーションや容易なテキスト改造の可能性が妨げられるためです．ゲーム内テキストのほとんどは最終的に， `Configs/Text` 内のローカライゼーション・データベースに格納され，言語別のバージョンに分割される予定です．ただし，これは mod にひとつの問題を引き起こします―新しいアイテムを追加し，そのテキストが本体データ設定に含まれていない場合に，どうやってプレイヤーが目にするテキストを追加すれば良いのでしょうか？

例えば，新しいスラスター・サブシステムを追加する場合，それに名前と説明文をつけたいはずです．しかし，ゲームがローカライゼーションに対応したため，名前と説明文はサブシステムの設定ファイルからは取得されません―ゲームは `internal_aux_thruster_mod` のようなサブシステムの名前を取り， `internal_aux_thruster_mod__name` や `internal_aux_thruster_mod__text` のようにローカライゼーション・キーを決定し，それらのキーを用いてロードされた言語の適切なテキスト領域からテキストを取得しようとします．（例： `Configs/Text/English/Sectors/equipment_subsystems.yaml` ）このテキスト領域を改造する機能がないと，ユーザー向けの名前・説明文を新しいアイテムにつけることができません．

このタイプのコンテンツをどのように使うかは上記のスクリーンショットで抜粋していますが，念のため，手順を踏んで概要を示します：
- あなたの mod が `ConfigOverrides\DataDecomposed\Equipment\Subsystems` に `internal_aux_thruster_mod.yaml` という新しい設定ファイルを含んでいるとします．そのようなファイルは元のゲームには存在しません―つまり，新しいアイテムであり，改造された物ではありません．ゲームはそれにテキストを表示できません．
- 他のサブシステムがゲーム内でどのようにローカライズされているか例を見てみましょう．簡単な方法がふたつあります：
    - あなたが dotPeek や Rider のような中間言語（IL）解析ソフト（デコンパイラ）をお持ちで，ゲームのコードベースを開く方法をご存じならば，対象となるデータベースクラスの `ResolveText` メソッドを読むことで，それぞれのアイテムについてどのテキスト領域でどんなテキスト・キー・パターンが使われているかわかります．
    - または， Notepad++ や Sublime Text のようなエディターを使いゲームのインストールフォルダーにある `Configs\Text\English\Sectors` で `internal_aux_thruster_hotrod` のような既存のサブシステムの名前を探すことで，そのようなテキストがどのファイルに格納されていて，どのようにテキスト・キーが構成されているかを見ることができます．
- Mod の `ConfigOverrides` フォルダーと同じ場所に `LocalizationEdits` という新しいフォルダーを追加してください．英語ローカライゼーションに追加したい新規の文字列ふたつ（名前と説明文）を宣言しているファイルをそのフォルダーの `equipment_subsystems` のテキスト領域に追加してください．それは，あなたが調べたようにサブシステム用のテキストがここに格納されているからです．
- すべてを正しいフォルダーに配置して `includesLocalizationEdits` フラグを mod のメタデータに含まれば，完了です―新しいアイテムがプレイヤー用のテキストをゲーム中で表示するようになります．

内部的には，ゲームが言語データベースと言語ごとに登録されたキーを読み込むたびにローカライゼーション設定が適用されます．つまり：

- 言語を再読み込みしても，変更は適用されます
- 言語を切り替えても，変更は適用されます
- 他の mod を介して読み込まれた複数のローカライゼーションや非公式ローカライゼーションにも対応することができます―例えば， `MyMod\LocalizationEdits\English\equipment_subsystems.yaml` ファイルを作成してプレイヤー向けの英語テキストを追加する一方で，二番目のファイル `MyMod\LocalizationEdits\Japanese\equipment_subsystems.yaml` を作成して日本語ローカライゼーションに対応することができます．または，ある mod 向けの特定言語ローカライゼーションを含む別の拡張 mod を作成することもできます．

例：このアイテムはゲーム本体には存在せず mod で追加されたものですが，スクリーンショットで示されているように，独自の名前と説明文がゲームで適切に表示されています．
![](https://wiki.braceyourselfgames.com/mods/mod_loc_edit.png)

## ローカライゼーション

![](https://wiki.braceyourselfgames.com/mods/mod_loc_full.png)

- Metadata フラグ： `includesLocalizations`
- フォルダー： `Localizations/`

このコンテンツタイプを使うと，ゲームに新規ローカライゼーションを追加することができます．一般的な原理は以下の通りです：
- ゲームのインストールフォルダー `Configs/Text` から公式の英語フォルダー `English` を `MyMod/Localizations` にコピーして，ローカライズする言語に名前を変更してください．例： `MyMod/Localizaions/French`
- そこに含まれるファイルのテキストをすべて翻訳してください
- ローカライゼーションを含む mod が読み込まれると，ゲーム設定ウィンドウに新しい言語設定が表示されてローカライゼーション言語を切り替えることができるようになります．

特記：
- ローカライゼーションシステムの対応範囲を確認するために，ローカライズされるテキストすべてを異なる色とランダムな文字列に置き換えて表示するコンソールコマンドがあります．
    ```
    > data.toggle-localization-debug
    ```
- ゲームのどの部分がローカライゼーション・データベースのどの部分を使用しているかを確かめるには， ILSpy や dotPeek のような中間言語解析ソフトを使用し，ゲームのインストールフォルダーから `Assembly-CSharp` を開いて `DataContainer` クラスを継承しているファイルで `ResolveText` という名前のメソッドを探すことをお勧めします．ゲーム内データベースの大部分はこのようなメソッドでテキストのローカライズを処理しており，それを読むことでローカライゼーション・キーがどのように生成されてデータ・キーの中からどのように使われているかわかるようになるでしょう．これは上述のローカライゼーション編集 mod においても役立ちます．


# その他
ゲームログに注意してください―何らかの問題が起きた場合に mod マネージャーから多くの情報が含まれていたり，すべて上手く動作した場合に読み込みが成功したことを確認したりすることができます．接頭辞 "Mod Manager" がついたメッセージをログの一番初めに向けて探してください．ログを表示するには， <kbd>Shift</kbd> + <kbd>F11</kbd> を押すか，アプリケーションのデータフォルダーにあるログファイルを開いてください [^9] ．

Mod の開発中は，`My Games/Phantom Brigade/Settings` フォルダーの `debug.yaml` にある `developerMode` を有効化して，追加オプション，デバッグ情報，コンソールコマンドにアクセスできるようにすると役に立つ場合があります．

**開発者モードまたは mod が有効なゲームからのバグとクラッシュの報告は BYG に処理されないことに注意してください．**


[^1]: 翻訳現在の見た目
[^2]: https://discord.gg/braceyourselfgames
[^3]: 半角スペース含む
[^4]: https://yaml.org/spec/1.2.2/#53-indicator-characters
[^5]: リストの番号（index）は0から始まる
[^6]: https://docs.microsoft.com/dotnet/core/tutorials/library-with-visual-studio
[^7]: https://harmony.pardeike.net/articles/patching.html
[^8]: 移動基地，敵施設，パトロール部隊など
[^9]: https://docs.unity3d.com/Manual/LogFiles.html

---

編集：Artyom Zuev
翻訳：ichihito_ohi
作成：Miketan

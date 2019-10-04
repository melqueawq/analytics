# analytics

## cookieの動作
LocalStorage非対応
1. cookieにuiがあるか調べる  
    〇 : そのuidを取得  
    × : 新たにuidを付与(アクセス時点のtimestampを使用)

1. member.jsonにuidが登録されているか調べる  
    〇 : 次へ  
    × : uidをmember.jsonに登録

1. uidをjsファイルに書き込んで/entryに送信


### 現状のjsonの保存形式
uidごとにデータをもたせた方がよいがとりあえずuidを保存することを優先
```
{
    "<cid>":[
        "<uid>",
        "<uid>",
        ...
    ],

    "<cid>":[
        ...
    ]
    ...
}
```

## 媒体定義
config.jsonに
```
"campaign":[
    {
        "name":"<cpName>"
        "cv":"<cvValue>",
        "ad":"<adValue>"
    },
    {
        ...
    },
    ...
]
```
を定義、CV(`param=<cvValue>`)送信時にqueryに`ad=<adValue>`があるなら、
campaignを調べ、cvValueとadValueのセットがあるならログをとる

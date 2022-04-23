HTTP GET POST 　違いがわからなかったのでメモ

冪等性:

> ある HTTP メソッドがべき等であるとは、サーバーが同じ状況にあるとき、特定のリクエストに対して何回でも続けて同じ効果が起こることをいいます。
> このことは、べき等なメソッドでは (統計を取る際のことを除いて) 副作用が生じるはずではないと言うこともできます 。
> 適切に実装された GET、HEAD、PUT、DELETE の各メソッドはべき等ですが、POST メソッドはそうではありません。安全な (en-US)メソッドはすべてべき等です。

> べき等なメソッド: GET, HEAD, PUT, DELETE, OPTIONS, TRACE
> べき等でないメソッド: POST,PATCH, CONNECT

<https://developer.mozilla.org/ja/docs/Glossary/Idempotent>
<https://developer.mozilla.org/ja/docs/Web/HTTP/Methods>

etc.
リクエストボディ

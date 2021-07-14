#### JWT payload - jti  

[참고페이지](https://www.ibm.com/docs/ko/was-liberty/base?topic=uocpao2as-json-web-token-jwt-oauth-client-authorization-grants)

- 선택적 옵션이다

- JWT 토큰의 고유 ID이다
- 존재하는 경우 동일한 JWT ID를 재사용할 수 없다 (`일종의 중복로그인 개념`)

#### JWT palyload public/private claim?

- public claim은 사용자 마음대로 쓸 수 있으나 충돌 방지를 위해 [정의된대로 사용하는 것](https://www.iana.org/assignments/jwt/jwt.xhtml)이 좋다고 함
- private claim은 통신을 주고 받는 당사자들끼리 협의해서 자유롭게 키와 값을 정할 수 있음
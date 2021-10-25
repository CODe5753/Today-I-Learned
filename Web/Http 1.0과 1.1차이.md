# Http 1.0 vs Http 1.1

## HTTP 1.1 특징

- 커넥션 유지(Persistent Connection)
- 호스트 헤더(Host Header)
- 강력한 인증 절차(Improved Authentication Procedure)

### 1.커넥션 유지

- 기존은 1 GET 1 Connection이었음
- N GET 1 Connection으로 바뀜
- 이로인해 서버는 TCP 세션 처리 부하를 줄일수 있기에 좋고, 클라이언트는 응답 속도가 개선됨

#### 1-1.파이프라이닝

- 기존은 Req#1 -> Resp#1 -> Req#2 -> Resp#2 식이었음
- 이를 개선하여 Req#1 -> Req#2 -> Req#3 각각 응답을 받아 처리
- 응답 속도를 높혀 페이지 뷰의 속도를 빠르게할 수 있는 기능

### 2. 호스트 헤더

- 1.0에서는 한 IP에 여러 도메인 할당이 불가능했음
- 1.1에서는 Host 헤더를 추가했고, 버추어 호스팅이 가능해졌음

### 3. 강력한 인증 절차

- 1.1에서 다음 2개의 헤더가 추가됨
  - proxy-authentication
  - proxy-authorization
- 실제 서버에서 클라이언트 인증을 요구하는 www-authentication 헤더가 1.0에도 있었음
- 하지만 클라이언트와 서버 사이에 프록시가 위치하는 경우 프록시가 사용자의 인증을 요구할 수 있는 방법이 없었음

## References

- [HTTP 1.0과 HTTP 1.1의 큰 차이점](https://withbundo.blogspot.com/2021/02/http-http-10-http-11.html)
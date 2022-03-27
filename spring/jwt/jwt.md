#### JWT 토큰 안전할까?

처음 `JWT` 개념을 들었을 때, `"뭐야 탈취되면 그냥 털리겠는데?"` 라는 생각을 했었습니다.

하지만 개발 세계가 호락호락하지만은 않죠. 

예상대로 `AccessToken`만 구현한다면 위와 같은 문제가 있겠지만 여러 대안이 있었습니다.

먼저 `JWT`를 구현하는 여러 방법에대해 순차적으로 알아보겠습니다.

1. ##### AccessToken 사용

   - 토큰을 발급하는 순간 서버측에서 사용자의 접속을 강제로 만료시키기 어려운 구조
     - 왜냐, 미리 정의된 비밀키로 유효인증을 처리하기 때문
   - 짧은 만료 시간을 설정하자
     - 만약 토큰이 탈취되더라도 빠르게 만료가 되기 때문
     - 하지만 사용자는 자주 로그인을 해야하는 문제 발생
   - 긴 만료 시간을 설정하자
     - 당연히 사용자가 자주 로그인 할 필요는 없어짐
     - 하지만 토큰이 탈취된다면 해당 토큰이 만료될 때 까지 사용이 가능해짐

2. ##### AccessToken + RefreshToken 사용

   - 짧은 만료시간을 갖는 `AccessToken`과 긴 만료시간을 갖는 `RefreshToken`의 조합
     - AccessToken: 30분 내외 만료
     - RefreshToken: 2주에서 한 달 만료
   - `AccessToken`이 만료 되었다는 오류를받으면 저장해둔 `RefreshToken`을 이용해 `AccessToken`을 재발급하는 구조
   - 만약 유효하지 않거나 만료된 `RefreshToken`은 사용자의 재로그인을 유도
   - `AccessToken`은 서버에 저장할 필요가 없으나 `RefreshToken`은 서버에 저장하고 검증에 활용해야 함
   - `JWT` 장점이 I/O 작업이 필요 없는 빠른 인증 처리인데, `RefreshToken` 이에 포함되지 않는 부가적인 기술임

3. ##### AccessToken + RefreshToken + Sliding Sessions 전략

   - `AccessToken` + `Sliding Sessions`는 `AccessToken`의 세션 기간을 늘려주었다면, 이 전략은 `RefreshToken`의 만료 기간을 늘려줌
   - `RefreshToken`의 만료 기간에 대한 제약을 받지 않음(계속 늘려주니까)
   - 즉, 글을 작성하거나 하는 유지가 필요한 상황에서 세션이 만료되는 문제를 방지할 수 있음
   - 하지만 서버에서 강제로 `RefreshToken`을 만료하지 않는 한 지속적으로 사용 가능함
   - 인증이 추가로 요구되는 경우에 대한 보안 강화가 필요(패스워드 확인한다던가)
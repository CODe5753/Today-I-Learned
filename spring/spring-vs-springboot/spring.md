# Spring

### 스프링이란?

- 오픈소스 프레임워크
- 종속 객체를 생성해주고 조립할 수 있는 프레임워크
- 자바 SE로 된 자바 객체(POJO)를 자바 EE에 의존적이지 않게 연결 해줌
- 국내 전자정부 표준프레임워크의 기반 기술로 쓰임

### 스프링 특징

1. 경량 컨테이너로서 자바 객체를 직접 관리
2. 제어 역행(IoC: Inversion of Control)
   - 애플리케이션의 느슨한 결합을 도모
   - 컨트롤의 제어권이 개발자가 아닌 프레임워크에 있으므로 필요에 따라 스프링에서 사용자의 코드를 호출하는 방식
3. 의존성 주입(DI: Dependency Injection) ★
   - 각각의 계층이나 서비스들 간에 의존성이 존재할 경우 프레임워크가 서로 연결시줌
4. 관점지향 프로그래밍(AOP: Aspect-Oriented Programming) ★
   - 트랜잭션이나 로깅, 보안과 같이 여러 모듈에서 <u>공통적으로 사용하는 기능의 경우 해당 기능을 분리</u>하여 관리할 수 있음
5. 트랜잭션 관리 프레임워크
   - 추상화된 트랜잭션 관리를 지원
   - 설정파일(xml, java, property 등)을 이용한 선언적인 방식 및 프로그래밍을 통한 방식을 모두 지원
6. MVC 패턴
   - Spring MVC라 불리는 MVC 패턴을 사용
   - DispatcherServlet이 Controller 역할을 담당

### 스프링 모듈

1. Spring Core

   - Spring 프레임워크의 근간이 되는 요소
   - IoC 또는 DI 기능을 지원하는 영역 담당
   - BeanFactory를 기반으로 Bean 클래스들을 제어할 수 있는 기능을 지원

2. Spring Context

   - Spring Core 바로 위에 있으면서 Spring Core에서 지원하는 기능 외에 추가적인 기능과 좀 더 쉬운 개발이 가능하도록 지원
   - 또한 JNDI, EJB등을 위한 Adaptor들을 포함

3. Spring DAO

   - 일반적으로 많이 사용해왔던 JDBC 기반하의 DAO 개발을 좀 더 쉽고 일관된 방법으로 개발하는 것이 가능하도록 지원

4. Spring ORM

5. Spring AOP

   - Spring 프레임워크에 Aspect Oriented Programming을 지원하는 기능
   - 이 기능은 AOP Alliance 기반 하에서 개발

6. Spring Web

   - Web Application 개발에 필요한 Web Application Context와 Multipart Request 등의 기능을 지원

   - 또한 Structs, Webwork와 같은 프레임워크의 통합을 지원하는 부분을 담당

7. Spring Web MVC

   - Spring 프레임워크에서 독립적으로 Web UI Layer에 Model-View-Controlelr를 지원하기 위한 기능
   - 지금까지 Structs, Webwork가 담당했던 기능들을 Spring Web MVC를 이용해 대체하는 것이 가능
   - 또한 Velocity, Excel, PDF와 같은 다양한 UI 기술들을 사용하기 위한 API를 제공

---

### References

[스프링 정의 및 특징 정리](https://goddaehee.tistory.com/156)
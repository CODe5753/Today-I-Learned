# Spring MVC 패턴
MVC는 **Model-View-Controller**의 약자이며 개발할 때 3가지 형태로 구분하여 개발하는 **소프트웨어 개발 방법론**



### Model

핵심 비즈니스 로직, DB 설계

### Controller

요청을 받아서 Model, View를 연결시켜주는 역할

### View

화면(유저)의 보여지는 부분



## MVC1

![img](res/222BF637521AF15B25.jpeg)

### 특징

- JSP로 구현한 기존 웹 어플리케이션은 MVC1 구조로 **웹 브라우저의 요청을 JSP가 받아서 처리**하는 구조
- JSP 페이지에 비즈니스 로직을 처리하기 위한 코드와 웹 브라우저에 결과를 보여주기 위한 출력 관리 코드가 뒤섞여 있는 구조
- JSP 내에서 표현(View), 저장(Model), 처리(Controller)되므로 재사용이 힘들고, 가독성이 떨어지고, 유지보수가 어려움

### 정리

- 정의: 모든 클라이언트 요청과 응답을 JSP가 담당하는 구조
- 장점: 단순한 페이지 작성으로 쉽게 구현이 가능. 중소형 프로젝트에 적합
- 단점: 웹 애플리케이션이 복잡해지면 유지보수 문제 발생

## MVC2

![img](res/2311AC46521AF3E80A.jpeg)

### 특징

- MVC1과 달리 웹 브라우저의 요청을 하나의 서블릿이 받게 됨
- 서블릿은 웹 브라우저의 요청을 처리한 후 결과를 JSP 페이지로 포워딩 함

### 정리

- 정의: 클라이언트의 요청/응답, 비즈니스 로직처리 부분을 모듈화 시킨 구조
- 장점: 처리작업의 분리로 인해 유지보수와 확장이 용이
- 단점: 구조 설계를 위한 시간이 많이 소요되므로 개발 기간이 증가

## Spring MVC

### 특징

`DispatcherServlet`이 `Controller` 부분을 처리함

### 순서

1. `Client`가 `DispatcherServlet`에게 요청을 보냄
2. `DispatcherServlet`은 `HandlerMapping`을 통해 요청 URL과 매칭되는 컨트롤러를 검색함
3. `DispatcherServlet`은 `HandlerAdapter`에게 처리를 요청함
4. `HandlerAdapter`는 `Controller`에게 실행을 요청함
5. `Controller`는 실행 결과를 `ModelAndView`/`String`/`Void` 형태로 리턴함
6. `HandlerAdapter`는 해당 결과를 `DispatcherServlet`에게 반환함
7. `DispatcherServlet`은 `ViewResolver`를 통해 컨트롤러 실행 결과를 보여줄 `View`를 탐색함
8. `DispatcherServlet`은 `View`에게 응답 생성을 요청함
9. `View`는 `JSP`로 응답을 생성하고 `Client`에게 응답함

---
### 참고 문헌

[디자인패턴-MVC패턴이란](https://medium.com/@jang.wangsu/%EB%94%94%EC%9E%90%EC%9D%B8%ED%8C%A8%ED%84%B4-mvc-%ED%8C%A8%ED%84%B4%EC%9D%B4%EB%9E%80-1d74fac6e256)

[MVC1, MVC2 패턴의 차이점과 Spring MVC 구조](https://nickjoit.tistory.com/9)
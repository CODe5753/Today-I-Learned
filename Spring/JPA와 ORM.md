#### JPA와 ORM

##### JPA?

- JPA는 ORM을 사용하기 위한 인터페이스를 모아둔 것
- JPA를 사용하기 위해서는 JPA를 구현한 Hibernate, EclipseLink, DataNucleus같은 ORM 프레임워크를 사용해야함

##### ORM?

- 객체와 DB의 테이블이 매핑을 이루는 것
- 즉, 객체가 테이블이 되도록 매핑 시켜주는 것
- SQL Query가 아닌 직관적인 코드(메서드)로서 데이터 조작이 가능
- 생산성이 매우 높아짐
- 하지만 ORM으로 표현하는데 한계가 있음
- raw query에 비해 느림
- `JDBC` < `Mybatis` < `ORM` 순으로 편함

#### QueryDSL

`com.ssafy.db.entity.QUser.java`에 보면 User Table을 생성하는 로직이 있습니다.

- SQL을 코드로 작성할 수 있도록 도와주는 빌더

- JPA 크리테이라에 비해 편리하고 실용적

- 오픈소스

  ##### QueryDSL 왜 써? SQL의 문제점?

  - SQL은 문자열이기에 Type-check가 불가능

  - 컴파일 시점에 알 수 있는 방법이 없음(자바와 문자열의 한계)

  - 해당 로직 실행 전까지 작동여부 확인을 할 수 없음

  - 쿼리 실행 시점에 오류를 발견함

    오타가 있는 경우

    ```SELECT * FROM MEMBERRRRR WHERE MEMBER_ID = '100'```

  ##### QueryDSL 장점?

  - 문자가 아닌 코드로 작성
  - 컴파일 시점에 문법 오류 발견
  - 코드 자동완성(IDE 도움)
  - 동적 쿼리
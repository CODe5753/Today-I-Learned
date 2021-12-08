### [원글로 이동](https://imksh.com/95)

---

## **개요**

[지난번 작성했던 글](https://imksh.com/94)에 이어 어떻게 민감정보를 숨기는지에 대해 작성하려고 합니다.

application.properties 또는 application.yml 파일을 작성하다 보면 datasource.**username**, datasource.**password**와 같이 형상관리 페이지에는 숨기고 싶은 정보들이 존재합니다.

이를 숨기거나 암호화할 수 있는 방법이 여러 개 존재하는데, 이 중 **사용자 입력을 통해 application.yml에 Argument 전달하는 방법**을 포스팅합니다.

---

## **결과물**

```
java -jar {jar 경로} --datasource.username=강승현 --datasource.password=비밀번호 --datasource.url=링크
```

위와 같이 **\--변수명=value** 형태로 값을 전달하게 될 것입니다.

---

## **방법**

.properties나 .yml 둘 중 어떤 것을 사용해도 상관없습니다.

**.yml 사용 시**

```
spring:
  datasource:
    url: ${datasource.url}
    username: ${datasource.username}
    password: ${datasource.password}
```

**.properties 사용 시**

```
spring.datasource.url: ${datasource.url}
spring.datasource.username: ${datasource.username}
spring.datasource.password: ${datasource.password}
```

여기서 ${  }  를 통해 argument 이름을 정할 수 있으며 상황에 맞게 원하는 이름으로 변경하면 됩니다.

저는 datasource의 username임을 명시하기 위해 datasource.username을 사용했지만 입력 시 너무 귀찮다고 하면, username 또는 USERNAME 처럼 대문자로 명시해도 됩니다.

이곳에 명시된 argument는 command에서 입력될 때 같은 이름이어야 합니다.

---

## **예시**

민감정보인 username을 전달한다고 가정하겠습니다.

```
spring:
  datasource:
    username: ${DATASOURCE_USERNAME}
```

위와 같이 네이밍을 했다면 커맨드에선 아래와 같이 전달하면 됩니다.

```
java -jar {jar 경로} --DATASOURCE_USERNAME=강승현
```
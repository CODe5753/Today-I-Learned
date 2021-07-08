# @ExceptionHandler, @ControllerAdvice

### 예외처리 과정

CURD 프로젝트를 하면서 예외 처리를 if문이나 try-catch나 상위 메서드로 예외를 던져주는 등 코드가 점점 복잡해지는 것을 경험했습니다.

즉 이후에 코드가 변경이 되는 경우 유지보수를 할 때마다 난감했던 기억이 있는데 이런 점을 개선하기 위해 @ControllerException, @ControllerAdvice를 사용합니다.

### @ExceptionHandler

@Controller, @RestController가 적용된 Bean내에서 발생하는 예외를 잡아 **하나의 메서드에서 처리**하는 기능을 하며 아래와 같이 적용합니다.

```java
@RestController
public class MyRestController{
   	@ExceptionHandler(NullPointerException.class)
    public Object nullex(Exception e){
        System.err.println(e.getClass());
        return "myService";
    }
}
```

또한 { Exception1.class, Exception2.class } 처럼 두 개 이상 등록도 가능합니다.

#### 주의사항

- 리턴 타입은 자유
- @ExceptionHandler를 적용한 Controller에서만 작동

### @ControllerAdvice

@ExceptionHandler는 하나의 클래스에 관여하지만, **@ControllerAdvice는 모든 @Controller에 관여**합니다.

```java
@RestController
public class MyAdvice{
    @ExceptionHandler(CustomException.class)
    public String custom(){
        return "hello custom";
    }
}
```



--------

##### 참고 페이지

- https://jeong-pro.tistory.com/195
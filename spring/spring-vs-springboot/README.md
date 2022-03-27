# Spring vs Spring boot

### 의존성 관리 측면

Spring에서는 설정에 너무 많은 시간을 소요합니다. 각 dependency마다 버전 호환성도 체크를 해야하지만 Spring boot에서는 이를 알아서 제공해주는 `spring-boot-starter`가 존재합니다.

### 자동 설정

기존 Spring에서는 Datasource만 생각해도 추가해야하는 데이터가 꽤 많습니다.

```java
@Bean
public DataSource dataSource(){
    return new EmbeddedDatabaseBuilder()
        	.setType(EmbeddedDatabaseType.H2)
        	.setName("imksh")
        	.addScript("schema.sql")
        	.setScriptEncoding("UTF-8")
        	.build();
}

@Bean
public JdbcTemplate jdbcTemplate(DataSource dataSource){
    return new JdbcTemplate(dataSource);
}
```



하지만 SpringBoot에서는 properties나 yaml로 간단히 작성이 가능합니다.

```yaml
spring:
	datasource:
		driver-class-name: org.h2.Driver
		url: jdbc:h2:mem:imkshdb
		username: testname
		password:
	h2:
		console:
			enabled: true
```

properties는 한 줄에 모든 내용을 작성하게 되면서 중복되는 내용이 계속해서 쓰입니다.

yaml은 위와 같이 tree형태로 중복된 부분을 최소화 하기 때문에 가독성 측면에서 좋습니다.

### 내장 WAS

대표적인 WAS엔 Tomcat이 있습니다.

Spring에서는 배포를 하기 위해서 `WAR 패키징` -> `WAS 설치` -> `WAS에 WAR 올리기` 순을 거쳤지만

Boot에선 이미 WAS가 내장되어 있기에 위와 같이 번거로운 과정을 거칠 필요가 없습니다.

### 모니터링

Spring의 여러 모듈 중에 `Actuator`라는 모듈이 있습니다. `애플리케이션의 관리 및 모니터링 지원`역할을 해주는데, 엔드포인트에서 헬스체크와 같은 정보를 노출할 수 있습니다. 하지만, 민감한 정보도 많으므로 보안(Spring Security)에 신경써야 합니다.


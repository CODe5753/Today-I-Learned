# Gradle 빌드 자동화

### 빌드란?

소스코드 파일을 컴퓨터에서 실행할 수 있는 가공물(`Artifact`)로 변환하는 과정

단순 **실행**과는 다름

#### 과정?

1. 소스 코드 컴파일
2. `테스트 코드` 컴파일
3. `테스트 코드` 실행
4. `테스트 코드` 리포트 작성
5. 기타 추가 설정한 작업 진행
6. 패키징 수행
   - JAVA 라이브러리 외에 외부 코드를 사용하는 경우 묶어줌
7. 최종 SW 결과물(Artifact)를 만들어 냄


### 실행(run)이란?

내가 작성한 코드 또는 테스트 코드를 컴파일을 거쳐 작동하는 것

인터프리터 언어(javascript, python)는 컴파일이 필요 없다.



### 빌드 툴

이런 빌드를 수동으로 진행한다면 많은 자원(시간)이 소모된다.

위와 같은 과정을 실수라도 하는 날엔...

그래서 빌드 툴이라는 것이 제공된다.

1. 소스코드의 빌드 과정을 자동으로 처리
2. 외부 소스 코드(외부 라이브러리) 자동 추가/관리

#### Ant

- 설정을 위해 xml 사용
- 간단하고 사용하기 쉬움
- 복잡한 처리를 하려 하면 빌드 스크립트가 장황해져 관리가 어려움
- 외부 라이브러리를 관리하는 구조가 없다
- 즉, 빌드만을 관리함

#### Maven

- 설정을 위해 xml 사용 (pom.xml)
- 외부 라이브러리를 관리할 수 있다
  - 라이브러리에 변동 사항이 있으면 자동으로 업데이트 하여 적용됨
- 장황한 빌드 스크립트 문제를 해결
- 라이프 사이클이 도입됨
  - clean이 가능하고 순서도 변경이 가능함
- 특정 경우에 xml이 복잡해짐
- xml 자체의 한계가 있음
- Ant가 가진 단점을 극복

#### Gradle

- 설정을 위해 groovy(JVM 언어)를 사용
- 외부 라이브러리 관리 가능
- 유연하게 빌드 스크립트를 작성할 수 있음
- 성능이 뛰어남 (maven의 **최대** 100배정도)
- 안드로이드에서 표준 빌드 시스템으로 채택함 이후 사용자 급증 
- maven에 비해 더 간결한 구성이 가능
  - xml은 태그로 관리되기 때문에 자체 언어인 groovy를 사용하기 때문

### Maven vs Gradle

- Gradle에 비해 Maven이 점유율이 더 높은 상황(점차 Gradle이 증가중)
- Gradle에 비해 Maven의 성능이 떨어짐
- 대규모 프로젝트에서 Gradle의 성능이 더 좋음
- Maven은 `pom.xml`, Gradle은 `build.gradle`
- Gradle은 설치 없이 사용 가능(Gradle Wrapper를 사용)



###  Maven vs Gradle 성능 측면

#### Incremental Build

- Gradle은 어떤 Task가 업데이트 되었고 안되었는지 체크하기 때문에 `Incremental Build`를 허용

- 즉, 이미 업데이트된 Task는 업데이트를 안한다는 뜻!
- 이게 프로젝트 규모(빌드 규모)가 커질수록 빌드 시간의 차이가 점점 벌어진다

#### 설정 주입 방식

- Maven의 경우 멀티 프로젝트에서 특정 설정을 다른 모듈에서 사용하려면 상속을 받아야 함
- Gradle은 설정 주입 방식을 제공함

#### 캐시

- Gradle은 Concurrent에 안전한 캐시를 허용
  - 2개 이상의 프로젝트에서 동일한 캐시를 사용할 경우, 서로 Overwrite되지 않도록 checksum 기반의 캐시를 사용
  - 캐시를 Repository와 동기화 가능

#### 커스터마이징

- 고도로 사용자 정의된 빌드를 작성하기 위해선 Groovy 기반의 Gradle을 사용하는게 훨씬 효율적

#### 코드로 직접 비교

플러그인을 추가하고 빌드하는 과정에서 코드 차이를 살펴보겠습니다.

- Maven 예시 코드

  ```xml
  <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
      <modelVersion>4.0.0</modelVersion>
      <groupId>com.programming.mitra</groupId>
      <artifactId>java-build-tools</artifactId>
      <packaging>jar</packaging>
      <version>1.0</version>
      <dependencies>
          <dependency>
              <groupId>junit</groupId>
              <artifactId>junit</artifactId>
              <version>4.11</version>
          </dependency>
      </dependencies>
      <build>
          <plugins>
              <plugin>
                  <groupId>org.apache.maven.plugins</groupId>
                  <artifactId>maven-checkstyle-plugin</artifactId>
                  <version>2.12.1</version>
                  <executions>
                      <execution>
                          <configuration>
                              <configLocation>config/checkstyle/checkstyle.xml</configLocation>
                              <consoleOutput>true</consoleOutput>
                              <failsOnError>true</failsOnError>
                          </configuration>
                          <goals>
                              <goal>check</goal>
                          </goals>
                      </execution>
                  </executions>
              </plugin>
              <plugin>
                  <groupId>org.codehaus.mojo</groupId>
                  <artifactId>findbugs-maven-plugin</artifactId>
                  <version>2.5.4</version>
                  <executions>
                      <execution>
                          <goals>
                              <goal>check</goal>
                          </goals>
                      </execution>
                  </executions>
              </plugin>
              <plugin>
                  <groupId>org.apache.maven.plugins</groupId>
                  <artifactId>maven-pmd-plugin</artifactId>
                  <version>3.1</version>
                  <executions>
                      <execution>
                          <goals>
                              <goal>check</goal>
                          </goals>
                      </execution>
                  </executions>
              </plugin>
          </plugins>
      </build>
  </project>
  ```

  이런 코드를 Gradle로는 아래와 같이 설정할 수 있습니다.

- Gradle 코드

  ```groovy
  apply plugin:'java'
  apply plugin:'checkstyle'
  apply plugin:'findbugs'
  apply plugin:'pmd'
  version ='1.0'
  repositories {
      mavenCentral()
  }
  dependencies {
      testCompile group:'junit', name:'junit', version:'4.11'
  }
  ```

  `gradle tasks --all`
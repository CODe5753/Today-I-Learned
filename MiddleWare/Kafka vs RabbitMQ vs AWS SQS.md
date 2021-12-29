# Kafka vs RabbitMQ vs AWS SNS/SQS 어떤 것을 선택해야 할까?
> 해당 포스트는 [원문](https://www.aspecto.io/blog/kafka-vs-rabbitmq-vs-aws-sns-sqs-which-broker-to-choose/)을 번역 및 의역하였습니다.  
> 1차 직역후 의역할 예정입니다.

MSA는 메시징 및 비동기 통신에 크게 의존합니다.

어떤 메세지 브로커를 사용할 지 선택하는 것은 매우 중요한 단계입니다.
하지만, 어떻게 `최선의` 메세지 브로커를 사용할 지 선택하는 것은 결코 쉽지 않습니다..

이 포스팅에서는 메세지 브로커에서도 흔히 볼 수 있는 Kafka, RabbitMQ, AWS SQS 세 가지에 대해 `선택하기 수월하도록` 간략한 설명을 제공합니다.

## Apache Kafka
우리가 잘 알고있는 [Apache](https://www.apache.org/)에서 개발 및 유지관리하는 오픈 소스 메시지 브로커입니다.

### 주요 특징
- Focus on streamable content, working with large data streams
- Message persistence and reprocessing capabilities are core features
- On-site hosting with third party options

> Kafka provides optimized stream-based processing of events, with a publish/subscribe model driving the communications between consumers.  

Kafka는 publish/subscribe 모델을 통해 최적화된 스트림 기반 이벤트 처리를 제공합니다.

> These events can be subdivided into topics, allowing for greater organization of your distributed application’s communication patterns, and are partitioned onto multiple servers within a cluster, allowing for a resilient and highly performant message delivery system.  

이러한 이벤트는 주제로 세분화되어 분산 응용 프로그램의 통신 패턴을 보다 잘 구성할 수 있으며 클러스터 내의 여러 서버로 분할되어 탄력적이고 고성능인 메시지 전달 시스템을 허용합니다.

### 기술 세부 사항 및 배포

### 강점 및 약점

## RabbitMQ

## Aws SQS/SNS

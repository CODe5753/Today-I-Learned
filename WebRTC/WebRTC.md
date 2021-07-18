# WebRTC

- 웹브라우저에서 바로 실시간 소통을 사용할 수 있음
- 구글이 VoIP 회사인 GIPS를 인수한 후 해당 회사의 음성/영상 코덱 및 에코캔슬링 기술을 갖게됨
- 이 기술을  WebRTC라는 이름으로 공개함(2011년)

### WebRTC 통신 방식

- P2P (Peer to Peer): 두 단말이 서로 1:1 통신하는 방식
- MCU, SFU: 대규모 서비스를 구축할 때 사용하는 방식, 중앙 서버를 두어 트래픽 중계하도록 함
  - Zoom, Google Meet에선 SFU를 사용한 대표적 기업

두 기기가 실시간 소통을 하기 위해 다음과 같은 사항이 필요합니다.

- 기기의 스트리밍 오디오 / 비디오 / 데이터를 가져올 수 있을 것
- 소통하고자 하는 기기의 IP 주소와 포트 등 네트워크 데이터 필요
- 에러 보고, 세션 초기화를 위해 신호 통신을 관리해야 함
- 서로 소통할 수 있는 해상도인지, 코덱은 맞는지 capability 정보 교환
- 실제 연결을 맺음
- 이후 스티리밍 오디오/비디오/데이터를 주고 받을 수 있어야 함


이를 위해 WebRTC는 다음 API를 제공합니다.

- MediaStream: 사용자의 카메라 혹은 마이크 등 input 기기의 데이터 스트림에 접근
- RTCPeerConnection: 암호화/대역폭 관리 기능. 오디오/비디오 연결을 함
- RTCDataChannel: 일반적인 데이터 P2P 통신



---

#### 참고자료

- [WebRTC](https://velog.io/@skyni/WebRTC%EC%97%90-%EB%8C%80%ED%95%9C-%EC%A0%95%EB%A6%AC)
- [WebRTC 연결방식](https://6987.tistory.com/entry/WebRTC-%EB%AF%B8%EB%94%94%EC%96%B4-%EC%97%B0%EA%B2%B0-%EB%B0%A9%EC%8B%9D-MCU-SFU-P2P)
- [WebRTC Kurento](https://gh402.tistory.com/43)
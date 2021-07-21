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

  

### STUN(Session Traversal Utillities for NAT) 서버

<p align="center"><img src="/res/webrtc-stun.png"></p>

- **클라이언트 자신의 Public Address(IP:PORT)를 알려줌**
- peer간의 직접 연결을 막는 등의 라우터 제한을 결정하는 프로토콜 (현재 다른 peer가 접근 가능한지 여부 결정)
- 클라이언트는 인터넷을 통해 클라이언트의 Public Address와 라우터의 **NAT 뒤에 있는 클라이언트가 접근 가능한지에 대한 답변을 STUN 서버에 요청**
  - 이 이유는 NAT에 기재되어 있다

### NAT(Network Address Translation)

- 단말에 Public IP 주소를 할당하기 위해 사용
- 라우터는 Public IP 주소를 갖고 있고 모든 단말들은 라우터에 연결되어 있으며 Private IP 주소를 가짐
- 각각의 단말이 유일한 Public IP 없이 인터넷 상에서 검색 가능
  - 공유기에 Public IP가 물려있고 공유기 하위에 Private IP(192.168.0.XXX)가 물린것과 같다
- 몇몇 라우터는 **Symmetric NAT**라 불리는 제한을 위한 NAT를 사용한다. 즉, **peer들이 이전에 연결한 적 있는 연결만 허용**한다.
  - 따라서, **STUN 서버에 의해 Public IP를 발견한다 해도 모두가 연결할 수 있는 것은 아님**
    - **이를 위해 TURN이 필요**

### TURN(Traversal Using Relays around NAT) 서버

<p align="center"><img src="/res/webrtc-turn.png"></p>

- TURN 서버와 연결하고 모든 정보를 그 서버에 전달하는 것으로 Symmetric NAT 제한을 우회하는 것을 의미
- 이를 위해 TURN 서버와 연결을 한 후 **모든 peer들에게** "**저 서버에 모든 패킷을 보내고 다시 나(TURN 서버)에게 전달해줘**"라고 해야 한다
- 이 과정에서 **오버헤드가 발생**하고 다른 대안이 없을 경우에만 사용한다

---

#### 참고자료

- [WebRTC](https://velog.io/@skyni/WebRTC%EC%97%90-%EB%8C%80%ED%95%9C-%EC%A0%95%EB%A6%AC)
- [WebRTC 연결방식](https://6987.tistory.com/entry/WebRTC-%EB%AF%B8%EB%94%94%EC%96%B4-%EC%97%B0%EA%B2%B0-%EB%B0%A9%EC%8B%9D-MCU-SFU-P2P)
- [WebRTC Kurento](https://gh402.tistory.com/43)
- [WebRTC 이론 및 P2P, SFU 실험](https://millo-l.github.io/WebRTC-%EC%9D%B4%EB%A1%A0-%EC%A0%95%EB%A6%AC%ED%95%98%EA%B8%B0/)
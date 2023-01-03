- - -
# 2023_1_2
- - -
* 우분투 설치 20.04 버전 Vmware안에 설치
  * image 주소 : https://releases.ubuntu.com/focal/ 데스크탑 버전 설치
* ROS2 설치 :
  * foxy : sudo apt install ros-foxy-desktop ros-foxy-rmw-fastrtps* ros-foxy-rmw-cyclonedds*
* testpub testsub 으로 ROS2 정상작동 확인.
* trutlesim_node 실행 후 teleop으로 움직임 확인.
* github연동, commit 시행, m_pubsub패키지 해제 및 mpub.py일부 작성dddㅇㅇㅇㅇddd

- - -
# 2023_1_3
- - -
* 메세지 퍼블리셔(mpub) ,섭스크라이버(msub) 작성
* 노드 분석
* mtime.py 코드, metime.py, metimepub.py코드 완성과 테스트
* 구글슬라이스 사용 연습
* 코딩으로 만든 노드를 통해 터틀심 움직여보기
* ros2 run turtlesim turtlesim_node --ros-args -r __ns:=/ns2 네임 스페이스 지정 : 개별실행해보기
* 터틀심 스폰해서 추가하기
* ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.5 , y: 7.0, theta: 1.5, name: 'turtle2'}"
* 터틀심 색바꾸기
* ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "{r: 100, g: 50, b: 200, width : 5}"
* opencv 코드 테스트
[EOF]

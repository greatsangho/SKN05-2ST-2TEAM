# SKN05-2ST-2TEAM
✅2차 프로젝트
허상호,신혜원,안태영,윤상혁,박초연<br>
개발기간: 2024.10.16-10.17

# 1. 팀 소개
<table align=center>
  <tbody>
    <tr>
      <td align="center">
        <div>
          <img src="https://cdn.discordapp.com/attachments/1295905336607375404/1296392221632761856/image.jpg?ex=67121ed7&is=6710cd57&hm=c617ea39f63d9d21077b0bed807b0445d9dcf83f2531a32bdd3c39cfc016cf83&"width="100px;"height="100px;" alt=""/>
          <a href="https://github.com/greatsangho"><div align=center>허상호</div></a>
        </div>
      </td>
      <td align="center">
        <div>
          <img
            src="https://cdn.discordapp.com/attachments/1295905336607375404/1296393429277872158/image0.jpg?ex=67121ff7&is=6710ce77&hm=98fb46e2982c196d4489a79cf31c216b3eff95d450173c9f6393d52f6fc6f93d&"width="100px;" alt=""/>
          <a href="https://github.com/"><div align=center>신혜원</div></a>
        </div>
      </td>
      <td align="center">
        <img src="https://cdn.discordapp.com/attachments/1275735988542378018/1296390947009204334/IMG_6249.jpg?ex=67121da7&is=6710cc27&hm=a06076a4ec56ca236455d95d319653886c4c807b65f7c81548ad3eba792302f3&"width="100px;" alt=""/>
        <a href="https://blog.naver.com/anthony_0502"><div align=center>안태영</div></a>
      </td>
      <td align="center">
        <img src="https://cdn.discordapp.com/attachments/1295905336607375404/1296394252787384383/image0.jpg?ex=671220bb&is=6710cf3b&hm=1a3371c8fc0b18a066568477dea437e72447b42e9dabbd9032a3a54842a73da7&"width="100px;" alt=""/>
        <a href="https://github.com/ggreing"><div align=center>윤상혁</div></a>
      </td>
      <td align="center">
        <img src="https://cdn.discordapp.com/attachments/1295905336607375404/1296395243763273820/image1.jpg?ex=671221a7&is=6710d027&hm=ed0b69e1156459d140a9bb610650f5ec4e3e76a94d80f23c6478ad4974dc77eb&"width="100px;" alt=""/>
        <a href="https://github.com/"><div align=center>박초연</div></a>
      </td>
    </tr>
  </tbody>
</table>

# 2. 기술 스택
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=white"/></a>
<img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"/></a>
<img src="https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Google Colab-F9AB00?style=flat-square&logo=Google Colab&logoColor=white"/></a>
<img src="https://img.shields.io/badge/streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/></a>

# 3. 프로젝트 개요
- 선정 주제: 캘리포니아 지역 통신사 고객 이탈 예측
- 데이터 수: 행 7,044개, 열 66개
- 프로젝트 필요성(배경): 한국 통신시장 점유
- 프로젝트 목표: 캘리포니아 A통신사 고객 이탈률 예측을 통해 통신 시장에 대한 고찰
- 분석 프로세스

# 4. 데이터 분석 및 전처리
**<데이터 개요>**
- 컬럼 수: 총 66개의 컬럼 중 불필요한 37개의 컬럼 제거 후 29개 사용
- 결측치 처리: Offer, Total Charges 등
- 데이터의 특성을 고려하여 인코딩 진행: Age, Number of Dependents 등

**<전처리>**
- 결측치 처리: Offer, Total Charges 등
- 이상치 및 데이터 확인
- 연속형 데이터의 분포 확인
- 데이터 인코딩

**<상관관계 분석>**
- 주요 컬럼 및 최종 선정 컬럼
- 가설에 따른 이탈률

# 5. 모델 성능비교 및 해석
- 하이퍼파라미터 그리드 설정
- Vorint, Stacking
- 하이퍼파라미터 튜닝
- GBM
- ROC 커브 시각화 함수, Precision-recall 함수, 박스플롯 비교 함수

# 6. 시사점
- 통신사 이탈에 큰 영향을 미치는 주요 요인
- 현재 통신사가 놓치고 있는 점
- 고객 만족도 향상 전략

# 7. 통신사 고객 이탈 예측 ppt 링크
<a href="https://www.canva.com/design/DAGTuG1KW4w/Clzo1YJ_lDL_e5stxA1u5w/view?utm_content=DAGTuG1KW4w&utm_campaign=share_your_design&utm_medium=link&utm_source=shareyourdesignpanel#1">캔바 ppt 주소</a>

# 8. Streamlit 화면구현
![스트림릿 최종](https://github.com/user-attachments/assets/cac10952-3b85-4dca-bc11-f8e53dac6f70)

- 데이터 분석을 통해 고객 만족도, 약정 기간, 선물 제공이 큰 상관관계를 가지는 것을 확인함
- 이탈률이 56%인 사람에게 약정 기간에 따른 좋은 선물 제공함으로써 이탈률을 37% 까지 감소시킬 수 있음을 확인함

# 9. 한줄 회고
<!-- 주석 -->
**허상호**: 첫번째 프로젝트를 발판삼아 두번째 프로젝트는 더 재미있게 할 수 있었습니다. 대회 준비를 하며 공부했던 것이 많이 도움이 되었습니다~~!!
<!-- 주석 -->
**신혜원**: 다양한 모델을 돌려 예측값을 얻고 예측값을 가지고 비즈니스에 적용해 볼 수 있었던 좋은 기회였습니다.
<!-- 주석 -->
**안태영**: 머신러닝을 통해 고객 이탈 0.96 정확도를 달성을 경험했습니다. 많은 것들을 배우고 사용하는 유용한 시간이 되었습니다.
<!-- 주석 -->
**윤상혁**: 부트캠프를 수강하면서 배운 내용들을 복습할 수 있는 좋은 기회였다고 생각한다. 특히 이번에 시각화 관련 코드를 작성하면서 많이 익숙해져 좋았다.
<!-- 주석 -->
**박초연**: 팀원들에게 많이 배울 수 있었던 프로젝트 경험이었습니다!

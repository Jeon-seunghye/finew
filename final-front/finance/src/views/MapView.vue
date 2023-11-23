<template>
  <div class="container">
    <h1 class="headers">은행 찾기</h1>
    <hr>
    <div class="wrapping">
      <div class="selecting">
        <p>선택</p>
        <div class="selectloc">
          <select v-model="selectedProvince" @change="updateCityOptions">
            <option v-for="province in provinces" :value = "province" :key="province">{{ province }}</option>
          </select>
        </div>
        <div class="selectloc">
          <select v-model="selectedCity" @change="moveToCity">
              <option value="0">시/군/구</option>
            <option v-for="city in cities[selectedProvince]" :value = "city" :key="city">{{ city }}</option>
          </select>
        </div>
        <div class="button-group">
          <button @click="searchBanks">검색</button>
        </div>
      </div>
      <div class="containermap">
        <div id="map" class="map"></div>
      </div>
    </div>
    <div class="results">
      <div>
        <p style="font-weight: bold; font-size: larger;">검색 결과 {{ searchedBanks.length }}개</p>
      </div>
      <div v-if="searchedBanks" class="search-results">
        <ul>
          <li v-for="bank in searchedBanks" :key="bank.name">{{ bank.name }}</li>
        </ul>
      </div>
      <div v-else>
        <p>검색 결과가 없습니다.</p>
      </div>
    </div>
  </div>
  <p class="mb-0 bg-light text-center py-2" style="width: 100%; font-size: small;" >&copy; 2023 Finew All Rights Reserved. 본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.</p>
</template>

<script setup>
  import { ref, onMounted } from 'vue';

  let map = null;
  const markers = ref([]);
  const searchedBanks = ref([]);
  let infowindow = null;

  const provinces = [
      '서울 특별시', '인천 광역시', '부산 광역시', '광주 광역시', '대구 광역시', '대전 광역시', '제주도', '경기도',
      '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상남도', '경상북도'
    ];
    let selectedProvince = ref(provinces[0]);
    
    const cities = {
        '서울 특별시': ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'],
        '인천 광역시': ['강화군', '계양구', '남동구', '동구', '미추홀구', '부평구', '서구', '연수구', '중구'],
        '부산 광역시': ['강서구', '금정구', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구', '기장군'],
        '광주 광역시': ['광산구', '서구', '남구', '동구', '북구'],
        '대구 광역시': ['달서구', '남구', '달성군', '동구', '북구', '서구', '수성구', '중구'],
        '대전 광역시': ['대덕구', '동구', '서구', '유성구', '중구'],
        '제주도': ['서귀포시', '제주시'],
        '경기도': ['가평군', '강화군', '고양시', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시', '양평군', '여주군', '여주시', '연천군', '오산시', '옹진군', '용인시', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '하남시', '화성시', '인천시청'],
        '강원도': ['강릉시', '고성군', '동해시', '삼척시', '속초시', '양구군', '양양군', '영월군', '원주시', '인제군', '정선군', '철원군', '춘천시', '태백시', '평창군', '홍천군', '화천군', '횡성군'],
        '충청북도': ['청주시', '흥덕구', '충주시', '상당구', '청원구', '서원구', '제천시', '음성군', '진천군', '옥천군', '영동군', '증평군', '괴산군', '보은군', '단양군'],
        '충청남도': ['태안군', '서산시', '당진시', '아산시', '천안시', '예산군', '홍성군', '보령시', '청양군', '공주시', '부여군', '서천군', '계룡시', '논산시', '금산군'],
        '전라북도': ['군산시', '익산시', '전주시', '정읍시', '남원시', '김제시', '완주군', '진안군', '무주군', '장수군', '임실군', '순창군', '고창군', '부안군'],
        '전라남도': ['목포시', '여수시', '순천시', '나주시', '광양시', '담양군', '곡성군', '구례군', '고흥군', '보성군', '화순군', '장흥군', '강진군', '해남군', '영암군', '무안군', '함평군', '영광군', '장성군', '완도군', '진도군', '신안군'],
        '경상남도': ['거창군', '함양군', '산청군', '하동군', '합천군', '의령군', '진주시', '사천시', '남해군', '창녕군', '함안군', '고성군', '통영시', '밀양시', '창원시', '거제시', '김해시', '양산시'],
        '경상북도': ['포항시', '경주시', '김천시', '안동시', '구미시', '영주시', '영천시', '상주시', '문경시', '경산시', '군위군', '의성군', '청송군', '영양군', '영덕군', '청도군', '고령군', '성주군', '칠곡군', '예천군', '봉화군', '울진군', '울릉군'],
    };
    let selectedCity = ref(0);

  onMounted(() => {
    if (window.kakao && window.kakao.maps) {
      initMap();
    } else {
      const script = document.createElement('script');
      script.onload = () => kakao.maps.load(initMap);
      script.src =
        '//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=8d50621f2057740f292ad9da94105701&libraries=services,clusterer,drawing';
      document.head.appendChild(script);
    }
  });

  const fixedLevel = 3;

  function initMap() {
    const container = document.getElementById('map');
    const mapOption = {
      center: new kakao.maps.LatLng(37.566826, 126.9786567),
      level: fixedLevel
    };
    map = new kakao.maps.Map(container, mapOption);
  }

  function searchBanks() {
    if (!selectedCity) return;

    markers.value.forEach(marker => {
        marker.setMap(null);
    });
    markers.value = []

    const ps = new kakao.maps.services.Places(map);
    ps.categorySearch('BK9', placesSearchCB, { useMapBounds: true });
  }

  function searchedBanksFunction(data, searchedBanks) {
    const mappedBanks = data.map(place => {
      return {
        name: place.place_name,
        // 필요에 따라 추가 정보 추가
      };
    });
    searchedBanks.value = mappedBanks;
  }

  function placesSearchCB(data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {
      const bounds = new kakao.maps.LatLngBounds();
      markers.value = [];
      
      searchedBanksFunction(data, searchedBanks);

      for (let i = 0; i < data.length; i++) {
        const marker = displayMarker(data[i]);
        markers.value.push(marker);
        bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
        searchedBanksFunction(data, searchedBanks); // 검색된 은행을 처리하는 함수 호출
      }
      // 검색된 장소들의 중심 좌표를 얻어와 지도의 중심으로 설정합니다.
      const centerLatLng = bounds.getCenter();
      map.setCenter(centerLatLng);
    }
  }

  function displayMarker(place) {
    const marker = new kakao.maps.Marker({
      map: map,
      position: new kakao.maps.LatLng(place.y, place.x)
    });

    infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });

    kakao.maps.event.addListener(marker, 'click', function() {
      infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
      infowindow.open(map, marker);
    });

    return marker;
  }

  function updateCityOptions() {
    console.log(selectedProvince)
    selectedCity.value = 0;
  }

  function moveToCity() {
    if (!selectedCity) return;
    console.log(selectedCity.value, selectedProvince.value)
    const geocoder = new kakao.maps.services.Geocoder();
    const callback = function(result, status) {
    if (status === kakao.maps.services.Status.OK) {
      // 첫 번째 검색 결과의 위치를 중심으로 이동합니다.
      if (result.length > 0) {
        const centerLatLng = new kakao.maps.LatLng(result[0].y, result[0].x);
        map.panTo(centerLatLng);
      }
    }
  };
  geocoder.addressSearch(selectedProvince.value + selectedCity.value, callback);
  }
</script>

<style scoped>
.wrapping{
  display: flex;
}
.headers{
  color: #255580;
  font-weight: bold;
  margin-top: 40px;
  margin-bottom: 20px;
}
.container{
  font-family: 'Noto Sans KR', sans-serif; /* Noto Sans KR 글씨체 적용 */
  margin-top: 20px;
  margin: 0 auto;
}
.containermap{
  margin-left: 30px;
  margin-top: 10px;
  width: 100%;
  height: 400px;
  border-radius: 15px;
  margin-bottom: 20px;
}
.selecting{
  padding-left: 20px;
  margin-top: 20px;
  margin-bottom: 20px;
}
.selecting select{
  width: 100px;
}
.selectloc{
  margin-bottom: 20px;
}
.map {
  margin-top: 10px;
  width: 100%;
  height: 400px;
  border-radius: 15px;
  margin-bottom: 20px;
}

.button-group{
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 15px;
  text-align: center;
  width: 100px;
}

.results{
  font-family: 'Noto Sans KR', sans-serif;
  margin-top: 10px;
  font-size: 15px;
}
.search-results {
  margin-bottom: 100px;
  margin-top: 20px;
  font-family: 'Noto Sans KR', sans-serif;
}
button {
  margin: 0 3px;
  border-radius: 5px;
  border: 1px solid gray;
  width: 100px;
}
</style>
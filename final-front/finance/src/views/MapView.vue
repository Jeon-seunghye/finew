<template>
  <div>
    <select v-model="selectedDistrict" @change="searchBanksByDistrict">
      <option v-for="district in seoulDistricts" :key="district.name" :value="district.name">
        {{ district.name }}
      </option>
    </select>
    <div ref="map" style="width: 100%; height: 500px;"></div>
  </div>
</template>


<script>
  import { ref, onMounted } from "vue";

  export default {
    setup() {
      const map = ref(null);
      const selectedDistrict = ref("종로구");
      const markers = ref([]);

      const seoulDistricts = [
        { name: "종로구", lat: 37.572036, lng: 126.976594 },
        { name: "중구", lat: 37.564613, lng: 126.997596 },
        { name: "용산구", lat: 37.531100, lng: 126.981074 },
        // ... (다른 구의 위도 경도 추가)
      ];

      onMounted(() => {
        const script = document.createElement("script");
        script.type = "text/javascript";
        script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=8d50621f2057740f292ad9da94105701&libraries=services&autoload=false`;
        script.async = true;
        script.onload = () => initializeMap(map);
        document.head.appendChild(script);
      });

      const initializeMap = (mapRef) => {
        window.kakao.maps.load(() => {
          const container = mapRef.value;
          const options = {
            center: new window.kakao.maps.LatLng(37.5665, 126.9780),
            level: 5,
          };

          const kakaoMap = new window.kakao.maps.Map(container, options);

          // 초기화 시에도 선택한 구에 대한 은행을 검색하고 해당 위치로 이동
          searchBanks(selectedDistrict.value, kakaoMap);
        });
      };

      const searchBanksByDistrict = () => {
        const district = selectedDistrict.value;
        searchBanks(district, map.value);
      };

      const searchBanks = (gu, map) => {
        const ps = new window.kakao.maps.services.Places();
        ps.keywordSearch(`은행 ${gu}`, (data, status, pagination) => {
          if (status === window.kakao.maps.services.Status.OK) {
            clearMarkers();
            for (let i = 0; i < data.length; i++) {
              displayMarker(data[i], map);
            }

            // 검색된 은행이 있을 경우, 첫 번째 은행 위치로 이동
            if (data.length > 0) {
              const firstBank = data[0];
              map.panTo(new window.kakao.maps.LatLng(firstBank.y, firstBank.x));
            }
          }
        });
      };

      const displayMarker = (place, map) => {
        const marker = new window.kakao.maps.Marker({
          map: map,
          position: new window.kakao.maps.LatLng(place.y, place.x),
        });

        window.kakao.maps.event.addListener(marker, "click", () => {
          console.log(place);
        });

        markers.value.push(marker);
      };

      const clearMarkers = () => {
        markers.value.forEach((marker) => {
          marker.setMap(null);
        });
        markers.value = [];
      };

      return { map, selectedDistrict, seoulDistricts, searchBanksByDistrict };
    },
  };
</script>

<style scoped>
#map {
  width: 90%;
  height: 500px;
}
</style>
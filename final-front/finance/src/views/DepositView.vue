
<template>
  <div id="nav">
    <h1>예금</h1>
    <div>
      <h3>검색</h3>
      <div>
        <select name="bank_name" id="bank_name">
          <option value="">
            
          </option>
        </select>
      </div>
      <div>
        <select name="save_term" id="save_term">
          <option value="">

          </option>
        </select>
      </div>
      <div>
        <button>검색</button>
      </div>
    </div>
  </div>
</template>

<script>
// export default {
//   name: "Nav",
//   data() {
//     return {
//       keyword: ''
//     }
//   },
//   methods: {
//     searchresultshow(keyword) {
//       if (keyword !== ''){ //검색어를 입력한 경우
//         this.$router.push({
//           name: "SearchPage",
//           params: {
//             keyword: this.keyword,
//             isResultShow: true,
//           },
//         });
//         this.keyword = ''
//         console.log('"',keyword,'"' + ' 검색')
//       } else {
//         alert('검색어를 입력해주세요!')  //검색어를 입력하지 않은 경우
//       }
//     },
//   }
// };
</script>
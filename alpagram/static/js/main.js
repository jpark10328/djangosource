$("#search").on({
  keyup: function () {
    //검색 창에 텍스트가 입력되면 입력된 글자 가져오기
    keyword = $(this).val();
    console.log(keyword);
    //keyword 서버로 전송
    $.ajax({
      url: "/apis/v1/users/list/",
      data: {
        keyword: keyword,
      },
      success: function (response) {
        console.log(response);
        //도착한 결과를 search-list 영역에 보여주기
        let str = "<div>";
        $.each(response.result, function (idx, user) {
          str += "<div class='row justify-content-start mt-2'><div class='col-sm-3'>";
          str += "<a href='" + user.id + "'>";
          str += "<img src='" + user.image + "'></div>";
          str += "<div class='col-sm-9'><div class='row'><div class='col'>";
          str += "<span class='small'>" + user.nickname + "</span></div></div></a>";
          str += "<div class='row'><div class='col'>";
          str += "<span class='small'>" + user.email + "</span></div></div></a>";
          str += "</div></div>";
        });
        str += "</div>";
        $(".search-list").html(str);
      },
      error: function (req, textstatus, error) {
        console.log(req.responseJSON.message);
        $(".search-list").html("<div>" + req.responseJSON.message + "</div>");
      },
    });
  },
  click: function () {
    $(".search-list").css("display", "block");
  },
  focusout: function () {
    $("#search").val("");
  },
});

//검색결과에서 클릭 시 : 이벤트 위임(현재 있는 영역에 이벤트를 걸었다가 나중에 다른 요소에게 이벤트를 넘김)
$(".search-list").on("click", "a", function (e) {
  //이벤트 중지
  e.preventDefault();
  //search-list 영역 숨기기
  $(".search-list").css("display", "none");
  //a가 가지고 있는 userid 가져오기
  userid = $(this).attr("href");
  //특정 user 정보를 볼 수 있는 url 이동
  location.href = "/users/get/?id=" + userid;
});

//새글 등록시 모달 창 이미지 띄우기
Dropzone.autoDiscover = false;
const dropzoneUploader = new Dropzone("form.dropzone", {
  init: function () {
    $("#upload").click(function () {
      //큐에 있던 이미지 파일 호출
      dropzoneUploader.processQueue();
    });
    this.on("addedfile", (file) => {
      console.log("A file has been added");
    });
    this.on("sending", function (file, xhr, formData) {
      formData.append("text", $("#text").val());
    });
    this.on("success", function (file, response) {
      console.log("성공");
      location.reload();
      $(".modal").hide();
    });
    this.on("queuecomplete", function () {
      console.log("업로드 성공");
    });
    this.on("error", function () {
      console.log("error 발생. 다시 시도해 주세요");
    });
  },

  paramName: "file",
  parallUploads: 10, //이미지 업로드 허용 갯수
  autoProcessQueue: false, //큐에 추가만할 뿐 자동으로 처리되지 않음
  type: "POST",
  acceptedFiles: ".jpg, .png, .gif, .jpeg",
  uploadMultiple: true,
});

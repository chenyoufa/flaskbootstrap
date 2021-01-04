"use strict";

var service = new Service();
Vue.component('mine', {
  template: "\n    <div class=\"mine-content\">\n      <div class=\"avatar\">\n        <img src=\"../images/avatar_4.jpeg\" alt=\"\">\n      </div>\n      <div class=\"user-info\">\n        <p>\u59D3\u540D\uFF1A{{userInfo.UserName}}</p>\n        <p>\u6240\u5C5E\u5355\u4F4D\uFF1A{{userInfo.Company}}</p>\n      </div>\n      <div v-if=\"isBinding\">\n        <div class=\"form-main\">\n          <p>\u5BC6\u7801</p>\n          <input v-model=\"psdText\" type=\"password\" placeholder=\"\u5BC6\u7801\">\n        </div>\n        <div class=\"form-main\">\n          <p>\u786E\u8BA4\u5BC6\u7801</p>\n          <input v-model=\"psdConfirmText\" type=\"password\" placeholder=\"\u786E\u8BA4\u5BC6\u7801\">\n        </div>\n      </div>\n      <button class=\"login-btn\" @click=\"updatePsdFn()\">\n        {{btnText}}\n      </button>\n      <loading v-if=\"showLoading\" tipsText=\"\u6B63\u5728\u767B\u5F55\"></loading>\n      <tips v-if=\"showTips\" :tipsText2=\"tipsText3\"></tips>\n    </div>\n  ",
  data: function data() {
    return {
      btnText: '保存密码',
      isBinding: true,
      psdText: '',
      userInfo: {
        UserName: '廖玉斌',
        Company: '清秀公安局'
      },
      showLoading: false,
      //显示加载
      showTips: false,
      // 显示提示
      tipsText3: '',
      psdConfirmText: ''
    };
  },
  mounted: function mounted() {
    var _this = this;

    this.userInfo = JSON.parse(window.localStorage.getItem('userInfo'));
    var _json = {
      nric: this.userInfo.NRIC
    };
    var formData = new FormData();
    Object.keys(_json).forEach(function (key) {
      formData.append(key, _json[key]);
    });
    service.http('GetUser', formData).then(function (res) {
      if (res.Tag === 1) {
        _this.btnText = '我的工资条';
        _this.isBinding = false;
      } else {
        _this.btnText = '保存密码';
        _this.isBinding = true;
      }
    }).catch(function (rej) {
      console.log(rej);
    });
  },
  methods: {
    updatePsdFn: function updatePsdFn() {
      var _this2 = this;

      if (!this.isBinding) {
        this.$router.push({
          name: 'salary'
        });
        return;
      }

      if (this.psdText.trim() === '' && this.psdText === '') {
        this.tipsText3 = '请输入密码';
        this.showTipsFn();
        return;
      }

      if (this.psdConfirmText !== this.psdText) {
        //两次密码输入不一致
        this.tipsText3 = '两次密码不一致';
        this.showTipsFn();
        return;
      }

      var _json = {
        nric: this.userInfo.NRIC,
        phonePsd: this.psdText
      };
      this.showLoading = true;
      var formData = new FormData();
      Object.keys(_json).forEach(function (key) {
        formData.append(key, _json[key]);
      });
      service.http('GetUpdate', formData).then(function (res) {
        _this2.showLoading = false;

        if (res.Tag === 1) {
          s;

          _this2.showTipsFn();

          _this2.btnText = '我的工资条';
          _this2.tipsText3 = '保存成功';
          window.localStorage.setItem('isBinding', 1);
          _this2.isBinding = true;
        } else {
          _this2.tipsText3 = '保存失败';

          _this2.showTipsFn();
        }
      }).catch(function (rej) {
        _this2.showLoading = false;
        _this2.tipsText3 = '保存失败';

        _this2.showTipsFn();

        console.log(rej);
      });
    },
    showTipsFn: function showTipsFn() {
      var _this3 = this;

      this.showTips = true;
      setTimeout(function () {
        _this3.showTips = false;
      }, 2000);
    }
  }
});
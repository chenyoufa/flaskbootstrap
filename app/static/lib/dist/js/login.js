/**
 *@Description: 添加描述信息 desc（快捷键）
 *@author Chendy
 *@date 2019/12/24
 **/
'use strict'; //us（快捷键）
var service = new Service(); //获取地址栏数据
String.prototype.getQuery = function (name) {
    var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)');
    var r = window.location.search.substr(1).match(reg);

    if (r != null) {
        return decodeURI(r[2]);
    }

    return null;
};
var vm = new Vue({
  el: '#app',
  data: function data() {
    return {
      showLoading: false,
      username: '',
      //用户姓名
      idCard: '',
      //身份证号码
      phoneNum: '',
      //电话号码
      ivCode: '',
      //验证码
      showTips: false,
      psdText: '',
      dataApi: 'PostLongin',
      tipsText3: '请填写正确个人信息',
      downSeconds: 120,
      sendTips: '获取验证码',
      countTimer: null,
      tipsText: '正在登录',
      code: '',
      //获取微信code
      openId: '' //返回的openId

    };
  },
  mounted: function mounted() {//console.log(''.getQuery('code'));
    this.code = ''.getQuery('code');
    this.authInfoFn();
  },
  methods: {
    loginFn: function loginFn() {
      var _this = this;

      if (this.phoneNum.trim() === '' || this.phoneNum === '' || /^1[3456789]d{9}$/.test(this.phoneNum)) {
        this.tipsText3 = '请输入正确的手机号';
        this.showTipsFn();
        return;
          }
      if (this.username.trim() === '' || this.username === '' || this.idCard === '' || this.idCard.trim() === '' || this.ivCode === '' || this.ivCode.trim() === '') {
        this.tipsText3 = '验证信息不能为空';
        this.showTipsFn();
        return;
      }

      this.showLoading = true;
      var _json = {
        name: this.username,
        nric: this.idCard,
        tel: this.phoneNum,
        code: this.ivCode,
        openid: this.openId
      };
      var formData = new FormData();
      Object.keys(_json).forEach(function (key) {
        formData.append(key, _json[key]);
      });
      this.tipsText3 = '请填写正确个人信息';
      service.http(this.dataApi, formData).then(function (res) {
        _this.showLoading = false;

        if (res.Tag === 1) {
          // this.$router.push({
          //   path: 'salary',
          //   query: {
          //     idCard: res.Data.NRIC
          //   }
          // });
          console.log('登录成功！！！！！！');
        } else {
          _this.showTipsFn();
        }
      }).catch(function (rej) {
        _this.showLoading = false;

        _this.showTipsFn();

        console.log(rej);
      });
    },
    showTipsFn: function showTipsFn() {
      var _this2 = this;

      this.showTips = true;
      setTimeout(function () {
        _this2.showTips = false;
      }, 2000);
    },
    //授权函数
    authInfoFn: function authInfoFn() {
      var _this3 = this;

      var _json = {
        code: this.code
      };
      this.showLoading = true;
      var formData = new FormData();
      Object.keys(_json).forEach(function (key) {
        formData.append(key, _json[key]);
      });
      service.http('PostOpenid', formData).then(function (res) {
        _this3.showLoading = false;

        if (res.data.Tag === 1) {
          _this3.$router.push({
            path: 'salary',
            query: {
              idCard: res.data.Data.NRIC
            }
          });
        } else {
          _this3.openId = res.openId;
        }

        console.log(res);
      }).catch(function (rej) {
        _this3.showLoading = false;
        console.log(rej);
      });
    },
    getCodeFn: function getCodeFn() {
      var _this4 = this;

      if (this.downSeconds < 120) {
        console.log(this.downSeconds);
        return;
      }

      if (this.phoneNum.trim() === '' || this.phoneNum === '' || this.phoneNum.length !== 11) {
        this.tipsText3 = '请填写手机号';
        this.showTipsFn();
        return;
      }

      clearInterval(this.countTimer);
      var _json = {
        tel: this.phoneNum
      };
      this.showLoading = true;
      var formData = new FormData();
      Object.keys(_json).forEach(function (key) {
        formData.append(key, _json[key]);
      });
      service.http('SaveForm', formData).then(function (res) {
        _this4.showLoading = false;

        if (res.Tag === 1) {
          _this4.tipsText3 = '已成功发送';

          _this4.showTipsFn();

          _this4.countTimer = setInterval(function () {
            _this4.downSeconds = _this4.downSeconds - 1;
            _this4.sendTips = "".concat(_this4.downSeconds, "s");

            if (_this4.downSeconds === 0) {
              _this4.downSeconds = 120;
              _this4.sendTips = '获取验证码';
              clearInterval(_this4.countTimer);
            }
          }, 1000);
        }
      }).catch(function (rej) {
        _this4.showLoading = false;
      });
    }
  }
});
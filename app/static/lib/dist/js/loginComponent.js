"use strict";

var service = new Service(); //获取地址栏数据

String.prototype.getQuery = function (name) {
    var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)');
    var r = window.location.search.substr(1).match(reg);

    if (r != null) {
        return decodeURI(r[2]);
    }

    return null;
};

Vue.component('login', {
    template: "\n    <div class=\"auth-content\">\n      <div>\n           <img class=\"login-logo\" src=\"../../../lib/dist/images/logo.png\" alt=\"\">\n          <h5>\u4E3A\u4E86\u5B89\u5168\uFF0C\u521D\u6B21\u8FDB\u5165\u8BF7\u9A8C\u8BC1\u8EAB\u4EFD</h5>\n          <div class=\"form-main\">\n            <p>\u59D3\u540D</p>\n            <input class=\"ml-55\" v-model=\"username\" type=\"text\" placeholder=\"\u8BF7\u8F93\u5165\u59D3\u540D\">\n          </div>\n          <div class=\"form-main\">\n            <p>\u8EAB\u4EFD\u8BC1\u53F7</p>\n            <input type=\"text\" v-model=\"idCard\" placeholder=\"\u8BF7\u8F93\u5165\u8EAB\u4EFD\u8BC1\u53F7\u7801\">\n          </div>\n          <div class=\"form-main\">\n            <p>\u624B\u673A\u53F7\u7801</p>\n            <input type=\"text\" v-model=\"phoneNum\" placeholder=\"\u8BF7\u8F93\u5165\u624B\u673A\u53F7\u7801\">\n          </div>\n          <div class=\"form-main\">\n            <p>\u9A8C\u8BC1\u7801</p>\n            <input class=\"ml-20\" type=\"text\" v-model=\"ivCode\" placeholder=\"\u8BF7\u8F93\u5165\u9A8C\u8BC1\u7801\">\n            <button @click=\"getCodeFn()\" class=\"get-code\">{{sendTips}}</button>\n          </div>\n          <button class=\"login-btn\" @click=\"loginFn()\">\n            \u767B\u5F55\n          </button>\n        </div>\n      <loading v-if=\"showLoading\" tipsText=\"\u6B63\u5728\u767B\u5F55\"></loading>\n      <tips v-if=\"showTips\" :tipsText2=\"tipsText3\"></tips>\n    </div>\n  ",
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
            code: '',
            //获取微信code
            openId: '' //返回的openId

        };
    },
    mounted: function mounted() {
        console.log(''.getQuery('code'));
        this.code = ''.getQuery('code');
        this.authInfoFn();
    },
    methods: {
        loginFn: function loginFn() {
            var _this = this;

            if (this.username.trim() === '' || this.username === '' || this.idCard === '' || this.idCard.trim() === '' || this.phoneNum.trim() === '' || this.phoneNum === '' || this.ivCode === '' || this.ivCode.trim() === '') {
                this.tipsText3 = '验证信息不能为空';
                this.showTipsFn();
                return;
            }

            this.showLoading = true;
            var _json = {
                userName: this.username,
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

                if (res.Data.NRIC) {
                    _this.$router.push({
                        path: 'salary',
                        query: {
                            idCard: res.Data.NRIC
                        }
                    });
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

            if (!this.downSeconds === 120) {
                return;
            }

            if (this.phoneNum.trim() === '' || this.phoneNum === '') {
                this.tipsText3 = '请填写手机号';
                this.showTipsFn();
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
                        _this4.downSeconds--;
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
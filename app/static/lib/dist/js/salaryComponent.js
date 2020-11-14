"use strict";

var service = new Service();
Vue.component('salary', {
    template: "\n    <div class=\"salary-content\">\n      <div>\n        <img class=\"salary-img\" src=\"../../../lib/dist/images/salary-bg.png\" alt=\"\">\n        <template>\n            <h5 class=\"salary-sum\" v-if=\"salaryInfo.RealWages\">{{salaryInfo.RealWages}}</h5>\n            <h5 v-else class=\"salary-sum f-16\">\u6682\u65F6\u6CA1\u6709\u6570\u636E</h5>\n        </template>\n        <p class=\"detail-title\">\u5E94\u53D1\u9879\u76EE</p>\n        <div class=\"bg-white\">\n            <div class=\"detail\" v-if=\"salaryInfo.BaseWage\">\n              <p>\u57FA\u672C\u5DE5\u8D44</p>\n              <p>{{salaryInfo.BaseWage}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.OverTimeSubsidies\">\n              <p>\u52A0\u73ED\u8865\u8D34</p>\n              <p>{{salaryInfo.OverTimeSubsidies}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.MeritPay\">\n              <p>\u7EE9\u6548\u5DE5\u8D44</p>\n              <p>{{salaryInfo.MeritPay}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.Allowance\">\n              <p>\u6D25\u8D34</p>\n              <p>{{salaryInfo.Allowance}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.Subsidies\">\n              <p>\u8865\u8D34</p>\n              <p>{{salaryInfo.Subsidies}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.TimeBonus\">\n              <p>\u5E74\u5EA6\u5956\u91D1</p>\n              <p>{{salaryInfo.TimeBonus}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.Other1\">\n              <p>\u5176\u4ED61</p>\n              <p>{{salaryInfo.Other1}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.Other2\">\n              <p>\u5176\u4ED62</p>\n              <p>{{salaryInfo.Other2}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.AttendanceDeduct\">\n              <p>\u6263\u8003\u52E4</p>\n              <p>{{salaryInfo.AttendanceDeduct}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.TeachersQualification\">\n               <p>\u6559\u5E08\u8D44\u683C</p>\n               <p>{{salaryInfo.TeachersQualification}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.EducationAllowance\">\n               <p>\u5B66\u5386\u6D25\u8D34</p>\n               <p>{{salaryInfo.EducationAllowance}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.TeacherChargeSubsidies\">\n              <p>\u73ED\u4E3B\u4EFB\u6D25\u8D34</p>\n              <p>{{salaryInfo.TeacherChargeSubsidies}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.ProfessionalTerm\">\n              <p>\u804C\u79F0</p>\n              <p>{{salaryInfo.ProfessionalTerm}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.OverWorkload\">\n              <p>\u8D85\u51FA\u5DE5\u4F5C\u91CF</p>\n              <p>{{salaryInfo.OverWorkload}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.LunchBreak\">\n              <p>\u9910\u8865</p>\n              <p>{{salaryInfo.LunchBreak}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.OverTimeSubsidies\">\n              <p>\u52A0\u73ED\u8865\u8D34</p>\n              <p>{{salaryInfo.OverTimeSubsidies}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.TeacherChargeSubsidies\">\n              <p>\u751F\u6D3B\u8865\u8D34</p>\n              <p>{{salaryInfo.TeacherChargeSubsidies}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.Training\">\n              <p>\u65E9\u8BAD/\u65E9\u8BFB</p>\n              <p>{{salaryInfo.Training }}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.GardenerAward\">\n              <p>\u56ED\u4E01\u5956</p>\n              <p>{{salaryInfo.GardenerAward}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.ShouldPayWage\">\n              <p>\u5E94\u53D1\u5DE5\u8D44</p>\n              <p>{{salaryInfo.ShouldPayWage}}</p>\n            </div>\n        </div>\n        <p class=\"detail-title\">\u4EE3\u6263\u4EE3\u7F34\u9879\u76EE</p>\n        <div class=\"bg-white\">\n            <div class=\"detail\" v-if=\"salaryInfo.PersonalISS\">\n              <p>\u4E2A\u4EBA\u793E\u4FDD</p>\n              <p>{{salaryInfo.PersonalISS}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.PersonalACC\">\n              <p>\u4E2A\u4EBA\u4F4F\u623F\u516C\u79EF\u91D1</p>\n              <p>{{salaryInfo.PersonalACC}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.PersonalIncomeTax\">\n              <p>\u4E2A\u7A0E</p>\n              <p>{{salaryInfo.PersonalIncomeTax}}</p>\n            </div>\n            <div class=\"detail\" v-if=\"salaryInfo.RealWages\">\n              <p>\u5B9E\u53D1\u5DE5\u8D44</p>\n              <p>{{salaryInfo.RealWages}}</p>\n            </div>\n        </div>\n        <p class=\"detail-title\">\u5907\u6CE8</p>\n        <div class=\"remark bg-white\" v-if=\"salaryInfo.Remark\">\n          <p>{{salaryInfo.Remark}}</p>\n        </div>\n      </div>\n      <loading v-if=\"showLoading\" tipsText=\"\u52A0\u8F7D\u4E2D...\"></loading>\n      <tips v-if=\"showTips\" tipsText2=\"\u60A8\u7684\u5DE5\u8D44\u6761\u6682\u65F6\u6CA1\u6709\u6570\u636E!\"></tips>\n  </div>\n  ",
    data: function data() {
        return {
            salaryInfo: {},
            showTips: false,
            showLoading: false,
            showPop: false
        };
    },
    mounted: function mounted() {
        var _this = this;

        document.title = '月薪';
        var _json = {
            nric: this.$route.query.idCard
        };
        var formData = new FormData();
        Object.keys(_json).forEach(function (key) {
            formData.append(key, _json[key]);
        });
        service.http('GetWxList', formData).then(function (res) {
            _this.showLoading = false;

            if (res.Tag === 1) {
                _this.salaryInfo = res.Data;
                var date = new Date(res.Data.WageDate);
                document.title = "".concat(date.getFullYear(), "\u5E74").concat(date.getMonth() + 1, "\u6708\u85AA\u8D44");
            } else {
                _this.showTipsFn();
            }
        }).catch(function (rej) {
            _this.showLoading = false;

            _this.showTipsFn();
        });
    },
    methods: {
        showTipsFn: function showTipsFn() {
            var _this2 = this;

            this.showTips = true;
            setTimeout(function () {
                _this2.showTips = false;
            }, 2000);
        },
        showPopFn: function showPopFn() {
            this.showPop = !this.showPop;
        }
    }
});
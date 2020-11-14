"use strict";

// 导入首页组件模块
var loginComponent = {
  template: '<login></login>'
};
var mineComponent = {
  template: '<mine></mine>'
};
var salaryComponent = {
  template: '<salary></salary>'
};
var routes = [{
  path: '/',
  name: 'login',
  component: loginComponent
}, {
  path: '/mine',
  name: 'mine',
  component: mineComponent
}, {
  path: '/salary',
  name: 'salary',
  component: salaryComponent
}];
var router = new VueRouter({
  routes: routes
});
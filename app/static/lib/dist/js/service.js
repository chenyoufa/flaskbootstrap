"use strict";

/**
 *@description 请求类
 * @date 2020-10-12
 * @copyright 微盐
 * @author Chendy
 *
 **/
var baseUrl = '';

var Service = function Service() {};
/**
 * 请求数据接口
 * @param api 接口
 * @param data 参数
 * @returns {Promise<unknown>}
 */


Service.prototype.http = function (api, data) {
  return new Promise(function (resolve, reject) {
    axios.post("".concat(baseUrl).concat(api), data).then(function (res) {
      resolve(res.data);
    }).catch(function (rej) {
      reject(rej);
    });
  });
};
"use strict";

Vue.component('tips', {
  template: "\n    <div class=\"tips-content\">\n        <p>{{tipsText2}}</p>\n    </div>\n  ",
  props: {
    tipsText2: {
      default: '暂无记录',
      type: String
    }
  }
});
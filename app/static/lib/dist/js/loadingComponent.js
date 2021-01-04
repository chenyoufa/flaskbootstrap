"use strict";

Vue.component('loading', {
  template: "\n    <div class=\"spinner-box\">\n        <svg version=\"1.1\" id=\"loader-1\" x=\"0px\" y=\"0px\" width=\"50px\" height=\"50px\" viewBox=\"0 0 50 50\" style=\"enable-background:new 0 0 50 50;\" xml:space=\"preserve\">\n                <path d=\"M43.935,25.145c0-10.318-8.364-18.683-18.683-18.683c-10.318,0-18.683,8.365-18.683,18.683h4.068c0-8.071,6.543-14.615,14.615-14.615c8.072,0,14.615,6.543,14.615,14.615H43.935z\" transform=\"rotate(120.131 25 25)\">\n                    <animateTransform attributeType=\"xml\" attributeName=\"transform\" type=\"rotate\" from=\"0 25 25\" to=\"360 25 25\" dur=\"1s\" repeatCount=\"indefinite\"></animateTransform>\n                </path>\n               </svg>\n        <div>\n            {{tipsText}}\n        </div>\n    </div>\n  ",
  props: {
    tipsText: {
      default: '加载中...',
      type: String
    }
  }
});
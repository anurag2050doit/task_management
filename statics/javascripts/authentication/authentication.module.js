(function () {
  'use strict';

  angular
    .module('site.authentication', [
      'site.authentication.controllers',
      'site.authentication.services'
    ]);

  angular
    .module('site.authentication.controllers', []);

  angular
    .module('site.authentication.services', ['ngCookies']);
})();
(function () {
  'use strict';

  angular
    .module('base', [
      'ui.router',
      'config',
      'routes',
      'site.layout',
      'site.authentication',
      'site.task',
    ])
    .run(run);

  angular
    .module('config', []);

  angular
    .module('routes', ['ngRoute', 'ui.router']);


  run.$inject = ['$http'];

  /**
   * @name run
   * @desc Update xsrf $http headers to align with Django's defaults
   */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
    return;
  }
})();
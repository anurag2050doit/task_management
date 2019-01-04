(function () {
  'use strict';

  angular
    .module('routes')
    .config(config);

  config.$inject = ['$routeProvider', '$stateProvider', '$urlRouterProvider'];

  function config($routeProvider, $stateProvider, $urlRouterProvider) {
    $routeProvider.when('/', {
        controller: 'LayoutController',
        controllerAs: 'vm',
        templateUrl: '/static/template/layout/index.html',
      }).when('/login', {
        controller: 'LoginController',
        controllerAs: 'vm',
        templateUrl: '/static/template/authentication/login.html',
      }).when('/task/detail/:taskId', {
        controller: 'TaskController',
        controllerAs: 'vm',
        templateUrl: '/static/template/task/task.html',
      }).when('/task/add', {
        controller: 'TaskAddEditController',
        controllerAs: 'vm',
        templateUrl: '/static/template/task/task_add_edit.html',
      })
     .otherwise('/');
  }
})();
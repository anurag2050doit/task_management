(function () {
  'use strict';

  angular
    .module('site.authentication.controllers')
    .controller('LoginController', LoginController);

  LoginController.$inject = ['$location', '$scope', 'Authentication'];

  function LoginController($location, $scope, Authentication) {
    var vm = this;

    vm.login = login;
    vm.error = null;

    activate();

    function activate() {
      if (Authentication.isAuthenticated()) {
        $location.url('/');
      }
    }

    /**
     * @name login
     * @desc Log the user in
     * @memberOf thinkster.authentication.controllers.LoginController
     */
    function login() {
      Authentication.login(vm.username, vm.password).then(function (d) {
        if (d.status === 400 || d.status === 500 || d.status === 401) {
          vm.error = d.data.message;
          return;
        }
      });
    }
  }
})();
/**
 * NavbarController
 * @namespace site.layout.controllers
 */
(function () {
    'use strict';

    angular
        .module('site.layout.controllers')
        .controller('NavbarController', NavbarController);

    NavbarController.$inject = ['$scope', 'Authentication'];

    /**
     * @namespace NavbarController
     */
    function NavbarController($scope, Authentication) {
        var vm = this;
        vm.isAuthenticated = Authentication.isAuthenticated();
        vm.user = Authentication.getAuthenticatedAccount();
        vm.logout = Authentication.logout;
    }
})();
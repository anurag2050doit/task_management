/**
 * Authentication
 * @namespace site.authentication.services
 */
(function () {
  'use strict';

  angular
    .module('site.authentication.services')
    .factory('Authentication', Authentication);

  Authentication.$inject = ['$cookies', '$http'];

  /**
   * @namespace Authentication
   * @returns {Factory}
   */
  function Authentication($cookies, $http) {
    /**
     * @name Authentication
     * @desc The Factory to be returned
     */
    var Authentication = {
      login: login,
      isAuthenticated: isAuthenticated,
    };

    return Authentication;

    ///////////////////

    /**
     * @name getAuthenticatedAccount
     * @desc Return the currently authenticated account
     * @returns {object|undefined} Account if authenticated, else `undefined`
     * @memberOf site.authentication.services.Authentication
     */
    function getAuthenticatedAccount() {
      if (!$cookies.authenticatedAccount) {
        return;
      }
      return JSON.parse($cookies.authenticatedAccount);
    }


    /**
     * @name isAuthenticated
     * @desc Check if the current user is authenticated
     * @returns {boolean} True is user is authenticated, else false.
     * @memberOf site.authentication.services.Authentication
     */
    function isAuthenticated() {
      return !!$cookies.authenticatedAccount;
    }


    /**
     * @name login
     * @desc Try to log in with email `username` and password `password`
     * @param {string} username The email entered by the user
     * @param {string} password The password entered by the user
     * @returns {Promise}
     * @memberOf site.authentication.services.Authentication
     */
    function login(username, password) {
      return $http({
        url: '/api-auth/login/',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        data: {
          username: username,
          password: password
        }
      }).then(loginSuccessFn, loginErrorFn);

      /**
       * @name loginSuccessFn
       * @desc Set the authenticated account and redirect to index
       */
      function loginSuccessFn(data, status, headers, config) {
        Authentication.setAuthenticatedAccount(data.data);
        window.location = '/';
      }

      /**
       * @name loginErrorFn
       * @desc Log "Epic failure!" to the console
       */
      function loginErrorFn(data, status, headers, config) {
        return data;
      }
    }


    /**
     * @name logout
     * @desc Try to log the user out
     * @returns {Promise}
     * @memberOf site.authentication.services.Authentication
     */
    function logout() {
      return $http.post('/auth/logout/')
        .then(logoutSuccessFn, logoutErrorFn);

      /**
       * @name logoutSuccessFn
       * @desc Unauthenticate and redirect to index with page reload
       */
      function logoutSuccessFn(data, status, headers, config) {
        Authentication.unauthenticate();

        window.location = '/';
      }

      /**
       * @name logoutErrorFn
       * @desc Log "Epic failure!" to the console
       */
      function logoutErrorFn(data, status, headers, config) {
        console.error('Epic failure!');
      }
    }


    /**
     * @name register
     * @desc Try to register a new user
     * @param {string} email The email entered by the user
     * @param {string} password The password entered by the user
     * @param {string} username The username entered by the user
     * @returns {Promise}
     * @memberOf site.authentication.services.Authentication
     */
    function register(email, password, username) {
      return $http.post('/api/v1/accounts/', {
        username: username,
        password: password,
        email: email
      }).then(registerSuccessFn, registerErrorFn);

      /**
       * @name registerSuccessFn
       * @desc Log the new user in
       */
      function registerSuccessFn(data, status, headers, config) {
        Authentication.login(email, password);
      }

      /**
       * @name registerErrorFn
       * @desc Log "Epic failure!" to the console
       */
      function registerErrorFn(data, status, headers, config) {
        console.error('Epic failure!');
      }
    }


    /**
     * @name setAuthenticatedUser
     * @desc Stringify the account object and store it in a cookie
     * @param {Object} account The acount object to be stored
     * @returns {undefined}
     * @memberOf site.authentication.services.Authentication
     */
    function setAuthenticatedAccount(account) {
      $cookies.authenticatedAccount = JSON.stringify(account);
    }


    /**
     * @name unauthenticate
     * @desc Delete the cookie where the account object is stored
     * @returns {undefined}
     * @memberOf site.authentication.services.Authentication
     */
    function unauthenticate() {
      delete $cookies.authenticatedAccount;
    }
  }
})();
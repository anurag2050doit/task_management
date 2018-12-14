/**
 * Dashboard
 * @namespace site.layout.services
 */

(function () {
  'use strict';

  angular
    .module('site.layout.services')
    .factory('Layout', Layout);


  Layout.$inject = ['$http'];


  function Layout($http) {
    /**
     * @name Layout
     * @desc The Factory to be returned
     */
    var Layout = {
      GetAllTask: GetAllTask
    };

    return Layout;

    /**
     * @name GetAllTask
     * @desc Return All Task
     * @returns {Promise}
     * @memberOf site.Layout.services.Layout
     */

    function GetAllTask() {
      return $http({
        url: '/api/v1/tasks/',
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(getTaskSuccessFn, getTaskSuccessFn)

      function getTaskSuccessFn(data, status, headers, config) {
        return data;
      }
    }
  }
})();
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
      GetAllTask: GetAllTask,
      getPaginationResponse: getPaginationResponse
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
        url: '/api/v1/task/',
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(getTaskSuccessFn, getTaskSuccessFn);

      function getTaskSuccessFn(data, status, headers, config) {
        return data;
      }
    }

    /**
     * @name GetAllTask
     * @desc Return All Task
     * @returns {Promise}
     * @memberOf site.Layout.services.Layout
     */
    function getPaginationResponse(url) {
      return $http({
        url: url,
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      })
    }
  }
})();
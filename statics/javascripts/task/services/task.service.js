/**
 * Dashboard
 * @namespace site.task.services
 */

(function () {
  'use strict';

  angular
    .module('site.task.services')
    .factory('Task', Task);


  Task.$inject = ['$http'];


  function Task($http) {
    /**
     * @name Task
     * @desc The Factory to be returned
     */
    var Task = {
      getTaskDetail: getTaskDetail,
      updateTaskStatus: updateTaskStatus,
    };

    return Task;

    /**
     * @name GetTaskDetail
     * @desc Return Task Detail of specific ID
     * @returns {Promise}
     * @memberOf site.Task.services
     */

    function getTaskDetail(taskId) {
      return $http({
        url: '/api/v1/task/' + taskId + '/',
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(getTaskSuccessFn, getTaskSuccessFn)

      function getTaskSuccessFn(data, status, headers, config) {
        return data;
      }
    }

    function updateTaskStatus(status, taskId) {
      return $http({
        url: '/api/v1/task/' + taskId + '/',
        method: 'PATCH',
        data: {
          "task_status": status
        },
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